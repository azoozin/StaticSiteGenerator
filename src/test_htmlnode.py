import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
        expected = ' href="https://example.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_repr(self):
        node = HTMLNode("p", "Hello, world!")
        expected_repr = "HTMLNode(tag='p', value='Hello, world!', children=[], props=None)"
        self.assertEqual(repr(node), expected_repr)

    def test_init(self):
        node1 = HTMLNode("p", "Hello")
        self.assertEqual(node1.tag, "p")
        self.assertEqual(node1.value, "Hello")
        self.assertEqual(node1.children, [])
        self.assertIsNone(node1.props)

        node2 = HTMLNode(children=[HTMLNode("b", "Bold")])
        self.assertIsNone(node2.tag)
        self.assertIsNone(node2.value)
        self.assertEqual(len(node2.children), 1)
        self.assertIsNone(node2.props)

# LeafNode tests
    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

# ParentNode tests
    def test_parentnode_tag_and_children(self):
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text")
        ]
        node = ParentNode("p", children)
        expected_html = "<p><b>Bold text</b>Normal text</p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_parentnode_no_tag(self):
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text")
        ]
        node = ParentNode(None, children)
        with self.assertRaises(ValueError) as context:
            node.to_html()
        # check if the raised error msg is the expected one
        self.assertEqual(str(context.exception), "No tag found.")

    def test_parentnode_empty_children(self):
        node = ParentNode("p", [])
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "No children found")
    
    def test_parentnode_nested_nodes(self):
        inner_children = [
            LeafNode("i", "italic text"),
            LeafNode(None, "normal text")
        ]

        inner_parent = ParentNode("span", inner_children)

        outer_children = [
            LeafNode("b", "Bold text"),
            inner_parent,
            LeafNode(None, "Additional text")
        ]

        outer_parent = ParentNode("div", outer_children)
        
        expected_html = "<div><b>Bold text</b><span><i>italic text</i>normal text</span>Additional text</div>"

        self.assertEqual(outer_parent.to_html(), expected_html)

    def test_parentnode_props_used(self):
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text")
        ]

        node = ParentNode("p", children, props={"href": "https://example.com", "target": "_blank"})
        expected_html = '<p href="https://example.com" target="_blank"><b>Bold text</b>Normal text</p>'
        self.assertEqual(node.to_html(), expected_html)
    


if __name__ == "__main__":
    unittest.main()