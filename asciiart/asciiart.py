from PIL import Image
import argparse

def make_asciiart(imagepath, w=500):
    img = Image.open(imagepath)
    width, height = img.size
    height = int(w / width * height)
    width = w
    img = img.resize((width, height))
    text = ""
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            if img.mode == "RGBA":
                pixel = pixel[:3]
            average = (pixel[0] + pixel[1] + pixel[2]) / 3
            if average < 60:
                text += "88"
            elif average < 120:
                text += "00"
            elif average < 180:
                text += "11"
            else:
                text += "  "
        text += "\n"
    return text

def main():
    parser = argparse.ArgumentParser(description="This is an asciiart generator")
    parser.add_argument("image")
    parser.add_argument("-w", "--width")
    args = parser.parse_args()
    if args.width == None:
        print(make_asciiart(args.image))
    else:
        print(make_asciiart(args.image, int(args.width)))

if __name__ == "__main__":
    main()

