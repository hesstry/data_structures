class ArrayStack:
  """
  An ArrayStack that implements stack structure methods push and pop.
  """

  def __init__(self, size):
  """
  parameters:
    size(int): The desired size of the array
    
  attributes:
    capacity(int): the maximum number of elements the array can have
    
    n(int): the current number of elements the array has
    
    data: the array itself
  """
    self.capacity = size

    self.n = 0

    self.data = [None]*self.capacity

  def get(self, i):
    """
    parameters:
      i(int): Index for desired element

    returns:
      self.data[i]: the element at the specified index

    functionality:
      simple get method for an element given some index
    """
    return self.data[i]

  def push(self, x):
    """
    parameters:
      x: An element to be pushed to the end of the array

    returns:
      None

    Functionality:
      Push x to the top of the stack, so a[n-1] = x

      Resize the array is the capacity has been reached
    """
    if self.n == self.capacity:

      self.resize()

    self.data[self.n] = x

    self.n += 1

  def pop(self):
    """
    parameters:
      None

    returns:
      x: The value that was removed from the end of the array, x = queue[n-1]
    
    functionality:
      Pops the last element of the array from the stack and returns it
    """
    x = self.data[self.n - 1]

    self.n -= 1

    if self.capacity >= 3*self.n:

      self.resize()

    return x

  def resize(self):
  """
  parameters:
    None
    
  returns:
    None
    
  functionality:
    Resizes the array to ensure space is properly available for push, or free if capacity >= 3*n
  """

    if self.n == 0:

      b = ArrayStack(1)

    else:
    
      b = ArrayStack(2*self.n)

    for i in range(0, self.n):

      b.data[i] = self.data[i]

      b.n += 1

    self.capacity = b.capacity

    self.n = b.n

    self.data = b.data

  def __str__(self):

    return ("Current array is size {0} \n Capacity {2} \n {1}".format(self.n, self.data[:self.n], self.capacity))


if __name__ == "__main__":

  a = ArrayStack(1)

  for i in range(10):

    a.push(i)

    print(a)

  for i in range(10):

    a.pop()

  print(a)
