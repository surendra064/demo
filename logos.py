#!python3.6
import fitz  # PyMuPDF
import pytesseract
import cv2
import numpy as np
import glob, os
import PIL
from slugify import slugify


def get_pixmaps_in_pdf(pdf_filename):
    doc = fitz.open(pdf_filename)
    xrefs = set()
    for page_index in range(doc.page_count):
        for image in doc.get_page_images(page_index):
            # print(image[0])
            xrefs.add(image[0])  # Add XREFs to set so duplicates are ignored
    pixmaps = [fitz.Pixmap(doc, xref) for xref in xrefs]
    doc.close()
    return pixmaps


def write_pixmaps_to_pngs(pixmaps):
    cnt = 0
    for i, pixmap in enumerate(pixmaps):
        # img = np.frombuffer(buffer=pixmap.samples, dtype=np.uint8).reshape((pixmap.height, pixmap.width, -1))
        # img = pixmap.pil_tobytes(format="png", optimize=True)
       
        try:
            pix = PIL.Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
            img = np.array(pix)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(gray)
            if(str(text)==""):
                text="logo"+str(i)
            text = slugify(text)
            
            print(text)
            pixmap.save(f'logoss\\{text}.png')
            cnt+=1
            
        except:
            print("Error loading image... [working on fix]")
    return  cnt

fpath = "C:\\Users\\SURENDRA\\Documents\\demoo\\files\\**\\*.pdf"


for file in glob.glob(fpath, recursive=True):
    print(f"Processing {file}")
    pixmaps = get_pixmaps_in_pdf(file)
    
    cnt = write_pixmaps_to_pngs(pixmaps)
    print(f"Found {cnt} logos")

# pixmaps = get_pixmaps_in_pdf('files\\011_ManagerFlash__04-02-23.pdf')
# write_pixmaps_to_pngs(pixmaps)