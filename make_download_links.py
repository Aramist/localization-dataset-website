import os
from pathlib import Path

dataset_dir = Path("/mnt/home/atanelus/ceph/neurips_datasets")
video_dir = Path("/mnt/home/atanelus/ceph/neurips_datasets/videos")

download_dir = Path("/mnt/home/atanelus/public_www/res/download_links")
links = [
    (
        dataset_dir / "audio" / "dyadgerbil-4m-e1_audio.h5",
        download_dir / "dyadgerbil-4m-e1_audio.h5",
    ),
    (
        dataset_dir / "audio" / "mouseearbud-24m-e3_audio.h5",
        download_dir / "mouseearbud-24m-e3_audio.h5",
    ),
    (
        dataset_dir / "audio" / "dyadmouse-24m-e3_audio.h5",
        download_dir / "dyadmouse-24m-e3_audio.h5",
    ),
    (
        dataset_dir / "audio" / "sologerbil-4m-e1_audio.h5",
        download_dir / "sologerbil-4m-e1_audio.h5",
    ),
    (
        dataset_dir / "audio" / "edison-4m-e1_audio.h5",
        download_dir / "edison-4m-e1_audio.h5",
    ),
    (
        dataset_dir / "audio" / "solomouse-24m-e3_audio.h5",
        download_dir / "solomouse-24m-e3_audio.h5",
    ),
    (
        dataset_dir / "audio" / "gerbilearbud-4m-e1_audio.h5",
        download_dir / "gerbilearbud-4m-e1_audio.h5",
    ),
    (
        dataset_dir / "audio" / "speaker-4m-e1_audio.h5",
        download_dir / "speaker-4m-e1_audio.h5",
    ),
    (
        Path("/mnt/ceph/users/njoseph/dataset/dataset_3.h5"),
        download_dir / "hexapod-8m-e2_audio.h5",
    ),
    (
        dataset_dir / "videos" / "sologerbil-4m-e1_video.h5",
        download_dir / "sologerbil-4m-e1_video.h5",
    ),
    (
        dataset_dir / "videos" / "edison-4m-e1_video.h5",
        download_dir / "edison-4m-e1_video.h5",
    ),
    (
        dataset_dir / "videos" / "speaker-4m-e1_video.h5",
        download_dir / "speaker-4m-e1_video.h5",
    ),
    (
        dataset_dir / "videos" / "dyadgerbil-4m-e1_video.h5",
        download_dir / "dyadgerbil-4m-e1_video.h5",
    ),
]


def make_download_links():
    for src, dst in links:
        if not src.exists():
            print(f"File {src} does not exist")
            continue
        if not dst.exists():
            os.symlink(src, dst)


if __name__ == "__main__":
    make_download_links()
