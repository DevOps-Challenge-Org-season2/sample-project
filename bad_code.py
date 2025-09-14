import os,sys   # bad practice: multiple imports on one line

def add_numbers(a,b):  # missing spaces after comma
  result=a+b     # bad indentation + no proper spacing
  print("Sum is:",result)   # print inside function (ok, but will trigger style/lint warnings)
  return result

def unused_function():
    x = 42   # unused variable
    return

add_numbers(2,3)

