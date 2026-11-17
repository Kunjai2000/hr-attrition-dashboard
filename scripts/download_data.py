"""Download the IBM HR Analytics Employee Attrition dataset and verify its checksum.

The dataset is already committed to ``data/raw/``. This script restores it from
IBM's public GitHub repository if the file is missing or has been modified.

Usage:
    python scripts/download_data.py
"""

from __future__ import annotations

import hashlib
import sys
import urllib.request
from pathlib import Path

SOURCE_URL = (
    "https://raw.githubusercontent.com/IBM/employee-attrition-aif360/"
    "master/data/emp_attrition.csv"
)
EXPECTED_SHA256 = "a5c31e38bd7fafc9bc333884eb181b06b41b8e5e488e8f7ccb27199fb3be7659"
TARGET_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "raw"
    / "WA_Fn-UseC_-HR-Employee-Attrition.csv"
)


def sha256_of(path: Path) -> str:
    """Return the SHA-256 hex digest of a file."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    """Download the dataset if needed and verify its integrity."""
    if TARGET_PATH.exists() and sha256_of(TARGET_PATH) == EXPECTED_SHA256:
        print(f"Dataset present and verified: {TARGET_PATH}")
        return 0

    TARGET_PATH.parent.mkdir(parents=True, exist_ok=True)
    print(f"Downloading dataset from {SOURCE_URL} ...")
    urllib.request.urlretrieve(SOURCE_URL, TARGET_PATH)

    actual = sha256_of(TARGET_PATH)
    if actual != EXPECTED_SHA256:
        print(f"Checksum mismatch: expected {EXPECTED_SHA256}, got {actual}")
        return 1

    print(f"Dataset downloaded and verified: {TARGET_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
