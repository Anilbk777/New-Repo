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


class NewLineELement(DocumentElement):
    def render(self):
        return "\n"


class Persistance(ABC):
    @abstractmethod
    def save(self, content: str):
        pass


class SaveToFile(Persistance):
    def save(self, content: str):
        with open("document.txt", "w") as f:
            f.write(content)
            print("data saved in document.txt successfylly")


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
        result = ""
        for element in elements:
            result += element.render()

        return result


class DocumentEditor:
    def __init__(self, doc: Document, db: Persistance):
        self.doc = doc
        self.db = db

    def add_text(self, text: str):
        self.doc.add_element(TextElement(text))

    def add_image(self, path: str):
        self.doc.add_element(ImageElement(path))

    def add_new_line(self):
        self.doc.add_element(NewLineELement())

    def save(self, content: str):
        self.db.save(content)


if __name__ == "__main__":
    doc_obj = Document()
    file_obj = SaveToFile()

    doc_editor = DocumentEditor(doc_obj, file_obj)
    doc_editor.add_text("Hello world")
    doc_editor.add_new_line()
    doc_editor.add_image("profile.png")
    doc_editor.add_new_line()
    doc_editor.add_text("I love python programming.")

    doc_render = DocumentRender(doc_obj)
    data = doc_render.render()
    print(data)

    doc_editor.save(data)
    doc_editor.add_text("this is new line to document.")

    
