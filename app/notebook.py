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

    def add_note(self,title: str,text:str, importance:str): -> int:

        new_code = len(self.notes) + 1

        self.notes.append(new_note)

        return new_note

#menu
print("1.agregar nota")
print("2.listar notas")
print("3.agregar etiqueta a nota")
print("4.Listar notas importantes")
print("5.Eliminar nota")
print("6.Mostrar notas por etiqueta")
print("7.Mostrar etiqueta con más notas")
print("8.Salir")








