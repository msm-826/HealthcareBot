import pandas as pd
from datas import Datas

class FindSymptoms:

    def __init__(self) -> None:
        pass

    def findingSymptoms(self, diseases, dt):

        dd = Datas()
        l1 = dd.get_l1()
        # kk = []
        for i in range (5):
            selected_rows = dt[dt["prognosis"] == diseases ].iloc[0].values
            selected_rows.tolist
            # print(selected_rows)

        ll = []

        for i in range(len(selected_rows)):
            if(selected_rows[i] == 1):
                ll.append(l1[i])
        return ll

# f = FindSymptoms()
# f.findingSymptoms("Fungal infection")