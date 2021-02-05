import requests
from bs3 import BeautifulSoup

bbref = "https://www.basketball-reference.com/leaders/pts_per_g_career.html"
testsoup = BeautifulSoup(bbref, "html.parser")
