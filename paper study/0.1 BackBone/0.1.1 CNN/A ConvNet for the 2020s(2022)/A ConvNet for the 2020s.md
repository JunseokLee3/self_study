# A ConvNet for the 2020s
**CVPR, 2022**

https://openaccess.thecvf.com/content/CVPR2022/html/Liu_A_ConvNet_for_the_2020s_CVPR_2022_paper.html

![Alt text](image.png)

## Abstract


- "Roaring 20s" Vission Transformers (ViTs)은 빠르게 cnn을 대체 했으며 이미지 classificaiton 모델에서 State-of-the-art을 달성했다.
	반면 ViT는 object detection과 semantic sgmentation 과 같은 일반적인 computer vison 문제에 어려움에 직면 했다.
	Hierarchical Transformer (예를들어 swin Trnasformers) 의 도입은 실질적으로 일반적인 vision backbone과 실행 가능하게 하고 넓은 vision 일에 놀라운 성능을 증명했다.

- 그러나 몇몇의 hybrid 접근의 효율성은 여전히 CNN의 고유한 유도적 편향보다는 Transformer의 본질적인 우월성에 크게 기인한다.

- 우리의 연구에서는 우리는 디자인 공간을 재검토하고** Pure Convnet이 달성 할 수 있는 한계를 테스트** 하다. 우리는 **vision Transformer을 설계에 맞추어 standard ResNet을 점진적으로   "modernize"하고** 그 과정에서 **성능 차이에 기여하는 몇 가지 핵심 구성요소를 발견**한다.
- 이 탐색의 결과는 ConvNeXt라고 불리는 pure Convnet 모델 제품군이다.

- 완전히 표준 ConvNet 모듈로 구성된 ConvNeXts는 **정확도와 확장성 측면에서 Transformers와 경쟁하여 87.8% ImageNet 상위 1위** 정확도를 달성하고 COCO 감지 및 ADE20K 세분화에서 Swin Transformers를 능가하는 동시에 표준 ConvNet의 단순성과 효율성을 유지합니다.


## Introduction

`(indcutive bias가 있음으로써 CNN은 어느곳에 고양이가 있던 그것을 잘 인식 한다.
그리고 근처에 있는 연관성을 더 중요하게 된다. 예를들어 얼굴에 눈을 더 관계 깊게 생각한다. CNN은 Translational invariance 이다. 어디에 사진이 있던 불변한다(인식한다).  그런데 CNN이 Trnaslation equvariance이 좋아서 detiction에 강해 그런데 instance segmentation에서 과연 강할까?)`

- 컴퓨터 비전에서 ConvNets의 완전한 우세(dominance)는 우연이 아니다. 많은 application  시나리오에서** "sliding window"  전략은 특히 high-resolution 이미지로 작업할 때 시각적 처리(visual processing) 에 필수적**이다.

- Convnet에는 다양한 computer vision application에 적합한 몇 가지 기본 제공 **inductive biases**가 있다. 
	- 가장 중요한 것은 **translaition equivariance**으로, 이는 *objection detection와 같은 task에 적합한 속성이다.  또한 ConvNets는 sliding-window 방식으로 사용할 때 계산이 공유되기 때문에 본질적으로 효율적*이다.
	- 수십 년 동안, 이것은 일반적으로 digit, faces, and pedestrians와 같은 제한된 객채 범주에서 ConvNets의 기본 사용이었다.
	- 2010년대에 들어서면서, region-based detectors 는 ConvNets을 visual recognition system의 fudamental building block으로 더욱 끌어 올렸다.

- ViT는 언어와 이미지의 큰 domain 차이임에도 큰 변화를 가져 왔다.
	-  이미지를 일련의 패치로 분할하는 초기 'patchify' 계층을 제외하고, ViT는 image-specific inductive bias을 도입하지 않으며 원래 NLP Transformer에 최소한의 변경을 가한다.
	- ViT의 주요 초점은 확장 동작에 있다. 더 큰 모델과 데이터 사이즈의 도움으로  Transformer은 표준 ResNet를 크게 능가 했다. 이미지 분류 작업에 대한 결과는 영감을 받지만, 하지만 *computer vision은 image classification에 제한되지 않는다*.

- 이전에 논의한 바 같이, 지난 10년 동안  수많은 computer vision 작업은 sliding window와 fullyconvolutional paradigm에 의존했다.
	- **ConvNet inductive biases가 없으면 vanilla ViT 모델은 일반(generic) vision backbone으로 채택되는데 많은 문제에 직면**한다. 
	- 가장 큰 문제는 **입력 크기와 관련한여 2차 복잡성**을 갖는 ViT의 global attention 설계 이다. 이는 imageNet 분류에 적합할 수 있지만 고해상도 입력으로 인해 빠르게 처리 할 수 없다.

- Hierarchical Transformers는 *이러한 격차를 해소하기 위해 hybrid 방식을* 사용한다.
	- 예를 들어 **"sliding window" 전략 (예를들어 attention within local windows)** 는 Transformers에 다시 도입되어 **ConvNets와 더 유사하게 동작할 수 있게 되었다**.
	- Swin Transformer는 Transformer가 일반적인(generic) vision backbone으로 채택 되고 image classification을 넘어 다양한 컴퓨터 비전 작업에서 최첨단 성능을 달성할 수 있음을 처음으로 보여줍니다.: 컨볼류션의 본질은 무관하지 않고 오히려 그것은 여전히 많은 바람을 받고 있으며 결코 퇴색하지 않았다.

- 이러한 관점에서, computer vision을 위한 Transformer의 많은 발전은 convolution을 되살리는 목표로 했다. 이러한 시도는 **비용이 많이 든다.**
	- sliding window self-attention 의 *pure 구현은 비용이 많이 든다.*
	- cyclic shifting과 같은 향상된 접근 방식을 사용하면* 속도를 최적화할 수 있지만, 시스템 설계가 더욱 정교해* 진다.
		
- 반면에, ConvNet이 비록 간단하고 군더더기 없는 방식으로 원하는 많은 속성을 이미 충족하고 있다는 것은 거의 아이러니 한다.
	- ConvNets가 활력을 읽어가는 유일한 이유는 (계층적) Transformer가 많은 비전 작업에서 ConvNets을 능가하기 때문이며, 성능 차이는 *일반적으로 multi head self-attention가 핵심 구성 요소인 Transformers의 superior scaling 동작에 기*인한다.
		
- 지난 10년간 점진적으로 개선된 ConvNets와 달리 Vision Transformers의 채택은 한 단계 변화했습니다.
	-  최근 문헌에서는 일반적으로 두 가지를 비교할 때 시스템 수준 비교(예: Swin Transformer 대 ResNet)가 채택됩니다. 
	- ConvNets와 계층적 비전 트랜스포머는 *서로 다르고 동시에 유사합니다.*
	- 둘 다 유사한 *유도 편향을 갖추고 있지만 교육 절차와 매크로/마이크로 레벨 아키텍처 설계에서는 크게 다릅니다.*

- 이 연구에서, 우리는 ConvNets와 Transformers 사이의 구조적 차이를 조사하고 네트워크 성능을 비교할 때 교란 변수를 식별하려고 노력합니다.
	-  우리의 연구는 **ConvNets에 대한 ViT 이전과 ViT 이후의 시대 사이의 격차를 해소하고 순수한 ConvNet이 달성할 수 있는 한계를 테스트하기 위한 것입니다.**

- 이를 위해 개선된 절차로 훈련된 표준 ResNet(예: ResNet-50)부터 시작합니다. 
	- 우리는 점진적으로 아키텍처를 계층적 비전 트랜스포머(예: Swin-T)의 구성으로 "현대화"합니다.

- 우리의 탐사는 다음과 같은 핵심 질문에 의해 지시됩니다: **트랜스포머의 설계 결정이 ConvNets의 성능에 어떤 영향을 미칩니까?** 
	- 이 과정에서 성능 차이에 기여하는 몇 가지 주요 구성 요소를 발견했습니다. *결과적으로 ConvNeXt라는 순수 ConvNets 제품군을 제안합니다.*
	
- 우리는 ImageNet 분류[17], COCO의 객체 감지/분할, ADE20K의 의미 분할[92]과 같은 다양한 비전 작업에서 ConvNeXt를 평가합니다. 
	- 놀랍게도, 전적으로 표준 ConvNet 모듈로 구성된 ConvNeXts는 모든 주요 벤치마크에서 **정확성, 확장성 및 견고성 측면에서 Transformer와 유리하게 경쟁**합니다. 
	- ConvNeXt는 표준 ConvNets의 효율성을 유지하며, 교육 및 테스트 모두에 대한 완전한 컨볼루션 특성으로 구현이 매우 간단합니다

##  2. Modernizing a ConvNet: a Roadmap