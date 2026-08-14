from pathlib import Path

import numpy as np
from PIL import Image


def save_image(image, output_path):
    """
    Save a PIL Image or NumPy array to an image file.

    Creates the parent output directory automatically.
    """

    output_path = Path(output_path)

    # Create the output directory if it doesn't exist.
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Convert NumPy arrays to PIL Images.
    if isinstance(image, np.ndarray):
        if image.dtype != np.uint8:
            image = np.clip(image, 0, 255).astype(np.uint8)

        image = Image.fromarray(image)

    # Save the resulting PIL Image.
    image.save(output_path)


def array_to_image(array):
    """
    Convert a NumPy array into a PIL Image.
    """
    array = np.asarray(array)

    if array.dtype != np.uint8:
        array = np.clip(array, 0, 255).astype(np.uint8)

    return Image.fromarray(array)