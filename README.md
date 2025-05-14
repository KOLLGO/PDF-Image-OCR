# PDF Image OCR
A Python Program extracting Images from a pdf-file and extracting the text using Optical Character Recognition
# Requirements
- Python Version 3.11
```bash 
pip install -r requirements.txt
```
- Install [Tesseract](https://github.com/tesseract-ocr/tesseract) and copy the path

# Var.py
This is where the Paths are saved, change these according to your System
- `tesseract_path`: The Path to your `tesseract.exe` file (Windows Default: `C:\\Program Files\\Tesseract-OCR\\tesseract.exe`)
- input_path: Path to your PDF-File (example: `"example_folder\\example.pdf"`)
- output_path: The extracted images and Text will go here (example: `".\\out\\"`)
- lang: language of the PDF (example: `"deu+eng"` for German and English)

# Extras
- If you already have got images:
  - place them in your `output_path` Folder
  - comment out the method call `image_extraction()` (to: `#image_extraction()`)
  - delete the `+ folder` in the line saying `input_folder = output_path + folder`
- If you only want to extract the images and do nott want to use OCR
  - comment out the line saying `ocr(input_folder, out_txt, lang)` (to: `#ocr(input_folder, out_txt, lang)`)
