#global
x="glow"
def outer():
  x = "bye"
  def inner():
    global x #bind to proper global variable
    x = "hello"
    print("inner:",x)
  inner()
  print("outer:",x)
outer()
print("global:",x)

# -->
# inner: hello
# outer: bye
# global: hello

#nonlocal
x="glow"
def outer():
  x = "bye"
  def inner():
    nonlocal x
    # global x
    x = "hello"
    print("inner:",x)
  inner()
  print("outer:",x)
outer()
print("global:",x)

# -->
# inner: hello
# outer: hello
# global: glow

#regular
x="glow"
def outer():
  x = "bye"
  def inner():
    x = "hello"
    print("inner:",x)
  inner()
  print("outer:",x)
outer()
print("global:",x)
# -->
# inner: hello
# outer: bye
# global: glow