**Identity shortcuts** (also called skip connections or identity connections) are used in certain types of deep learning models, like Residual Networks (ResNets). They are paths in the model that allow the input to a layer (or group of layers) to be added directly to the output. Because they simply "pass through" the input without altering it, they are "parameter-free" – they do not add any extra parameters to the model.

Now, let's talk about **bottleneck architectures**. This type of architecture in deep learning models, like the one used in ResNet, often consists of three layers: two 1x1 convolution layers sandwiching a 3x3 convolution layer. The first 1x1 convolution reduces the dimensionality (this helps to keep the computational complexity in check), the 3x3 convolution processes the reduced input, and the last 1x1 convolution restores the dimensionality.

**Identity shortcuts in bottleneck architectures** help in maintaining the flow of information through the network, which is especially important when the network gets deeper. As these shortcuts are parameter-free, they do not contribute to the computational complexity of the model. 

Here is a very basic example: Let's assume that we have a simple deep learning model with a bottleneck architecture like this (input dimensions are just illustrative):

```
1. Input Layer (256 channels)
2. 1x1 Convolution (64 channels)  -- Reduces dimensionality
3. 3x3 Convolution (64 channels)  -- Processes the reduced input
4. 1x1 Convolution (256 channels) -- Restores the dimensionality
5. Output Layer (256 channels)
```

In this model, an identity shortcut would directly connect the Input Layer with the Output Layer, bypassing the bottleneck layers. If an input 'x' enters the model, it is processed through the bottleneck layers (let's call this transformation F(x)), and also bypasses these layers via the identity shortcut. The final output of the model is F(x) + x.

Now, let's imagine replacing this identity shortcut with a **projection shortcut**. A projection shortcut performs a linear transformation of the input before adding it to the output. In our case, it would have to transform the 256-channel input to match the 256-channel output of the bottleneck (i.e., after the dimensions have been reduced and then restored). This transformation is not free - it requires learning additional parameters, effectively doubling the model's size and time complexity because it's connected to the high-dimensional input and output.

Therefore, using identity shortcuts in bottleneck designs can lead to more efficient models in terms of computational resources, as they keep the same level of performance without increasing model complexity.