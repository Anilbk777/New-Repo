from abc import ABC, abstractmethod


class DocumentElement(ABC):

    @abstractmethod
    def render(self)->str:
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


class NewLineElement(DocumentElement):
    def render(self)-> str:
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
        self.title = title
        self._elements: list[DocumentElement] = []

    def add_element(self, element: DocumentElement):
        if not isinstance(element, DocumentElement):
            raise TypeError(f"{element} is not a type of DocumentELement")
        
        self._elements.append(element)

    def get_elements(self) -> list[DocumentElement]:
        return self._elements.copy()


class DocumentRenderer:
 
    def render(self , elements:list[DocumentElement]) -> str:
        result = "".join(element.render() for element in elements)

        return result


class DocumentEditor:
    def __init__(self, document: Document):
        self.document = document

    def add_text(self, text: str):
        self.document.add_element(TextElement(text))

    def add_image(self, path: str):
        self.document.add_element(ImageElement(path))

    def add_new_line(self):
        self.document.add_element(NewLineElement())


class DocumentService:  
    def __init__(self,  
        document: Document,
        renderer: DocumentRenderer,
        persistence: Persistence
        ):

        self.document = document
        self.renderer = renderer
        self.persistence = persistence

    def save_document(self) -> None:
        elements = self.document.get_elements()
        content = self.renderer.render(elements)
        self.persistence.save(content)

if __name__ == "__main__":

  
