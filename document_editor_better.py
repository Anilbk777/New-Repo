from abc import ABC, abstractmethod


class DocumentElement(ABC):

    @abstractmethod
    def render(self):
        pass


class TextElement(DocumentElement):

    def __init__(self, text: str):
        self.text = text

    def render(self):
        return self.text


class ImageElement(DocumentElement):

    def __init__(self, path: str):
        self.path = path

    def render(self):
        return "[Image: " + self.path + "]"


class Persistance(ABC):
    @abstractmethod
    def save(self):
        pass


class SaveToFile(Persistance):
    def save(self, content: str):
        with open("document.txt", "w") as f:
            f.write(content)


class SaveToDB(Persistance):
    def save(self):
        print("save to my database.")


class Document:
    def __init__(self):
        self.elements: list[DocumentElement] = []

    def add_element(self, el: DocumentElement):
        self.elements.append(el)

    def get_element(self):
        return self.elements


class DocumentRender:
    def __init__(self, doc: Document):
        self.doc = doc

    def render(self):
        elements = self.doc.get_element()
        for element in elements:
            print(element.render())


class DocumentEditor:
    def __init__(self, doc: Document, db: Persistance):
        self.doc = doc
        self.db = db

    def add_text(self, text: str):
        self.doc.add_element(TextElement())
