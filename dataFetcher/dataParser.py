import os
from bs4 import BeautifulSoup

class Parser:

    def __init__(self):
        self._className = os.getenv("CLASS_NAME")

    def get_substitution_of_class(self, data):
        soup = BeautifulSoup(data, 'html.parser')
        table = soup.find('table').find_all('tr')[1:]
        general_substitutions = []
        substitutions = []
        for el in table:
            withoutTr = str(el).replace('<tr class="svp-gerade">', '').replace('<tr class="svp-ungerade">', '').replace(' </tr>', '')
            content = withoutTr.split("\r\n")[1:]
            element = []
            for x in content:
                element.append(x.split('>')[1].replace('</td', ''))
            general_substitutions.append(element[:-1])
        lastClass = ""
        for sub in general_substitutions:
            if sub[0] == "" or sub[0] == " ":
                if lastClass == self._className:
                    substitutions.append(sub)
            if sub[0].replace(' ', '') == self._className:
                substitutions.append(sub)
                lastClass = sub[0].replace(' ', '')
        return substitutions





