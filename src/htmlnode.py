class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # String representing html tags
        self.value = value # String representing value of html tags
        self.children = children if children is not None else [] # List of children of this node object
        self.props = props # Dictionary representing attributes of the html tag

    def to_html(self): # Children of class should override to render themselves as HTML
        raise NotImplementedError("Method 'to_html' not implemented")

    def props_to_html(self):
        if not self.props:
            empty_props = ""
            return empty_props

        html_props = []
        for key, value in self.props.items():
            html_props.append(f'{key}="{value}"')
    
        return " " + " ".join(html_props)

    def __repr__(self):
        # !r calls __repr__ on each variable
        return f"HTMLNode(tag={self.tag!r}, value={self.value!r}, children={self.children}, props={self.props})"

### CHILD CLASSES ###

# Leaf node has no children
# A leaf node is a node without children (like leaf in a tree branch)
class LeafNode(HTMLNode):
    # No children should be set
    # Value must be required
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

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

# Parent node has children but no value
# A node that is not a "leaf node" is a parent node i.e it has children
# # # (like a branch in a tree with child leaves)
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("No tag found.")
        if not self.children:
            raise ValueError("No children found")
        
        props_str = ''
        if hasattr(self, 'props') and self.props:
            props_str = ' '.join([f'{key}="{value}"' for key, value in self.props.items()])

        complete_html = ''
        if self.children:
            html_string_list = []
            
            for child in self.children:
                html_string_list.append(child.to_html())

            concat_html_strings = "".join(html_string_list)
            complete_html = f"<{self.tag}>{concat_html_strings}</{self.tag}>"

        if props_str:
            # Include props_str in the opening tag if it exists
            complete_html = f"<{self.tag} {props_str}>{concat_html_strings}</{self.tag}>"
        else:
            complete_html = f"<{self.tag}>{concat_html_strings}</{self.tag}>"
            
        return complete_html
