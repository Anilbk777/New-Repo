class DocumentEditor:
    def __init__(self):
        self.render_document:str = None
        self.elements :list[str] = []
    
    def add_text(self, text:str):
        self.elements.append(text)
    
    def add_image(self, path:str):
        self.elements.append(path)

    def render_document(self):
        if self.render_document is None:
            for i in self.elements:
                if i.endswith(".img"):
                    self.render_document += "["+ i +"]" + "\n"
                else:
                    self.render_document += i + "\n"

        return self.render_document

