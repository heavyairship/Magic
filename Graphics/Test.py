#!/usr/bin/env python


from Context import Context
from Buffer import Buffer
from Shader import Shader
from Program import Program
from Texture import Texture
from Mat4 import Mat4
import OpenGL.GL as gl
import ctypes


c = Context()

b = Buffer(gl.GL_ARRAY_BUFFER, gl.GL_STATIC_DRAW, ctypes.c_int)
b.sync()
b.push(1)
b.push(2)
b.push(3)
b.push(4)
b.push(5)
b[12] = 3

assert(b[0]==1)
assert(b[1]==2)
assert(b[2]==3)
assert(b[3]==4)
assert(b[4]==5)
assert(b[5]==0)
assert(b[13]==None)
b.sync()

t = Texture('Images/Sen Triplets.jpg')
assert(t.width==480)
assert(t.height==680)

f = Shader('Shader/Model.frag', gl.GL_FRAGMENT_SHADER)
v = Shader('Shader/Model.vert', gl.GL_VERTEX_SHADER)
p = Program('Shader/Model.prog')
assert(p.worldViewProjectionMatrix==0)

m = Mat4()
m = Mat4.frustum(0, 1, 0, 1, 0, 1)
m = m * m
print(m)

