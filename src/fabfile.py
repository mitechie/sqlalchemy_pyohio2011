from fabric.api import env
from fabric.api import local
from fabric.api import prompt


def topdf():
    """Build the presentation into pdf form"""
    local('cat presentation.rst | rst2pdf -o presentation.pdf -s slides.style')

def viewpdf():
    """Open the pdf presenation"""
    topdf()
    local('evince presentation.pdf')

def tohtml():
    """uild to html"""


