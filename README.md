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
<br><br/>


## 5. 트러블 슈팅
<details>
  <summary>해당 장르의 책을 조회하기에 어려움이 있었다.</summary>
  <div markdown="1">
 
* url에 name을 지정해주고 views.py 의 함수 안에 name 을 넣음으로 해당 장르의 소설책만 가져올 수 있었다.
   [📄코드](https://github.com/yinmsk/webtachu/blob/fb13f919f245fa79718c1779d79bf5f18bf14178/books/views.py#L14)
  </div>
</details>

<details>
  <summary>좋아요 누른 작품 최신순 정렬에 어려움이 있습니다. BookModel의 id값으로 정렬을 하려 했지만 정렬을 할 수 없었습니다</summary>
  <div markdown="1">
 
* 정렬이 되지 않았던 이유는 BookModel의 id 는 book_id이므로 선호작품 등록 순서와는 관계가 없었기 때문이었다. <br>
   raw query로 users_favorites에 접근하여 해결 할 수 있었습니다. raw query 중간 테이블에 접근해 id값을 받아와 정렬했습니다.
   [📄코드](https://github.com/zeonga1102/webtachu/blob/master/users/views.py#L118)
  </div>
</details>


## 6. 회고 느낀점
* 장고 템플릿을 사용한점이 편리했는데 백엔드의 자료를 손쉽게 html에 띄워줄 수 있다는 점이 좋았습니다.
* 장고를 처음 사용하게 되었는데 반복해서 구현해야 하는 부분들이 이미 만들어져 있어서 좋았습니다.
 * 로그인 / 회원가입 / 인증 등
* 또한 장고는 models.py, views.py 와 같이 파일이 역할별로 구분되어있어서 잘 정리되고 체계적으로 프로그램을 만들 수 있다는 점이 좋았습니다.
* 앞으로 장고를 더 많이 다루게 되고 사용하게 된다고 했는데 잘 익혀 보고 싶다.
