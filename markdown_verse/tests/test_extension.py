from markdown import markdown
from unittest import TestCase

from markdown_verse.extension import VerseExtension


class TestExtension(TestCase):
    def test_default_config(self):
        source = """
'''
Arctic fox's den
adorned with flowers and snow
garden in winter
'''
        """.strip()

        expected = """
<div class="verse">Arctic fox's den
adorned with flowers and snow
garden in winter</div>
        """.strip()

        html = markdown(source, extensions=[VerseExtension()])
        self.assertEqual(html, expected)

        html = markdown(source, extensions=['markdown_verse'])
        self.assertEqual(html, expected)

    def test_custom_config(self):
        source = """
'''
Arctic fox's den
adorned with flowers and snow
garden in winter
'''
        """.strip()

        expected = """
<verse>Arctic fox's den
adorned with flowers and snow
garden in winter</verse>
        """.strip()

        html = markdown(source, extensions=[VerseExtension(
            tag='verse', tag_class='')])
        self.assertEqual(html, expected)

    def test_mixed(self):
        self.maxDiff = None
        source = """
Some text.

    '''
    Arctic fox's den
    adorned with flowers and snow
    garden in winter
    '''

'''
Arctic fox's den
adorned with flowers and snow
garden in *winter*
'''
        """.strip()

        expected = """
<p>Some text.</p>
<pre><code>'''
Arctic fox's den
adorned with flowers and snow
garden in winter
'''
</code></pre>
<verse>Arctic fox's den
adorned with flowers and snow
garden in <em>winter</em></verse>
        """.strip()

        html = markdown(source, extensions=[VerseExtension(
            tag='verse', tag_class='')])
        self.assertEqual(html, expected)
