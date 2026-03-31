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
