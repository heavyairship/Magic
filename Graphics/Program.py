#!/usr/bin/env python

import OpenGL.GL as gl
import re
from Shader import Shader

class Program(object):
   def __init__(self, path):
      self.id = gl.glCreateProgram()
      self.fragment = Shader(re.sub('.prog$', '.frag', path), gl.GL_FRAGMENT_SHADER)
      self.vertex = Shader(re.sub('.prog$', '.vert', path), gl.GL_VERTEX_SHADER)
      try:
         self.geometry = Shader(re.sub('.prog$', '.geom', path), gl.GL_GEOMETRY_SHADER)
      except IOError, e:
         self.geometry = None
      
      if self.fragment:
         gl.glAttachShader(self.id, self.fragment.id)
      if self.vertex:
         gl.glAttachShader(self.id, self.vertex.id)
      if self.geometry:
         gl.glAttachShader(self.id, self.geometry.id)

      gl.glLinkProgram(self.id)
      if gl.glGetProgramiv(self.id, gl.GL_LINK_STATUS) != gl.GL_TRUE:
         raise Exception(gl.glGetProgramInfoLog(self.id))

      uniforms = gl.glGetProgramiv(self.id, gl.GL_ACTIVE_UNIFORMS)
      maxlen = gl.glGetProgramiv(self.id, gl.GL_ACTIVE_UNIFORM_MAX_LENGTH)

      for i in range(0,uniforms):
         name, size, kind = gl.glGetActiveUniform(self.id, i)
         setattr(self, name, gl.glGetUniformLocation(self.id, name))
