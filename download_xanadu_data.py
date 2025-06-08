"""
Adapted from: https://github.com/XanaduAI/xanadu-qca-data (Apache 2.0 license)

This script downloads `samples.npy` from the public S3 bucket provided by
Xanadu for their Nature paper on quantum computational advantage:
https://www.nature.com/articles/s41586-022-04725-x

Only the `samples.npy` file is downloaded for each figure, and saved as:
    data/fig2.npy, data/fig3a.npy, etc.
"""

import requests
from pathlib import Path

BASE_URL = "https://qca-data.s3.amazonaws.com/"
TARGET_DIR = Path("data")
FIGURES = ["fig2", "fig3a", "fig3b", "fig4", "figS15"]
FILENAME = "samples.npy"

for fig in FIGURES:
    remote_path = f"{fig}/{FILENAME}"
    local_path = TARGET_DIR / f"xanadu_borealis_{fig}.npy"
    print(f"Downloading {remote_path} → {local_path}...")

    response = requests.get(BASE_URL + remote_path)
    response.raise_for_status()  # fail early if broken

    local_path.write_bytes(response.content)
    print(f"Downloaded {remote_path} → {local_path}")