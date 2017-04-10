import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
from cStringIO import StringIO
from wand.image import Image
from PIL import Image as PI
import pyocr
import pyocr.builders
import io

def pdfparser(data):
    tool = pyocr.get_available_tools()[0]
    lang = 'eng+ell'
    req_image = []
    final_text = []
    words = []
    image_pdf = Image(filename=data, resolution=600)
    image_jpeg = image_pdf.convert('jpeg')
    for img in image_jpeg.sequence:
        img_page = Image(image=img)
        req_image.append(img_page.make_blob('jpeg'))
    for img in req_image:
        txt = tool.image_to_string(
            PI.open(io.BytesIO(img)),
            lang=lang,
            builder=pyocr.builders.TextBuilder()
        )
        final_text.append(txt)
    for x in final_text:
        try:
            word = x.encode('utf8')
            print(word)

        except UnicodeEncodeError , e:
            print(e)
            continue

if __name__ == '__main__':
    pdfparser(sys.argv[1])
