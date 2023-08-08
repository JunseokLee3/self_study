# TransZero++: Cross Attribute-Guided Transformer for Zero-Shot Learning

https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9987664

## 저널 : IEEE Transactions on Pattern Analysis and Machine Intelligence (2022), q1, if 23.6, 1%

## 저널 : ![Alt text](image.png)

## Abstrat :

- 제로샷 학습(ZSL)은 보는 클래스에서 보이지 않는 클래스로 Semantic knowledge을 전달함으로써 새로운 클래스 인식 문제를 해결합니다. 
  - Semantic knowledge은 일반적으로 다른 클래스 간에 공유된 속성 설명으로 표현되며, 이는 차별적 영역 특징을 나타내는  object attributes을 로컬화하기 위한 강력한 선행 요소로 작용하여 ZSL을 발전시키기 위한 유의미하고 충분한 시각적 의미적 상호 작용을 가능하게 합니다.
- 기존의  attention-based models은 ZSL에서 효과적인 지식 전달을 위한 핵심 의미 지식을 표현하기 위한 시각적 특징의 전달 가능하고 차별적인 속성 현지화를 무시하는 unidirectional(단방향) attention을 사용하여 단일 이미지에서 하위 지역 특징을 학습하는 데 어려움을 겪었습니다.
- 본 논문에서는 ZSL의 핵심 의미 지식 표현에 대한 시각적 특징을 정교화하고 정확한 속성 현지화를 학습하기 위해 TransZero++라고 하는 cross attribute-guided Transformer network를 제안합니다. 
  - 구체적으로, TransZero+는 속성 기반 시각적 특징과 시각 기반 속성 특징을 각각 학습하기 위해 attribute → Visual Transformer 서브넷(AVT)과 VAT ( visual → attribtue Transformer 서브넷)를 사용합니다.
  - feature-level 및  prediction-level 의미론적 collaborative losses을 추가로 도입함으로써 두 속성 유도 변환기는 의미론적 협력 학습을 통해 핵심 의미 지식 표현에 대한 의미론적 기반 시각적 임베딩을 학습하도록 서로 가르칩니다. 
- 마지막으로 AVT와 VAT에 의해 학습된 의미론적 기반 시각적 임베딩은 ZSL 분류를 위한 클래스 의미 벡터와 협력된 바람직한 시각적-시각적 상호 작용을 수행하기 위해 융합됩니다. 
- 광범위한 실험은 TransZero+가 세 가지 황금 ZSL 벤치마크와 대규모 ImageNet 데이터 세트에서 새로운 최첨단 결과를 달성한다는 것을 보여줍니다. 프로젝트 웹 사이트는 https://shiming-chen.github.io/TransZero-pp/TransZero-pp.html 에서 이용할 수 있습니다.

## 1 INTRODUCTION AND MOTIVATION

![Alt text](image-1.png)

- 생성 모델은은 상당한 개선을 달성했지만 의미적 지식 [34], [35], [36]을 표현하기 위해 Red Legged Kittiwake의 세분화된 속성 정보(예: "bill color yellow")를 캡처하는 데 부족한 전역적(전체적) 시각적 특징 1에 의존합니다. 
  - 차별적이고 전달 가능한 의미적 지식은 일반적으로 몇 가지 속성에 해당하는 몇 개의 영역에 포함되어 그림 1(a)과 같이 보이는 클래스에서 보이지 않는 클래스로 효율적인 지식 전달을 가능하게 하기 때문입니다. 
  - 따라서 이러한 방법으로 학습된 시각적 특징 표현은 열등하여 지식 전달을 위한 바람직하지 않은 시각적-의미적 상호 작용을 초래합니다. 
  - 보다 최근에는 그림 1(b)과 같이 소수의 주의 기반 모델 [34], [37], [38], [39], [40], [41], [42]에서 보다 차별적인 영역 특징을 탐색하려고 시도했습니다. 
  - 그러나 이러한 방법은 
    - i) ZSL 분류를 위해 얽힌 영역(그리드) 특징을 직접 취하므로 시각적 특징이 보이지 않는 클래스로 전달되는 것을 방해합니다. 
    - i) 핵심 의미적 지식 표현을 위한 차별적 속성 현지화(예: 독특한 새 몸 부분)의 중요성을 무시하고 단방향 주의를 사용하여 단순히 영역 임베딩(예: 전체 새 몸)을 학습합니다. 
  - 따라서 ZSL에서 효율적인 의미적 지식 전달을 가능하게 하기 위해 시각적 특징에서 핵심 의미적 지식을 적절히 발견하는 것은 매우 필요하게 되었습니다.


- 위의 과제를 해결하기 위해 본 논문에서는 그림 1(d)과 같이 의미론적 협력 학습을 통해 ZSL에서 보이는 클래스에서 보이지 않는 클래스로 효율적인 지식 전달을 위한 핵심 의미 지식을 발견하는 TransZero++라는 교차 속성 유도 변압기를 제안합니다.
  - 구체적으로, TransZero++는 속성 기반 시각적 특징과 시각적 기반 속성 특징을 각각 학습하는 두 개의 속성 유도 트랜스포머 서브넷(즉, 속성→비주얼 트랜스포머(AVT)과 시각→비주얼 트랜스포머(VAT)로 구성되며, 이들은 두 개의 매핑 함수 M_1과 M_2를 사용하여 의미 임베딩 공간에 추가로 매핑되어 바람직한 시각-시각적 상호 작용을 수행합니다.

- AVT 및 VAT에서 우리는 먼저 
  - i) ImageNet과 ZSL 벤치마크 간의 교차 데이터 세트 편향을 완화하고 
  - ii) 보이는 클래스에서 보이지 않는 클래스로의 전달 가능성을 향상시키기 위해 서로 다른 영역 간의 얽힌 상대 기하학 관계를 줄임으로써 시각적 특징을 증가시키는 기능 증강 인코더를 사용합니다.
  
- 이러한 증강된 시각적 특징은 다음과 같은 순차적 학습을 촉진할 것입니다. 
  - 지역성을 강조하는 시각적 특징을 학습하기 위해 AVT에서 Attribute→Visual Decoder를 사용하여 시맨틱 속성 정보의 안내에 따라 주어진 이미지에서 각 속성과 가장 관련이 많은 이미지 영역(속성 기반 시각적 특징으로 표시됨)을 지역화합니다.

- 또한 VAT에서 시각적 기반 속성 특징을 학습하기 위해 visual→attribute 디코더를 사용합니다. 
  - feature-level and prediction-level의 semantical collaborative losses을 더 도입함으로써 두 attribute-guided transformers는 의미론적 협업 학습을 통해 핵심(key) 의미 지식 표현을 위한 두 가지 보완적 semantic-augmented visual embeddings을 더 학습하도록 서로 가르칩니다.
- 마지막으로, semantic vectors와 협력한semantic-augmented visual embeddings을 활용하여 ZSL 분류를 위한 바람직한visual-semantic interaction을 수행합니다. 
- 광범위한 실험은 TransZero+가 3개의 ZSL 벤치마크와 대규모 ImageNet 데이터 세트에서 새로운 최첨단을 달성한다는 것을 보여줍니다. 
  - 정성적인 결과는 또한 TransZero+가 시각적 기능을 정제하고 시맨틱 증강 기능 표현을 위한 속성 영역을 정확하게 현지화한다는 것을 보여줍니다.





