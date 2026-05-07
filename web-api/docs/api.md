# API 문서

## 엔드포인트

| 메서드 | 경로 | 설명 |
|--------|------|------|
| GET | /health | 서버 상태 확인 |
| GET | /todos | Todo 목록 조회 |
| POST | /todos | Todo 생성 |

## 데이터 모델

### Todo

| 필드 | 타입 | 설명 |
|------|------|------|
| id | int | 자동 생성 고유 ID |
| title | string | Todo 제목 (필수) |
| done | boolean | 완료 여부 (기본값: false) |

## 에러 응답

- `400 Bad Request` — title 누락 시 `{"error": "title is required"}`

## 제한사항

- 데이터는 메모리에 저장되므로 서버 재시작 시 초기화됩니다.
