import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode()
        self.assertIsInstance(node, HTMLNode)

    def test_eq(self):
        node = HTMLNode("p", "This is a paragraph", [], {"class": "text"})
        node2 = HTMLNode("p", "This is a paragraph", [], {"class": "text"})
        self.assertEqual(node, node2)

    # Tests the __eq__ method for different tag names
    def test_eq_different_tag(self):
        node = HTMLNode(tag="p")
        node2 = HTMLNode(tag="h1")
        self.assertNotEqual(node, node2)

    # Tests the __eq__ method for different values
    def test_eq_different_value(self):
        node = HTMLNode(value="This is a paragraph")
        node2 = HTMLNode(value="This is a different paragraph")
        self.assertNotEqual(node, node2)

    # tests the __eq__ method for same children
    def test_eq_same_children(self):
        node = HTMLNode(children=[HTMLNode("p", "Child 1")])
        node2 = HTMLNode(children=[HTMLNode("p", "Child 1")])
        self.assertEqual(node, node2)

    # tests the __eq__ method for different children
    def test_eq_different_children(self):
        node = HTMLNode(children=[HTMLNode("p", "Child 1")])
        node2 = HTMLNode(children=[HTMLNode("p", "Child 2")])
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("p", "This is a paragraph", [], {"class": "text"})
        self.assertEqual(
            repr(node),
            "HTMLNode(p, This is a paragraph, [], {'class': 'text'})",
        )

    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            "This is a link",
            [],
            {"href": "https://example.com", "target": "_blank"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://example.com" target="_blank"',
        )
