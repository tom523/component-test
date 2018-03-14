# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1518271324.771
_enable_loop = True
_template_filename = 'tpl.txt'
_template_uri = 'tpl.txt'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        name = context.get('name', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'hello, ')
        __M_writer(unicode(name))
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 0, "29": 23, "22": 1, "23": 1}, "uri": "tpl.txt", "filename": "tpl.txt"}
__M_END_METADATA
"""
