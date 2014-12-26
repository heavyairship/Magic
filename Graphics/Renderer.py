#!/usr/bin/env python

import OpenGL.GL as gl
import ctypes
from Program import Program
from Matrix import Matrix
from Buffer import Buffer

class Vertex(ctypes.Structure):
   _fields_ = (
      ('x', ctypes.c_float),
      ('y', ctypes.c_float),
      ('z', ctypes.c_float),
      ('u', ctypes.c_float),
      ('v', ctypes.c_float),
   )

class Attr(object):
   POSITION, TEXCOORD = range(2)

class Renderer(object):
   def __init__(self): 
      self.program = Program('Shader/Quad.prog')

      # Prepare quad geometry
      self.vbuffer = Buffer(gl.GL_ARRAY_BUFFER, gl.GL_STATIC_DRAW, Vertex)
      self.vbuffer.push(Vertex(-.5, -.5, 0, 0, 1))
      self.vbuffer.push(Vertex(-.5,  .5, 0, 0, 0))
      self.vbuffer.push(Vertex( .5, -.5, 0, 1, 1))
      self.vbuffer.push(Vertex( .5,  .5, 0, 1, 0))

      # Set up vertex array object for mapping structs => shader inputs
      vao = (ctypes.c_int * 1)()
      gl.glGenVertexArrays(1, vao)
      self.vao = vao[0]
      stride = ctypes.sizeof(Vertex)
      gl.glBindVertexArray(self.vao)
      gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vbuffer.id)
      gl.glEnableVertexAttribArray(Attr.POSITION)
      offset = ctypes.c_void_p(0)
      gl.glVertexAttribPointer(Attr.POSITION, 3, gl.GL_FLOAT, gl.GL_FALSE, stride, offset)
      gl.glEnableVertexAttribArray(Attr.TEXCOORD)
      offset = ctypes.c_void_p(12)
      gl.glVertexAttribPointer(Attr.TEXCOORD, 2, gl.GL_FLOAT, gl.GL_FALSE, stride, offset)
      gl.glBindVertexArray(0)

   def render(self, g):
      # Render all objects attached to the graphics context.
      for quad in g.quad:
         self.quad(g, quad)
      for text in g.text:
         self.text(g, text)

   def quad(self, g, quad):
      # Enable alpha blending/transparency
      self.vbuffer.sync()

      gl.glUseProgram(self.program.id)
      gl.glEnable(gl.GL_BLEND)
      gl.glEnable(gl.GL_DEPTH_TEST)
      gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
      
      # Bind texture
      gl.glUniform1i(self.program.tex, 0) 
      gl.glBindTexture(gl.GL_TEXTURE_2D, quad.texture.id)
      
      # Set up geometry transforms
      worldMatrix = Matrix.scale(quad.width, quad.height, 1) 
      worldMatrix = Matrix.translate(quad.x, quad.y, 0) * worldMatrix
      worldViewProjectionMatrix = g.viewProjectionMatrix * worldMatrix
      #worldViewProjectionMatrix = g.viewProjectionMatrix
      gl.glUniformMatrix4fv(self.program.worldViewProjectionMatrix, 1, 0, 
                            worldViewProjectionMatrix.data)

      # Draw geometry
      gl.glBindVertexArray(self.vao)
      gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 4)
      gl.glBindVertexArray(0)
      

   def text(self, g, text):
      pass
