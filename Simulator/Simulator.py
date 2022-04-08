# Ordonnanceur
from GBP.Buf import Buf
from GBP.Gen import Gen
from GBP.Proc import Proc
from GBP.step import Step


def Simulator():
    t = 0
    t_fin = 10
    ta = 0
    proc = Proc("Process 1")
    gen = Gen("Generator 1")
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
        print(f'La liste des events : {ins}')

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
            if component in imms and not component.inputEvents:
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
