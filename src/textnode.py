class TextNode():
    def __init__(self, text, type, url):
        self.text = text # Text content of node
        self.type = type # Type of text, strings like "bold" or "italic"
        self.url = url # Url of link/image. If text is a link, default url to None.
    
    def __eq__(self, obj):
        if (self.text == obj.text
            and self.type == obj.type
            and self.url == obj.url):
            return True
    
    # Return string representation of TextNode
    def __repr__(self):
        return f"TextNode({self.text}, {self.type}, {self.url})"
