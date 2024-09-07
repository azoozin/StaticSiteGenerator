import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_eq_different_content(self):
        # Test different content
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("Different content", "bold")
        self.assertNotEqual(node, node2)

    def test_eq_different_style(self):
        # Test same content but different style
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_eq_different_type(self):
        # Test equality with different types
        node = TextNode("This is a text node", "bold")
        not_a_node = "This is a text node"  # Just a string, not a TextNode
        self.assertNotEqual(node, not_a_node)

    def test_eq_self(self):
        # Test a node against itself
        node = TextNode("This is a text node", "bold")
        self.assertEqual(node, node)


if __name__ == "__main__":
    unittest.main()