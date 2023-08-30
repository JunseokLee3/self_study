# Prototypical Contrast Adaptation for Domain Adaptive Semantic Segmentation

## 저널 및 학회 : ECCV 2022, 거의 q1급

## 저자 : ![Alt text](image.png)

https://link.springer.com/chapter/10.1007/978-3-031-19830-4_3
https://arxiv.org/pdf/2207.06654.pdf%E4%BB%A3%E7%A0%81%E5%9C%B0%E5%9D%80%EF%BC%9Ahttps://github.com/jiangzhengkai/ProCA
https://github.com/jiangzhengkai/ProCA


## Abstract :

- Unsupervised Domain Adaptation (UDA)은 label이 있는 훈련된 모델은 unlabel된 target을 체택하는 거을 목표
- **Prototypical Contrast Adaptation (ProCA) 본인 제안한 모델.**
  - ProCA은 supervised domain adaptive semantic segmentation을 위해 간단하고 효율적인 contrastive learning 방법이다.
    - 이전 방법은 단순히 다양한 도메인에 걸치 intra-class representation distiributions(분포)의 정렬을 고려 했다.
    - 반면 inter-class strutural 관계 에는 불충분한 탐구 했다. 
    - 이는 target domian에 표현들을 정렬에서 source domain에서 하는 것처럼 쉽게 구분되지 않는다.
  - 대신에 ProCA는 class-wise prototypes안에 있는 inter-class information을 통합합니다.
    - 그리고 adaption을 위해 class-centered distribution alignment을 체택합니다.
  - postive로써의 같은 클래스 prototype와 negative로서의 다른 클래스는 class-centered distribution alignment을 성취하기위해 고려됨으로써, ProCA은 classical domain adaptation tasks에서 state-of-the-art 성능을 달성한다.
[inter and itra 차이점](/paper%20study/image%20study/0.0%20참고/0.0.1/ira%20and%20inter%20diffence.md)

## Introduction
- Deep neural network(DNN)의 개발 이후 많은 이미지 문제 그리고 semantic segmentation 문제에서 눈에 뛰게 개선을 이루었따.
  - 하지만 일부 학습되지 않은 testing data에서는 일부 drop이 일어 나고 있다.
  - target domain에서 pixel-wise large-scale semantic segmentation은 비용이 많이 들고 시간이 많이 소비된다.
  - 그래서 **Unsupervised Domain Adaptation (UDA)은 이러한 문제를 풀기 위해 유망한 방향**이다.


- UDA 몇몇 방법들은 **source 와 targe domain의 adversarial training losses을 최소화 하는 방법으로 두 도메인 간의 불일치를 줄였다**.
  - 구체적으로 two-player game으로 공식화되어 있다.
    - backbone network(i.e. ResNet-101 backbone) 은 feature 추출기로써, 반면 discriminator(구별기)는 어떤 domain에서 feature가 나왔는지 식별한다.
    - minmax game에서 평행상태에 도달하기 위해, 그것은 일반화를 위해 domain 불변성 representation 을 생성하기 위한 backbone network가 필요로 한다.
  - 몇몇 adverarial training은 두 도메인 사이에서 정렬되고 구별 할 수하는 특징의 분포를 초래한다.
  - 그러나 global feature distribution은 domain들에 걸쳐 closer(밀집) 되더라도, 그것은 target domain에 different semantic categories의 기인하여 pixels이 잘 구별 되도록 보장 되지 않는다.
    - 그것은 poor 일반화 능력과 성능이 저하된다.
    - `위에 문제점들을 나열 했다. 근데 잘 이해가 되지 않는다. 무슨 말이지?`
    - [조금더 문제점에 관련 자세한 설명](/paper%20study/image%20study/0.0%20참고/0.0.1/왜%20UDA가%20나왔는지%20그리고%20문제점.md)


- 위에 문제들을 해겨하기 위해, **몇몇은 category-wise information을 고려대상**으로 하다.
  - 높은 신뢰도 예측을 장려하는 아이디어는 결과의 **entropy를 최소함**으로써 이루어졌따.
    - 두 **classifiers(분류자)의 output 사이의 불일치는 implicitly(암묵적)으로 category-level alignment을 달성하는데 활용** 되었다.
  - 추가로 **fine-grained adverarial learning framework는 domain discrimination에서의 class information 을 통합하기 위해 제안** 되었다. 
    - 그것은 **fine-grained level 에서의 특징 배열에 도움**을 준다.
  - 그러나 **이전 접근들은 몇몇 intra-class에서의 adversarial training은 source 와 target dmoain 간 representational structure의 일관성으로 독려하지 않는 경향**이 있다.
    - **즉(namely), 어느정도로(to some extent), targent domain에서 multiple categories는 같은 group에서 잘 투영이되고, 같은 그룹은 반대로 source domian에서 잘 구별**된다.
  - 그러므로 단지 intra-class distributional alignment는 labeled source data로부터 learned representations의 최고로 활용하는데 불충분 할 수 있다.

- class-level information을 최대한 활용하기 위해서, 우리는 unsupervised domain adaptive semantic segmentation을 위해 Prototypical Contrast Adaptation (ProCA)을 제안한다.
  - **직관적으로(Intuitively), 다른 domain에서의 같은 category는 high representational similartiy를 공유**하도록 되어 있다.
  - 그러므로 **multiple prototypes, (i.e the approximated representational centroid of various categories 다양한 categories의 대략적인 표현 중심)은 source와 target domains 둘다 inter-class 관계를 묘사하는데 활용**된다.
  - 구체적으로 **오로지 source domian에서 훈련된 segmentaiton model은 얻은 이후, category-wise prototypes features을 source domain 에서 특징의 중심을 계산하여 얻는다**.
    - 그런다음 contrastive learning은 domian adaptation 과정에 도입이 된다.
    - 특히 target domain의 pixel은 추정된 의사 레이블과 동일한 클래스를 가진 해당 프로토타입에 더 가깝게 당겨지고 다른 프로토타입에서 밀려납니다
  - 또한 불변성 domains을 위해, category-wise prototypes은 두 domain의 current feature에 의해 추가로 업데이트 된다. 
  - 게다가 몇몇 prototyupe contrastive adaption 전략읜 feature와 output level에 simultaneously 적용된다.
  - self-training framework의 기반으로, 우리는 class-aware pseudo-label thresholds으로 성능을 향상 시켰다.

- 의미론적 분할에 대한 도메인 적응 벤치마크, 즉 GTA5 → Cityscapes 및 SYNTIA → Cityscapes에 대한 실험 결과는 최첨단 성능으로 이어지는 접근 방식의 효과를 더욱 입증합니다. 
  - 특히, DeepLab-v2 네트워크와 ResNet-101 백본을 사용하여 GTA5 [35] 및 SYNTIA [36] 데이터 세트에서 적응할 때 Cityscapes [4] 의미론적 분할 MioU를 56.3%, 53.0% 달성하여 이전의 최첨단 데이터를 크게 능가합니다.


- We summarize the major contributions as follows:
  - 우리는 semantic segmentation에서의 UDA problem을 위해 다른 categories의 features을 제약들을 명시적 도입함으로써 ProCA을 제안한다.
    - 이것은 동시에 prototypes에 같은 same class를 가까이 당기는 뿐만 아니라 다른 classes prototypes으로부터 멀리 보냅니다. 
    - multi-level variant(변형)은 또한 더 adaptation ability를 향상 시키기 위해 디자인 되었다.
  - scheme을 업데이트하는 Online prototypes은 domian 불변성과 class-wise prototypes의 구별 능력을 향상 시키기 위해 도입되었다.
  - self-training method의 class-wize adaptive thresholds을 결합하여 제안된 방법을 56.3%와 52.6%을 mIOU을 달성했다. (GTA5 and SYNTHIA)


## 2. Related Works

### 2.1 Semantic Segmentation

### 2.2 UDA for Semantic Segmentation

- 기존 semantic segmentation의 UDA에서 크게 3가지로 나누어진다.
  - **style transfer, feature alignmnet 그리고 self-training**
    - 최근 unpaired image-to-image translation 작업의 발전에 힘입어[55], style transfer에 대한 연구는 가상(virtual) 데이터에서 실제 데이터로의 매핑을 학습하는 것을 목표로 합니다[12, 31].
  - feature alignment에서의 이전 works은 **domain-invariant features을 얻기 위해 source와 target domains사이에 불일치를 최소화**한다.
    - 이는 도메인별 레이어에 걸쳐 도메인 간 **MMD(Maximum Mean Discrepancy) 거리를 직접 최소화하거나 도메인 인식 판별 기능 생성을 방지하기 위해 판별자를 사용하여 적대적인 방식으로 모델을 학습**함으로써 달성할 수 있습니다[13].
  - 또한 feature alignment안에 class-wise information을 쳬택하기 위해 몇가지 일을 시도한다.
  - fine-grained adversarial learning framework는 discriminator안에 class information 을 합치기 위해 제안 되었다. 
      - 이는 feature을 클래스 인식 방식으로 정렬하여 feature 적응(adaptation) 및 성능을 향상시키는 데 도움이 됩니다.
  - self training에 대한 접근 방식(Approaches)은 주로 대상 도메인에 pseudo-labels을 할당(assigning)하는 데 중점을 둡니다.
    - Iterative self-training method 제안되며[56] 유사 레이블(pseudo-labels)을 대안으로 생성하고 샘플링 모듈(sampling module)로 모델을 재학습(retraining)하여 범주 불균형 문제(category imbalanced issue)를 처리합니다.
    - pseudo-label 생성을 수정하기 위해 Uncertainty estimation  [50]이 제안되었습니다. 일관성 기반 방법 [1]은 서로 다른 섭동의 예측 간의 일관성을 강화함으로써 채택되었습니다.
  - [48]의 작업에서, prototype-based smaple-wise preudo-label correction 전략은 제안 되었고 segmentation performanc을 향상시키기 위해 복잡한 multi-stage training framework에 embede된다.
- 그럼에도 불구하고 위에 있는 방법들은 명시적으로 다른 categories의 clusters 사이에서의 relationship의 modeling을 무시한다.
  - 우리는 직접적으로 prototypical contrastive adaptation 에 의해 다른 category centroids의 여러 제한조건들을 탐험한다.
  - 이러한 방법은 target domain에서의 비슷한 distribution에서의 categories을 쉽게 distinguish 할 수 있다. 또한 우수한 성능을 이끈다.


### 2.3 Contrastive Learning

- Contrastive learning은 self-supervised representation learning에서 주목할 만한 성능을 보인다.
  - STC는 video instance segmentation task을 위해 연관된 embedding을 학습하기 위해 contrastive learning을 사용한다. 
  - UDA semantic segmentation에서 CLST는 마지막에 적응된 feature representation을 학습하기 위해 contrastive learning을 활용을 시도한다.
  - 동시 작업 SDCA[21]는 UDA segmentation을 위해 contrast adaptation을 수행하기 위해 highorder semantic information를 사용할 것을 제안하지만, 우리는 그것이 필요하지 않다는 것을 발견했습니다.
  - 본 논문에서는 contrastive learning의 도움을 받아 서로 different categories와 pixel-wise features의 관계를 명시적으로 모델링하여 unsupervised domain adaptive seantic segmentaiton에 대한 domian-invaariant representation을 얻습니다.

## 3 Methodology

![Alt text](image-1.png)

- source domain과 target domian 사이의 distribution 거리를 최소화함으로써 이전의 접근 방식은 domain adaptation problem에 대한 domain-invariante representations을 얻는 것을 목표로 합니다. 
  - 그러나 inter-class structural 관계는 충분히 탐구되지 않았습니다.
  - 그림 1의 (a)을 보면, two domain을 걸쳐 intra-class의 배열을 한 후, 그것은 different categories을 구별하기 위해 더 많은 문제점이 있다. 그 이유는 souce domain에서 확인된 desiction boundaries을 target domain 에서 유지하기가 어렵다.
  - 그러므로 우리는 새로운 category-aware prototypical contrast adaptation을 제아한다. 
    - 이것은 contrstive manner에서 명시적으로 intra-class와 inter-class의 관계를 모델링하기 위해 multiple prototypes을 도입했다.

- 이전에 유사한 state-of-the-art 방법들은, segmentation model은 supervised manner에서 sorce domian을 우선 훈련한다.
  - 동시에 multiple prototypes는 각각 category을 표현하기 위해 초기화 된다.
  - 대조적 적응은 inter-class relationship을 제한하기 위해 쳬택 되었다.
  - prototype은 domain-invariant representation을 향상시키기위해 source domain와 target domain 모두 업데이트 했다.
  - 마지막으로 우리는 self-training을 위하여 class-aware adaptive thresholds을 가진 수정된 pseudo-label generation 을 표현했다. 이것은 새로우 sota를 달성했다.


### 3.1 Preliminaries


![Alt text](image-2.png)

- 이전 works을 따르면, segmentation model은 예측 $p^s_n$와 C라는 주석이 달린 ground-truth label $Y_n^s \in \mathbb{L^{H * W}}, \mathbb{L} = \{1,2, ..., C\}$ , $x_n^s \in \mathbb{H * W}$으로 주어진 이미지.
  - 우리는 standard cross-entropy loss를 쓴다.

![Alt text](image-3.png)

  - $N_s$는 source domian images의 수이다. 
  - $H$와 $W$는 이미지의 높이와 넓이 이다.
  - i,j는 pixel index의 높이와 넓이이다.
  - C 는 catgories의 수이다.
  - $p_n^s \in \mathbb{R^{H*W*C}}$는 image $x_n^s$의 예측된 확률이다. 이는 prediction $C(F(x_n^s))$이다.
  - $y_n^s \in \{0, 1\}^{H*W*C}$는 ground-truth label $Y_n^s$의 one-hot 표현이다.

![Alt text](image-4.png)


### 3.2 Prototypical Contrast Adaptation

- 그림 2에 나와 있는 것처럼 여기 intra-class와 inter-class relation들은 prototypes-based contrastive learning에 의해 동시에 고려된다.
  - 구체적으로 ProCA  세가지 stages로 포함된다. 
    - **prototypes initialization, contrast adaptation, prototypes updating**
  
**Prototypes Initialization**
- labeled source domain 에서 후련된 모델을 얻은 이후, class-aware prototypes는 계산 될 수 있다.
![Alt text](image-5.png)
  - $F^s_{n,i,j} \in \mathbb{R^d}$는 dimension d를 가진 source feature vectord가 추출된것이다. 
  - c는 카테고리 ㅊ의 수의 인덱스이다.
  - H와 W는 feature의 Height와 width을 나타낸다.
  - $\mathbb{I}[Y^s_{n,i,j}=c]$는 함수를 나타낸다. 이것은 만약 $Y_{n,i,j}^s=c$ 이라면 1의 equals이다. 그리고 다른 경우는 0이다.
  - Prototypes는 다양한 categories의 근사 표현된 centroid으로써 참조된다.

**Contrast Adaptation.**
- target domain의 주어진 이미지, 해당되는 feature $F_s^t$은 공유된 backbone network $\mathcal{F}$에 의해 추출된다. 
  - 따라서 그것의 pseudo-label $y_n^{~t} \in \{0,1\}^{H * W * C}$는 source domina에서 classifier $\mathcal{C}$에의해 생산된다.
  -  여기에, pseudo-label은 extrated features와 그것들의 해당되는 prototypes와 연결시킨다.
  -  그러므로 우리는 features와 각 prototypes의 사이의 유사성을 계산할수 있다. ![Alt text](image-6.png)

![Alt text](image-7.png)




# 나의 의견
## 이해하는거 다시 정리중
- Unsupervised Domain Adaptation (UDA)은 label이 있는 것을 훈련하여 unlabled된 것을 분류하는 문제이다.
- 약간 Zero shot learning과 few show learning의 느낌이 강하다.
- 또한 UDA는 GAN의 방법을 영감 받아 two-player 가 있다. (i.e 분류기와 추출기)
  - 초기 source와 target domain간의 불일치를 줄이기 위해 설계 되었다.
  - GAN의 adversarial의 방법을 영감 받아. 분류기는 두 domain을 구분할 수 없는 생성한다.
  - 분류기는 어떤 domain에서 feature가 나왔는지 식별한다.
  - 몇몇 adversarial training은 두 domains 사이를 정렬되고 구별 할 수 있는 특징의 분포를 초래한다.
    - 그러나 global feature distribution은 domain들에 걸쳐 밀접 되더라도, target domian의 다른 semantic categories에 의해 잘 구별되도록 보장 되지 않는다
    - 이것은 일반화 능력과 성능에 악여향을 미친다.

- 위의 문제를 해결하기위해 category-wise information을 고려했다.
  - entropy 최소함으로써 이루어 졌다.
  - 두 classifier은 ouput 사이의 불일치는 category-levle alignment을 달성하는데 활용 되었다.
  - 그러나 몇몇 intra-class 에서의 adversarial training은 source와 target domain 간 representational strucyture의 일관성을 독려하지 않았다.
  - target domain에서 multiple categories와 같은 group에서 잘 투영되고 같은 그룹은 반대로 source domain에서 잘 구별 된다.
    - 그러므로 intra-class distirvution alignment는 labeld source data로 부터 learned representation을 최고로 활용하는데 불충분 할 수 있다.


- 그니깐 요약하자면 다른 것들은 intra-class에 잘 되지만 inter-class에는 강한 강점이 보이지 않은것이고 저자들은 prototypes를 이용하여 inter-class 까지 잘 구별 되는 모델을 만들었다는 말