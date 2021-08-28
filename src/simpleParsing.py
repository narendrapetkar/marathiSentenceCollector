from ebooklib import epub

from bs4 import BeautifulSoup
from ebooklib import epub
import ebooklib
import time, os

bookpath = "../books/sampleBook.epub"
book = epub.read_epub(bookpath)
fname = time.strftime("%Y_%m_%d_%H_%M_%S_output.txt")

chapText = []
finalList = []
devnagariNumbers = ['०', '१', '२', '३', '४', '५', '६', '७', '८', '९']
latinNumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
specialChars = ['~', '`', '@', '#', '$', '^', '&', '*', '(', ')', '-', '_', '=',
                 "+", '{', '}', '[', ']', '\\', "/"]

if not os.path.exists("../output"):
    os.mkdir("../output")

def selectLine(line):
    """
    Rules :
        1. There should be no numbers

    """
    # rule 1 : sentence should not have numbers
    for ch in devnagariNumbers + latinNumbers:
        if ch in line:
            return False
    # rule 6 : sentence should not be longer than 14 words
    # additional filter added to have more meaningful sentences
    strLen = len(line.split(" "))
    if strLen >=15 or strLen<=5:
        return False
    
    # rule 4 : no special characters
    for sc in specialChars:
        if sc in line:
            return False

    # rule 5 : Foreign letters should not be included 
    for ch in line:
        if ord(ch) < int("0x900", 16) or ord(ch) > int("0x097F", 16):
            # unicode range out of devnagari characters
            if ch not in specialChars:
                # characters allowed in marathi e.g. ; : ; "" '' ?
                # these are not a part of specialChars
                return True
            else:
                return False
    # if no rule blocking
    return True

with open("../output/"+fname,'w',encoding = 'utf-8') as f:
    for i in book.get_items():
        if i.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(i.get_content(), "html.parser")
            chapText.append(soup.get_text(strip=True))
            for ct in chapText:
                lines = ct.split("\n")
                sentences = list()
                for line in lines:
                    sentences.extend(line.split("."))
                if sentences!= None:
                    if len(sentences) <= 0:
                        continue
                else:
                    continue
                for sentence in sentences:
                    if selectLine(sentence):
                        f.write(sentence.strip() + ".\n")