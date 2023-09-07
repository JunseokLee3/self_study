# NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis


## 저널 : 2021년 q1, if 14.065, 0.81


## 저자 : ![Alt text](image.png)

공식 사이트 : https://www.matthewtancik.com/nerf
한국인이 만든거 https://modulabs.co.kr/blog/nerf-from-2d-to-3d/



[Rendering](/paper%20study/image%20study/0.0%20참고/0.0.1/rendering.md)

## abstrct:
- sparse 입력 view 세트을 사용하여 기본적인 continuous volumetrice(연속 체적) scene function을 최적화함으로써 complex scene의 새로운 view을 합성하기 위해 최첨단 성능 달성했다.
  - algorithm에  a scene에 fully-connected deep network(non-colvolutional) 을 사용하여 표현 했다.
  - input으로 5D ( spatial location (x,y,z) 그리고 viewing direction (theta, phi)) 
  - output으로 해당 공간 위치에서의 체적 밀도와 관찰 시점에 따라 달라지는 발산된 밝기입니다\
  - 우리는 카메라 광선을 따라 5차원 좌표를 조회(querying)하여 view을 합성하며, 우리는 classic volume rendering techniques을 사용하여 이미지안에있는 output colors와 densities을 투영한다.
  - [rendering 렌더링이란?](/paper%20study/image%20study/0.0%20참고/0.0.1/렌더링.md)
  - Because volume rendering은 본질적으로 미분가능(differentiable)하기 때문에, 우리의 표현 방식을 최적화기 위해 필요한 유일한 입력은 known 카메라 pose를 가진 이미지의 집합이다.
  - `위에거 해석 :  기술적으로, 미분 가능한 시스템은 훈련 중에 그라디언트(미분 값)를 사용하여 최적화될 수 있습니다. 따라서, 체적 렌더링의 이러한 특성을 활용하면, 알려진 카메라 포즈를 가진 이미지만을 사용하여 해당 표현 방식을 최적화할 수 있습니다.`
  - 우리는 complicated geometry 형태와 외관을 가진 장면들의 사실적인(photorealistic) 새로운 뷰를 렌더링하기 위해 'neural radiance fields'를 어떻게 효과적으로 최적화하는지 설명하며, 이전의 신경 렌더링 및 뷰 합성 연구보다 더 우수한 결과를 보여줍니다."

## 1 Introduction

- 이 연구에서는, 연속(continuous) 5D 장면 표현의 매개변수를 직접 최적화하여 캡처된 이미지의 렌더링 오류를 최소화함으로써, 오랫동안 지속되어(long-standing) 온 뷰 합성 문제를 새로운 방식으로 해결합니다.
  
- 우리는 고정된 장면(static scene)을 연속적인 5차원 함수로 표현하며, 이 함수는 공간의 각 점 (x, y, z)에서 각 방향 (θ, φ)으로 발산되는 방사도와, 미세한 불투명도( differential opacity)처럼 작동하여 (x, y, z)를 통과하는 광선이 얼마나 많은 방사도를 축적하는지를 제어하는 밀도를 출력합니다."
  - 우리의 방법은 합성곱 레이어 없이 깊은 완전 연결 신경망(다층 퍼셉트론 또는 MLP로도 불림)을 최적화하여 5차원 좌표 (x, y, z, θ, φ)에서 단일 체적 밀도와 뷰에 종속적인 RGB 색상으로 회귀하는 이 함수를 표현합니다.
  - neural raidance filed (NeRF)
    - 1) 3D 포인트의 샘플 세트를 생성하기 위해 카메라 광선을 장면을 통해 진행시키고, 
    - 2) 해당 포인트와 그에 해당하는 2D 시점 방향을 신경망의 입력으로 사용하여 색상 및 밀도의 출력 세트를 생성하며, 
    - 3) 해당 색상 및 밀도를 2D 이미지로 누적하기 위해 고전적인 볼륨 렌더링 기술을 사용합니다.
  - 본질적으로으로 미분 가능하기 때문에, gradient descent를 사용하여 관측된 각 이미지와 표현에서 렌더링된 해당 뷰 간의 오차를 최소화하여 이 모델을 최적화할 수 있습니다.
  - 여러 뷰에서 이 오차를 최소화(minimize)하면 네트워크가 실제 장면 내용을 포함하는 위치에 높은 부피 밀도와 정확한 색상을 할당함으로써 장면의 일관된(coherent) 모델을 예측하도록 권장합니다.
  -  그림 2는 이 전체 파이프라인을 시각화합니다.

![Alt text](image-1.png)
```
이 설명은 어떻게 신경 라디언스 필드가 장면을 표현하고 이미지를 렌더링하는지에 대한 과정을 개요로 보여주는 것입니다.
(a): 카메라의 광선을 따라 3D 공간의 특정 위치와 그 위치에서의 시야 방향(5D 좌표)을 샘플링합니다.
(b): 해당 5D 좌표들이 다층 퍼셉트론(MLP)에 입력되며, MLP는 해당 위치와 방향에 대한 색상과 부피 밀도를 출력합니다.
(c): 출력된 색상과 부피 밀도 값들은 볼륨 렌더링 기법을 사용하여 최종적인 이미지로 합성됩니다.
(d): 이 렌더링 프로세스는 미분 가능하므로, 렌더링된 이미지와 실제 캡처된 이미지 간의 차이(잔차)를 최소화하는 방향으로 신경 라디언스 필드를 최적화할 수 있습니다.
```

- 복잡한 장면에 대한 neural radiance field representation을 최적화하는 기본 구현은 충분히 고해상도의 표현으로 수렴하지 않으며, 카메라 광선당 필요한 샘플 수에서 비효율적입니다.
  - 우리는 MLP가 더 높은 주파수의 함수를 표현할 수 있도록 위치 인코딩을 사용하여 입력 5D 좌표를 변환함으로써 이러한 문제를 해결합니다. 
  - 또한 이 고주파 장면 표현을 적절하게 샘플링하기 위해 필요한 쿼리 수를 줄이기 위한 계층적 샘플링 절차를 제안합니다.



# 2 Related Work

- 컴퓨터 비전에서 유망한 최근 방향은 3D 공간 위치로부터 해당 위치의 부호 거리(the signed distance) [6]과 같은 형상의 암시적 표현으로 직접 매핑하는 MLP의 가중치로 객체 및 장면을 인코딩하는 것입니다.
  - 그러나, 이러한 방법들은 지금까지 삼각형 메시(triangle meshes) 또는 보셀 그리드(voxel grids)와 같은 이산적인 표현을 사용하여 장면을 표현하는 기술과 동일한 정밀도(fidelity)로 복잡한 기하학을 갖는 현실적인 장면을 재현할 수 없었습니다.
  - 이 섹션에서는 이 두 가지 작업 방식을 검토하고 우리의 접근법과 대비시킵니다. 우리의 접근법은 복잡한 현실적인 장면을 렌더링하는데 있어 최첨단의 결과를 가져오기 위해 신경망 장면 표현의 능력을 향상시킵니다. 
  - (`두 가지 작업 방식` :)
    -  1. 3D 공간 위치에서 그 위치의 사인 거리와 같은 형태의 암시적 표현으로 직접 매핑하는 MLP의 가중치로 객체와 장면을 인코딩하는 최근의 방향성.
    -  2. 삼각형 메시 또는 보셀 그리드와 같은 이산적인 표현을 사용하여 장면을 표현하는 기술.


- MLP를 사용하여 저차원 좌표에서 색상으로 매핑하는 유사한 접근법은 이미지[44], 텍스처링된 재료[12,31,36,37] 및 간접 조명 값[38]과 같은 다른 그래픽 기능을 표현하는 데에도 사용되었습니다.

[continuous 3D shapes](/paper%20study/image%20study/0.0%20참고/0.0.1/continuous%203d%20shapes.md)

**Neural 3D shape representations**
- 최근의 연구에서는 연속적인 3D 형상( continuous 3D shapes )의 암시적 표현을 레벨 셋으로서 조사하였으며, 이를 위해 xyz 좌표를 사인 거리 함수(signed distance functions)나 점유 필드(occupancy fields)로 매핑하는 딥 네트워크를 최적화하였다. 
  - 그러나 이러한 모델들은 일반적으로 ShapeNet과 같은 합성 3D 형상 데이터셋에서 얻은 실제 3D 기하학에 대한 접근 요구로 인해 제한적이다.
  - 후속 작업에서는 2D 이미지만을 사용하여 신경 암시적 형상 표현을 최적화할 수 있는 차별화 가능한 렌더링 함수를 공식화함으로써 지상 진리 3D 형상에 대한 요구 사항을 완화했습니다.
  - Niemeyer 등[29]은 표면을 3D 점유 필드(occupancy fields)로 표현하고 각 광선에 대한 표면 교차점을 찾기 위해 수치적 방법을 사용한 후 암시적 미분(differentiation)을 사용하여 정확한 도함수(derivative )를 계산합니다. 
    - 각 광선 교차 위치는 해당 지점에 대한 확산 색상을 예측하는 신경 3D 질감 필드의 입력으로 제공됩니다
  - Sitzmann 등[42]은 각 연속적인 3D 좌표에서 특징 벡터와 RGB 색상을 단순히 출력하는 덜 직접적인 신경 3D 표현을 사용하고, 각 광선을 따라 3D 공간을 탐색하는 순환 신경망으로 구성된 미분 가능한 렌더링 함수를 제안합니다.
  - `Ray marching` :  컴퓨터 그래픽스에서 사용되는 기법으로, 광선이 3D 공간에서 어떻게 진행되는지를 시뮬레이션하는 방법을 말합니다. 따라서 "marches along each ray"는 광선을 따라 3D 공간을 탐색한다는 의미로 해석해야 합니다.



- 이러한 기법들은 복잡하고 고해상도의 geometiry를 표현할 수 있는 잠재력을 가지고 있지만, 지금까지는 geometric 복잡성이 낮은 단순한 형태에 제한되어 왔습니다, 그 결과 과도하게 부드러운 렌더링이 됩니다.  `(실제 구현에서는 단순한 형태에만 제한되어 있다는 것을 지적)`
  - 우리는 5D 방사선 필드(adiance fields) (2D 시점 종속적 외관(view-dependent)을 가진 3D 볼륨)를 인코드하기 위해 **네트워크를 최적화하는 대체 전략이 더 높은** 해상도의 geometry와 appearance을 표현하여 복잡한 장면의 사진같은 새로운 뷰를 렌더링할 수 있다는 것을 보여줍니다.
  

**View synthesis and image-based rendering**

- 주어진 조밀한 뷰 샘플링에서는 단순한 빛 필드 샘플 보간 기술(simple light field sample interpolation techniques) [21,5,7]을 사용하여 사진같은 새로운 뷰를 재구성할 수 있습니다. [simple light field sample interpolation techniques](/paper%20study/image%20study/0.0%20참고/0.0.1/simple%20light%20field%20sample%20interpolation%20techniques.md)
  - 더 희소한 뷰 샘플링을 가진 새로운 뷰 합성에 대해 컴퓨터 비전 및 그래픽스 커뮤니티는 관찰된 이미지에서 전통적인 지오메트리와 외관 표현(apperance representation)을 예측함으로써 중요한 진전을 이루었습니다.
  - 하나의 대중적인 접근 방식 클래스는 장면의 메시 기반 표현(mesh-based representations)을 사용하며, 이는 무광택(diffuse) [48] 또는 뷰 종속적 [2,8,49] 외관(view-dependent [2,8,49] appearance)을 가집니다. 
  - 미분 가능한(Differentiable) 래스터라이저(Rasterizers:) [4,10,23,25] 또는 패스 트레이서(Pathtracers) [22,30]는 그래디언트 하강을 사용하여 입력 이미지를 재현하기 위해 메시 표현을 직접 최적화할 수 있습니다. 
  - [래스터라이저(Rasterizers:)  또는 패스 트레이서(Pathtracers) ](/paper%20study/image%20study/0.0%20참고/0.0.1/rasterizers%20or%20pathtracers.md)
  - 그러나 이미지 재투영을 기반으로 한 그래디언트 기반 메시 최적화는 종종 어렵습니다, 주로 지역 최소값 또는 손실 풍경의 나쁜 조건화 때문입니다. 더욱이, 이 전략은 최적화 전에 초기화로 제공되는 고정된 위상을 가진 템플릿 메시를 필요로 합니다 [22], 이는 일반적으로 제약이 없는 실제 세계의 장면에서 사용할 수 없습니다.
