import logging

import requests
from requests.exceptions import HTTPError, ConnectionError

logging.basicConfig(level=logging.DEBUG)


def download_images(img_links, dir_path, req_headers=None):
    """
    Download all the images from a list of links and save them to the target directory.

    :param img_links: List of image links
    :param dir_path: String of directory path
    :param req_headers: Dictionary of headers sent with GET requests, usually contains user-agent header
    :return:
    """

    def get_image_name(img_link):
        return img_link.split('/')[-1]

    logging.info("Downloading images starts")
    for link in img_links:
        img_name = get_image_name(link)

        try:
            # Download image
            img = requests.get(link, headers=req_headers)
            img.raise_for_status()

            # Save image
            file_path = f'{dir_path}/{img_name}'
            with open(file_path, 'wb') as handle:
                handle.write(img.content)

        except HTTPError as e:
            logging.debug(e)
        except ConnectionError as e:
            logging.debug(e)

        except FileExistsError as e:
            logging.debug(e)
        except FileNotFoundError as e:
            logging.debug(e)

    logging.info("Downloading images completes")
