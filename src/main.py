from textnode import TextNode
from htmlnode import HTMLNode

def main():
    textnode_test = TextNode("texttextext", "bold", "google.com")
    textnode_text_two = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(textnode_test.__repr__())
    print(textnode_text_two.__repr__())

    node = HTMLNode("p", "Hello, world!")
    print("node repr:")
    print(repr(node))
    print(node.__str__())

main()