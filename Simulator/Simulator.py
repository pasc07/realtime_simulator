# Ordonnanceur
from math import inf

from Const.Const import JOB
from GBP.Adder import Adder
from GBP.Buf import Buf
from GBP.Gen import Gen
from GBP.Proc import Proc
from GBP.step import Step
import matplotlib.pyplot as plt
import numpy as np

from Plot.PlotData import plot_step


def Simulator():
    t = 0
    t_fin = 10
    ta = 0
    gen = Gen("Generator 1")
    proc = Proc("Process 1")
    buf = Buf("Buffer 1")
    Components = [gen, buf, proc]
    imms = []

    # init
    for component in Components:
        component.init()
        ta = component.avancement()
        component.tr = ta  # tr = ta en s0
        print(f'Les composants:{component.name}\nta = {ta}')

    print("********Les evolutions*********")
    print(f't:  {t}')
    while t < t_fin:
        imms = []
        list_tr = []
        # for component in Components:
        #     print(f'La liste des events avant: {ins}')
        # recuperer les tr dans une liste
        for component in Components:
            list_tr.append(component.tr)
            print(f'tr {component.name}: {component.tr}')
        # recup le min de la liste
        tr_min = min(list_tr)

        # Faire une liste des composants imminents
        for component in Components:
            if component.tr == tr_min:
                imms.append(component)

        # print(f'Imms :{imms}')
        t = t + tr_min
        # mettre a jour te et tr
        for component in Components:
            component.te += tr_min
            component.tr -= tr_min

        for component in Components:
            component.generateOutput()
        # for component in Components:
        # print(f'La liste des events {component.name}: {component.inputEvents}')
        # Liste des entree impactee par les sortie
        ins = {}
        for component in Components:
            ins.update(component.outputEvents)
        print(f'La liste des entrees impactees : {ins}')

        # Recherche si l'entree est presente et mettre dans inputEvents du composant
        # Notifier
        for component in Components:
            for ipt in component.inputs:
                if ipt in ins:
                    component.inputEvents[ipt] = ins[ipt]
        # for component in Components:
        # print(f'La liste des events after init {component.name}: {component.inputEvents}')
        for component in Components:
            print(f'tr {component.name}: {component.tr}')
            # print(f'Imms 2 :{imms}')
            if component in imms and not component.inputEvents:  # dict vide
                component.internal()
                component.tr = component.avancement()
                component.tl = t
                component.tn = t + component.te
                component.te = 0
            elif component not in imms and component.inputEvents:
                component.external()
                component.tr = component.avancement()
                component.tl = t
                component.tn = t + component.te
                component.te = 0
            elif component in imms and component.inputEvents:
                component.conflict()
                component.tr = component.avancement()
                component.tl = t
                component.tn = t + component.te
                component.te = 0
        for component in Components:
            component.inputEvents.clear()
            component.outputEvents.clear()
        list_tr.clear()
        imms.clear()
        ins.clear()

        print(f't:  {t}')
        print("*********************************************************")


def geneStep():
    step1 = Step("step", 0.0, 3, 1.25)
    t = 0
    t_fin = 100

    step1.init()
    step1.tr = step1.avancement()
    print(f' Boucle ')
    while t < t_fin:
        print(f't: {t}')
        tr_min = step1.tr
        t = t + tr_min
        step1.te += tr_min
        step1.tr -= tr_min
        step1.generateOutput()
        step1.internal()
        step1.tr = step1.avancement()
        step1.tl = t
        step1.tn = t + step1.te
        step1.te = 0
        step1.inputEvents.clear()
        step1.outputEvents.clear()
    print(f't: {t}')


def simu_adder():
    gen = Gen("Generator")
    step1 = Step("step1", 1.0, -3, 0.65)
    step2 = Step("step2", 0.0, 1, 0.35)
    step3 = Step("step3", 0.0, 1, 1.0)
    step4 = Step("step4", 0.0, 4, 1.5)
    adder = Adder("Adder")
    t = 0
    t_fin = 2
    Components = [gen, step1, step2, step3, step4]
    imms = []
    # init
    adder.init()  # ToDo
    for component in Components:
        component.init()
        component.tr = component.avancement()  # tr = ta en s0
        print(f'Les composants:{component.name}\nta = {component.tr}')

    # Variable to draw figure
    xValue = [0]
    yValue = [0]
    print(f' Boucle ')
    while t < t_fin:
        print(f't: {t}')

        imms = []
        list_tr = []
        # for component in Components:
        #     print(f'La liste des events avant: {ins}')
        # recuperer les tr dans une liste
        for component in Components:
            list_tr.append(component.tr)
            print(f'tr {component.name}: {component.tr}')
        # recup le min de la liste
        tr_min = min(list_tr)

        # Faire une liste des composants imminents
        for component in Components:
            if component.tr == tr_min:
                imms.append(component)

        # print(f'Imms :{imms}')
        t = t + tr_min
        # mettre a jour te et tr
        for component in Components:
            component.te += tr_min
            component.tr -= tr_min
        dict_out = {}
        for component in Components:
            component.generateOutput()
            adder.inputEvents = component.outputEvents
            adder.external()
            adder.generateOutput()
            if (JOB or "add") not in component.outputEvents:
                dict_out.update(component.outputEvents)
            adder.internal()
        val = adder.add(dictionary=dict_out)
        xValue.append(t)
        yValue.append(val)
        print(f'adder *********************** dict ={adder.inputEvents} : {val}')
        # for component in Components:
        # print(f'La liste des events {component.name}: {component.inputEvents}')
        # Liste des entree impactee par les sortie
        ins = {}
        for component in Components:
            ins.update(component.outputEvents)
        print(f'La liste des entrees impactees : {ins}')

        # Recherche si l'entree est presente et mettre dans inputEvents du composant
        # Notifier
        adder.inputEvents.update(ins)
        for component in Components:
            for ipt in component.inputs:
                if ipt in ins:
                    component.inputEvents[ipt] = ins[ipt]
        # for component in Components:
        # print(f'La liste des events after init {component.name}: {component.inputEvents}')

        for component in Components:
            print(f'tr {component.name}: {component.tr}')
            # print(f'Imms 2 :{imms}')
            if component in imms and not component.inputEvents:  # dict vide
                component.internal()
                component.tr = component.avancement()
                component.tl = t
                component.tn = t + component.te
                component.te = 0
            elif component not in imms and component.inputEvents:
                component.external()
                component.tr = component.avancement()
                component.tl = t
                component.tn = t + component.te
                component.te = 0
            elif component in imms and component.inputEvents:
                component.conflict()
                component.tr = component.avancement()
                component.tl = t
                component.tn = t + component.te
                component.te = 0

        # for component in Components:
        #     component.inputEvents.clear()
        #     component.outputEvents.clear()

        list_tr.clear()
        imms.clear()
        ins.clear()
        adder.inputEvents.clear()
        print(f't:  {t}')
        print("*********************************************************")
    xValue_array = np.asarray(xValue)
    yValue_array = np.asarray(yValue)
    plot_step(xValue_array, yValue_array)
