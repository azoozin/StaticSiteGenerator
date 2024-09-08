from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    # No children should be set
    # Value must be required
    def __init__(self, value, tag=None, props=None):
        # tell parent constructor what parameter goes into which since we changed value and tag position
        super().__init__(tag=tag, value=value, props=props, children=[])

    # override parent method
    def to_html(self):
        if not self.value:
            raise ValueError("No value found.")
        if not self.tag:
            return f"{self.value}"
        props_string = self.props_to_html()
        opening_tag = f"<{self.tag}{props_string}>"
        closing_tag = f"</{self.tag}>"
        return f"{opening_tag}{self.value}{closing_tag}"