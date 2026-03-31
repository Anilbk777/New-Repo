from abc import ABC, abstractmethod


class DocumentElement(ABC):

    @abstractmethod
    def render(self):
        pass


class TextElement(DocumentElement):

    def __init__(self, text: str):
        self.text = text

    def render(self) -> str:
        return self.text


class ImageElement(DocumentElement):

    def __init__(self, path: str):
        self.path = path

    def render(self) -> str:
        return "[Image: " + self.path + "]"


class NewLineELement(DocumentElement):
    def render(self):
        return "\n"


class Persistence(ABC):
    @abstractmethod
    def save(self, content: str):
        pass

class SaveToFile(Persistence):

    def __init__(self, path:str):
        self.path = path
        
    def save(self, content: str):
        try:
            with open(self.path, "w") as f:
                f.write(content)
            print(f"Successfully Saved to {self.path}")

        except IOError as e:
            print(f"Error: {e}")
            raise

class SaveToDB(Persistence):
    def save(self, content: str) -> None:
        # Implement properly
        pass


class Document:
    def __init__(self, title:str = "Untitled"):
        self._elements: list[DocumentElement] = []

    def add_element(self, element: DocumentElement):
        if not isinstance(element, DocumentElement):
            raise TypeError(f"{element} is not a type of DocumentELement")
        
        self._elements.append(element)

    def get_elements(self) -> list[DocumentElement]:
        return self._elements.copy()


class DocumentRenderer:
    def __init__(self, doc: Document):
        self.doc = doc

    def render(self):
        elements = self.doc.get_elements()
        for element in elements:
            result = "".join(element.render())

        return result


class DocumentEditor:
    def __init__(self, document: Document):
        self.document = document

    def add_text(self, text: str):
        self.document.add_element(TextElement(text))

    def add_image(self, path: str):
        self.document.add_element(ImageElement(path))

    def add_new_line(self):
        self.document.add_element(NewLineELement())


class DocumentService:  
    def __init__(self, document: Document, persistence: Persistence):
        self.editor = DocumentEditor(document)
        self.renderer = DocumentRenderer(document)
        self.persistence = persistence

    def save_document(self) -> None:
        content = self.renderer.render()
        self.persistence.save(content)



