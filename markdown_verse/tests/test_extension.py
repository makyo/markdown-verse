from markdown import markdown
from unittest import TestCase

from markdown_verse.extension import VerseExtension


class TestExtension(TestCase):
    def test_default_config(self):
        source = """
Hello World
===========

'''
Arctic fox's den
adorned with flowers and snow
garden in winter
'''
        """.strip()

        expected = """
<h1>Hello World</h1>
<p><div class="verse">Arctic fox's den
adorned with flowers and snow
garden in winter</div></p>
        """.strip()

        html = markdown(source, extensions=[VerseExtension()])
        self.assertEqual(html, expected)

        html = markdown(source, extensions=['markdown_verse'])
        self.assertEqual(html, expected)

    def test_custom_config(self):
        source = """
Hello World
===========

'''
Arctic fox's den
adorned with flowers and snow
garden in winter
'''
        """.strip()

        expected = """
<h1>Hello World</h1>
<p><verse>Arctic fox's den
adorned with flowers and snow
garden in winter</verse></p>
        """.strip()

        html = markdown(source, extensions=[VerseExtension(
            tag_tuple=('<verse>', '</verse>'))])
        self.assertEqual(html, expected)
