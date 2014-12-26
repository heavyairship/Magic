#!/usr/bin/env python

from __future__ import division
import Config
import threading
import glfw
import os
import OpenGL.GL as gl
import Queue
from Renderer import Renderer
from Quad import Quad
from Texture import Texture
from Matrix import Matrix

class Context(object):
   def init(self):
      # Initialize the renderer, set up the Window.
      glfw.init()
      glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
      glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
      glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)
      glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
      glfw.window_hint(glfw.DECORATED, gl.GL_TRUE)
      glfw.window_hint(glfw.DECORATED, gl.GL_TRUE)
      glfw.window_hint(glfw.RESIZABLE, gl.GL_FALSE)

      width = Config.windowWidth
      height = Config.windowHeight

      self.aspect = width/height

      # Initialize the window
      self.window = glfw.create_window(width, height, "Magic", None, None)
      glfw.make_context_current(self.window)
      self.renderer = Renderer()
      self.quad = []
      self.text = []

      # Set up camera
      self.viewMatrix = Matrix.identity()

      # Set up view transform. View is always 16 units high, and 16 * aspect units
      # wide. The extra space outside of a 4:3 ratio is unused, to make sure that
      # all the cards always fit in a 4:3 aspect monitor. 
      vHeight = 2
      vWidth = vHeight * self.aspect
      self.projectionMatrix = Matrix.ortho(-vWidth/2, vWidth/2, vHeight/2, -vHeight/2, -1, 1)
      self.viewProjectionMatrix = self.projectionMatrix * self.viewMatrix

      # Set up viewport
      fbWidth, fbHeight = glfw.get_framebuffer_size(self.window)
      gl.glViewport(0, 0, fbWidth, fbHeight)

      # Set up communication queue
      self.queue = Queue.Queue(1)

   def poll(self):
      # Poll for input events and handle them
      glfw.poll_events()

      # Dequeue
      try:
         task = self.queue.get()
         task()
      except Queue.Empty, e:
         pass

   def render(self):
      # Render one frame
      gl.glClearColor(0, 0, 0, 0)
      gl.glClear(gl.GL_COLOR_BUFFER_BIT|gl.GL_DEPTH_BUFFER_BIT)
      self.renderer.render(self)
      glfw.swap_buffers(self.window)

   def tick(self):
      # Update physics/animations for the current tick
      pass

   def run(self):
      # This is the main game loop 
      self.init()
      while not glfw.window_should_close(self.window):
         self.poll()
         self.tick()
         self.render()
         assert(gl.glGetError()==0) # Remove this in prod
      glfw.terminate()
      os._exit(0)

