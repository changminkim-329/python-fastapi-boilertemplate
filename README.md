1. 할일
   poetry 가상환경 설정 및 실행
   dev 에서 사용할 라이브러리 설정 및 실행 mypy, pytest, black, isort
   git init and ignore

```

```

dev_dependencies

```
black = "^22.12.0"
pytest = "^7.2.0"
mypy = "^0.991"

```

## 폴더구조
```
api -> controller/{resource}.py
core -> core : 서비스에 꼭 필요한 정보들 토큰,환경변수,
crud -> crud/{resource}.py repo와 비슷한 느낌
db/ -> 연결하고 세션만들기
models/{resource}.py 엔티티 + base엔티티
schemas/{resource}.py 스키마들/리소스
middlewares/ -> client와 controller 
utils/ -> 날짜/s3버킷 등 담당하는 객체 또는 함수
```


## 여담
pylint제외 이유 : 코드 표준을 준수여부를 체크하는 파이린트는
독스트링 무조건 필수적으로 작성해야하고 불필요한 에러 때문에 개발속도가 느려질 수 있음

reference

- [makefile-githook](https://seonghyeon.dev/keep-python-code-clean-with-git-hook-and-makefile)
- [[Python] 코드 검사 자동화(Mypy를 사용한 타입 힌팅, Pylint를 사용한 코드 검사)](https://kimjingo.tistory.com/203)


- [fastapi 자습서에소개된 fullstack](https://github.com/tiangolo/full-stack-fastapi-postgresql/tree/master/%7B%7Bcookiecutter.project_slug%7D%7D/backend/app/app)