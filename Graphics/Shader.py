#!/usr/bin/env python

import OpenGL.GL as gl

class Shader(object):
   def __init__(self, path, kind):
      with open(path) as fd:
         self.source = fd.read()
      self.id = gl.glCreateShader(kind)
      gl.glShaderSource(self.id, self.source)
      gl.glCompileShader(self.id)
      if gl.glGetShaderiv(self.id, gl.GL_COMPILE_STATUS) != gl.GL_TRUE:
         raise Exception(gl.glGetShaderInfoLog(self.id))
