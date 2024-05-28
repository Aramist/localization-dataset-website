""" Helper script for making repeated html elements
"""

# modal format:
"""
<div class="modal fade" id="speaker-4m-details-modal" tabindex="-1" role="dialog" aria-labelledby>
    <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
        <div class="modal-header">
            <h5 class="modal-title text-capitalize">Speaker-4M</h5>
            <button type="button" class="close btn btn-outline-danger"
            data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
            </button>
        </div>

        <div class="modal-body">
            <ul>
            <li><p class="text-dark">A dataset of sounds emitted by a
                stationary speaker at ~400 positions.</p></li>
            <li><p class="text-dark">Stimuli include 5 noise-free gerbil
                vocalizations and a white noise stimulus, each presented at
                three volume levels.</p></li>
            <li><p class="text-dark">The speaker's positions lie along a
                square grid with ~2cm spacing.</p></li>
            <li><p class="text-dark"># instances: 70,914</p></li>
            <li><p class="text-dark"># stimulus classes: 18</p></li>
            <li><p class="text-dark">Sampling rate: 125kHz</p></li>
            <li><p class="text-dark"># Microphones: 4</p></li>
            <li><p class="text-dark">Enclosure Dimensions: </p></li>
            <li><p class="text-dark">Size: 15GB</p></li>
            </ul>
        </div>

        </div>
    </div>
</div>
"""


def make_modal_block(title: str, descriptions: list[str]) -> str:
    """Make a modal block for a dataset

    Args:
        title (str): The title of the dataset
        descriptions (list[str]): A list of descriptions for the dataset

    Returns:
        str: A string representing the modal block
    """

    modal_block = f"""<div class="modal fade" id="{title}-details-modal" tabindex="-1" role="dialog" aria-labelledby>
    <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
        <div class="modal-header">
            <h5 class="modal-title text-capitalize">{title}</h5>
            <button type="button" class="close btn btn-outline-danger"
            data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
            </button>
        </div>

        <div class="modal-body">
            <ul>
    """
    for desc_item in descriptions:
        modal_block += f"""<li><p class="text-dark">{desc_item}</p></li>\n"""

    modal_block += """</ul>
        </div>

        </div>
    </div>
</div>
    """

    return modal_block


edison_info = {
    "title": "Edison-4M",
    "descriptions": [
        "A dataset of sounds emitted by an Edison robot performing a random walk around the Small Shoebox arena. The stimuli are gathered from longitudinal recordings of gerbil families [Peterson et al. 2023. eLife] and presented through an earbud. The dataset includes ground truth locations for the earbud and the robot’s orientation.",
        "# instances: 266,877",
        "# unique stimuli: 10,049",
        "# microphones: 4",
        "Sampling rate: 125kHz",
        "Environment: Large shoebox",
        "Size: 44GB",
    ],
}

solo_gerb_info = {
    "title": "SoloGerbil-4M",
    "descriptions": [
        "A dataset of vocalizations emitted by lone, freely-behaving adolescent gerbils in response to a call presented through a speaker.",
        "# instances: 90,434",
        "# microphones: 4",
        "Sampling rate: 125kHz",
        "Environment: Large shoebox",
        "Size: 7.5GB",
    ],
}

gerbil_earbud_info = {
    "title": "GerbilEarbud-4M",
    "descriptions": [
        "A dataset of sounds emitted by an earbud affixed to the head of a freely-behaving adult gerbil. The stimuli are gathered from longitudinal recordings of gerbil families [Peterson et al. 2023. eLife].",
        "# instances: 7698",
        "# microphones: 4",
        "Sampling rate: 125kHz",
        "Environment: Large shoebox",
        "Size: 1.3GB",
    ],
}

hexapod_info = {
    "title": "Hexapod-8M",
    "descriptions": [
        "A dataset of sounds emitted by an ultrasonic speaker affixed to a hexapod robot walking in parallel lines across the Large Arena. As it walks, the arm carrying the speaker is rotated to different orientations to vary the directionality of the emitted sounds throughout the dataset. The stimuli are gathered from longitudinal recordings of gerbil families [Peterson et al. 2023. eLife].",
        "# instances: 156,900",
        "# unique stimuli: 100",
        "# microphones: 8",
        "Sampling rate: 192kHz",
        "Environment: Large Arena",
        "Size: 236GB",
    ],
}


mouse_earbud_info = {
    "title": "MouseEarbud-24M",
    "descriptions": [
        "A dataset of sounds emitted by an earbud affixed to the head of a lone, freely-behaving mouse. The stimuli are noise-filtered mouse vocalizations. Ground truth locations include elevation (position along z-dimension), but not orientation.",
        "# instances: 200,000",
        "# microphones: 24",
        "Sampling rate: 250kHz",
        "Environment: Princeton environment",
        "Size: 208GB",
    ],
}

solo_mouse_info = {
    "title": "SoloMouse-24M",
    "descriptions": [
        "A dataset of vocalizations emitted by a freely-behaving mouse.",
        "# instances: 549",
        "# microphones: 24",
        "Sampling rate: 250kHz",
        "Environment: Princeton environment",
        "Size: 362MB",
    ],
}


# print(make_modal_block(**edison_info))
# print(make_modal_block(**solo_gerb_info))
# print(make_modal_block(**gerbil_earbud_info))
# print(make_modal_block(**hexapod_info))
# print(make_modal_block(**mouse_earbud_info))
# print(make_modal_block(**solo_mouse_info))


# Format for dataset cards:
"""
<div class="col-lg-3 col-md-6 col-sm-12">
    <div class="card dataset-card">
    <img class="card-img-top" src="res/placeholder.png"
        alt="Speaker-4M">
    <div class="card-img-overlay text-white dark-transluscent"
        style="height: 3rem">
        <h5 class="card-title">Speaker-4M</h5>
    </div>
    <div class="card-body">
        <p class="card-text overflow-hidden">A dataset of sounds
        emitted by a stationary speaker at ~400 positions.</p>
        <p class="card-text"> Size: 15GB</p>
        <div class="btn-group">
        <button class="btn btn-outline-secondary" type="button"
            data-toggle="modal"
            data-target="#speaker-4m-details-modal">Details</button>
        <button class="btn btn-primary btn-outline-primary"
            type="button" data-toggle="modal"
            data-target="#speaker-4m-downloads-modal"><img
            src="res/download-icon-light.svg"
            height="18px" /></button>
        </div>
    </div>
    </div>
</div>
"""


def make_dataset_card(title: str, description: str, size: str) -> str:
    """Make a dataset card

    Args:
        title (str): The title of the dataset
        description (str): A description of the dataset
        size (str): The size of the dataset

    Returns:
        str: A string representing the dataset card
    """

    card = f"""<div class="col-lg-3 col-md-6 col-sm-12">
    <div class="card dataset-card">
    <img class="card-img-top" src="res/placeholder.png"
        alt="{title}">
    <div class="card-img-overlay text-white dark-transluscent"
        style="height: 3rem">
        <h5 class="card-title">{title}</h5>
    </div>
    <div class="card-body">
        <p class="card-text overflow-hidden">{description}</p>
        <p class="card-text"> Size: {size}</p>
        <div class="btn-group">
        <button class="btn btn-outline-secondary" type="button"
            data-toggle="modal"
            data-target="#{title}-details-modal">Details</button>
        <button class="btn btn-primary btn-outline-primary"
            type="button" data-toggle="modal"
            data-target="#{title}-downloads-modal"><img
            src="res/download-icon-light.svg"
            height="18px" /></button>
        </div>
    </div>
    </div>
</div>
    """

    return card


# print(
#     make_dataset_card(
#         "Speaker-4M",
#         "A dataset of sounds emitted by a stationary speaker at ~400 positions.",
#         "15GB",
#     )
# )
# print(
#     make_dataset_card(
#         "Edison-4M",
#         "A dataset of sounds emitted by an Edison robot performing a random walk around the Small Shoebox arena.",
#         "44GB",
#     )
# )
# print(
#     make_dataset_card(
#         "SoloGerbil-4M",
#         "A dataset of vocalizations emitted by lone, freely-behaving adolescent gerbils in response to a call presented through a speaker.",
#         "7.5GB",
#     )
# )
# print(
#     make_dataset_card(
#         "GerbilEarbud-4M",
#         "A dataset of sounds emitted by an earbud affixed to the head of a freely-behaving adult gerbil.",
#         "1.3GB",
#     )
# )
# print(
#     make_dataset_card(
#         "Hexapod-8M",
#         "A dataset of sounds emitted by an ultrasonic speaker affixed to a hexapod robot walking in parallel lines across the Large Arena.",
#         "236GB",
#     )
# )
# print(
#     make_dataset_card(
#         "MouseEarbud-24M",
#         "A dataset of sounds emitted by an earbud affixed to the head of a lone, freely-behaving mouse.",
#         "208GB",
#     )
# )
# print(
#     make_dataset_card(
#         "SoloMouse-24M",
#         "A dataset of vocalizations emitted by a freely-behaving mouse.",
#         "362MB",
#     )
# )


# Format for download modals:
"""
      <div class="modal fade" id="speaker-4m-downloads-modal" tabindex="-1"
        role="dialog" aria-labelledby>
        <div class="modal-dialog modal-dialog-centered" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title text-capitalize">Speaker-4M download
                links</h5>
              <button type="button" class="close btn btn-outline-danger"
                data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>

            <div class="modal-body">
              <ul>
                <li><a class="link-primary" href="#">speaker-4m_audio.h5
                    (15GB)</a></li>
                <li><a class="link-secondary" href="#">speaker-4m_video.h5 (?GB)</a></li>
                <li><a class="link-secondary" href="#">speaker-4m_metadata.csv
                    (8.3MB)</a></li>
              </ul>
            </div>

          </div>
        </div>
      </div>
"""


def make_downloads_modal(title: str, links: list[str]) -> str:
    """Make a downloads modal

    Args:
        title (str): The title of the dataset
        links (list[str]): A list of download links

    Returns:
        str: A string representing the downloads modal
    """

    modal = f"""<div class="modal fade" id="{title.lower()}-downloads-modal" tabindex="-1"
        role="dialog" aria-labelledby>
        <div class="modal-dialog modal-dialog-centered" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title text-capitalize">{title} download links</h5>
              <button type="button" class="close btn btn-outline-danger"
              data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
        
          <div class="modal-body">
            <ul>
    """
    for n, link in enumerate(links):
        if n == 0:
            modal += f"""<li><a class="link-primary" href="#">{link}</a></li>\n"""
        else:
            modal += f"""<li><a class="link-secondary" href="#">{link}</a></li>\n"""

    modal += """</ul>
        </div>

      </div>
    </div>
    </div>
        """

    return modal


# print(
#     make_downloads_modal(
#         "Speaker-4M",
#         [
#             "speaker-4m_audio.h5 (15GB)",
#             "speaker-4m_video.h5 (?GB)",
#             "speaker-4m_metadata.csv (8.3MB)",
#         ],
#     )
# )

print(
    make_downloads_modal(
        "Edison-4M",
        [
            "edison-4m_audio.h5 (44GB)",
            "edison-4m_video.h5 (?GB)",
            "edison-4m_metadata.csv (76MB)",
        ],
    )
)


print(
    make_downloads_modal(
        "SoloGerbil-4M",
        [
            "sologerbil-4m_audio.h5 (7.5GB)",
            "sologerbil-4m_video.h5 (?GB)",
            "sologerbil-4m_metadata.csv (41MB)",
        ],
    )
)


print(
    make_downloads_modal(
        "GerbilEarbud-4M",
        [
            "gerbilearbud-4m_audio.h5 (1.3GB)",
            "gerbilearbud-4m_video.h5 (?GB)",
            "gerbilearbud-4m_metadata.csv (?MB)",
        ],
    )
)


print(
    make_downloads_modal(
        "Hexapod-8M",
        [
            "hexapod-8m_audio.h5 (236GB)",
            "hexapod-8m_video.h5 (?GB)",
            "hexapod-8m_metadata.csv (?MB)",
        ],
    )
)


print(
    make_downloads_modal(
        "MouseEarbud-24M",
        [
            "mouseearbud-24m_audio.h5 (208GB)",
        ],
    )
)


print(
    make_downloads_modal(
        "SoloMouse-24M",
        [
            "solomouse-24m_audio.h5 (362MB)",
        ],
    )
)
