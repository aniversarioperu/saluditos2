#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
from glob import glob
from bs4 import BeautifulSoup
import sys
import json


def extract_data():
    rows = []
    for filename in glob("html/*html"):
        with codecs.open(filename, "r", "latin-1") as handle:
            soup = BeautifulSoup(handle.read())
            table = soup.find('table', attrs={'align':'center'})
            for row in table.find_all('tr'):
                rows.append([val.text.strip() for val in row.find_all('td', attrs={'class':'menu1'})])

    data = [] 
    for row in rows:
        if len(row) > 2:
            obj = {}
            obj['fecha'] = row[0]
            obj['numero'] = row[1]
            obj['titulo'] = row[3]
            obj['autores'] = row[4]
            data.append(obj)

    with codecs.open("saluditos.json", "w", "utf-8") as writer:
        writer.write(json.dumps(data, indent=4))

def clean_data():
    with codecs.open("saluditos.json", "r", "utf-8") as handle:
        new_data = []
        data = json.loads(handle.read())
        for i in data:
            if i['titulo'].startswith("Interpelar") or \
                    i['titulo'].startswith("SUMILLA") or \
                    i['titulo'].startswith("Acuerdan") or \
                    i['titulo'].startswith("Autorizar") or \
                    i['titulo'].startswith("Ampl") or \
                    i['titulo'].startswith("Censur") or \
                    u"Comisión Investigadora" in i['titulo'] or \
                    i['titulo'].startswith("Considerar") or \
                    i['titulo'].startswith("Constituir") or \
                    i['titulo'].startswith("Convocar") or \
                    i['titulo'].startswith("Decl") or \
                    i['titulo'].startswith("Demandar") or \
                    i['titulo'].startswith("El procedi") or \
                    i['titulo'].startswith("Exhortar") or \
                    i['titulo'].startswith("Implementar") or \
                    i['titulo'].startswith("Incluir") or \
                    i['titulo'].startswith("Incorporar") or \
                    i['titulo'].startswith("Instar") or \
                    i['titulo'].startswith("Invitar") or \
                    i['titulo'].startswith("Moci") or \
                    i['titulo'].startswith("Otorgar") or \
                    i['titulo'].startswith("Que el Pleno") or \
                    i['titulo'].startswith("Ratificar") or \
                    i['titulo'].startswith("Reafirmar") or \
                    i['titulo'].startswith("Recomendar") or \
                    i['titulo'].startswith("Respaldar") or \
                    i['titulo'].startswith("Exigir") or \
                    i['titulo'].startswith("Solicitar") or \
                    i['titulo'].startswith("Suspender") or \
                    i['titulo'].startswith("Conformar"):
                pass
            else:
                new_data.append(i)
    with codecs.open("saluditos_limpiados.json", "w", "utf-8") as handle:
        handle.write(json.dumps(new_data, indent=4))


extract_data()

clean_data()

# numero de saludos congresista molina
fechas = []
with codecs.open("saluditos_limpiados.json", "r", "utf-8") as handle:
    for i in json.loads(handle.read()):
        if 'molina' in i['autores'].lower():
            print i['fecha']

