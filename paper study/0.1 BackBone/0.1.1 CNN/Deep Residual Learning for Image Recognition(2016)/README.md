#### [Deep Residual Learning for Image Recognition 자세한 설명](./Deep%20Residual%20Learning%20for%20Image%20Recognition.md)


# Deep Residual Learning for Image Recognition

**ResNet, CVPR, 2016**

https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf

**AUTHOR**

| Kaiming He | Xiangyu Zhang | Shaoqing Ren | Jian Sun |
| ---------- | ------------- | ------------ | -------- |

"Deep Residual Learning for Image Recognition" 논문은 깊은 신경망을 훈련하는 데 있어서 중요한 도전 과제를 해결하는 방법에 대해 다루고 있습니다. 이 논문에서 제안하는 핵심 개념은 '잔차 학습(residual learning)'으로, 이는 신경망이 입력에 대한 차이(잔차)를 학습하도록 하는 방법입니다.

주요 내용은 다음과 같습니다:

1. **잔차 학습**: 이 논문은 각 층이 원하는 출력을 직접 학습하는 대신, 입력과 출력 사이의 차이(잔차)를 학습하도록 제안합니다. 이는 신경망이 항등 매핑(identity mapping)을 학습하는 것이 더 쉽다는 가정에 기반하고 있습니다.

2. **단축 연결(shortcut connections)**: 잔차 학습은 '단축 연결'이라는 개념을 도입하여 구현됩니다. 단축 연결은 하나 이상의 층을 건너뛰는 연결로, 입력을 직접 출력에 더하는 역할을 합니다. 이는 복잡도를 추가하지 않으면서 신경망의 최적화를 돕습니다.

3. **심층 잔차 네트워크의 성능**: 이 논문에서 제시한 심층 잔차 네트워크는 매우 깊은 네트워크를 훈련하는 데 성공하였고, 이로 인해 ImageNet 데이터셋에서 우수한 결과를 달성하였습니다. 또한, 이 논문의 저자들은 이 방법이 다른 시각 인식 작업에도 적용 가능하다고 주장하였습니다.

이 논문은 심층 신경망을 훈련하는 데 있어서 중요한 도전 과제를 해결하였으며, 이로 인해 딥러닝 분야에 큰 영향을 미쳤습니다. 특히, 이 논문에서 제안한 잔차 학습과 단축 연결의 개념은 현재 많은 딥러닝 모델에서 사용되고 있습니다.

![Alt text](image-10.png)

# 나의 의견

- 나는 Convnext라는 논문을 읽고 다시 Resnet을 읽었다. 
왜냐하면 Convnext는 pure한 Resnet을 변형 시켜 swin-transformer로 하나하나 바꾸어 가는 가정이기 때문이다.

- 이때 Resnet의 채널수 그리고 block의 구조를 하나씩 하나씩 바꾸는 과정을 보았는데 순간 나는 왜 이렇게 하지 못했을 까? 라는 생각이 들었다.
- 그래서 Resnet을 읽게 되었다. 
- 읽고 너무 놀랬다. 하나하나 짜임새가 있고 빈틈이 없다. 물론 인공 지능은 실험을 통해서 알수 있는 부분이 있지만, 내가 말하는 빈틈이 없다는 주장하고 하는 주제에 대하여 뒷받침하는 내용들을 꼼꼼히 챙겨 주었다.
- 독자들이 읽기 쉽게 과정이 눈에 그려진다.
- 이 것을 읽고 많은 영감을 얻었다.
- 그냥 Resnet을 썼는데, 이러한 것들이 있는 지는 몰랐다.