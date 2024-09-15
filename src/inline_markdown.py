import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    result = []

    for node in old_nodes:
        if node.text_type != text_type_text:
            result.append(node)
            continue

        if not re.search(r"!\[(.*?)\]\((.*?)\)", node.text):
            result.append(node)
            continue

        images = extract_markdown_images(node.text)
        if not images:
            continue

        contents = re.split(r'(!\[[^\]]*\]\([^\)]*\))', node.text)

        for content in contents:
            if content == '':
                continue

            img_match = re.match(r'!\[(.*?)\]\((.*?)\)', content)
            if img_match:
                alt_text = img_match.group(1)
                url = img_match.group(2)
                result.append(TextNode(TEXT=alt_text, TEXT_TYPE= text_type_image, URL= url))
            else:
                result.append(TextNode(TEXT=content, TEXT_TYPE=text_type_text))

    return result


def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes: 
        if node.text_type != text_type_text:
            result.append(node)
            continue

        if not re.search(r"\[(.*?)\]\((.*?)\)", node.text):
            result.append(node)
            continue


        contents = re.split(r'(\[[^\]]*\]\([^\)]*\))', node.text)
        for content in contents: 
            if content == '':
                continue

            link_match = re.match(r'\[(.*?)\]\((.*?)\)', content)
            if link_match:
                link_text = link_match.group(1)
                url = link_match.group(2)
                result.append(TextNode(TEXT=link_text, TEXT_TYPE=text_type_link, URL=url))
            else:
                result.append(TextNode(TEXT=content, TEXT_TYPE=text_type_text))
    return result