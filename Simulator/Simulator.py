# Ordonnanceur
from GBP.Buf import Buf
from GBP.Gen import Gen
from GBP.Proc import Proc


def Simulator():
    t = 0
    t_fin = 10
    ta = 0
    proc = Proc("Process 1")
    gen = Gen("Generator 1")
    buf = Buf("Buffer 1")
    Components = [proc, gen, buf]
    imms = []

    # init
    for component in Components:
        component.init()
        ta = component.avancement()
        component.tr = ta  # tr = ta en s0
    print(f'Les composants:{Components}\nta = {ta}')

    print("********Les evolutions*********")
    while t < t_fin:
        for component in Components:
            print(f't:  {t}')
            if component == buf:
                print(f'q:  {component.q}')
            print(f'InputEvents:   {component.inputEvents}')
            print(f'outputEvents:   {component.outputEvents}')
        list_tr = []
        # recuperer les tr dans une liste
        for component in Components:
            list_tr.append(component.tr)
        # recup le min de la liste
        tr_min = min(list_tr)
        # Faire une liste des composants imminents
        for component in Components:
            if component.tr == tr_min:
                imms.append(component)
        t += tr_min
        # mettre a jour te et tr
        for component in Components:
            component.te += tr_min
            component.tr -= tr_min

        for component in Components:
            component.generateOutput()
        # Liste des entree impactee par les sortie
        ins = []
        for component in Components:
            ins.append(component.outputEvents)
        for component in Components:
            component.inputEvents = inputEvents

        for component in Components:
            if component in imms and component.inputEvents is None:
                component.internal()
                component.tr = component.avancement()
                component.tl = t - component.te
                component.tn = t + component.tr
            elif component not in imms and component.inputEvents is not None:
                component.external()
                component.tr = component.avancement()
                component.tl = t - component.te
                component.tn = t + component.tr
            elif component in imms and component.inputEvents is not None:
                # component.conflict()
                component.tr = component.avancement()
                component.tl = t - component.te
                component.tn = t + component.tr
