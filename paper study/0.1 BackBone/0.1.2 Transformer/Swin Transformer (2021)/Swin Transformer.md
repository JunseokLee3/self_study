# Swin Transformer: Hierarchical Vision Transformer using Shifted Windows

https://openaccess.thecvf.com/content/ICCV2021/papers/Liu_Swin_Transformer_Hierarchical_Vision_Transformer_Using_Shifted_Windows_ICCV_2021_paper.pdf

## 저널 및 학회 : ICCV (2021)

## 저자 : ![Alt text](image.png)

## Abstract

- 이 논문은 컴퓨터 비전을 위한 범용 백본 역할을 할 수 있는 Swin Transformer라는 새로운 비전 Transformer를 제시합니다. 
- 언어에서 비전으로 Transformer를 적응시키는 데 있어서의 어려움은 시각적 실체의 규모의 큰 변화와 텍스트의 단어에 비해 이미지의 픽셀의 높은 해상도와 같은 두 도메인 간의 차이로 인해 발생합니다. 
	- 이러한 차이를 해결하기 위해 우리는 Shifted window로 표현이 계산되는 hierarchical sTransformer를 제안합니다. 
	- Shifted windowing scheme은 자기 주의 계산을 중첩되지 않는 local 윈도우로 제한하는 동시에 cross-window connection을 허용함으로써 더 큰 효율성을 가져옵니다.
- 이 계층적 아키텍처는 다양한 스케일로 모델링할 수 있는 유연성을 가지고 있으며 이미지 크기에 대한 선형 계산 복잡성을 가지고 있습니다. 
	- 이러한 Swin Transformer의 품질은 이미지 분류(ImageNet-1K의 경우 87.3 Top-1 정확도)와 객체 검출(COCO testdev의 경우 58.7 박스 AP 및 51.1 마스크 AP) 및 의미론적 분할(ADE20K val의 경우 53.5 mIoU)과 같은 밀도 높은 예측 작업을 포함하여 광범위한 비전 작업과 호환됩니다. 
	- 이 성능은 COCO의 경우 +2.7 박스 AP 및 +2.6 마스크 AP, ADE20K의 경우 +3.2 mIoU라는 큰 차이로 이전의 최첨단 성능을 능가하며, Transformer 기반 모델의 비전 백본으로서의 가능성을 보여줍니다.
- 계층적 설계와 시프트된 윈도우 접근 방식은 또한 모든 MLP 아키텍처에 유익한 것으로 입증되었습니다. 
- 코드와 모델은 https://github.com/microsoft/Swin-Transformer.에서 공개적으로 사용할 수 있습니다.

![Alt text](image-1.png)

## 1. Introduction

- Figure1, 에 나와 있는 것처럼 작은 크기의 패치(patch)에서 시작되어 깊은 Transformer에서는 인접합(neighboring) 패치를 병합하는 계층적 구조를 가지고 있다.
	- 이러한 계층적 특징 맵을 통해 Swin  Trnasformer 모델은 특징피라미트네트워크(feature pyramid networks (FPN))과 U-net과 같은 예측을 편리하게 사용할 수 있게 된다.
	- `-> 이 말은 다양한 활용성이 있다는 뜻이구만`
- 선형 계산 복잡성(linear computational complexity)는 중복되지 않는(non-overlapping) 창(window)내의 로컬로 self-attentio으로 계산으로 달성된다.
	- 각 패치의 수는 고정되어 있으며, 복잡성은 이미지 크기에 따라 선형이 된다. 
- 이러한 장점은 Swin-transformer를 다양한 비전 으로 적합하게 만든다. (vit의 2차 복잡성을 갖는 single resolution(단일 해상도)에 비해)
	- 또한 shifted widow 접근은  sliding window보다 낮은 latency를 보인다.

![Alt text](image-2.png)

- Swin Trnsformer의 핵심 설계는 Figure 2.와 같이 연속적인(consecutive) self-attention간의(between) 창(window) 파티션의 이동시키는 것이다. 전환된(shifted) 창(window)은  이전 layer의 창들과 연결해주며, 모델링 power(능력)을 크게 향상 시킨다. [Sliding Window와 Shifted Window](../../../0.0%20참고/Sliding%20Window와%20Shifted%20Window.md)
	- 이 전략은 실제 세계(real-world)에서 효율적이다. query 패치는 동일한 key set1 을 공유한다. 이는 하드웨어 메모리를 용이하게 한다.
- 대조적으로 slidin window 기반 self-attention  접근법은 서로 다른 query pixcel으로 일반 hardware에서  인해 낮은 latency(지연시간)의 어려움을 겪고 있다.
	- `(일반 하드웨어 에서 슬라이딩 윈도우(sliding window) 기반 convolution layer를 구현하는 효율적인 방법이 있다. 하지만  feature map을 걸친 kenel weight의 공유로 때문에 실저로 효율적인 메모리 엑세스를 갖는 것은 어렵다.)`
- Swin Transformer는 이미지 분류(classification), 물체 감지(object detection) 그리고 의미 분할(semantic segmentation)의 이미지 인식(recognition) 작업에서 강력한 성능을 달성한다.


## 2. Related work

**CNN and variants**
 - CNN은 컴퓨터 비전의 중요한 역할은 함.

**Self-attention based backbone architectures.**
 - self-attention Resnet보다 좋은 성능을 가졌지만 메모리 사용량이랑 trade-off를 하게 된다.
 - 값비싼 메모리 사용량으로 대기시간이 기랃.

**self-attention/Transformers to complement CNNS**
 - standard CNN 구조에 self-attention과 Trnasformer을 더하는 것이다.  
   - distant  의존성과 heterogeneous 상호작용에 능력을 제공 한다.
 - 최근에는 트랜스포머의 인코더 디커도 설계가 객체 감지 및 instance(segnentation) 작업 탐구 하고 있다.

**Transformer based vision backbones**
- Vit는 컴퓨터 비전에 선구의 역할은 했다. 
  - 겹치지 않은 중간크기의 이미지 패치로 분류 작업을 한다.
  -  그것은 속도와 정확도를 trade-off 하는 결과를 이루다.
- 반면 ViT는 large-scale 훈련 이미지가 필요하다. 
  - Deit는 상대적 작은 데이터로 분류 성능을 보였으나, 범용성이 부겆절하다.
- 낮은 이미지 해상도와 계산 복잡도가 2차인 것도 있다.
- `모델이 아직 연산에 대해서 비효율 적이다.`

## 3. Method

### 3.1. Overall Architecture

![Alt text](image-3.png)

- Swin-Transformer은 RGB 이미지를 Vit와 같이 패치 분할 모듈에 중복되지 않게 분할 한다.
	- 각 패치는 ''token" 으로 처리되며  픽셀 RGB 값의 연결로 설정 된다.
	- 4x4의 패치 크기를 사용하여 각 패치의 feature dimension은 4x4x3  = 48이다.
	- 선형 임베딩 레이거 이 가공되지 않은 값들의 feature을 임의 차원(C)로 투영된다.

		- 1단계 (H/4 +  W/4) 이다.
			- 계층적(hierarchical) 표현을 하기 위해 layer가 깊어 질 수록 패치합성레이어(patch merging layer)을 이용하여 토큰의 수를 줄인다.
			- 처음 패치합성 레이어는  2x2의 각 그룹의  features를 연결한다. 그리고 선형 레이어를 적용하여 4C 차원을 가지게 연결 한다.
			- 이렇게 하면 2x2 = 4(2x 다운샘플링 의 토큰 감소와 출력 차원은 2C를 가지게 된다.
			- H/8 + H/8 로 유지 된다.
		- 이 패치는 2단계이다.
			- 3단계 4단계를 거치면서 H/16+ W/16와 H/32 * W/32 의 출력을 가진다.
			- 이 단계들은 convolutional layer와 같은 계층적인 feature 맵 해상도를 가진다.
- 결과적으로 제안된 아키택처는 편리하게 다양한 비전 작업을 재 설계 할 수 있다.

**Swin Transformer block**
- MSA 모듈을 다른 레이어와 동일하게 유지하면서 shfited widows교체 했다.
- Swin Transformer은 shifted window ased MSA module으로 이루어졌있다. (GELU가 포함된 2계층의 MLP)
  
### 3.2 Shifted Window based Self-Attention

- 이미지 분류를 위한 표준(standard) Transformer  구조는 전역(global) self-attention으 이루어져 있다. self-attention은 토큰과 다른 토큰간의 관계를 계산한다.
- global 계산은 토큰수와 관련하여 이차 복잡성으로 이어진다.  조밀한  예측을 위해 엄청난 토큰 세트를 요구하거나 고해상도 이미지를 나타내는 많은 비전 문제에 적합하지 않다.


**Self-attention in non-overlapped windows**

- 효율적인 모델리을 위해 창 내의 self-attention 계산을 제안한다. 
	- 창은 겹치지 않는 방식으로 이미지를 균등하게 분할 하도록 배열된다.
	- 각 창에 MxM 패치가 포함되어 있다고 가정하면 글로벌 MSA 모듈과 h x w 패치의 이미지를 기반으로 한 창의 복잡도는 3이다.
- 우리는 복잡성을 판달할때 softmax를 제외한다.

![Alt text](image-4.png)

- 여기서 전자는 패치 번호 hw 에 2차이고, M이 고정된 경우 후자는 선형이다.( 기본값으로 7로 설정)
- 글로벌 자기 주의(global self attenton) 게싼은 일반적으로 대규모 하드웨어에 대해 감당할 수 없는 반면, window(창) 기반 자기 주의(self attention)은 확장 가능하다.