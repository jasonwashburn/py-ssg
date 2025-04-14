from enum import Enum


# Normal text
# **Bold text**
# _Italic text_
# `Code text`
# Links, in this format: [anchor text](url)
# Images, in this format: ![alt text](url)


class TextType(Enum):
    NORMAL = "normal"
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
