class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # String representing html tags
        self.value = value # String representing value of html tags
        self.children = children # List of children of this node object
        self.props = props # Dictionary representing attributes of the html tag

        def to_html(self): # Children of class should override to render themselves as HTML
            raise NotImplementedError("Method  'to_html' not implemented")

        def props_to_html(self):
            html_result_str = " " # String has to begin with a space HTML attributes always separated by space
            if not self.props:
                empty_props = " "
                return empty_props

            for key, value in self.props.items():
                html_result_str += f'{key}="{value}" ' # HTML attributes always separated by space
            return html_result_str.strip() # remove leading or trailing spaces