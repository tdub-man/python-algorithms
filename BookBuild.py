from urllib import request
import subprocess
from bs4 import BeautifulSoup
from itertools import count
import shutil
import os
from tempfile import TemporaryDirectory as tDir
# from functools import partial


def parseChaps(source):
    with request.urlopen(source) as response:
        soup = BeautifulSoup(response,"html.parser")
        listLinks = [ a.get("href") for a in soup.find_all('a') if a.parent.name == "li" ]
        return listLinks
def toPDF(chapRoot,chaps,bookName):
    with tDir() as t:
        startDir = os.getcwd()
        os.chdir(t)
        for c,i in zip(chaps,count()):
            subprocess.call(["echo","Converting " + chapRoot + c])
            subprocess.call(["wkhtmltopdf", chapRoot + c, "Part-{:02d}.pdf".format(i)])
        pdfName = "{0}.pdf".format(bookName)
        args = ["gs","-dBATCH","-dNOPAUSE","-q",
            "-sDEVICE=pdfwrite","-dPDFSETTINGS=/prepress",
            "-sOutputFile="+pdfName,"*.pdf"]
        subprocess.call(["echo","\nJoining PDF's..."])
        subprocess.call(" ".join(args),shell=True)
        shutil.move(pdfName,startDir)

def testCL():
    cl = "http://www.gigamonkeys.com/book/"
    clBook = "Practical-CL"
    chs = parseChaps(cl)
    toPDF(cl,chs,clBook)
def testHS():
    hs = "http://learnyouahaskell.com/chapters/"
    hsroot = "http://learnyouahaskell.com/"
    hsBook = "LYA-Haskell"
    chs = parseChaps(hs)
    toPDF(hsroot,chs,hsBook)

testCL()
# testHS()
