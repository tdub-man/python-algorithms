from urllib import request
from subprocess import call as s_call
from bs4 import BeautifulSoup
from itertools import count
from shutil import move as mv
from os import getcwd,chdir
from tempfile import TemporaryDirectory as tDir


def parseChaps(source):
    with request.urlopen(source) as response:
        soup = BeautifulSoup(response,"html.parser")
        listLinks = [ a.get("href") for a in soup.find_all('a') if a.parent.name == "li" ]
        return listLinks
def toPDF(chapRoot,chaps,bookName):
    with tDir() as t:
        startDir = getcwd()
        chdir(t)
        for c,i in zip(chaps,count()):
            s_call(["echo","Converting " + chapRoot + c])
            s_call(["wkhtmltopdf", chapRoot + c, "Part-{:02d}.pdf".format(i)])
        pdfName = "{0}.pdf".format(bookName)
        args = ["gs","-dBATCH","-dNOPAUSE","-q",
            "-sDEVICE=pdfwrite","-dPDFSETTINGS=/prepress",
            "-sOutputFile="+pdfName,"*.pdf"]
        s_call(["echo","\nJoining PDF's..."])
        s_call(" ".join(args),shell=True)
        mv(pdfName,startDir)

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
