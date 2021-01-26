class DynamicArray:

    def __init__(self, size):
        """
        ***Private attributes are not used to make this implementation simpler***

        parameters:
          size(int): determines the initial size capacity of the array

        attributes:
          n(int): the number of elements in the queue

          data(array): the array of elements
        """

        self.capacity = size
        self.n = 0
        self.data = [None] * self.capacity

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

        if i >= 0 & i <= self.n - 1:
            return self.data[i]

        return None

    def set(self, i, x):
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

        if i >= 0 & i <= self.n - 1:
            self.data[i] = x
            return self.data[i]

        return None

    def add(self, i, x):
        """
        parameters:
            i(int): index to add element to
            x: any value to append to the array

        returns:
            array[i] if index within proper bounds
            None otherwise

        Functionality:
            If self.n == capacity, then resize is called first to make room for an additional element

            shifts all elements right one index first to make space for x, adds x to list at index i

            n is incremented to update the number of elements in the queue
        """
        if i < 0 or i >= self.n+1:
            return None

        if self.n == self.capacity:
            self.resize()

        for ind in range(self.n-1, i, -1):
            # shifts right starting at last index so overwriting of values doesn't occur
            # This can be a costly method
            self.data[self.n] = self.data[ind]

        self.data[i] = x

        self.n += 1

    def remove(self, i):
        """
        parameters:
          i(int): Index of element to remove

        returns:
          x: The element that was removed from the queue

          None: if i isn't within index boundaries

        Functionality:
          Removes the element in the queue corresponding to array[] and returns this value

          n is decremented to update the number of elements in the array

          If the array capacity grows to be too large compared to the number of elements in the array, then
          resize() is called to free up space

            the relation "capacity >= 3*n" allows for a maximum sequential remove() depth of n/2 elements, allowing
            for a downsize that results in new capacity values divisible by 2 until capacity == 1 is reached
        """
        if i < 0 or i >= self.n + 1:
            return None

        x = self.data[i]

        # shift over all elements left one starting with array[i+1]
        for ind in range(i+1, self.n):
            self.data[ind-1] = self.data[ind]

        self.n -= 1

        if self.capacity >= 3 * self.n:
            self.resize()

        return x


    def resize(self):
        """
        parameters:
          None

        returns:
          None

        functionality:
          Resizes the array to either make room for add(), or decrease room because
          remove() was called many more times than add() and capacity >= 3*n
        """
        if self.n == 0:
            b = DynamicArray(1)
            
        else:
            b = DynamicArray(2 * self.n)

        for k in range(self.n):
            b.data[k] = self.data[k]
            b.n += 1

        self.capacity = b.capacity

        self.n = b.n

        self.data = b.data


    def __str__(self):
        return ("Current array is size {0} capacity {2}: {1}".format(self.n, self.data[:self.n], self.capacity))


if __name__ == "__main__":

# Runs a simple implementation of the DynamicArray

    a = DynamicArray(1)

    for i in range(20):
        a.add(i, i)
        print(a)

    for i in range(20):
        a.remove(i)
        print(a)
