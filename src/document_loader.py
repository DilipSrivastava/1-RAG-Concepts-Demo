from numpy import add
from pypdf import PdfReader

class DocumentLoader:

    def load_pdf(self, file):
        """Load text from a PDF file."""
        
        print("Executing PDF document loader")

        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    