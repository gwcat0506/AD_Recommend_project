# 코드
코드 실행 시,  `1.Data_Acquisition` ~ `5.Visualization` 차례로 진행
## 1.Data_Acquisition
웹사이트 자체적으로 제공하는 csv 파일 외에    
<u>크롤링 및 가공이 필요한 데이터</u> 들을 처리한 코드들과 사용한 xsl 파일 입니다. 
- 광고크롤링
- 동별사업체-종사자수
## 2.Data_Preprocessing
데이터 전처리를 위한 폴더입니다.   
전처리 진행 순서는 아래와 같습니다. (파일명과 무관) 
```
1) 결측치 처리 및 데이터 형식 통일 
    → 2.데이터_전처리.ipynb
2) 이상치 제거 
    → 2.데이터_전처리.ipynb
3) 필요한 컬럼 추가 및 데이터 병합을 위한 전처리
    → 2.데이터_전처리.ipynb    
    → 4.위경도_자료_역단위로_나누기.ipynb
    → 5.동_상권_병합.ipynb
4) 데이터 병합
    → 6.최종_데이터_병합.ipynb
5) 데이터 카테고리화
    → 7.데이터_카테고리화.ipynb
```
- 1.EDA
- 2.데이터_전처리.ipynb
- 3.GPS_구-동.ipynb
- 4.위경도_자료_역단위로_나누기.ipynb
- 5.동_상권_병합.ipynb
- 6.최종_데이터_병합.ipynb
- 7.데이터_카테고리화.ipynb
## 3.Labeling
네이버 트랜드, 카카오 데이터 트랜드 등의 정보를 활용하여 최종 데이터와 광고를 매칭 시켜주었습니다.   
광고는 총 29개의 카테고리로 분류가 되어있어 0~28 의 int 형태로 라벨링 해주었습니다.
- 광고_라벨링.ipynb
## 4.Visualization
최종 데이터를 활용하여 따릉이 대여소 위치, 개인정보, 공간정보를 시각화하였습니다.
- 공간정보_시각화.ipynb
- 사용자개별정보_시각화.ipynb
- 성별_시각화.ipynb
- 시간정보_시각화.ipynb
## 5.Modeling
크게 1,2차 모델링으로 구분하여 진행하였습니다.   
1차 모델링은 Pycaret을 활용하여 Decision Tree Classifier 모델을 활용하였습니다.   
2차 모델링은 앙상블 모델로 Random Forest와 XGBoost 모델을 활용하였습니다.
- 1.Pycaret - 가상환경 학습 모델.ipynb
- 2.RandomForest_XGBoost_모델_비교_분석.ipynb
- 3.추가_학습_모델.ipynb



[데청캠_팀퍼스트.pdf](https://github.com/gwcat0506/AD_Recommend_project/files/9446933/_.pdf)


