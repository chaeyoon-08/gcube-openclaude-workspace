# Web API 프로젝트

Flask 기반 간단한 Todo 웹 API입니다.

## 설치

```bash
cd web-api
pip install -r requirements.txt
```

## 실행

```bash
python src/app.py
```

서버가 `http://127.0.0.1:5000` 에서 실행됩니다.

## 테스트

```bash
pytest
```

## API 사용법

### 헬스 체크

```
GET /health
```

**응답:**
```json
{"status": "ok"}
```

### Todo 목록 조회

```
GET /todos
```

**응답:**
```json
[
  {"id": 1, "title": "Buy milk", "done": false},
  {"id": 2, "title": "Read book", "done": false}
]
```

### Todo 생성

```
POST /todos
Content-Type: application/json

{"title": "Buy milk"}
```

**응답 (201 Created):**
```json
{"id": 1, "title": "Buy milk", "done": false}
```

`title` 필드가 누락되면 400 에러를 반환합니다.
