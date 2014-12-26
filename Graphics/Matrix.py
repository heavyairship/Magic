#!/usr/bin/env python

from __future__ import division
import ctypes

class Matrix(object):
   def __init__(self, *args):
      self.data = (ctypes.c_float * 16)(*args)

   def __mul__(self, other):
      ret = Matrix()
      out, m1, m2 = ret.data, other.data, self.data

      out[0] = m1[0]*m2[0] + m1[1]*m2[4] + m1[2]*m2[8] + m1[3]*m2[12]
      out[1] = m1[0]*m2[1] + m1[1]*m2[5] + m1[2]*m2[9] + m1[3]*m2[13]
      out[2] = m1[0]*m2[2] + m1[1]*m2[6] + m1[2]*m2[10] + m1[3]*m2[14]
      out[3] = m1[0]*m2[3] + m1[1]*m2[7] + m1[2]*m2[11] + m1[3]*m2[15]
      
      out[4] = m1[4]*m2[0] + m1[5]*m2[4] + m1[6]*m2[8] + m1[7]*m2[12]
      out[5] = m1[4]*m2[1] + m1[5]*m2[5] + m1[6]*m2[9] + m1[7]*m2[13]
      out[6] = m1[4]*m2[2] + m1[5]*m2[6] + m1[6]*m2[10] + m1[7]*m2[14]
      out[7] = m1[4]*m2[3] + m1[5]*m2[7] + m1[6]*m2[11] + m1[7]*m2[15]
      
      out[8] = m1[8]*m2[0] + m1[9]*m2[4] + m1[10]*m2[8] + m1[11]*m2[12]
      out[9] = m1[8]*m2[1] + m1[9]*m2[5] + m1[10]*m2[9] + m1[11]*m2[13]
      out[10] = m1[8]*m2[2] + m1[9]*m2[6] + m1[10]*m2[10] + m1[11]*m2[14]
      out[11] = m1[8]*m2[3] + m1[9]*m2[7] + m1[10]*m2[11] + m1[11]*m2[15]
      
      out[12] = m1[12]*m2[0] + m1[13]*m2[4] + m1[14]*m2[8] + m1[15]*m2[12]
      out[13] = m1[12]*m2[1] + m1[13]*m2[5] + m1[14]*m2[9] + m1[15]*m2[13]
      out[14] = m1[12]*m2[2] + m1[13]*m2[6] + m1[14]*m2[10] + m1[15]*m2[14]
      out[15] = m1[12]*m2[3] + m1[13]*m2[7] + m1[14]*m2[11] + m1[15]*m2[15]

      return ret

   def __str__(self):
      return '\n'.join((
         '%f, %f, %f, %f' % (self[0], self[4], self[8], self[12]),
         '%f, %f, %f, %f' % (self[1], self[5], self[9], self[12]),
         '%f, %f, %f, %f' % (self[2], self[6], self[10], self[14]),
         '%f, %f, %f, %f' % (self[3], self[7], self[11], self[15])))

   @staticmethod
   def frustum(left, right, bottom, top, near, far):
      l, r, b, t, n, f = left, right, bottom, top, near, far
      return Matrix(
         2*n/(r-l),    0,            0,                0,
         0,            2*n/(t-b),    0,                0,
         (r+l)/(r-l),  (t+b)/(t-b),  -(far+n)/(far-n), -1,
         0,            0,            -2*far*n/(far-n), 0)

   def __getitem__(self, index):
      return self.data[index]

   @staticmethod
   def ortho(left, right, bottom, top, near, far):
      l, r, b, t, n, f = left, right, bottom, top, near, far
      return Matrix(
         2/(r-l),  0,        0,        0,
         0,        2/(t-b),  0,        0,
         0,        0,        -2/(f-n), 0,
         -(r+l)/(r-l), -(t+b)/(t-b), -(f+n)/(f-n), 1)

   @staticmethod
   def identity():
      return Matrix(
         1, 0, 0, 0,
         0, 1, 0, 0,
         0, 0, 1, 0,
         0, 0, 0, 1) 

   @staticmethod
   def translate(x, y, z):
      return Matrix(
         1, 0, 0, 0,
         0, 1, 0, 0,
         0, 0, 1, 0,
         x, y, z, 1)

   @staticmethod
   def scale(x, y, z):
      return Matrix(
         x, 0, 0, 0,
         0, y, 0, 0,
         0, 0, z, 0,
         0, 0, 0, 1) 

