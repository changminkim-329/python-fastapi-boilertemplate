


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

여담
pylint제외 이유 : 코드 표준을 준수여부를 체크하는 파이린트는
독스트링 무조건 필수적으로 작성해야하고 불필요한 에러 때문에 개발속도가 느려질 수 있음

https://kimjingo.tistory.com/203