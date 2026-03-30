import os
from pathlib import Path


class DocumentEditor:
    def __init__(self):

        self.elements: list[str] = []

    def add_text(self, text: str):
        self.elements.append(text)

    def add_image(self, path: str):
        self.elements.append(path)

    def render_document(self):

        document = ""

        for i in self.elements:
            if i.endswith(".img"):
                document += "[" + i + "]" + "\n"
            else:
                document += i + "\n"
        return document

    def save_to_file(self, path: str, content: str):
        if Path(path).exists():
            with open(path, "a") as f:
                if content != "":
                    f.write(content)
                    print(f"data saved to {Path(path)} successfully.")
                else:
                    print("No document to add in the file.")
        else:
            print(f"The path doesn't exist. {Path(path)}")


if __name__ == "__main__":
    doc = DocumentEditor()
    doc.add_text("Hello guys")
    doc.add_image("profile.img")
    doc.add_text("I am from pokhara.")
    doc.add_image("house.img")

    document = doc.render_document()
    print(document)

    doc.save_to_file("document.txt", document)

    doc.add_text("this one is another text")
    doc2 = doc.render_document()
    print(doc2)
