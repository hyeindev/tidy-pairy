# Tidy Pairy

냉장고 식재료 관리 애플리케이션입니다.
냉장고 사진을 촬영하면 AI가 자동으로 식재료를 인식하여 목록으로 관리할 수 있습니다.

## 프로젝트 구조

```
tidy_pairy/
├── frontend/    # Flutter 모바일 앱
└── backend/     # FastAPI 서버
```

## 기술 스택

### Frontend
- Flutter 3.x
- Dart
- Dio (HTTP 클라이언트)
- Image Picker

### Backend
- Python 3.11+
- FastAPI
- OpenAI GPT-4o-mini Vision API

## 시작하기

### 사전 요구사항

- Python 3.11 이상
- Flutter SDK 3.x 이상
- OpenAI API Key

### Backend 실행

1. backend 디렉토리로 이동
```bash
cd backend
```

2. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. 의존성 설치
```bash
pip install fastapi uvicorn python-dotenv openai python-multipart
```

4. 환경변수 설정

`.env` 파일 생성:
```
OPENAI_API_KEY=your-openai-api-key
```

5. 서버 실행
```bash
# 로컬에서만 접근
uvicorn main:app --reload

# 같은 네트워크의 모바일 기기에서 접근 가능하게 하려면
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

서버가 실행되면:
- API 서버: http://localhost:8000
- API 문서 (Swagger): http://localhost:8000/docs

### Frontend 실행

1. frontend 디렉토리로 이동
```bash
cd frontend
```

2. 의존성 설치
```bash
flutter pub get
```

3. 백엔드 서버 주소 설정

`lib/main.dart` 파일에서 API 서버 주소를 수정합니다:
```dart
final response = await dio.post(
  'http://<YOUR_IP>:8000/analyze',  // 본인의 IP 주소로 변경
  data: formData,
);
```

4. 앱 실행
```bash
# 연결된 디바이스 확인
flutter devices

# 앱 실행
flutter run

# 특정 플랫폼으로 실행
flutter run -d chrome    # 웹
flutter run -d macos     # macOS
flutter run -d ios       # iOS 시뮬레이터
flutter run -d android   # Android 에뮬레이터
```

## API

### POST /analyze

냉장고 이미지를 분석하여 식재료 목록을 반환합니다.

**Request**
- Content-Type: `multipart/form-data`
- Body: `image` (파일)

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
      "name": "계란",
      "category": "기타",
      "count": 10,
      "location": "냉장고 문 쪽 중단"
    }
  ]
}
```

**카테고리 종류**
- 과일
- 야채
- 유제품
- 육류
- 음료
- 조미료
- 기타

## 라이선스

MIT License
