In the context of machine learning, a square matrix is simply a matrix that has the same number of rows and columns. The subscript s in W_s suggests that it is a specific type of weight matrix used in the network. 

Consider a simple 2x2 square matrix:

    W_s = [ w11  w12 ]
          [ w21  w22 ]

In the context of deep learning, these values w11, w12, w21, w22 are learnable parameters or weights, and they're updated during the training process. 

Let's say we have a 2-dimensional input vector X = [x1, x2]. This matrix can be used to transform the input vector, resulting in a new vector Y:

    Y = W_s * X

This is computed as follows:

    Y = [ w11*x1 + w12*x2 ]
        [ w21*x1 + w22*x2 ]

This matrix W_s could be used instead of the identity matrix in the mentioned Eqn.(1) to transform the input. However, the text you provided suggests that using the identity matrix is sufficient and more efficient for addressing the degradation problem in deep learning (which refers to a degradation in performance as the network depth increases). 

The identity matrix, for comparison, is a special type of square matrix where all the elements of the principal diagonal are ones, and all other elements are zeros. For example, a 2x2 identity matrix is:

    I = [ 1  0 ]
        [ 0  1 ]

This identity matrix, when used to transform an input vector, doesn't change its values:

    Y = I * X = X

---
1. **Identity Matrix**: An identity matrix is a special type of square matrix where all the elements of the principal diagonal are ones, and all other elements are zeros. In other words, if the matrix is represented as a grid of numbers, the numbers from the top-left to the bottom-right (the diagonal) are all ones, and all the other numbers in the grid are zeros. 

   Here's an example of a 3x3 identity matrix:
   ```
   I = [ 1  0  0 ]
       [ 0  1  0 ]
       [ 0  0  1 ]
   ```

   When you multiply any matrix or vector with this identity matrix, you'll get the original matrix or vector back.

   For example, if you have a vector V = [v1, v2, v3] and you multiply it with this identity matrix, you'll get V itself.

2. **Square Matrix W_s**: This is another type of square matrix, but unlike the identity matrix, it doesn't have any particular pattern of numbers. The values can be anything and are typically learned during the training process in machine learning.

   Here's an example of a 3x3 square matrix:
   ```
   W_s = [ w11  w12  w13 ]
         [ w21  w22  w23 ]
         [ w31  w32  w33 ]
   ```
   
   In this matrix, each 'w' represents a weight, and the two numbers after 'w' represent the row and column of the weight.

   This matrix can be used to transform an input vector X = [x1, x2, x3] into another vector Y:
   ```
   Y = W_s * X
   ```
   The multiplication is done as follows:
   ```
   Y = [ w11*x1 + w12*x2 + w13*x3 ]
       [ w21*x1 + w22*x2 + w23*x3 ]
       [ w31*x1 + w32*x2 + w33*x3 ]
   ```

   In the context of ResNet, this W_s matrix is used to transform the input of a layer before it is added to the output of the layer, but only when the input and output have different dimensions (i.e., they don't match). The values of the weights in the W_s matrix are learned during the training process.

---
In the context of machine learning and neural networks, x1, x2, x3 are the elements of the input vector that is being processed by the matrix W_s. 

When you multiply a matrix by a vector in linear algebra, you're essentially taking a combination of the elements of the vector, with the specific combination determined by the elements of the matrix.

Let's consider a simple example where you have an input vector X = [x1, x2, x3], and you want to transform it using a matrix W_s. Each element in the resulting vector is a weighted sum of the input elements, where the weights come from the matrix W_s.

Here is what's happening step-by-step:

1. You take the first row of the matrix W_s, which is [w11, w12, w13].
2. You multiply each element of this row by the corresponding element of the vector X, and then add up the results. That gives you the first element of the new vector Y:

   `y1 = w11*x1 + w12*x2 + w13*x3`

This process is repeated for the other rows of the matrix W_s to produce the other elements of the vector Y.

In the context of neural networks, the operation of multiplying a matrix by a vector (or another matrix) and then adding a bias vector is fundamental and is used in every layer of the network. The weights in the matrix are the parameters of the network that are learned during the training process.