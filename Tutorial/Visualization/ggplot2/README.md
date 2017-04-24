## 외우지 않는 R 시각화 : ggplot2 뽀개기

**Notice**

ggplot2는 다른 그래픽 패키지와 달리 데이터를 효과적으로 분석하도록 해주는 grammar of graphic를 확장한 Layered grammar of graphics 를 탑제하였습니다. 다만 qplot의 경우 Quick plot의 약자답게 빠르고 간편한 대신 이러한 철학을 대변할 수 없다는 단점이 있습니다. 따라서 본 문서에서는 ggplot2의 문법적 이해를 통해 암기를 최대한 줄이는 것을 목표로 하기 때문에 qplot의 경우 생략하였습니다.

**홈페이지** : pizza12333.github.io

## 들어가며

SAS, Matlab 등 여러 상용 분석툴과 비교해서 R의 장점 중 한 가지는 바로 '손쉽고 예쁜 시각화를 무료로'라는 것이다. 보통 손쉬우면 못생겼고, 예쁘면 돈을 내야했다. 하지만 R은 적당히 쉬우며 아주 아름다운 플롯을 무료로 그릴 수 있다. 이러한 장점 때문일까 전세계 R을 쓰는 사람들은 데이터 시각화를 위한 패키지로 ggplot2를 선택한다. 하지만 단지 예쁘다는 이유로 ggplot2가 R시각화 대표하게된 이유를 설명하기에는 분명 부족하다. 

ggplot2가 갖는 장점은 근원에는 다른 접근법 즉 "Grammar of graphics"에 있다. 이 grammar of graphics 덕분에 우리는 디자이너나 전문 개발자가 아닌 분석가가 될 수 있는 것이다. 하지만 대부분이 ggplot2를 공부하는 방법은 GoG(Grammar of graphics)에 대한 이해 없이 단지 cookbook 형식으로 코드를 외운다. 이러한 공부법의 폐단은 Hadley Wickham이 그의 저서 "ggplot2 elegnt graphics for data analysis"에서 명시했듯 ggplot2를 지금의 명성으로 이끈 방법론, 철학은 도외시 한 채 그래픽 사례쯤으로 생각하고 전부 외우는것과 다르지 않을 것이다.$_{^{**}1)}$

암기는 언젠가 까먹게 돼있다. 하지만 이해는 끝까지 남는다. 예를 들어

	Q : 1 부터 100까지 자연수의 합을 구하시오

라는 문제에서 단지 공식만 외워서 공부했다면 공식을 기억하지 못한다면 풀수 없는 문제이다. 아니면 1부터 100까지 단순무식하게 더하는 수밖에 없다. 하지만 이를 공부할 때 외우지 않고 핵심을 이해했다면, 공식을 까먹더라도 

	1 + 100 = 101
	2 + 99 = 101
	3 + 98 = 101
	...
	49 + 52 = 101
	50 + 51 = 101
	51 + 50 = 101

라는 규칙을 도출 할 수 있고 이를 통해 문제에 대한 답을 도출할 수 있다.

	50 * 101 = 5050

	
"따라서 외우지 않고"라는 타이틀을 정하게 됐다. 처음 R과 함께 ggplot2를 봤을 때 복잡한 코드들을 바라보며 이걸 언제 외워 언제 다쓸 수 있을지 의문이었다. 하지만  "ggplot2 elegnt graphics for data analysis"라는 책을 "전희원씨의 R기반 시각화"에서 알게 됐고 ggplot2가 외워서 사용할 필요가 없다는 사실을 깨달았다.R을 사용하는 사람들의 대부분은 전문 개발직군 보다 비 개발직군인 경우가 많을 것이라 생각한다. 따라서 부족한 실력에 문서를 공개하는 것이 많이 부끄럽지만 과거의 나와 같은 어려움을 겪는 사람들을 돕고 싶어 문서를 만들게 됐다. 

부족한 실력이지만 여기까지 올 수 있도록 아낌없이 가르침을 주시고 길을 밝혀주시는 **혜현용**형과 삶의 단 하나의 이유인  **가족**들에게 감사를 드립니다.

<hr/>
$_{^{**}1)}$  " Without the grammar, there is no underlying theory and existing graphics packages are just a big collection of special cases." 를 의역하였습니다.
<hr/>

## 코드 및 참고 문헌
### * 저장소
본 문서에서 사용된 모든 코드와 자료는 [깃허브 저장소](https://github.com/pizza12333/project_repo/tree/master/Tutorial/Visualization/ggplot2)에 업로드 돼어 있다. 따라서 필요시 아래 링크를 통해 다운받을 수 있다.

링크주소: https://github.com/pizza12333/project_repo/tree/master/Tutorial/Visualization/ggplot2

### * 참고문헌

본 문서를 만들기 위해 인용 또는 참고한 문서는 다음과 같다.

* "ggplot2 elegnt graphics for data analysis(2009)", Hadley Wickham, Springer
* "R in a Nutshell 2nd Edition(2012)", Joseph Adler, O'Reilly 
* "ggplot2 Essentials(2015)", Donato Teutonico, Packt
* "R 기반의 시각화", 전희원
* "R Graphic cookbook(2013)", Winston Chang, O'Reilly 

### INDEX

#### Chapter 01 : ggplot2 시작하기
* 들어가며
1. Introduction of R basic grahic systems 
2. Layered Grammar of graphics in ggplot2

Comming soon
