from leafnode import LeafNode
import unittest


class TestLeafNode(unittest.TestCase):
    def test_leaf_can_init(self):
        node = LeafNode("p", "Hello, world!")
        assert node.tag == "p"
        assert node.value == "Hello, world!"

    def test_leaf_to_html_raises_value_error_when_no_value(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
