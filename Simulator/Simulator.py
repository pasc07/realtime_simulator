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

from Plot.PlotData import PlotData
from Simulator.Integral import Integral


def Simulator():
    t = 0
    t_fin = 20
    ta = 0
    # gen = Gen("Generator 1")
    # proc = Proc("Process 1")
    # buf = Buf("Buffer 1")
    # Components = [gen, buf, proc]
    step1 = Step("step1", 1.0, -3, 0.65)
    step2 = Step("step2", 0.0, 1, 0.35)
    step3 = Step("step3", 0.0, 1, 1.0)
    step4 = Step("step4", 0.0, 4, 1.5)
    step5 = Step("step5", 0.0, 4.9, 1.5)
    adder = Adder("Adder")
    plot = PlotData("Plot")
    intg = Integral("Integral")
    adder.inputs = [step1.name, step2.name, step3.name, step4.name]
    Components = [step1, step2, step3, step4, adder]
    # init
    for component in Components:
        component.init()
        ta = component.avancement()
        component.tr = ta  # tr = ta en s0
        print(f'Composants:{component.name}\nta = {ta}')

    print("********Les evolutions*********")
    print(f't:  {t}')
    while t < t_fin:
        print(f't Start:  {t}')
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
        for component in imms:
            component.generateOutput()
        print(f'adder *********************** dict 1 ={adder.inputEvents} : {adder.output}')
        # for component in Components:
        # print(f'La liste des events {component.name}: {component.inputEvents}')
        # Liste des entree impactee par les sortie
        ins = {}
        for component in imms:
            ins.update(component.outputEvents)
        print(f'La liste des evenements generer pdt le cycle: {ins}')

        # Recherche si l'entree est presente et mettre dans inputEvents du composant
        # Notifier
        for component in Components:
            for ipt in component.inputs:
                if ipt in ins:
                    # component.inputEvents[ipt] = ins[ipt]
                    component.inputEvents.update(dict({ipt: ins[ipt]}))

        # for component in Components:
        # print(f'La liste des events after init {component.name}: {component.inputEvents}')
        for component in Components:
            print(f'tr {component.name}: {component.tr}')
            # print(f'Imms 2 :{imms}')
            if component in imms and not component.inputEvents:  # dict vide
                print(f'****Internal {component.name}')
                component.internal()
                component.tr = component.avancement()
                component.tl = t
                component.tn = t + component.te
                component.te = 0
            elif component not in imms and component.inputEvents:
                print(f'****External {component.name}')
                component.external()
                component.tr = component.avancement()
                component.tl = t
                component.tn = t + component.te
                component.te = 0
            elif component in imms and component.inputEvents:
                print(f'****Conflict {component.name}')
                component.conflict()
                component.tr = component.avancement()
                component.tl = t
                component.tn = t + component.te
                component.te = 0
        plot.addPoint(t, adder.output)
        for component in Components:
            component.inputEvents.clear()
            component.outputEvents.clear()
        list_tr.clear()
        imms.clear()
        ins.clear()
        # adder.inputEvents.clear()
        print(f't End:  {t}')
        print("*********************************************************")
    # Plot
    plot.plot_step()
