# PDF Image OCR
A Python Program extracting Images from a pdf-file and extracting the text using Optical Character Recognition. Afterwards, you may feed an LLM running locally via [Ollama](https://github.com/ollama/ollama) with the data. 
# Requirements
- The Project was made for Windows. If your OS is another like macOS or Linux, you need to adjust some paths because of `\\`.
- Python Version 3.11
```bash 
pip install -r requirements.txt
```
- Install [Tesseract](https://github.com/tesseract-ocr/tesseract) and copy the path
- Install [Ollama](https://ollama.com)
- in console (example model: `llama3.2`):
  ```bash
  ollama pull <YourModel>
  ```

# Var.py
This is where the Paths are saved, change these according to your System
- `tesseract_path`: The Path to your `tesseract.exe` file (Windows Default: `C:\\Program Files\\Tesseract-OCR\\tesseract.exe`)
- input_path: Path to your PDF-File (example: `"example_folder\\example.pdf"`)
- output_path: The extracted images and Text will go here (example: `".\\out\\"`)
- lang: language of the PDF (example: `"deu+eng"` for German and English)
- model: the ollama model you want to use (example: `llama3.2` for English, `cas/discolm-mfto-german` for German)

# Extras
- If you already have got images:
  - place them in your `output_path` folder
  - comment out the method call `image_extraction()` (to: `#image_extraction()`)
  - delete the `+ folder` in the line saying `input_folder = output_path + folder`
- If you only want to extract the images and do not want to use OCR/AI
  - comment out the method call `ocr(input_folder, out_txt, lang)` (to: `#ocr(input_folder, out_txt, lang)`)
  - comment out the method call `feedllm()` (to: `#feedllm()`)
- If you only want to use the AI with a txt file you have:
  - comment out the method call `image_extraction()` (to: `#image_extraction()`)
  - delete the `+ folder` in the line saying `input_folder = output_path + folder`
  - comment out the method call `ocr(input_folder, out_txt, lang)` (to: `#ocr(input_folder, out_txt, lang)`)
  - place the `.txt` file in your `output_path` folder and rename it to `out.txt`
