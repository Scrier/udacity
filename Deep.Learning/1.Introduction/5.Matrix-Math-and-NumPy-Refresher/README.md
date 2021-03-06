# Matrix Math and NumPy Refresher

## 1. Introduction

![part1-1](readme/part1-1.png)

Deep learning involves a lot of matrix math, and it’s important for you to understand the basics before diving into 
building your own neural networks. These lessons provide a short refresher on what you need to know for this course, 
along with some guidance for using the [NumPy](http://www.numpy.org/) library to work efficiently with matrices in Python.

## 2. Data Dimensions

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F1.Introduction%2F5.Matrix-Math-and-NumPy-Refresher%2Freadme&filename=1%20-%20Data%20Has%20Dimensions.mp4&fid=0MZqBkd&open=normal)
 
## 3. Data in NumPy

Python is convenient, but it can also be slow. However, it does allow you to access libraries that execute faster code 
written in languages like C. NumPy is one such library: it provides fast alternatives to math operations in Python and 
is designed to work efficiently with groups of numbers - like matrices.

NumPy is a large library and we are only going to scratch the surface of it here. If you plan on doing much math with 
Python, you should definitely spend some time exploring its [documentation](https://docs.scipy.org/doc/numpy/reference/) to learn more.

### Importing NumPy

When importing the NumPy library, the convention you'll see used most often – including here – is to name it `np`, like so:

    import numpy as np
    
Now you can use the library by prefixing the names of functions and types with `np.`, which you'll see in the following examples.

### Data Types and Shapes

The most common way to work with numbers in NumPy is through `ndarray` objects. They are similar to Python lists, but 
can have any number of dimensions. Also, `ndarray` supports fast math operations, which is just what we want.

Since it can store any number of dimensions, you can use `ndarray`s to represent any of the data types we covered 
before: scalars, vectors, matrices, or tensors.

### Scalars

[Scalars in NumPy](https://docs.scipy.org/doc/numpy/reference/arrays.scalars.html) are a bit more involved than in 
Python. Instead of Python’s basic types like `int`, `float`, etc., NumPy lets you specify signed and unsigned types, 
as well as different sizes. So instead of Python’s `int`, you have access to types like `uint8`, `int8`, `uint16`, 
`int16`, and so on.

These types are important because every object you make (vectors, matrices, tensors) eventually stores scalars. And 
when you create a NumPy array, you can specify the type - **but every item in the array must have the same type**. In 
this regard, NumPy arrays are more like C arrays than Python lists.

If you want to create a NumPy array that holds a scalar, you do so by passing the value to NumPy's `array` function, 
like so:

    s = np.array(5)
    
You can still perform math between `ndarray`s, NumPy scalars, and normal Python scalars, though, as you'll see in the 
element-wise math lesson.

You can see the shape of your arrays by checking their `shape` attribute. So if you executed this code:

    s.shape

it would print out the result, an empty pair of parenthesis, `()`. This indicates that it has zero dimensions.

Even though scalars are inside arrays, you still use them like a normal scalar. So you could type:

    x = s + 3

and `x` would now equal `8`. If you were to check the type of `x`, you'd find it is probably `numpy.int64`, because its 
working with NumPy types, not Python types.

By the way, even scalar types support most of the array functions. so you can call `x.shape` and it would return `()` 
because it has zero dimensions, even though it is not an array. If you tried that with a normal Python scalar, you'd 
get an error.

### Vectors

To create a vector, you'd pass a Python list to the `array` function, like this:

    v = np.array([1,2,3])

If you check a vector's `shape` attribute, it will return a single number representing the vector's one-dimensional 
length. In the above example, `v.shape` would return `(3,)`

Now that there is a number, you can see that the shape is a tuple with the sizes of each of the `ndarray`'s dimensions. 
For scalars it was just an empty tuple, but vectors have one dimension, so the tuple includes a number and a comma. 
(Python doesn’t understand `(3)` as a tuple with one item, so it requires the comma. You can read more about tuples 
[here](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences))

You can access an element within the vector using indices, like this:

    x = v[1]

Now `x` equals `2`.

NumPy also supports advanced indexing techniques. For example, to access the items from the second element onward, you 
would say:

    v[1:]

and it would return an array of `[2, 3]`. NumPy slicing is quite powerful, allowing you to access any combination of 
items in an `ndarray`. But it can also be a bit complicated, so you should read up on it [in the documentation](https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html).

### Matrices

You create matrices using NumPy's `array` function, just you did for vectors. However, instead of just passing in a 
list, you need to supply a list of lists, where each list represents a row. So to create a 3x3 matrix containing the 
numbers one through nine, you could do this:

    m = np.array([[1,2,3], [4,5,6], [7,8,9]])

Checking its `shape` attribute would return the tuple `(3, 3)` to indicate it has two dimensions, each length 3.

You can access elements of matrices just like vectors, but using additional index values. So to find the number `6` in 
the above matrix, you'd access `m[1][2]`.

### Tensors

Tensors are just like vectors and matrices, but they can have more dimensions. For example, to create a 3x3x2x1 tensor, 
you could do the following:

    t = np.array([[[[1],[2]],[[3],[4]],[[5],[6]]],[[[7],[8]],\
        [[9],[10]],[[11],[12]]],[[[13],[14]],[[15],[16]],[[17],[17]]]])

And `t.shape` would return `(3, 3, 2, 1)`.

You can access items just like with matrices, but with more indices. So `t[2][1][1][0]` will return `16`.

### Changing Shapes

Sometimes you'll need to change the shape of your data without actually changing its contents. For example, you may 
have a vector, which is one-dimensional, but need a matrix, which is two-dimensional. There are two ways you can do 
that.

Let's say you have the following vector:

    v = np.array([1,2,3,4])

Calling `v.shape` would return `(4,)`. But what if you want a 1x4 matrix? You can accomplish that with the `reshape` 
function, like so:

    x = v.reshape(1,4)

Calling `x.shape` would return `(1,4)`. If you wanted a 4x1 matrix, you could do this:

    x = v.reshape(4,1)

The `reshape` function works for more than just adding a dimension of size 1. Check out its [documentation](https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html) 
for more examples.

One more thing about reshaping NumPy arrays: if you see code from experienced NumPy users, you will often see them use 
a special slicing syntax instead of calling `reshape`. Using this syntax, the previous two examples would look like 
this:

    x = v[None, :]

or

    x = v[:, None]

Those lines create a slice that looks at all of the items of v but asks NumPy to add a new dimension of size 1 for the 
associated axis. It may look strange to you now, but it's a common technique so it's good to be aware of it.

## 4. Element-wise Matrix Operations

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F1.Introduction%2F5.Matrix-Math-and-NumPy-Refresher%2Freadme&filename=2%20-%20Element-wise%20Matrix%20Operations.mp4&fid=0MZqBkd&open=normal)
 
## 5. Element-wise Operations in NumPy

### The Python way
Suppose you had a list of numbers, and you wanted to add 5 to every item in the list. Without NumPy, you might do 
something like this:

```python
values = [1,2,3,4,5]
for i in range(len(values)):
    values[i] += 5

# now values holds [6,7,8,9,10]
```

That makes sense, but it's a lot of code to write and it runs slowly because it's pure Python.

**Note:** Just in case you aren't used to using operators like `+=`, that just means "add these two items and then 
store the result in the left item." It is a more succinct way of writing `values[i] = values[i] + 5`. The code you see 
in these examples makes use of such operators whenever possible.

### The NumPy way

In NumPy, we could do the following:

```python
values = [1,2,3,4,5]
values = np.array(values) + 5

# now values is an ndarray that holds [6,7,8,9,10]
```

Creating that array may seem odd, but normally you'll be storing your data in `ndarray`s anyway. So if you already had 
an `ndarray` named `values`, you could have just done:

    values += 5

We should point out, NumPy actually has functions for things like adding, multiplying, etc. But it also supports using 
the standard math operators. So the following two lines are equivalent:

```python
x = np.multiply(some_array, 5)
x = some_array * 5
```

We will usually use the operators instead of the functions because they are more convenient to type and easier to read, 
but it's really just personal preference.

One more example of operating with scalars and `ndarray`s. Let's say you have a matrix `m` and you want to reuse it, but 
first you need to set all its values to zero. Easy, just multiply by zero and assign the result back to the matrix, 
like this:

```python
m *= 0

# now every element in m is zero, no matter how many dimensions it has
```

### Element-wise Matrix Operations
The same functions and operators that work with scalars and matrices also work with other dimensions. You just need to 
make sure that the items you perform the operation on have compatible shapes.

Let's say you want to get the squared values of a matrix. That's simply `x = m * m` (or if you want to assign the value 
back to m, it's just `m *= m`

This works because it's an element-wise multiplication between two identically-shaped matrices. (In this case, they are 
shaped the same because they are actually the same object.)

Here's the example from the video:

```python
a = np.array([[1,3],[5,7]])
a
# displays the following result:
# array([[1, 3],
#        [5, 7]])

b = np.array([[2,4],[6,8]])
b
# displays the following result:
# array([[2, 4],
#        [6, 8]])

a + b
# displays the following result
#      array([[ 3,  7],
#             [11, 15]])
```

And if you try working with incompatible shapes, like the other example from the video, you'd get an error:

```python
a = np.array([[1,3],[5,7]])
a
# displays the following result:
# array([[1, 3],
#        [5, 7]])
c = np.array([[2,3,6],[4,5,9],[1,8,7]])
c
# displays the following result:
# array([[2, 3, 6],
#        [4, 5, 9],
#        [1, 8, 7]])

a.shape
# displays the following result:
#  (2, 2)

c.shape
# displays the following result:
#  (3, 3)

a + c
# displays the following error:
# ValueError: operands could not be broadcast together with shapes (2,2) (3,3)
```

You'll learn more about what that "could not be broadcast together" means in a later lesson, but for now, just notice 
that the two shapes are different so we can't perform the element-wise operation.

## 6. Matrix Multiplication: Part 1

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F1.Introduction%2F5.Matrix-Math-and-NumPy-Refresher%2Freadme&filename=3%20-%20Matrix%20Multiplication%3A%20Part%201.mp4&fid=0MZqBkd&open=normal)
 
Some more information about [dot products](https://en.wikipedia.org/wiki/Dot_product)

## 7. Matrix Multiplication: Part 2

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F1.Introduction%2F5.Matrix-Math-and-NumPy-Refresher%2Freadme&filename=4%20-%20Matrix%20Multiplication%3A%20Part%202.mp4&fid=0MZqBkd&open=normal)
 
### Important Reminders About Matrix Multiplication

 * The **number** of **columns** in the **left** matrix **must equal** the **number** of **rows** in the **right** matrix.
 * The **answer** matrix **always has** the **same number** of **rows** as the **left** matrix and the **same number** of **columns** as the **right** matrix.
 * **Order matters**. Multiplying **A•B** is **not the same** as multiplying **B•A**.
 * Data in the **left** matrix **should be** arranged as **rows**., while data in the **right** matrix **should be** arranged as **columns**.

If you keep these four points in mind, you should always be able to figure out how to properly arrange your matrix 
multiplications when building a neural network.

## 8.NumPy Matrix Multiplication
You've heard a lot about matrix multiplication in the last few videos – now you'll get to see how to do it with NumPy. 
However, it's important to know that NumPy supports several types of matrix multiplication.

Element-wise Multiplication
You saw some element-wise multiplication already. You accomplish that with the `multiply` function or the `*` operator. 
Just to revisit, it would look like this:

```python
m = np.array([[1,2,3],[4,5,6]])
m
# displays the following result:
# array([[1, 2, 3],
#        [4, 5, 6]])

n = m * 0.25
n
# displays the following result:
# array([[ 0.25,  0.5 ,  0.75],
#        [ 1.  ,  1.25,  1.5 ]])

m * n
# displays the following result:
# array([[ 0.25,  1.  ,  2.25],
#        [ 4.  ,  6.25,  9.  ]])

np.multiply(m, n)   # equivalent to m * n
# displays the following result:
# array([[ 0.25,  1.  ,  2.25],
#        [ 4.  ,  6.25,  9.  ]])
```

### Matrix Product

To find the matrix product, you use NumPy's `matmul` function.

If you have compatible shapes, then it's as simple as this:

```python
a = np.array([[1,2,3,4],[5,6,7,8]])
a
# displays the following result:
# array([[1, 2, 3, 4],
#        [5, 6, 7, 8]])
a.shape
# displays the following result:
# (2, 4)

b = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
b
# displays the following result:
# array([[ 1,  2,  3],
#        [ 4,  5,  6],
#        [ 7,  8,  9],
#        [10, 11, 12]])
b.shape
# displays the following result:
# (4, 3)

c = np.matmul(a, b)
c
# displays the following result:
# array([[ 70,  80,  90],
#        [158, 184, 210]])
c.shape
# displays the following result:
# (2, 3)
```

If your matrices have incompatible shapes, you'll get an error, like the following:

```python
np.matmul(b, a)
# displays the following error:
# ValueError: shapes (4,3) and (2,4) not aligned: 3 (dim 1) != 2 (dim 0)
```

### NumPy's dot function

You may sometimes see NumPy's `dot` function in places where you would expect a `matmul`. It turns out that the results 
of `dot` and `matmul` are the same if the matrices are two dimensional.

So these two results are equivalent:

```python
a = np.array([[1,2],[3,4]])
a
# displays the following result:
# array([[1, 2],
#        [3, 4]])

np.dot(a,a)
# displays the following result:
# array([[ 7, 10],
#        [15, 22]])

a.dot(a)  # you can call `dot` directly on the `ndarray`
# displays the following result:
# array([[ 7, 10],
#        [15, 22]])

np.matmul(a,a)
# array([[ 7, 10],
#        [15, 22]])
```

While these functions return the same results for two dimensional data, you should be careful about which you choose 
when working with other data shapes. You can read more about the differences, and find links to other NumPy functions, 
in the `matmul` and `dot` documentation.

## 9.Matrix Transposes

[![Video](../../../images/video.jpg)](http://scrier.myqnapcloud.com:8080/share.cgi?ssid=0MZqBkd&ep=&path=%2FDeep.Learning%2F1.Introduction%2F5.Matrix-Math-and-NumPy-Refresher%2Freadme&filename=5%20-%20Matrix%20Transposes.mp4&fid=0MZqBkd&open=normal)
 
## 10. Transposes in NumPy

Getting the transpose of a matrix is really easy in NumPy. Simply access its T attribute. There is also a `transpose()` 
function which returns the same thing, but you’ll rarely see that used anywhere because typing `T` is so much easier. :)

For example:

```python
m = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
m
# displays the following result:
# array([[ 1,  2,  3,  4],
#        [ 5,  6,  7,  8],
#        [ 9, 10, 11, 12]])

m.T
# displays the following result:
# array([[ 1,  5,  9],
#        [ 2,  6, 10],
#        [ 3,  7, 11],
#        [ 4,  8, 12]])
```

NumPy does this without actually moving any data in memory - it simply changes the way it indexes the original matrix - 
so it’s quite efficient.

However, that also means you need to be careful with how you modify objects, because **they are sharing the same data**. 
For example, with the same matrix `m` from above, let's make a new variable `m_t` that stores `m`'s transpose. Then look 
what happens if we modify a value in `m_t`:

```python
m_t = m.T
m_t[3][1] = 200
m_t
# displays the following result:
# array([[ 1,   5, 9],
#        [ 2,   6, 10],
#        [ 3,   7, 11],
#        [ 4, 200, 12]])

m
# displays the following result:
# array([[ 1,  2,  3,   4],
#        [ 5,  6,  7, 200],
#        [ 9, 10, 11,  12]])
```

Notice how it modified both the transpose and the original matrix, too! That's because they are sharing the same copy 
of data. So remember to consider the transpose just as a different view of your matrix, rather than a different matrix 
entirely.

### A real use case

I don't want to get into too many details about neural networks because you haven't covered them yet, but there is one 
place you will almost certainly end up using a transpose, or at least thinking about it.

Let's say you have the following two matrices, called `inputs` and `weights`,

```python
inputs = np.array([[-0.27,  0.45,  0.64, 0.31]])
inputs
# displays the following result:
# array([[-0.27,  0.45,  0.64,  0.31]])

inputs.shape
# displays the following result:
# (1, 4)

weights = np.array([[0.02, 0.001, -0.03, 0.036], \
    [0.04, -0.003, 0.025, 0.009], [0.012, -0.045, 0.28, -0.067]])

weights
# displays the following result:
# array([[ 0.02 ,  0.001, -0.03 ,  0.036],
#        [ 0.04 , -0.003,  0.025,  0.009],
#        [ 0.012, -0.045,  0.28 , -0.067]])

weights.shape
# displays the following result:
# (3, 4)
```

I won't go into what they're for because you'll learn about them later, but you're going to end up wanting to find the 
**matrix product** of these two matrices.

If you try it like they are now, you get an error:

```python
np.matmul(inputs, weights)
# displays the following error:
# ValueError: shapes (1,4) and (3,4) not aligned: 4 (dim 1) != 3 (dim 0)
```

If you did the matrix multiplication lesson, then you've seen this error before. It's complaining of incompatible shapes 
because the number of columns in the left matrix, `4`, does not equal the number of rows in the right matrix, `3`.

So that doesn't work, but notice if you take the transpose of the `weights` matrix, it will:

```python
np.matmul(inputs, weights.T)
# displays the following result:
# array([[-0.01299,  0.00664,  0.13494]])
```

It also works if you take the transpose of `inputs` instead and swap their order, like we showed in the video:

```python
np.matmul(weights, inputs.T)
# displays the following result:
# array([[-0.01299],# 
#        [ 0.00664],
#        [ 0.13494]])
```

The two answers are transposes of each other, so which multiplication you use really just depends on the shape you 
want for the output.
