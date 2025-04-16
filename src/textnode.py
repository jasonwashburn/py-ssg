from enum import Enum
from leafnode import LeafNode


# Normal text
# **Bold text**
# _Italic text_
# `Code text`
# Links, in this format: [anchor text](url)
# Images, in this format: ![alt text](url)


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


# In textnode.py create a class called TextNode. It should have 3 properties that can be set in the constructor:
# self.text - The text content of the node
# self.text_type - The type of text this node contains, which is a member of the TextType enum.
# self.url - The URL of the link or image, if the text is a link. Default to None if nothing is passed in.


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    # TextNode(TEXT, TEXT_TYPE, URL)
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


# It should handle each type of the TextType enum. If it gets a TextNode that is none of those types,
# it should raise an exception. Otherwise, it should return a new LeafNode object.


# TextType.TEXT: This should return a LeafNode with no tag, just a raw text value.
# TextType.BOLD: This should return a LeafNode with a "b" tag and the text
# TextType.ITALIC: "i" tag, text
# TextType.CODE: "code" tag, text
# TextType.LINK: "a" tag, anchor text, and "href" prop
# TextType.IMAGE: "img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)
#
def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unknown text type: {text_node.text_type}")
