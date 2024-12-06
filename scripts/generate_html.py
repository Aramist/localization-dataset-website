import argparse
import json
import typing as tp
from pathlib import Path

newline = "\n"


def load_txt(file_path: str) -> str:
    with open(file_path, "r") as ctx:
        return ctx.read()


def load_json(file_path: str) -> dict:
    with open(file_path, "r") as ctx:
        return json.load(ctx)


output_path = Path("src/index.html")
template_dir = Path("scripts/templates")
strings_dir = Path("scripts/strings")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--strings", type=Path)
    ap.add_argument("--templates", type=Path)
    ap.add_argument("-o", "--output", type=Path)
    args = ap.parse_args()
    template_dir = args.templates
    strings_dir = args.strings
    output_path = args.output

DATASET_CARD_TEMPLATE = load_txt(template_dir / "dataset_card.template.html")
ENVIRONMENT_CARD_TEMPLATE = load_txt(template_dir / "environment_card.template.html")
DATASET_DETAIL_MODAL_TEMPLATE = load_txt(
    template_dir / "dataset_detail_modal.template.html"
)
DATASET_DOWNLOAD_MODAL_TEMPLATE = load_txt(
    template_dir / "dataset_download_modal.template.html"
)
ENVIRONMENT_DETAIL_MODAL_TEMPLATE = load_txt(
    template_dir / "environment_detail_modal.template.html"
)

dataset_info = load_json(strings_dir / "dataset_info.json")
environment_info = load_json(strings_dir / "environment_info.json")


def make_link_list(links: list[dict[str, str]]) -> str:
    """Generates an html list of links from a list of dictionaries containing link information.

    Args:
        links (list[dict[str, str]]): A list of dictionaries containing link information. Each dictionary should have the following keys:
            - url (str): The URL of the link.
            - size (str): The size of the file at the URL.
    """

    links_text = []
    # First link is primary, rest are secondary
    for i, link in enumerate(links):
        class_type = "link-primary" if i == 0 else "link-secondary"
        name = Path(link["url"]).name
        links_text.append(
            f"<li><a class='{class_type}' href='{link['url']}'>{name}({link['size']})</a></li>"
        )
    return f"<ul>{newline}{newline.join(links_text)}{newline}</ul>"


def make_bullet_list(items: list[str]) -> str:
    """Given a list of strings, return a formatted HTML list of items.

    Args:
        items (list): A list of strings to be formatted as a bullet list.
    """
    list_items = []
    for item in items:
        if "<p" not in item:
            item = f"<p class='text-dark'>{item}</p>"
        else:
            item = item
        list_items.append(f"<li>{item}</li>")
    # list_items = "\n".join(
    #     [f"<li><p class='text-dark'>{item}</p></li>" for item in items]
    # )
    list_items = "\n".join(list_items)

    return f"""<ul>
        {list_items}
    </ul>"""


def generate_dataset_card(dataset_info: dict[str, tp.Any]) -> str:
    """Given a dictionary of information about a dataset, return a formatted card
    as a string of HTML text.

    Args:
        card_data (dict): A dictionary containing information about a dataset.
            The dictionary should have the following keys:
            - card_title (str): The title of the dataset.
            - card_bg_image_url (str): The URL of the background image for the card.
            - short_description (str): A short description of the dataset.
            - size (str): The size of the dataset.
    """

    return DATASET_CARD_TEMPLATE.format(**dataset_info)


def generate_environment_card(environment_info: dict[str, tp.Any]) -> str:
    """Given a dictionary of information about an environment, return a formatted card
    as a string of HTML text.

    Args:
        environment_info (dict): A dictionary containing information about an environment.
            The dictionary should have the following keys:
            - card_title (str): The title of the environment.
            - card_bg_image_url (str): The URL of the background image for the card.
            - short_description (str): A short description of the environment.
    """
    return ENVIRONMENT_CARD_TEMPLATE.format(**environment_info)


def generate_download_modal(dataset_info: dict[str, tp.Any]) -> str:
    """Generates html text for a modal containing download links for a dataset.

    Args:
        modal_data (dict[str, str]):

    Returns:
        str: HTML text for a modal containing download links for a dataset.
    """
    links = make_link_list(dataset_info["links"])
    rendered_html = DATASET_DOWNLOAD_MODAL_TEMPLATE.format(
        **dataset_info, links_list=links
    )
    return rendered_html


def generate_dataset_details_modal(dataset_info: dict[str, tp.Any]) -> str:
    """Generates html text for a modal containing details about a dataset.

    Args:
        modal_data (dict[str, str]): A dictionary containing information about a dataset. Expects the following keys:
            - card_title (str): The title of the dataset.
            - card_bg_image_url (str): The URL of the background image for the card.
            - short_description (str): A short description of the dataset.
            - full_description (str): A full description of the dataset.
            - num_samples (int): The number of samples in the dataset.
            - size (str): The size of the dataset.
            - environment (str): The environment in which the dataset was recorded.
            - num_microphones (int): The number of microphones used to record the dataset.
            - sampling_rate (str): The sampling rate of the dataset.
            - additional_bullets (list[str]): A list of additional details about the dataset.

    Returns:
        str: HTML text for a modal containing details about a dataset.
    """
    list_items = [
        dataset_info["full_description"],
        f"# samples: {dataset_info['num_samples']}",
        *dataset_info["additional_bullets"],
        f"# microphones: {dataset_info['num_microphones']}",
        f"Sampling rate: {dataset_info['sampling_rate']}",
        f"Environment: {dataset_info['environment']}",
        f"Size: {dataset_info['size']}",
    ]
    html_list = make_bullet_list(list_items)
    rendered_html = DATASET_DETAIL_MODAL_TEMPLATE.format(**dataset_info, list=html_list)
    return rendered_html


def generate_environment_details_modal(environment_info: dict[str, tp.Any]) -> str:
    """Generates html text for a modal containing additional details about an environment.

    Args:
        environment_info (dict[str, tp.Any]): Information dictionary for the environment. Expects the following keys:
            - card_title (str): The title of the environment.
            - card_bg_image_url (str): The URL of the background image for the card.
            - short_description (str): A short description of the environment.
            - full_description (str): A full description of the environment.
            - num_microphones (int): The number of microphones in the environment.
            - microphone_model (str): The model of the microphones in the environment.
            - sampling_rate (str): The sampling rate of the environment.
            - dimensions (list[str]): The dimensions of the environment.

    Returns:
        str: html text
    """

    list_items = [
        environment_info["full_description"],
        f"# microphones: {environment_info['num_microphones']}",
        f"Microphone model: {environment_info['microphone_model']}",
        f"Sampling rate: {environment_info['sampling_rate']}",
        "Dimensions (m):",
        make_bullet_list(environment_info["dimensions"]),
    ]
    html_list = make_bullet_list(list_items)
    rendered_html = ENVIRONMENT_DETAIL_MODAL_TEMPLATE.format(
        **environment_info, list=html_list
    )
    return rendered_html


def generate_webpage():
    """Generates the main page from the master template, subtemplates, and data files."""

    master_template = load_txt("scripts/templates/index.template.html")
    dataset_cards = [generate_dataset_card(dataset) for dataset in dataset_info]
    environment_cards = [generate_environment_card(env) for env in environment_info]
    dataset_details_modals = [
        generate_dataset_details_modal(dataset) for dataset in dataset_info
    ]
    environment_details_modals = [
        generate_environment_details_modal(env) for env in environment_info
    ]
    download_modals = [generate_download_modal(dataset) for dataset in dataset_info]

    return master_template.format(
        dataset_cards="\n".join(dataset_cards),
        environment_cards="\n".join(environment_cards),
        dataset_details_modals="\n".join(dataset_details_modals),
        environment_details_modals="\n".join(environment_details_modals),
        download_modals="\n".join(download_modals),
    )


if __name__ == "__main__":
    with open(output_path, "w") as f:
        f.write(generate_webpage())
    print(f"Successfully wrote webpage to {output_path}")
