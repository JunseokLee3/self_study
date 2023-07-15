The degradation problem is a phenomenon where deeper networks start to perform worse, despite having more layers that should in theory be able to learn more complex functions. This is attributed to the difficulty of training deeper networks due to issues like vanishing gradients.

To tackle this issue, the authors of the ResNet paper introduce the concept of residual learning, where instead of trying to learn some desired underlying mapping H(x) directly with a stack of layers, they instead learn the residual function F(x) = H(x) - x. 

The intuition here is that if the desired mapping H(x) was close to the identity mapping (i.e., H(x) = x), then it is easier to learn the residual mapping F(x) = H(x) - x, which would be closer to zero, compared to directly learning the identity mapping. This is because pushing residuals (differences) towards zero is a more straightforward task for the learning process.

So, in the end, they change the task of the layers from learning H(x) to learning F(x) = H(x) - x, and then they obtain the desired output by adding the input x back to the learned residual F(x), thus F(x) + x = H(x).

This approach essentially forms the basis of skip or shortcut connections, a key component of ResNet architecture, where the input to a stack of layers is added to their output. This eases the training of the network and has been found to greatly improve the performance of deep neural networks. 

In a practical sense, imagine trying to model a complex scene with a photograph. Directly learning the scene (H(x)) could be complex and challenging. However, if you already have a similar scene and you try to learn only the difference (F(x)) or residual, it would be easier. After learning the difference, you then add back this learned difference to your original scene (x) to get a more accurate depiction of the complex scene (H(x)).