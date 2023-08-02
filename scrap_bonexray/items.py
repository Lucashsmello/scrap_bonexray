from dataclasses import dataclass


@dataclass
class ImageItem:
    age_month: int
    body_region: str
    image_urls: list[str]
    images = None
    filename: str
