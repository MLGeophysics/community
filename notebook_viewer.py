from __future__ import print_function
import re
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
import sys
import os
from urllib.parse import quote

NOTEBOOK_SYNTAX = re.compile(r'\{notebook:\s*(.+?)\s*\}')

class NotebookExtension(Extension):
    def __init__(self, configs={}):
        self.config = {
            'base_path': ['.', 'Default location from which to evaluate ' \
                'relative paths for the include statement.'],
            'encoding': ['utf-8', 'Encoding of the files used by the include ' \
                'statement.']
        }
        for key, value in configs.items():
            self.setConfig(key, value)

    def extendMarkdown(self, md, md_globals):
        md.preprocessors.add(
            'include', NotebookExtensionPreprocessor(md,self.getConfigs()),'_begin'
        )


class NotebookExtensionPreprocessor(Preprocessor):
    '''This includes an ability to include jupyter notoebooks'''
    def __init__(self, md, config):
        super(NotebookExtensionPreprocessor, self).__init__(md)
        self.base_path = config['base_path']
        self.encoding = config['encoding']

    def _genNBViewer(self, filename, account='MLGeophysics', repo='community'):
        # check that the .ipynb is in the filename
        ext = os.path.splitext(filename)[1]
        if ext is '':
            fname = fname + '.ipynb'
        # get the directory of this file and clean that from the directory of
        #   the notebook file so it has a relative file path under the repo
        # TODO: this is complicated and I aint spending the time to figure it out tonight
        # Make the filename url firnely
        # filename = quote(filename)
        # return the div iframe pointing to nbviewer
#         return [r'''
# <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
#         <iframe src="http://nbviewer.jupyter.org/github/{}/{}/blob/master/{}" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
# </div>
# '''.format(account, repo, filename)]
        import nbconvert
        #return [nbconvert.HTMLExporter().from_filename(filename)[0]]
        return [r'''
<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: 50%;">
        {}
</div>
'''.format(nbconvert.HTMLExporter().from_filename(filename)[0].split('</head>')[1])]


    def run(self, lines):
        done = False
        while not done:
            for line in lines:
                loc = lines.index(line)
                m = NOTEBOOK_SYNTAX.search(line)
                if m:
                    text = self._genNBViewer(m.group(1))
                    line_split = NOTEBOOK_SYNTAX.split(line, maxsplit=0)
                    if len(text) == 0: text.append('')
                    text[0] = line_split[0] + text[0]
                    text[-1] = text[-1] + line_split[2]
                    lines = lines[:loc] + text + lines[loc+1:]
                    break
            else:
                done = True
        return lines


def makeExtension(*args,**kwargs):
    return NotebookExtension(kwargs)
