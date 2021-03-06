# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.0
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError('Python 2.7 or later required')

# Import the low-level C/C++ module
if __package__ or '.' in __name__:
    from . import _gpl
else:
    import _gpl

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if name == "thisown":
        return self.this.own(value)
    if name == "this":
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if not static:
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if name == "thisown":
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _gpl.delete_SwigPyIterator

    def value(self):
        return _gpl.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _gpl.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _gpl.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _gpl.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _gpl.SwigPyIterator_equal(self, x)

    def copy(self):
        return _gpl.SwigPyIterator_copy(self)

    def next(self):
        return _gpl.SwigPyIterator_next(self)

    def __next__(self):
        return _gpl.SwigPyIterator___next__(self)

    def previous(self):
        return _gpl.SwigPyIterator_previous(self)

    def advance(self, n):
        return _gpl.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _gpl.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _gpl.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _gpl.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _gpl.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _gpl.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _gpl.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _gpl:
_gpl.SwigPyIterator_swigregister(SwigPyIterator)

DrawMode_TRIANGLES = _gpl.DrawMode_TRIANGLES
DrawMode_LINES = _gpl.DrawMode_LINES
DrawMode_POINTS = _gpl.DrawMode_POINTS
class VertexBuffer(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _gpl.VertexBuffer_swiginit(self, _gpl.new_VertexBuffer(*args))
    __swig_destroy__ = _gpl.delete_VertexBuffer

    def data(self, new_data, size):
        return _gpl.VertexBuffer_data(self, new_data, size)

    def bind(self):
        return _gpl.VertexBuffer_bind(self)

    def unbind(self):
        return _gpl.VertexBuffer_unbind(self)

# Register VertexBuffer in _gpl:
_gpl.VertexBuffer_swigregister(VertexBuffer)

class VertexBufferLayoutElement(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    type = property(_gpl.VertexBufferLayoutElement_type_get, _gpl.VertexBufferLayoutElement_type_set)
    count = property(_gpl.VertexBufferLayoutElement_count_get, _gpl.VertexBufferLayoutElement_count_set)
    normalized = property(_gpl.VertexBufferLayoutElement_normalized_get, _gpl.VertexBufferLayoutElement_normalized_set)

    def __init__(self):
        _gpl.VertexBufferLayoutElement_swiginit(self, _gpl.new_VertexBufferLayoutElement())
    __swig_destroy__ = _gpl.delete_VertexBufferLayoutElement

# Register VertexBufferLayoutElement in _gpl:
_gpl.VertexBufferLayoutElement_swigregister(VertexBufferLayoutElement)

class VertexBufferLayout(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _gpl.VertexBufferLayout_swiginit(self, _gpl.new_VertexBufferLayout())
    __swig_destroy__ = _gpl.delete_VertexBufferLayout

    def elements(self):
        return _gpl.VertexBufferLayout_elements(self)

    def stride(self):
        return _gpl.VertexBufferLayout_stride(self)

# Register VertexBufferLayout in _gpl:
_gpl.VertexBufferLayout_swigregister(VertexBufferLayout)

class VertexArray(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _gpl.VertexArray_swiginit(self, _gpl.new_VertexArray(*args))
    __swig_destroy__ = _gpl.delete_VertexArray

    def bind(self):
        return _gpl.VertexArray_bind(self)

    def unbind(self):
        return _gpl.VertexArray_unbind(self)

    def vertex_buffer(self, new_vertex_buffer):
        return _gpl.VertexArray_vertex_buffer(self, new_vertex_buffer)

    def layout(self, new_layout):
        return _gpl.VertexArray_layout(self, new_layout)

# Register VertexArray in _gpl:
_gpl.VertexArray_swigregister(VertexArray)

class IndexBuffer(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _gpl.IndexBuffer_swiginit(self, _gpl.new_IndexBuffer(*args))
    __swig_destroy__ = _gpl.delete_IndexBuffer

    def bind(self):
        return _gpl.IndexBuffer_bind(self)

    def unbind(self):
        return _gpl.IndexBuffer_unbind(self)

    def count(self):
        return _gpl.IndexBuffer_count(self)

# Register IndexBuffer in _gpl:
_gpl.IndexBuffer_swigregister(IndexBuffer)

class Shader(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _gpl.Shader_swiginit(self, _gpl.new_Shader(*args))
    __swig_destroy__ = _gpl.delete_Shader

    def get_uniform_location(self, dirpath):
        return _gpl.Shader_get_uniform_location(self, dirpath)

    def set_uniform(self, *args):
        return _gpl.Shader_set_uniform(self, *args)

    def bind(self):
        return _gpl.Shader_bind(self)

    def unbind(self):
        return _gpl.Shader_unbind(self)

# Register Shader in _gpl:
_gpl.Shader_swigregister(Shader)

class Texture(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _gpl.Texture_swiginit(self, _gpl.new_Texture(*args))
    __swig_destroy__ = _gpl.delete_Texture

    def load(self, filepath):
        return _gpl.Texture_load(self, filepath)

    def bind(self, slot=0):
        return _gpl.Texture_bind(self, slot)

    def unbind(self):
        return _gpl.Texture_unbind(self)

    def width(self):
        return _gpl.Texture_width(self)

    def height(self):
        return _gpl.Texture_height(self)

# Register Texture in _gpl:
_gpl.Texture_swigregister(Texture)

class Renderer(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _gpl.Renderer_swiginit(self, _gpl.new_Renderer(*args))
    __swig_destroy__ = _gpl.delete_Renderer

    def init(self, width, height, title):
        return _gpl.Renderer_init(self, width, height, title)

    def draw(self, vertex_array, index_buffer, shader, mode):
        return _gpl.Renderer_draw(self, vertex_array, index_buffer, shader, mode)

    def start_frame(self):
        return _gpl.Renderer_start_frame(self)

    def end_frame(self):
        return _gpl.Renderer_end_frame(self)

    def should_close(self):
        return _gpl.Renderer_should_close(self)

    def width(self):
        return _gpl.Renderer_width(self)

    def height(self):
        return _gpl.Renderer_height(self)

# Register Renderer in _gpl:
_gpl.Renderer_swigregister(Renderer)

class vec3(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    x = property(_gpl.vec3_x_get, _gpl.vec3_x_set)
    y = property(_gpl.vec3_y_get, _gpl.vec3_y_set)
    z = property(_gpl.vec3_z_get, _gpl.vec3_z_set)

    def __init__(self, *args):
        _gpl.vec3_swiginit(self, _gpl.new_vec3(*args))
    __swig_destroy__ = _gpl.delete_vec3

# Register vec3 in _gpl:
_gpl.vec3_swigregister(vec3)

class vec4(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    x = property(_gpl.vec4_x_get, _gpl.vec4_x_set)
    y = property(_gpl.vec4_y_get, _gpl.vec4_y_set)
    z = property(_gpl.vec4_z_get, _gpl.vec4_z_set)
    w = property(_gpl.vec4_w_get, _gpl.vec4_w_set)

    def __init__(self, *args):
        _gpl.vec4_swiginit(self, _gpl.new_vec4(*args))
    __swig_destroy__ = _gpl.delete_vec4

# Register vec4 in _gpl:
_gpl.vec4_swigregister(vec4)

class Base(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _gpl.Base_swiginit(self, _gpl.new_Base(*args))
    __swig_destroy__ = _gpl.delete_Base

    def draw(self, renderer, mvp):
        return _gpl.Base_draw(self, renderer, mvp)

# Register Base in _gpl:
_gpl.Base_swigregister(Base)
cvar = _gpl.cvar

class Point(Base):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    s_vertex_buffer_layout = property(_gpl.Point_s_vertex_buffer_layout_get, _gpl.Point_s_vertex_buffer_layout_set)
    s_index_buffer = property(_gpl.Point_s_index_buffer_get, _gpl.Point_s_index_buffer_set)

    def __init__(self, initial_position, initial_color, initial_size):
        _gpl.Point_swiginit(self, _gpl.new_Point(initial_position, initial_color, initial_size))
    __swig_destroy__ = _gpl.delete_Point

    def draw(self, renderer, mvp):
        return _gpl.Point_draw(self, renderer, mvp)

    def position(self, *args):
        return _gpl.Point_position(self, *args)

    def size(self, *args):
        return _gpl.Point_size(self, *args)

# Register Point in _gpl:
_gpl.Point_swigregister(Point)

class Canvas(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    s_renderer = property(_gpl.Canvas_s_renderer_get, _gpl.Canvas_s_renderer_set)

    def __init__(self):
        _gpl.Canvas_swiginit(self, _gpl.new_Canvas())
    __swig_destroy__ = _gpl.delete_Canvas

    def render(self):
        return _gpl.Canvas_render(self)

    def __lshift__(self, primitive):
        return _gpl.Canvas___lshift__(self, primitive)

# Register Canvas in _gpl:
_gpl.Canvas_swigregister(Canvas)



