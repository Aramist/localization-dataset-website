from pathlib import Path

import cv2
import h5py
import numpy as np
import pandas as pd
from tqdm import tqdm


def make_dataset_video_file_mp4(dataset_metadata_path: Path, output_path: Path):
    md = pd.read_csv(dataset_metadata_path)

    sample_video_path = md.iloc[0].video_path
    cap = cv2.VideoCapture(sample_video_path)
    width, height = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(
        cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    )
    cap.release()
    del cap

    writer = cv2.VideoWriter(
        str(output_path),
        cv2.VideoWriter_fourcc(*"mp4v"),
        10,
        (width, height),
        isColor=True,
    )

    # Can't guarantee the dataset is sorted by video_path, so this will be
    # inefficient
    last_cap = None
    last_vid_path = None
    for _, row in tqdm(md.iterrows(), total=len(md)):
        if last_vid_path != row.video_path:
            last_vid_path = row.video_path
            if last_cap is not None:
                last_cap.release()
            last_cap = cv2.VideoCapture(last_vid_path)

        idx = row["frame_idx"]
        last_cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
        ret, frame = last_cap.read()
        if ret:
            writer.write(frame)
    writer.release()


def make_dataset_video_file(
    dataset_audio_path: Path, dataset_metadata_path: Path, output_path: Path
):
    ground_truth = None
    with h5py.File(dataset_audio_path, "r") as f:
        if "locations" in f:
            ground_truth = f["locations"][:]

    md = pd.read_csv(dataset_metadata_path)

    sample_video_path = md.iloc[0].video_path
    cap = cv2.VideoCapture(sample_video_path)
    width, height = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(
        cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    )
    cap.release()

    with h5py.File(output_path, "w") as f:
        vid_dset = f.create_dataset(
            "video",
            (len(md), height, width, 3),
            dtype=np.uint8,
            compression="gzip",
            chunks=(30, height, width, 3),
        )

        if ground_truth is not None:
            f.create_dataset("labels", data=ground_truth)

        for i, row in tqdm(md.iterrows(), total=len(md)):
            cap = cv2.VideoCapture(row.video_path)
            idx = row["frame_idx"]
            cap.set(cv2.CAP_PROP_POS_FRAMES, idx)
            ret, frame = cap.read()
            cap.release()
            if ret:
                vid_dset[i] = frame[..., ::-1]


if __name__ == "__main__":
    meta_dir = Path("/mnt/home/atanelus/ceph/datasets")
    dataset_dir = Path("/mnt/home/atanelus/ceph/neurips_datasets/audio")
    vid_dir = Path("/mnt/home/atanelus/ceph/neurips_datasets/videos/")
    vid_dir.mkdir(exist_ok=True, parents=True)

    audio_files = [
        dataset_dir / "speaker-4m-e1_audio.h5",
        dataset_dir / "sologerbil-4m-e1_audio.h5",
        dataset_dir / "edison-4m-e1_audio.h5",
        dataset_dir / "dyadgerbil-4m-e1_audio.h5",
        dataset_dir / "gerbilearbud-4m-e1_audio.h5",
    ]

    metadata_files = [
        meta_dir / "speaker_metadata.csv",
        meta_dir / "solo_gerbil_metadata.csv",
        meta_dir / "edison_metadata.csv",
        meta_dir / "dyadgerbil_metadata.csv",
        meta_dir / "gerbilearbud_metadata.csv",
    ]

    output_files = [
        vid_dir / "speaker-4m-e1_video.h5",
        vid_dir / "sologerbil-4m-e1_video.h5",
        vid_dir / "edison-4m-e1_video.h5",
        vid_dir / "dyadgerbil-4m-e1_video.h5",
        vid_dir / "gerbilearbud-4m-e1_video.h5",
    ]

    # for a, m, o in zip(audio_files, metadata_files, output_files):
    # if not o.exists():
    # make_dataset_video_file(a, m, o)

    for m, o in zip(metadata_files, output_files):
        o = o.with_suffix(".mp4")
        if not o.exists():
            make_dataset_video_file_mp4(m, o)
