# Ivan Tinov, ID# 110255332, CSE 337 HW1_q3
import urllib.request
from bs4 import BeautifulSoup


def one_step_ahead():
    r = urllib.request.urlopen("https://finance.yahoo.com/commodities/").read()
    website = BeautifulSoup(r, "html.parser")

    file = open('commodoties.txt', 'w')
    td = website.find_all('td')
    td_line = ""
    j = 0
    for i in td:
        if i.get_text() == "":
            file.write(td_line[:-1] + "\n")
            td_line = ""
            j = 0
        else:
            if j < 5:
                td_line = td_line + i.get_text() + ","
                j += 1
    file.close()


one_step_ahead()

