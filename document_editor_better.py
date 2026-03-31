from abc import ABC, abstractmethod

class DocumentElement(ABC):

    @abstractmethod
    def render(self):
        pass


class TextElement(DocumentElement):

    def render(self):
        pass


class ImageElement(DocumentElement):

    def render(self):
        pass

class Persistance(ABC):
    @abstractmethod
    def save(self):
        pass

class SaveToFile(Persistance):
    def save(self,content:str):
        with open("document.txt", "w") as f:
            f.write(content)
        
class SaveToDB(Persistance):
    def save(self):
        print("save to my database.")

class Document:
    def __init__(self):
        self.elements:list[DocumentElement] = []
    
    def add_element(self, el: DocumentElement):
        self.elements.append(el)

    def get_element(self):
        return self.elements
    

class DocumentRender:
    def __init__(self,doc: Document):
        self.doc = doc
    
    def render(self):
        elements= self.doc.get_element()
        for  element in elements:
            print(element.render())


