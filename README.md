# 티켓플레이스 Movie API
### Introduction
영화 제목, 원제, 제작 연도, 감독, 출연진, 장르, 상영 시간, 영화 관련 영상 링크, 시놉시스를 제공해주는 REST API.  

### Dependencies

* [Python](https://www.python.org/) (Python 3.9.7 사용. Python 3.10.X와는 Compatability Issue.)
* [Flask](https://flask.palletsprojects.com/) - Python Framework
* [Flask-JWT](https://https://pythonhosted.org/Flask-JWT/) - 유저 Authentication
* [SQLAlchemy](https://docs.sqlalchemy.org/) - ORM
* [Pip](https://pypi.org/project/pip/) - Dependency Management
* [RESTful](https://restfulapi.net/)

### 가상 환경 (UNIX / MacOS)

```
$ python3 -m venv venv
$ source venv/bin/activate
```
### 가상 환경 (Windows)

[윈도우 Python 가상 환경 설치 및 실행](https://docs.python.org/ko/3.9/library/venv.html)

Dependencies 설치:

```
$ pip install -r code/requirements.txt
```

### 실행
 
```
$ python3 code/app.py
```
### 초기화
```
$ rm code/movie.db
```

### 테스팅

테스팅은 Postman을 이용해서 진행했습니다.

* [Postman 설치 및 설정](https://choisiel.tistory.com/14)

* [Postman 테스팅 자동화](https://heropy.blog/2020/08/31/postman-api-testing/)


### API Reference

#### User 가입
```http
  POST /api/v1/register
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. 아이디 |
| `password` | `string` | **Required**. 비밀번호 |

#### JWT Authentication
```http
  POST /auth
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. 아이디 |
| `password` | `string` | **Required**. 비밀번호 |

#### 모든 영화 정보 가져오기

```http
  GET /api/v1/movies
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `jwt` | `string` | **Required**. JWT** |

#### movie_id로 영화 정보 가져오기

```http
  GET /api/v1/movies/{movie_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `jwt` | `string` | **Required**.  JWT**|
| `movie_id`      | `integer` | **Required**. 영화 movie_id |

```http
  PUT /api/v1/movies/{movie_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `jwt` | `string` | **Required**.  JWT**|
| `movie_id`      | `integer` | **Required**. 영화 movie_id |
| `title`      | `string` | **Required**. 제목 |
| `year`      | `integer` | **Required**. 제작 년도 |
| `original_title`      | `string` | **Required**. 원제 |
| `genres`      | `list[string]` | **Required**. 장르 |
| `running_time`      | `integer` | **Required**. 상영 시간 |
| `director`      | `string` | **Required**. 감독 |
| `cast`      | `list[string]` | **Required**. 출연진 |
| `movie_clips`      | `list[string]` | **Required**. 관련 영상 링크 |
| `summary`      | `string` | **Required**. 시놉시스 |

```http
  DELETE /api/v1/movies/{movie_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `jwt` | `string` | **Required**.  JWT**|
| `movie_id`      | `string` | **Required**. 영화 movie_id |

```http
  POST /api/v1/movies
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `jwt` | `string` | **Required**.  JWT**|
| `movies`      | `list[dict]` | **Required**. 영화 정보들이 담긴 dict |

**JWT Authentication 비활성화를 원하시면 ``` code/resources/movie.py ```에 ``` @jwt_required()```를 모두 주석처리해 주세요.
