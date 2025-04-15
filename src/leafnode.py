from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str | None,
        value: str | None,
        props: dict[str, str] | None = None,
    ):
        super().__init__(
            tag, value, [], props
        )  # Initialize the parent class with no children

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value to convert to HTML.")
        if self.tag is None:
            return self.value

        return f"<{self.tag}>{self.value}</{self.tag}>"
