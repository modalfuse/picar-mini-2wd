#!/usr/bin/env python3
"""Create a Zenodo deposition, optionally prereserve DOI, upload archive, publish.

Usage:
  export ZENODO_ACCESS_TOKEN=...   # https://zenodo.org/account/settings/applications/tokens/new/
  python scripts/zenodo_publish.py [--publish]

Without --publish: creates draft + prereserves DOI and prints it.
With --publish: uploads zip of the repo (excluding .git) and publishes.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
import zipfile
from pathlib import Path

import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
API = os.environ.get("ZENODO_API", "https://zenodo.org/api")
TOKEN = os.environ.get("ZENODO_ACCESS_TOKEN") or os.environ.get("ZENODO_TOKEN")


def req(method: str, url: str, data: bytes | None = None, content_type: str | None = None):
    if not TOKEN:
        raise SystemExit(
            "Missing ZENODO_ACCESS_TOKEN. Create one at "
            "https://zenodo.org/account/settings/applications/tokens/new/ "
            "(scopes: deposit:write, deposit:actions) and export it."
        )
    headers = {"Authorization": f"Bearer {TOKEN}"}
    if content_type:
        headers["Content-Type"] = content_type
    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request) as resp:
            body = resp.read()
            return resp.status, json.loads(body.decode()) if body else {}
    except urllib.error.HTTPError as e:
        err = e.read().decode(errors="replace")
        raise SystemExit(f"HTTP {e.code} {url}\n{err}") from e


def load_metadata() -> dict:
    path = ROOT / ".zenodo.json"
    meta = json.loads(path.read_text(encoding="utf-8"))
    # Zenodo deposition metadata uses slightly different nesting
    return meta


def create_deposition(prereserve: bool = True) -> dict:
    payload = {"metadata": load_metadata()}
    if prereserve:
        payload["metadata"]["prereserve_doi"] = True
    # Remove empty orcid fields Zenodo may reject
    creators = []
    for c in payload["metadata"].get("creators", []):
        c2 = {k: v for k, v in c.items() if v}
        creators.append(c2)
    payload["metadata"]["creators"] = creators
    status, data = req(
        "POST",
        f"{API}/deposit/depositions",
        data=json.dumps(payload).encode(),
        content_type="application/json",
    )
    print("created deposition", data.get("id"), "http", status)
    return data


def make_zip(dest: Path) -> Path:
    skip_dirs = {".git", "__pycache__", ".venv", "node_modules"}
    zip_path = dest / "picar-mini-2wd-v1.1.0.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in ROOT.rglob("*"):
            if not path.is_file():
                continue
            rel = path.relative_to(ROOT)
            if any(part in skip_dirs for part in rel.parts):
                continue
            if rel.as_posix().startswith("scripts/zenodo_publish"):
                pass
            zf.write(path, arcname=str(Path("picar-mini-2wd") / rel))
    print("zip", zip_path, zip_path.stat().st_size)
    return zip_path


def upload_file(deposition: dict, zip_path: Path) -> None:
    bucket = deposition["links"]["bucket"]
    data = zip_path.read_bytes()
    url = f"{bucket}/{zip_path.name}"
    status, _ = req("PUT", url, data=data, content_type="application/octet-stream")
    print("uploaded", zip_path.name, "http", status)


def publish(deposition_id: int) -> dict:
    status, data = req("POST", f"{API}/deposit/depositions/{deposition_id}/actions/publish")
    print("published http", status)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--publish", action="store_true", help="Upload zip and publish")
    parser.add_argument("--deposition-id", type=int, default=0, help="Reuse existing draft id")
    args = parser.parse_args()

    if args.deposition_id:
        _, deposition = req("GET", f"{API}/deposit/depositions/{args.deposition_id}")
    else:
        deposition = create_deposition(prereserve=True)

    doi_info = deposition.get("metadata", {}).get("prereserve_doi") or {}
    doi = deposition.get("doi") or doi_info.get("doi")
    print("DOI:", doi)
    print("record html:", deposition.get("links", {}).get("html"))
    out = ROOT / "scripts" / ".zenodo_deposition.json"
    out.write_text(json.dumps(deposition, indent=2), encoding="utf-8")
    print("wrote", out)

    if not args.publish:
        print("Draft only. Re-run with --publish --deposition-id", deposition["id"], "after updating README/papers with the DOI.")
        return

    with tempfile.TemporaryDirectory() as tmp:
        zip_path = make_zip(Path(tmp))
        upload_file(deposition, zip_path)
    published = publish(deposition["id"])
    print("final DOI:", published.get("doi"))
    print("doi_url:", published.get("doi_url"))
    (ROOT / "scripts" / ".zenodo_published.json").write_text(
        json.dumps(published, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
