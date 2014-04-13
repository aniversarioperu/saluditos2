#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import datetime
import subprocess
from glob import glob
import requests
import codecs
import brewer2mpl
import sys
import glob
import itertools as it
from time import sleep
import random
import re

import os.path


def plot_saluditos(filename):
    filename = re.sub(".csv", "", filename)

    import numpy as np
    plt.rcParams['font.family'] = 'Dosis'

    y_axis = []
    dates = []

    sorted_datos = []
    with codecs.open(filename + ".csv", "r", "utf-8") as handle:
        datos = handle.readlines()
        for i in datos:
            i = i.strip().split(",")
            date = i[1]
            date = datetime.datetime.strptime(date, "%d/%m/%Y")
            sorted_datos.append((date, i[0]))
            #dates.append(date)

            #y_axis.append(i[0])
    sorted_datos.sort()
    for i in sorted_datos:
        y_axis.append(int(i[1]))
        dates.append(i[0])

    # queremos color
    set2 = brewer2mpl.get_map('Set2', 'qualitative', 3).mpl_colors
    color = set2[0]

    fig, ax = plt.subplots(1)
    if 'dia' in filename and 'Molina' in filename:
        ax.set_title(u'Saludos por día, Agustín Molina', fontsize=20,
                fontweight='bold')
    else:
        ax.set_title(u'Saludos por día emitidos por el Congreso', fontsize=20,
                fontweight='bold')
    ax.tick_params(color="gray")
    for spine in ax.spines.values():
        spine.set_edgecolor("gray")

    plt.plot(dates, y_axis, color=color)
    plt.xticks(rotation="45")
    plt.tight_layout()
    plt.savefig(filename + ".png")

    print y_axis

    y_values = []
    x_labels = []
    # calcular nuevos followers por semana
    for i,grp in it.groupby(dates, lambda i: (i.date() - dates[0].date()).days // 7):
        j = 0
        semana = list(grp)
        x_labels.append(semana[0].date())
        tmp = 0
        for k in semana:
            index = dates.index(k)
            tmp += y_axis[index]
        y_values.append(tmp)
    print y_values


    ind = np.arange(len(y_values))
    fig, ax = plt.subplots(1)
    rects1 = ax.bar(ind, y_values, width=0.5, color="#2ecc71", edgecolor="#3498db")
    ax.set_xticks(ind + 0.2)
    if 'dia' in filename and 'Molina' in filename:
        ax.set_title(u'Saludos por semana, Agustín Molina', fontsize=20,
                fontweight='bold')
    else:
        ax.set_title(u'Saludos por semana emitidos por el Congreso', fontsize=20,
                fontweight='bold')

    ax.tick_params(axis="x", color="gray", labelsize=8)
    for spine in ax.spines.values():
        spine.set_edgecolor("gray")

    ax.set_xticklabels(x_labels)
    plt.ylim([0,max(y_values) + 2])
    plt.xticks(rotation="90")
    plt.tight_layout()
    plt.savefig(filename + "_semana.png")

for filename in glob.glob("*csv"):
    plot_saluditos(filename)
