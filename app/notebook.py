# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.


class Note:
        HIGH:str = "HIGH"
        MEDIUM:str = "MEDIUM"
        LOW:str = "LOW"



def __init__(self,code:str,title:str,text:str,importance:str)
        self.code = code
        self.title = title
        self.text = text
        self.importance = importance
        self.date = datetime.now()


class Notebook:
    def __init__(self):
        self.notes: List[Note] = []

    def add_note(self,title: str,text:str, importance:str): -> int

        new_code = len(self.notes) + 1











