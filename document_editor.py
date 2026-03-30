class DocumentEditor:
    def __init__(self):
        self.render_document:str = None
        self.elements :list[str] = []
    
    def add_text(self, text:str):
        self.elements.append(text)

