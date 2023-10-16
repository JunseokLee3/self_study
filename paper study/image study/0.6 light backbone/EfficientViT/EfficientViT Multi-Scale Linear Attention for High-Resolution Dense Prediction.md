# EfficientViT: Multi-Scale Linear Attention for High-Resolution Dense Prediction


- 핵심:
  - cost and effiecicey
    - 기존 softmax 가 문제
    - relu linear attentino을 처음 도입한 모델
  - relu linear attention
    - 하지만 softmax의 계산량에 비해 relu가 훨씬 이득
    - softmax 보다 sharp 하게 못잡음
    - 단점 극복을 위해 channel 별로 depth wise convoution 도입
    - 이후 채널 별 concat을 통해 일부분 집중하게 됨
  - depth wise convolution 채널별 계싼 역시
    - group을 이룸으로써 불 필요한 연산량 없앰




