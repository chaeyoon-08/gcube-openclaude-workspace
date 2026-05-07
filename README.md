# Todo CLI

Python으로 만든 간단한 Todo CLI 도구입니다.

## 설치

```bash
chmod +x todo.py
```

## 사용법

### 할 일 추가

```bash
python todo.py add "할 일 내용"
```

### 할 일 목록 조회

```bash
python todo.py list
```

### 할 일 완료 처리

```bash
python todo.py done <id>
```

## 예시

```bash
$ python todo.py add "장보기"
Added: 장보기

$ python todo.py add "운동하기"
Added: 운동하기

$ python todo.py list
  [ ] 1. 장보기
  [ ] 2. 운동하기

$ python todo.py done 1
Done: 장보기

$ python todo.py list
  [✓] 1. 장보기
  [ ] 2. 운동하기
```

## 데이터 저장

모든 할 일은 `todos.json` 파일에 JSON 형식으로 저장됩니다.
