class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # String representing html tags
        self.value = value # String representing value of html tags
        self.children = children if children is not None else [] # List of children of this node object
        self.props = props # Dictionary representing attributes of the html tag

    def to_html(self): # Children of class should override to render themselves as HTML
        raise NotImplementedError("Method  'to_html' not implemented")

    def props_to_html(self):
        if not self.props:
            empty_props = " "
            return empty_props

        html_props = []
        for key, value in self.props.items():
            html_props.append(f'{key}="{value}"')
    
        return " " + " ".join(html_props)

    def __repr__(self):
        # !r calls __repr__ on each variable
        return f"HTMLNode(tag={self.tag!r}, value={self.value!r}, children={self.children}, props={self.props})"