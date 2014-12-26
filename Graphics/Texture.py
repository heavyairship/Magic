#!/usr/bin/env python

import OpenGL.GL as gl
import PIL.Image

class Texture(object):
   def __init__(self, path):
      im = PIL.Image.open(path)
      pixel = im.tostring('raw', 'RGBX', 0, -1)
      self.id = gl.glGenTextures(1)
      self.width = im.size[0]
      self.height = im.size[1]
      gl.glBindTexture(gl.GL_TEXTURE_2D, self.id)
      gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR_MIPMAP_LINEAR);
      gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR);
      gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_CLAMP_TO_EDGE);
      gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_CLAMP_TO_EDGE);
      gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGBA8, self.width, self.height, 0, gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, pixel)
      gl.glGenerateMipmap(gl.GL_TEXTURE_2D)
      im.close()
