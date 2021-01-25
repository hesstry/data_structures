class ArrayQueue:
  """Implementation of an ArrayQueue"

  def __init__(self, size):
  """
  ***Private attributes are not used to make this implementation simpler***
  
  parameters:
    size(int): determines the initial size capacity of the array
    
  attributes:
    j(int): the index of the first element of the queue
    
    n(int): the number of elements in the queue
    
    data(array): the array of elements
  """

    self.capacity = size

    self.j = 0

    self.n = 0

    self.data = [None]*self.capacity
    
  def get(self, i):
  """
  parameters:
    i(int): Index for desired element

  returns:
    self.data[i]: the element at the specified index if index contains an element

    None other wise

  functionality:
    simple get method for an element given some index
  """
    if i >= 0 & i <= self.n-1:

      return self.data[i]

    return None

  def set(self,i, x):
    """
    parameters:
      i(int): Index for desired element to change

      x: value to change element to

    returns:
      array[i] if set properly

      None otherwise

    functionality:
      simple set method for an element given some index
    """
    if i >= 0 & i <= self.n-1:

      self.data[i] = x

      return self.data[i]

    return None

  def add(self, x):
  """
  parameters:
    x: any value to append to the array
    
  returns:
    None
    
  Functionality:
    Appends items to the array, first checking whether or not there is space to append. If 
    no space exists, then resize() is called,
    causing the array to double in capacity.
    
    Modular arithmetic is used to allow for items to be appended in open spaces at the beginning 
    of the queue. These will come into existence whenever remove() is called, as items from a 
    queue are removed from the beginning.
    
      (self.j + self.n) % self.capacity will choose the next available index in the queue
    
    n is incremented to update the number of elements in the queue
  """
    if self.n + 1 > self.capacity:

      self.resize()

    self.data[(self.j + self.n) % self.capacity] = x

    self.n += 1

  def remove(self):
  """
  parameters:
    None
    
  returns:
    x: The element that was removed from the queue
    
  Functionality:
    Removes the element in the queue corresponding to queue[self.j] and returns this value
    
    j is incremented to update the new first element in the queue
    
    n is deremented to update the number of elements in the queue
    
    If the queue capacity grows to be too large compared to the number of elements in the queue, then 
    resize() is called to free up space, causing the new array
    
      the relation "capacity >= 3*n" allows for a maximum sequential remove() depth of n/2 elements, allowing
      for a downsize that results in new capacity values divisible by 2
  """
    x = self.data[self.j]

    self.j += 1

    self.n -= 1

    if self.capacity >= 3*self.n:

      self.resize()

    return x

  def resize(self):
    
    b = ArrayQueue(2*self.n)

    for k in range(self.n):

      b.data[k] = self.data[self.j + k]

      b.n += 1

    self.capacity = b.capacity

    self.j = 0

    self.n = b.n

    self.data = b.data

  def __str__(self):

    return ("Current array is size {0} capacity {2}: {1}".format(self.n, self.data[:self.n], self.capacity))

if __name__ == "__main__":

  # Runs a simple implementation of the ArrayQueue

  a = ArrayQueue(1)

  for i in range(20):

    a.add(i)

    print(a)

  for i in range(20):

    a.remove()

  print(a)
