''' Tests for xhtml to rest converter '''

from StringIO import StringIO
from xml.dom.minidom import parseString

import xhtml2rest as xr

import nose.tools as nt

def handle_text(txt):
    dom = parseString(txt)
    ditem = xr.handleNode(dom)
    return ditem.format(79)


def test_formatting():
    res = handle_text('<b>text with spaces</b>')
    yield nt.assert_equal, res, '**text with spaces**'
    res = handle_text('<i>text with spaces</i>')
    yield nt.assert_equal, res, '*text with spaces*'
    res = handle_text('<tt>text with spaces</tt>')
    yield nt.assert_equal, res, '``text with spaces``'
    

def test_links():
    res = handle_text('<a href="format.html">text with spaces</a>')
    yield nt.assert_equal, res, '`text with spaces`_'
    # disallow markup in link text
    res = handle_text('<a href="format.html"><tt>text with spaces</tt></a>')
    yield nt.assert_equal, res, '`text with spaces`_'
    
