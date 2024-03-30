import cv2

def pixel2ascii(pixel):
 
    ascii_chars = "(@%$^*=-:. "
    #ascii_chars = "(*%$#^=-:. "
    return ascii_chars[int(pixel / 255 * len(ascii_chars)-1)]

def image2ascii(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    height, width = image.shape
    aspect_ratio = width / height
    output_width = 100
    output_height = int(output_width /2*aspect_ratio)
    image = cv2.resize(image, (output_width, output_height))
    ascii_image = ""
    for row in image:
        for pixel in row:
            ascii_image += pixel2ascii(pixel)
        ascii_image += "\n"
    return ascii_image

if __name__ == "__main__":
    path = "download.jpeg"
    print(image2ascii(path))
