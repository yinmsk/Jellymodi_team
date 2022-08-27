<p align="center"><img src="https://user-images.githubusercontent.com/104331479/185329655-95f41df4-dec5-4e94-b6b8-471a0ef2deba.png" width="80%" height="80%"></p>

# <img src="https://user-images.githubusercontent.com/104331479/185330319-86af99b3-0eb2-4a75-a0c4-2b36808a3734.png" width="30" height="30"/> Project Jellymodi

**머신러닝 사물인식 프로젝트 - 젤리모디(Jellymodi: Jelly mood diary)**

Python OpenCV 를 이용하여 얼굴 표정을 인식하고, 분석한 표정에 해당하는 젤리 이모티콘을 넣어 일기를 쓰는 웹사이트 제작
***
<br><br/>


## 1. 개발 기간, 참여 인원
* 개발기간: 2022.05.18 - 2022.05.25
* **Team** <a href="https://github.com/cmjcum"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
김동근 <a href="https://github.com/yinmsk"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
노을 <a href="https://github.com/minkkky"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
이정아 <a href="https://github.com/zeonga1102"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
이현경 <a href="https://github.com/LULULALA2"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
* **S.A** <a href="https://cold-charcoal.tistory.com/68">블로그로 이동(☞ﾟヮﾟ)☞</a>
***
<br><br/>


## 2. 사용 기술
* Python 3.8
* Flask
* MongoDB
* Tensorflow 2.9
<br><br/>


## 3. ERD 설계
![jellymodi](https://user-images.githubusercontent.com/104487608/187019946-deb2d4ad-50a2-49ae-b093-3e2189e23038.png)
<br><br/>


## 4. 기능 소개
<details>
  <summary>로그인, 회원가입 기능 구현 <a href="https://github.com/yinmsk/Jellymodi_team/blob/56376460d46d1fafaad91119eafd2f5fe963813c/api/login.py#L12">📄코드</a></summary>
  <div markdown="1">
 
* db에 이미 가입된 이메일이 있으면 "중복된 이메일" 이라는 메세지를 보내도록 구현했습니다.
* 비밀번호를 hashlib 를 사용해 저장했습니다.
* try / except 문을 사용해 token가 만료되었을 때, 올바르게 디코딩되지 않았을 때 서로 다른 메세지를 유저한에게 보내게 됩니다.
  </div>
</details>

<details>
  <summary>일기 작성 <a href="https://github.com/zeonga1102/Jellymodi_team/blob/master/api/post.py#L51">📄코드</a></summary>
  <div markdown="1">
 
* 사용자가 작성한 일기 내용과 사진, 얼굴 표정에 알맞은 젤리 아이콘을 저장합니다.
  </div>
</details>
<br><br/>


## 5. 트러블 슈팅
<details>
  <summary>7개의 감정이 담긴 표정을 학습 시켰었는데 모델의 정확도가 높지 않았다.</summary>
  <div markdown="1">
 
* 7개의 표정으로 학습을 시키다 보니 애매하게 실제로 어떤 감정을 가진 표정인지 사람인 내가 봐도 구분하기 어려웠었기 때문에,<br>
    표정을 4개로 줄이고 학습을 시키니 0.6,7 정도의 정확도만 나오던 모델이 정확도가 0.9까지 오를 수 있었다.
  </div>
</details>

<details>
  <summary>월별로 내림차순 / 일별로도 오름차순 으로 구현하고 싶었지만 일별 오름차순이 구현되지 못했습니다. </summary>
  <div markdown="1">
 
* 000
     [📄코드](https://github.com/yinmsk/Jellymodi_team/blob/2a95094b57557c4065531ab199e8305879bcaa5e/app.py#L18)
  </div>
</details>
<br><br/>


## 6. 회고 느낀점
* 이번 프로젝트는 특히 내가 사용하고 있는 무다라는 어플에서 아이디어가 시작되어 만들게 된 점이 좋았고 재미있게 프로젝트를 할 수 있었다.
* 팀원 모두가 머신러닝 모델을 학습할 수 있어서 더 좋았던 시간인것 같았고 모델의 정확도가 오르는걸 보면서 즐겁게 프로젝트를 할 수 있었습니다.
* 프로젝트 발표 후 피드백에서 실제 서비스를 해도 좋겠다고 호평을 받기도 했어서 더 좋았습니다. 
