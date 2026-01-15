# Tidy Pairy Server

냉장고 이미지를 분석하여 식재료를 자동으로 감지하는 FastAPI 서버입니다.
OpenAI GPT-4o-mini Vision API를 활용하여 냉장고 사진에서 식품을 인식하고 JSON 형태로 반환합니다.

## 기능

- 냉장고 이미지 업로드
- Vision AI를 통한 식재료 자동 감지
- 식재료별 이름, 카테고리, 수량, 위치 정보 반환

## 설치

### 1. 저장소 클론

```bash
git clone https://github.com/your-username/tidy_pairy_server.git
cd tidy_pairy_server
```

### 2. 가상환경 생성 및 활성화

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. 의존성 설치

```bash
pip install fastapi uvicorn python-dotenv openai python-multipart
```

### 4. 환경 변수 설정

프로젝트 루트에 `.env` 파일을 생성하고 OpenAI API 키를 설정합니다:

```
OPENAI_API_KEY=your-openai-api-key
```

## 실행

```bash
uvicorn main:app --reload
```

서버가 `http://localhost:8000`에서 실행됩니다.

## API

### POST /analyze

냉장고 이미지를 분석하여 식재료 목록을 반환합니다.

**Request**
- Content-Type: `multipart/form-data`
- Body: `image` (file) - 냉장고 이미지 파일

**Response**

```json
{
  "filename": "fridge.jpg",
  "detected_items": [
    {
      "name": "우유",
      "category": "유제품",
      "count": 1,
      "location": "냉장고 문 쪽 상단"
    },
    {
      "name": "사과",
      "category": "과일",
      "count": 3,
      "location": "냉장고 중간 선반"
    },
    {
      "name": "계란",
      "category": "기타",
      "count": 10,
      "location": "냉장고 문 쪽 중단"
    }
  ]
}
```

**카테고리 종류**
- 과일, 야채, 유제품, 육류, 음료, 조미료, 기타

## API 문서

서버 실행 후 아래 URL에서 Swagger UI를 통해 API를 테스트할 수 있습니다:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 기술 스택

- Python 3.14
- FastAPI
- OpenAI GPT-4o-mini Vision API
- Uvicorn
