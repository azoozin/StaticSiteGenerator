import unittest

from htmlnode import HTMLNode, LeafNode

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

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()