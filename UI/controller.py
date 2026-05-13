import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()


    def handle_Analizza(self,e):
        try:
            UtenteInput = int(self._view.txtDistanzaMinima.value)


        except ValueError:
            self._view.txt_result.controls.append(ft.Text("Inserire un numero valido"))
            self._view.update_page()
            return

        self._model.buildGraph(UtenteInput)
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view.txt_result.controls.append(
            ft.Text(f"Il grafo contiene {self._model.getNumNodi()} nodi e {self._model.getNumArchi()} archi"))
        if self._model.getNumArchi() == 0:
            self._view.txt_result.controls.append(ft.Text("la distanza minima inserita è troppo grande "))

        """metodo più comodo per me quello sotto, mi porto direttamente la lista del dto arco """
        #archi = self._model.stampaArchi(UtenteInput)
        #for a in archi :
        #    self._view.txt_result.controls.append(ft.Text(f"{a}"))

        #con il metodo .edges del grafo

        graph =self._model.getGrafo()
        arches = graph.edges(data="weight")
        listaArchi=[(u,v,d) for u,v,d in arches ]
        for u,v,w in listaArchi:
            self._view.txt_result.controls.append(ft.Text(f"DA ---> :{u}  ,  ---> A :  {v} , ||| DISTA :  {w} miglia"))



        self._view.update_page()

