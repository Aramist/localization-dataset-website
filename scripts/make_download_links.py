import json
import os
from pathlib import Path


def make_download_links():
    html_dir = Path("/mnt/home/atanelus/public_www/")

    with open(
        "/mnt/home/atanelus/dataset_website/scripts/strings/dataset_info.json", "r"
    ) as ctx:
        data = json.load(ctx)

    links = []
    for dataset in data:
        for link_info in dataset["links"]:
            src = link_info["cluster_path"]
            if src is None:
                continue
            src = Path(src)
            dest = html_dir / Path(link_info["url"])
            links.append((src, dest))

    print(f"Symlinking {len(links)} files")

    for src, dst in links:
        if not src.exists():
            print(f"File {src} does not exist")
            continue
        if not dst.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            os.symlink(src, dst)


if __name__ == "__main__":
    make_download_links()
