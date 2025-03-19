from pypdf import PdfReader, PdfWriter, generic
from config import Config
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.units import mm
import io


class Combiner:
    config: Config
    pagesize: tuple[float, float]
    x: float

    def __init__(self, config: Config) -> None:
        self.config = config
        if config.language == "EN":
            self.pagesize = letter
            self.x = 130.5
        else:
            self.pagesize = A4
            self.x = 134.5

    def combine(self):
        sources = self.config.files
        target_file = PdfWriter()
        page_number = 1

        # append output pages and annotations in toc
        for source in sources:
            try:
                pdf = PdfReader(source.path)
                for page in pdf.pages:
                    if source.id is not None:
                        page.merge_page(
                            self.add_button_page_number(page_number))
                        page_number += 1
                    target_file.add_page(page)
                if len(source.title) > 0:
                    target_file.add_outline_item(
                        title=source.title, page_number=source.page, fit=generic.Fit.xyz())
            except Exception:
                continue
        metadata = {}
        metadata["/Producer"] = ""
        target_file.page_mode = "/UseOutlines"
        target_file.add_metadata(metadata)
        for page in target_file.pages:
            page.compress_content_streams()
        target_file.write(self.config.destination)

    def add_button_page_number(self, page_number: int):
        buffer = io.BytesIO()
        can = canvas.Canvas(buffer, pagesize=self.pagesize)
        can.setFont("Times-Roman", 8)
        can.drawString(self.x * mm, 7 * mm,
                       f"{page_number} / {self.config.total}")
        can.save()
        p = PdfReader(buffer)
        return p.pages[0]
