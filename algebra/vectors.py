"""
Name: Oliwia Zacharska

Unit tests:

>>> v1 = Vector([1, 2, 3])
>>> v2 = Vector([4, 5, 6])

>>> v1 * 2
Vector ([2, 4, 6])

>>> 2 * v1
Vector ([2, 4, 6])

>>> v1 * v2
Vector ([4, 10, 18])

>>> v1 @ v2
32

>>> a = Vector([2, 1, 2])
>>> b = Vector([0.5, 1, 0.5])

>>> a // b
Vector ([1.0, 2.0, 1.0])

>>> a % b
Vector ([1.0, -1.0, 1.0])

>>> a == (a // b) + (a % b)
True
"""


class Vector:
    """
    Represent a vector and basic operations with it.
    """

    vector = []
    vector = list()

    def __init__(self, iterable):
        """
        Build a vector from an iterable.

        Args:
            iterable: Iterable with the components of the vector.

        Returns:
            None.
        """
        self.vector = [elemento for elemento in iterable]

    def __repr__(self):
        """
        Return the official representation of the vector.

        Args:
            None.

        Returns:
            A string.
        """
        return "Vector (" + repr(self.vector) + ")"

    def __str__(self):
        """
        Return the string representation of the vector.

        Args:
            None.

        Returns:
            A string.
        """
        return str(self.vector)

    def __getitem__(self, key):
        """
        Return one component of the vector.

        Args:
            key: Position of the component.

        Returns:
            The requested component.
        """
        return self.vector[key]

    def __len__(self):
        """
        Return the dimension of the vector.

        Args:
            None.

        Returns:
            An integer.
        """
        return len(self.vector)

    def __setitem__(self, key, value):
        """
        Change one component of the vector.

        Args:
            key: Position to modify.
            value: New value.

        Returns:
            None.
        """
        self.vector[key] = value

    def __eq__(self, other):
        """
        Compare two vectors.

        Args:
            other: Another vector.

        Returns:
            A boolean.
        """
        return self.vector == other.vector

    def __add__(self, other):
        """
        Add a scalar to a vector or add two vectors.

        Args:
            other: A scalar or another vector.

        Returns:
            A new vector.
        """
        if isinstance(other, (int, float, complex)):
            return Vector([elemento + other for elemento in self])
        else:
            return Vector([uno + otro for uno, otro in zip(self, other)])

    __radd__ = __add__

    def __neg__(self):
        """
        Return the opposite vector.

        Args:
            None.

        Returns:
            A new vector.
        """
        return Vector([-elemento for elemento in self])

    def __sub__(self, other):
        """
        Subtract a scalar or a vector.

        Args:
            other: A scalar or another vector.

        Returns:
            A new vector.
        """
        return -(other + (-self))

    def __iadd__(self, other):
        """
        Add and assign.

        Args:
            other: A scalar or another vector.

        Returns:
            The modified vector.
        """
        if type(other) in (float, int, complex):
            for indice, elemento in enumerate(self):
                self.vector[indice] += other
            return self
        else:
            for indice, elemento in enumerate(self):
                self.vector[indice] += other[indice]
            return self

    def __mul__(self, other):
        """
        Multiply a vector by a scalar or compute the
        Hadamard product of two vectors.

        Args:
            other: A scalar or another vector.

        Returns:
            A new vector.
        """
        if isinstance(other, (int, float, complex)):
            return Vector([elemento * other for elemento in self])
        else:
            return Vector([uno * otro for uno, otro in zip(self, other)])

    __rmul__ = __mul__

    def __matmul__(self, other):
        """
        Compute the dot product of two vectors.

        Args:
            other: Another vector.

        Returns:
            A number.
        """
        return sum([uno * otro for uno, otro in zip(self, other)])

    def __floordiv__(self, other):
        """
        Return the tangential component of this vector
        with respect to another vector.

        Args:
            other: Another vector.

        Returns:
            A new vector.
        """
        return ((self @ other) / (other @ other)) * other

    def __mod__(self, other):
        """
        Return the normal component of this vector
        with respect to another vector.

        Args:
            other: Another vector.

        Returns:
            A new vector.
        """
        return self - (self // other)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)