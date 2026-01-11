from pypdf import PdfReader

def load_contract(file):
    reader = PdfReader(file.file)
    text = ""
    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content + "\n"
    return text
