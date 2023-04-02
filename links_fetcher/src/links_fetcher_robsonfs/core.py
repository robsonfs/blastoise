from typing import Optional

import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet


def get_source(url: str) -> (int, str):
    try:
        resp = requests.get(url)
    except Exception as err:
        raise Exception("Could not fetch the provided URL")

    return resp.status_code, resp.text


def tag_extractor(url: str, tag_name: Optional[str] = "a") -> ResultSet:
    """The standard behaviour is to return a list of "a" elements. But it should
    work with any HTML tag. (Not tested with any tag other than "a", though)."""
    _, source = get_source(url)  # Ignoring status_code for now
    soup = BeautifulSoup(source, "html.parser")

    return soup.find_all(tag_name)


    
