# Deep Residual Learning for Image Recognition

**ResNet, CVPR, 2016**

**AUTHOR**

| Kaiming He | Xiangyu Zhang | Shaoqing Ren | Jian Sun |
| ---------- | ------------- | ------------ | -------- |

## Abstract

- 심층 신경망은 훈련하기가 더 어렵습니다. 
	- 우리는 이전에 사용된 것보다 훨씬 더 깊은 네트워크의 훈련을 용이하게 하기 위해 **residual learning 프레임워크**를 제시합니다.
	- 우리는 참조되지 않은 함수를 학습하는 대신 layer 입력을 참조하여 residual functions를 학습하는 것으로 layer를 명시적으로 재구성합니다.
	- 우리는 이러한 **residual networks가 최적화하기 쉽고 상당히 증가된 깊이에서 정확성을 얻을 수 있음을 보여주는 포괄적인 경험적 증거** 를 제공합니다.
	- ImageNet 데이터 세트에서 우리는 VGG 네트[40]보다 8배 깊이인 최대 152개의 레이어로 residual nets를 평가하지만 여전히 복잡성이 낮습니다.
	-  이러한 잔여 네트워크의 앙상블은 ImageNet 테스트 세트에서 3.57% 오류를 달성합니다. 
	- 이 결과는 ILSVRC 2015 분류 과제에서 1위를 차지했습니다. 우리는 또한 100개와 1000개의 레이어가 있는 CIFAR-10에 대한 분석을 제시합니다.
- 표현의 깊이는 많은 시각적 인식 작업에서 중요합니다. 
	- 극도로 심층적인 표현 덕분에 COCO 객체 감지 데이터 세트에서 28%의 상대적 개선 효과를 얻었습니다. 
	- Deep residual nets는 ILSVRC & COCO 2015 대회 1에 제출한 기반이며, ImageNet 탐지, ImageNet 현지화, COCO 탐지 및 COCO 분할 작업에서 1위를 차지했습니다.

## 1. Introduction

- 심층 컨볼루션 신경망[22, 21]은 이미지 분류[21, 49, 39]에 대한 일련의 혁신을 이끌었습니다. 
	- 심층 네트워크는 low/mid/highlevel feature[49]과 분류기를 end-to-end 다층 방식으로 자연스럽게 통합하며, 기능의 "levels"은 **적층된(stacked) layer의 수(깊이)에 의해 강화될 수 있습니다**. ```*(이때 그냥 나온게 아니고 이런 트렌드로 발전 방향이 있었구나 이런 수요가 맞물려서 이런 논문이 나왔구나)*```
	- 최근의 증거[40, 43]는 **네트워크 깊이가 매우 중요**하다는 것을 보여주며, 까다로운 ImageNet 데이터 세트[35]에 대한 선도적인(leading) 결과[40, 43, 12, 16]는 모두 16[40]에서 30[16]까지 깊이가 있는 *"매우 깊은" [40] 모델을 이용*합니다. 
	- *다른 많은 중요하지 않은 시각적 인식 작업[7, 11, 6, 32, 27]도 매우 깊은 모델의 혜택을 많이 받았습니다*.
- **깊이의 중요성에 따라 다음과 같은 문제가 발생합니다: 더 나은 네트워크를 배우는 것이 더 많은 계층을 쌓는 것만큼 쉽습니까?**
	- 이 질문에 대답하는 데 걸림돌이 된 것은 gradients(그라디언트) vanishing/exploding이라는 악명 높은 문제 [14, 1, 8]로, *처음부터 수렴(convergence)을 방해합니다. 
	- 그러나 이 문제는 주로 normalized initialization [23, 8, 36, 12]와 intermediate normalization layers [16]에 의해 해결되었으며, 이는 수십 개의 계층을 가진 네트워크가 backpropagation로 tochastic gradient descent(SGD)을 위해 수렴을* 시작할 수 있게 합니다 [22].```(이미 이런것을 해결하기 위해 여러가지 것들이 나왔었다. 하지만 수렴은 나중에 CNN의 확장성의 문제로 다시 생기게 된다.)``` <br>
  
- 더 깊은 네트워크가 수렴을 시작할 수 있을 때, 성능 저하 문제가 노출되었습니다: 네트워크 깊이가 증가함에 따라 정확도가 포화(saturated) 상태가 되고(이는 놀라운 일이 아닐 수 있음) 급격히 저하됩니다.
	- 예기치 않게 이러한 성능 저하가 과적합(overfitting)으로 인한 것이 아니며 적절하게 깊은 모델에 더 많은 레이어를 추가하면 [10, 41]에 보고되고 실험에 의해 철저히 검증된 바와 같이 더 높은 학습 오류가 발생합니다. ```(나는 overfitting인지 알았는데 아니였구나. 그럼 무엇일까?)```
	- Fig 1은 전형적인 예를 나타낸다.
  
  ![Alt text](image.png)

  - (훈련 정확도의) degradation는 모든 시스템이 비슷하게 최적화하기 쉬운 것은 아니라는 것을 나타냅니다. 
	- 더 얕은 아키텍처와 더 많은 계층을 추가하는 더 깊은 아키텍처를 고려해 보겠습니다.
	- 더 깊은 모델에 대한 솔루션이 존재합니다. 
	- 추가된 레이어는 ID(identity mapping항등식) 매핑이고, 다른 레이어는 학습된 얕은 모델에서 복사됩니다. (ID : F(x) = x)
	- 이 구성된 솔루션의 존재는 심층 모델이 얕은 모델보다 높은 교육 오류를 발생시키지 않아야 함을 나타냅니다.
	-  그러나 실험에 따르면 현재 해결책은 구성된 솔루션보다 비교적 우수하거나 더 나은 솔루션을 찾을 수 없습니다(또는 실현 가능한 시간 내에 그렇게 할 수 없습니다).

- 본 논문에서는 **deep residual learning 프레임워크를 도입하여 성능 degradation 문제를 해결**합니다. 
	- [(ResNets) 잔차(residual)가 왜 좋은지 설명](../../../0.0%20참고/(ResNets)%20잔차(residual)가%20왜%20좋은지%20설명.md)
	- 몇 개의 적층된 레이어가 원하는 기본(underlying) 매핑에 직접 적합하기를 바라는 대신, 이러한 레이어가 residual 매핑에 적합하도록 명시적으로 허용합니다. 
	- 공식적으로, 원하는 기본 매핑을 H(x)로 표시하고, 쌓인 비선형 레이어가 F(x) := H(x) - x의 다른 매핑에 맞도록 합니다. 원래 매핑은 F(x)+x로 recast됩니다.
	- 우리는 참조되지 않은 원래 매핑을 최적화하는 것보다 잔여 매핑을 최적화하는 것이 더 쉽다고 가정합니다. 
	- 극단적으로, identity mapping이 최적인 경우, nonlinear layers 스택에 의해 identity mapping을 적합시키는 것보다 residual를 0으로 푸시하는 것이 더 쉬울 것입니다.
	- `(논문을 자세히 보면, 저자의 주장하는 이론과 그것을 설명하는 논리력이 굉장히 매력있다. 예를들어 skip connenctio의 왜 좋은 설명하려 할떄, 나는 그냥 이전 정보를 주니깐 이렇게 생각하지만, 이게 gradient관점 그리고 학습에 관점에서 설명을 해주었다. 물론 모델이 black box라서 이 설명이 또 완벽한 인과관계를 가지는 것은 아니다. 하지만 경험적인 이유를 들어서 이러한 이유다. 라는 방식으로 설명이 굉장히 매력있고 이해가 잘 된다. )`
![Alt text](image-1.png)

- F(x) + x의 공식화는 **"shortcut connections"**을 가진 feedforward 신경망을 통해 실현될 수 있습니다(그림 2).
	- shortcut connections [2, 33, 48]은 하나 이상의 레이어를 건너뛰는(skipping) 연결입니다. `(Resnet이 나오기 전에 이미 여러 논문에서 나오고 있었다)`
	- 우리의 경우, shortcut connections은 단순히 identity mapping을 수행하고, 그 출력은 적층된 레이어의 출력에 추가됩니다(그림 2).
	-  ID( identity) shortcut connections은 추가 parameter나 computational complexity을 추가하지 않습니다.
	-  전체 네트워크는 여전히 backpropacation를 사용하여 SGD에 의해 end -to-end로 훈련될 수 있으며, solvers를 수정하지 않고도 공통 라이브러리(예: 카페[19])를 사용하여 쉽게 구현할 수 있습니다.
  
- 우리는 성능 저하 *degradation를 보여주고 우리의 방법을 평가하기 위해 ImageNet [35]에 대한 포괄적인 실험*을 제시합니다. 
  1. **극도로 심층적인 잔여 네트워크는 최적화하기 쉽지만, 상대적인 "plain(일반)" 네트워크(단순히 레이어를 쌓는)는 깊이가 증가할 때 더 높은 훈련 오류**를 나타냅니다. 
  2. **deep residual nets는 크게 증가한 깊이에서 정확도 향상을 쉽게 누릴 수 있어 이전 네트워크보다 훨씬 나은 결과**를 얻을 수 있습니다.
  
- CIFAR-10 세트[20]에도 *유사한 현상이 나타나 우리 방법의 최적화 어려움과 효과가 특정 데이터 세트와 유사하지 않음을 시사*합니다.
	- 우리는 100개 이상의 layers가 있는 이 데이터 세트에서 성공적으로 훈련된 모델을 제시하고 1000개 이상의 layers가 있는 모델을 탐색합니다.

- ImageNet 분류 데이터 세트[35]에서, 우리는 극도로 깊은 잔류 그물에 의해 우수한 결과를 얻습니다.
	-  152 layer residual net는 ImageNet에 표시된 네트워크 중 가장 깊은 네트워크이며 VGG 네트워크보다 복잡성이 낮습니다[40]. 
	- 우리 ensemble은 ImageNet 테스트 세트에서 상위 5개 오류가 3.57%이며, ILSVRC 2015 분류 대회에서 1위를 차지했습니다. 
	- extremely deep representations은 또한 다른 인식 작업에서 우수한 일반화 성능을 가지며, ILSVRC 및 COCO 2015 대회에서 ImageNet 탐지, ImageNet 현지화, COCO 탐지 및 COCO 세분화 부문에서 추가로 1위를 차지했습니다. 
	- 이 강력한 증거는 잔류 학습 원리가 일반적이라는 것을 보여주며, 우리는 그것이 다른 비전 및 비전 문제에 적용될 수 있을 것으로 기대합니다.

## 2. Related Work


**Residual Representations.**
- 이미지 인식에서, VLAD[18]는 사전에 대하여 residual vectors에 의해 인코딩하는 표현이고, Fisher Vector[30]는 VLAD의 확률적 버전[18]으로서 공식화될 수 있다.
	- 두 가지 모두 이미지 검색 및 분류를 위한 강력한 shallow 표현입니다 [4, 47]. 
	- 벡터 양자화의 경우, reisual vectors [17]을 *인코딩하는 것이 원래 벡터를 인코딩하는 것보다 더 효과적인 것으로 나타났습니다.*

- low-level vision의 비전과 computer graphics에서 편미분 방정식(Partial Differential Equations PDE)을 해결하기 위해 널리 사용되는 멀티그리드 방법(Multigrid method)[3]은 시스템을 여러 규모의 하위 문제로 재구성하며, 각 하위 문제는 더 거칠고(coarser) 미세한 규모 사이(finer scale)의 residual solution을 담당합니다.
	- [**Multigrid Methods:**와 **Hierarchical Basis Preconditioning:*이 왜 수렴하는지 빠른 이유](../../../0.0%20참고/Multigrid%20Methods와%20Hierarchical%20Basis%20Preconditioning이%20빠른%20이유%20.md)
	- Multigrid의 대안은 두 scale 사이의 residual vector를 나타내는 변수에 의존하는 계층적 기초 전제 조건 [44, 45]입니다. 
	- 이러한 solver는 solution의 residual nature을 모르는 표준 solver보다 훨씬 빠르게 수렴되는 것으로 나타났습니다 [3, 44, 45].
	-  이러한 방법은 좋은 재구성(reformulation) 또는 전제 조건을 통해 최적화를 단순화할 수 있음을 시사합니다.

**Shortcut Connections.**
- shortcut connections로 이어지는 관행과 이론 [2, 33, 48]은 오랫동안 연구되어 왔습니다.
	-  다층 퍼셉트론(MLP)을 훈련하는 초기 관행은 네트워크 입력에서 출력에 연결된 선형 레이어를 추가하는 것입니다 [33, 48]. 
	- [43, 24]에서, 몇 개의 중간 레이어는 vanishing/exploding gradients를 해결하기 위한 보조(auxiliary) 분류기에 직접 연결됩니다. 
	- [38, 37, 31, 46]의 논문은 바로 가기 연결에 의해 구현된 layer responses, 기울기(gradient) 및 전파된(propagated) 오류 중심화 방법을 제안합니다. [43]에서 "inception" 계층은 shortcut branch와 몇 개의 더 깊은 분기로 구성됩니다.

- 우리의 연구와 동시에, **"highway networks"[41, 42]는 게이트(gate) 기능이 있는 shortcut connections을 제시합니**다 [15].
	- *이러한 게이트는 데이터 의존적이며 매개 변수가 없는 identity shortcuts와 대조적으로 매개 변수가 있습니*다.
	- gated short가 *"closed"(0에 가까워짐)인 경우 high-way networks의 레이어는 non-residual functions를 나타*냅니다.
	-  **반대로**,* 우리의 공식은 항상 residual functions를 학습합니다. 우리의 identity shortcuts는 결코 닫히지 않으며, 모든 정보는 항상 전달되며*, additional residual functions를 학습해야 합니다. 
	- 또한, *high-way networks는 극단적으로 증가된 깊이(e.g., over 100 layers)에서 정확도 향상을 보여주지 않았습니다*.

## 3. Deep Residual Learning

### 3.1. Residual Learning

- H(x)를 몇 개의 스택 레이어(반드시 entire net일 필요는 없음)에 맞는 기본(underlying) 매핑으로 간주하고 x는 이러한 레이어 중 첫 번째 레이어에 대한 입력을 나타냅니다.
	- 여러 개의 비선형 레이어(multiple nonlinear)가 점근적(asymptotically)으로 복잡한 function^2를 근사할 수 있다고 가정하면 , residual functions, 즉 H(x) − x(입력과 출력이 동일한(equivalent) 차원이라고 가정)를 점근적으로 근사할 수 있다는 가설을 세우는 것과 같습니다.`(여기서 근사하다는 말이 참 어렵다. 근사가 무엇일까?)`  [신경망에서 근사하다는 것은 무엇일까?](../../../0.0%20참고/신경망에서%20근사하다는%20것은%20무엇일까.md)
- 
	- 따라서 적층된 레이어가 H(x)에 근접할 것으로 예상하는 대신, 우리는 이러한 레이어가 잔차 함수 F(x) := H(x) - x에 근접하도록 명시적으로 허용합니다. 
	- 따라서 원래 함수는 F(x)+x가 됩니다. 두 양식 모두 원하는 함수에 점근적(asymptotically)으로 근사할 수 있어야 하지만(가설대로 as hypothesized) 학습의 용이성(ease)은 다를 수 있습니다.

- 이 재구성은 분해 문제에 대한 반 직관적 인 현상(counterintuitive phenomena)에 의해 동기가 부여됩니다 (그림 1, 왼쪽). 
	- 소개에서 설명했듯이 추가된 계층을 ID 매핑으로 구성할 수 있는 경우 더 깊은 모델은 더 얕은 모델보다 학습 오류(training error)가 크지 않아야 합니다.
	- 성능 저하 문제는 솔버(solvers)가 여러 비선형 레이어(multiple nonlinear layers)에 의한 ID 매핑을 근사화하는 데 어려움이 있을 수 있음을 시사합니다. 
	- residual learning reformulation을 통해 identity mapping이 최적인 경우 솔버는 단순히 identity mapping에 접근하기 위해 여러 비선형 레이어(nonlinear layers)의 가중치를 0으로 유도할 수 있습니다.

![Alt text](image-2.png)

- 실제 경우, **identity mapping이 최적일 가능성은 낮지만, 우리의 reformulation은 문제를 전제하는 데 도움**이 될 수 있습니다. 
	- *최적의 함수가 zero mapping보다 identity mapping에 더 가까우면 solover가 identity mapping을 참조하여 섭동(perturbations)을 찾는 것이 새로운 함수로 학습하는 것보다 더 쉬울 것입니다.*   ["Perturbations"의 의미](../../../0.0%20참고/Perturbations의%20의미.md)
	- 우리는 실험을 통해 학습된 residual 함수가 일반적으로 반응이 작다는 것을 보여주며, 이는 ID 매핑이 합리적인 전제 조건을 제공한다는 것을 시사합니다. 


 ### 3.2. Identity Mapping by Shortcuts
![Alt text](image-3.png)
![Alt text](image-4.png)
- 우리는 **몇 개의 적층된 모든 레이어에 잔여 학습을 채택**합니다.
	- 여기서 x와 y는 고려된 레이어의 입력 및 출력 벡터입니다.
	-  함수 F(x, {W_i})는 학습할 잔여 매핑을 나타냅니다.
	-  두 개의 층을 갖는 그림 2의 예에서, σ가 ReLU [29]를 나타내며 표기를 단순화하기 위해 편향이 생략된 F = W_{2σ}(W_{1x}).
	-  F + x 작업은 바로 가기 연결 및 요소별 추가에 의해 수행됩니다. 
	- 우리는 추가 후 두 번째 비선형성을 채택합니다(즉, σ(y), 그림 2 참조)..

- 방정식(1)의 shortcut connections은 extra parameter나 computation complexity을 유발하지 않습니다.
	-  이것은 실제로 매력적일 뿐만 아니라 일반 네트워크와 residual 네트워크 간의 비교에서도 중요합니다. 
	- 우리는 동일한 수의 매개 변수, 깊이, 폭 및 계산 비용을 동시에 갖는 일반/잔류 네트워크를 공정하게 비교할 수 있습니다(except for the negligible element-wise addition). `(비교를 할때 철저히 똑같이 비교를해야지 독자들에게 본인의 주장을 확실히 할 수 있다.)`
- x와 F의 dimension는 방정식(1)에서 같아야 합니다.
	-  그렇지 않은 경우(e.g., when changing the input/output channels) 바로 가기 연결로 linear projection W_s를 수행하여 dimension를 일치시킬 수 있습니다: `(이것도 엄청 친절히 답변해 주었다. 지금 medical 쪽 실험에 skip connection을 했을 때 일부러 차원을 맞추기 위해서 linear projoction을 했다.)`
	- 우리는 또한 방정식(1)에서 사각 행렬(square matrix) W_s를 사용할 수 있습니다.  [square matrix 설명](../../../0.0%20참고/square%20matrix%20설명.md)
	- 그러나 우리는 실험을 통해 identity mapping이 성능 저하 문제를 해결하기에 충분하고 경제적이므로 W는 치수를 일치시킬 때만 사용된다는 것을 보여줄 것입니다.

- residual 함수 F의 형태는 유연(flexible)합니다. 
	- 이 논문의 실험은 두 개 또는 세 개의 레이어를 갖는 함수 F(그림 5)를 포함하는 반면 더 많은 레이어가 가능합니다. 
	- 그러나 F가 단일 레이어만 가지고 있다면, Eqn.(1)은 inear layer와 유사합니다: y = W1_x + x. 이에 대해 우리는 이점을 관찰하지 못했습니다.
- 또한 위의 표기법은 단순성을 위해 fully-connected layers에 관한 것이지만 convolutional layers에 적용할 수 있습니다.
	-  함수 F(x, {W_i})는 multiple convolutional layers를 나타낼 수 있습니다. 
	- element-wise 추가는 채널별로 두 개의 feature maps에서 수행됩니다.


### 3.3. Network Architectures


- 우리는 다양한 일반/잔여망(plain/residual)을 테스트했고, 일관된 현상을 관찰했습니다. 
	- 논의를 위한 사례(instance)를 제공하기 위해 ImageNet에 대한 두 가지 모델을 다음과 같이 설명합니다.
 
**Plain Network.**
