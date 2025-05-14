import os
from pdf2image import convert_from_path
from var import input_path, output_path, lang, tesseract_path
import pytesseract
from PIL import Image


def image_extraction():
    if(not os.path.isdir(output_path+folder)):
        os.makedirs(output_path + folder)
    for i in range(len(images)):
        images[i].save(output_path + folder + '\\page' + str(i) + '.jpg', 'JPEG')


def ocr(input_folder, output_file, language):
    supported_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tiff")
    pytesseract.pytesseract.tesseract_cmd = tesseract_path

    try:
        with open(output_file, "w", encoding="utf-8") as out_f:
            for filename in os.listdir(input_folder):
                if filename.lower().endswith(supported_extensions):
                    image_path = os.path.join(input_folder, filename)
                    try:
                        img = Image.open(image_path)
                        text = pytesseract.image_to_string(img, lang=language)

                        if text.strip():
                            out_f.write(f"\n\n─── {filename} ───\n")
                            out_f.write(text)
                            print(f"Text extracted from {filename}.")
                        else:
                            print(f"No Text Recognized in {filename}.")
                    except Exception as e:
                        print(f"Error at {filename}: {e}")

        print(f"\nText saved in {output_file}")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    # Image Output Folder
    splitpath = input_path.split("\\")
    images = convert_from_path(input_path)
    folder = splitpath[-1]
    splitpath = folder.split(".")
    folder = splitpath[0]

    image_extraction()

    #args OCR
    out_txt = output_path + folder + '\\out.txt'
    input_folder = output_path + folder

    ocr(input_folder, out_txt, lang)
