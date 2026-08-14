from PIL import Image
import numpy as np


def load_image(path):
    """
    Load an image from disk.
    """

    image = Image.open(path)

    return image


def convert_to_grayscale(image):
    """
    Convert an image to grayscale.
    """

    return image.convert("L")


def image_to_array(image):
    """
    Convert a PIL image into a uint8 NumPy array.
    """

    return np.array(image, dtype=np.uint8)


def split_into_blocks(image_array, block_size=8):
    """
    Split a 2D grayscale image into square blocks.
    """

    height, width = image_array.shape

    if height % block_size != 0 or width % block_size != 0:
        raise ValueError(
            "Image dimensions must be divisible by block size."
        )

    blocks = []

    for row in range(0, height, block_size):
        for col in range(0, width, block_size):

            block = image_array[
                row:row + block_size,
                col:col + block_size
            ]

            blocks.append(block.copy())

    return blocks


def flatten_block(block):
    """
    Convert an image block into a one-dimensional array.
    """

    return block.flatten()