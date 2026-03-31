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

class Document:
    def __init__(self):
        self.elements:list[DocumentElement] = []
    
    def add_element(self, el: DocumentElement):
        self.elements.append(el)

    def get_element(self):
        return self.elements