def pixel_to_binary(value):
    return format(value, "08b")


pixel = 173

print("Pixel:", pixel)
print("Binary:", pixel_to_binary(pixel))