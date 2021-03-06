# Flask Movie API π₯
### Introduction
μν μ λͺ©, μμ , μ μ μ°λ, κ°λ, μΆμ°μ§, μ₯λ₯΄, μμ μκ°, μν κ΄λ ¨ μμ λ§ν¬, μλμμ€λ₯Ό μ κ³΅ν΄μ£Όλ REST API.  

### Dependencies

* [Python](https://www.python.org/) (Python 3.9.7 μ¬μ©. Python 3.10.Xμλ Compatability Issue.)
* [Flask](https://flask.palletsprojects.com/) - Python Framework
* [Flask-JWT](https://https://pythonhosted.org/Flask-JWT/) - μ μ  Authentication
* [SQLAlchemy](https://docs.sqlalchemy.org/) - ORM
* [Pip](https://pypi.org/project/pip/) - Dependency Management
* [RESTful](https://restfulapi.net/)

### κ°μ νκ²½ (UNIX / MacOS)

```
$ python3 -m venv venv
$ source venv/bin/activate
```
### κ°μ νκ²½ (Windows)

[μλμ° Python κ°μ νκ²½ μ€μΉ λ° μ€ν](https://docs.python.org/ko/3.9/library/venv.html)

Dependencies μ€μΉ:

```
$ pip install -r code/requirements.txt
```

### μ€ν
 
```
$ python3 code/app.py
```
### μ΄κΈ°ν
```
$ rm code/movie.db
```

### νμ€ν

νμ€νμ Postmanμ μ΄μ©ν΄μ μ§ννμ΅λλ€.

* [Postman μ€μΉ λ° μ€μ ](https://choisiel.tistory.com/14)

* [Postman νμ€ν μλν](https://heropy.blog/2020/08/31/postman-api-testing/)


### API Reference

#### User κ°μ
```http
  POST /api/v1/register
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. μμ΄λ |
| `password` | `string` | **Required**. λΉλ°λ²νΈ |

#### JWT Authentication
```http
  POST /auth
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. μμ΄λ |
| `password` | `string` | **Required**. λΉλ°λ²νΈ |

#### λͺ¨λ  μν μ λ³΄ κ°μ Έμ€κΈ°

```http
  GET /api/v1/movies
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `jwt` | `string` | **Required**. JWT** |

#### movie_idλ‘ μν μ λ³΄ κ°μ Έμ€κΈ°

```http
  GET /api/v1/movies/{movie_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `jwt` | `string` | **Required**.  JWT**|
| `movie_id`      | `integer` | **Required**. μν movie_id |

#### movie_idλ‘ μν μ λ³΄ μμ νκΈ°

```http
  PUT /api/v1/movies/{movie_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `jwt` | `string` | **Required**.  JWT**|
| `movie_id`      | `integer` | **Required**. μν movie_id |
| `title`      | `string` | **Required**. μ λͺ© |
| `year`      | `integer` | **Required**. μ μ λλ |
| `original_title`      | `string` | **Required**. μμ  |
| `genres`      | `list[string]` | **Required**. μ₯λ₯΄ |
| `running_time`      | `integer` | **Required**. μμ μκ° |
| `director`      | `string` | **Required**. κ°λ |
| `cast`      | `list[string]` | **Required**. μΆμ°μ§ |
| `movie_clips`      | `list[string]` | **Required**. κ΄λ ¨ μμ λ§ν¬ |
| `summary`      | `string` | **Required**. μλμμ€ |

#### movie_idλ‘ μν μ­μ νκΈ°

```http
  DELETE /api/v1/movies/{movie_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `jwt` | `string` | **Required**.  JWT**|
| `movie_id`      | `string` | **Required**. μν movie_id |


#### μ μνλ€ μ λ³΄ μΆκ°

```http
  POST /api/v1/movies
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `jwt` | `string` | **Required**.  JWT**|
| `movies`      | `list[dict]` | **Required**. μν μ λ³΄λ€μ΄ λ΄κΈ΄ dict |

**JWT Authentication λΉνμ±νλ₯Ό μνμλ©΄ ``` code/resources/movie.py ```μ ``` @jwt_required()```λ₯Ό λͺ¨λ μ£Όμμ²λ¦¬ν΄ μ£ΌμΈμ.
