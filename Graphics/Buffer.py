#!/usr/bin/env python

import OpenGL.GL as gl
import ctypes
import math

class Buffer(object):
   def __init__(self, target, usage, kind):
      # Flat buffer of vertices for rendering things
      self.target = target
      self.usage = usage
      self.kind = kind
      self.capacity = 4
      self.count = 0
      self.stride = ctypes.sizeof(kind)
      self.element = (kind * self.capacity)()
      self.status = 'dirty'

      # Generate OpenGL buffer
      self.id = gl.glGenBuffers(1)
   
   def reserve(self, count):
      # Reserve 'count' slots in the buffer
      if count <= self.count: return
      if count <= self.capacity:
         self.count = count
         return
      capacity = count+count//2
      self.element = (self.kind * capacity)(*self.element)
      self.count = count
      self.capacity = capacity
      self.status = 'dirty'

   def push(self, element):
      index = self.count
      self.reserve(index+1)
      self.element[index] = element
      self.status = 'dirty'

   def __setitem__(self, index, element):
      self.reserve(index+1)
      self.element[index] = element
      self.status = 'dirty'

   def __getitem__(self, index):
      if index < self.count:
         return self.element[index]
      else:
         return None

   def sync(self):
      # Sync the buffer with the graphics hardware if the buffer is dirty
      if self.status == 'synced': return
      size = self.stride * self.count 
      gl.glBindBuffer(self.target, self.id)
      gl.glBufferData(self.target, size, self.element, self.usage)
      self.status = 'synced'

