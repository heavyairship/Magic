def checkType(instance,type_):
   if not isinstance(instance,type_):
      raise TypeError("actual: %s, expected: %s" % (str(type(instance)),str(type_)))
