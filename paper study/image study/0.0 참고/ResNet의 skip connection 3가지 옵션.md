1. **Residual learning**: This is a technique used in deep learning to help prevent the problem of vanishing gradients. It allows the model to learn an identity function that ensures the highest possible learning speed.

2. **Zero-padded dimensions**: In the context of convolutional neural networks, padding is the process of adding extra artificial pixels around the input image. Zero padding means filling these pixels with zeros.

3. **Projection shortcuts**: They are a kind of skip connection in a residual network. Instead of copying values to the next layer, it might apply a transformation (or projection) to these values before adding them to the output of a block.

4. **Bottleneck architectures**: This term often refers to a particular type of design of a layer or set of layers in a neural network where the number of inputs and/or outputs is reduced then expanded to save computational resources.

Now, let's breakdown the provided information:

The authors are discussing the results of an experiment involving three different options (A, B, and C) for some sort of deep learning model. They compared the performance of these options to a basic model (the plain counterpart).

- **Option A**: This model is performing better than the plain model but not as well as B. The authors suggest the lower performance of A might be due to the use of zero-padding, which they suspect doesn't contribute to the residual learning process. Meaning, these zero-padded dimensions are not improving the model's performance.

- **Option B**: This model outperforms A slightly, which suggests that whatever changes were made between A and B were beneficial. They didn't mention what differentiates B from A, however.

- **Option C**: This model performs a bit better than B. The authors think this is because of the use of 'projection shortcuts'. However, because the difference in performance between B and C is marginal, they conclude that while these shortcuts improve performance, they are not essential. Also, these shortcuts may increase the complexity and computational cost of the model, so the authors decide to not use option C in further experiments.

The authors then mention 'identity shortcuts' as important for not increasing complexity, especially for bottleneck architectures. 'Identity shortcuts' might be a special type of shortcut (or skip connection) where the input is directly added to the output of a block, without any transformation. They can help a deep learning model to learn more efficiently and avoid problems related to training deeper networks.

In summary, the authors are comparing different techniques to improve the performance of a deep learning model, while trying to keep the model from becoming too complex or computationally expensive.