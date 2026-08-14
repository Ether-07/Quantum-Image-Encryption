from src.image.preprocessing import (
    load_image,
    convert_to_grayscale,
    image_to_array,
    split_into_blocks
)


input_path = "images/test.png"

image = load_image(input_path)

print("Original image:")
print("Size:", image.size)
print("Mode:", image.mode)

gray_image = convert_to_grayscale(image)

print("\nGrayscale image:")
print("Size:", gray_image.size)
print("Mode:", gray_image.mode)

pixels = image_to_array(gray_image)

print("\nPixel array:")
print("Shape:", pixels.shape)
print("Data type:", pixels.dtype)
print("Minimum:", pixels.min())
print("Maximum:", pixels.max())

blocks = split_into_blocks(
    pixels,
    block_size=8
)

print("\nBlock information:")
print("Number of blocks:", len(blocks))
print("First block shape:", blocks[0].shape)

print("\nFirst block:")
print(blocks[0])