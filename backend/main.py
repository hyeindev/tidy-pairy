import os
import base64
import json

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
print("🔍 ENV INIT:", os.getenv("OPENAI_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_client():
    key = os.getenv("OPENAI_API_KEY")
    print("🔑 Loaded Key In Request:", key)
    return OpenAI(api_key=key)


@app.post("/analyze")
async def analyze_image(image: UploadFile = File(...)):
    client = get_client()     # ★★★ 반드시 필요!!

    # 파일 읽기
    content = await image.read()

    # Vision용 base64 변환
    b64_image = base64.b64encode(content).decode("utf-8")

    # Vision API 요청
    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": "너는 냉장고 내부 식재료를 분석하는 Vision Object Detection 모델이다. 첨부된 냉장고 사진을 분석하고, JSON 배열만 반환해라. "
                        "원하는 JSON 응답 필드 -> name(식재료명), category(과일/야채/유제품/육류/음료/조미료/기타), count(식품갯수/ 갯수파악 안될경우 -1), location(냉장고에서 어느위치에있는지 텍스트로 설명). "
                        #"반찬통은 별도의 식품종류 분석없이 그냥 name=반찬통, category=반찬, count=냉장고에있는모든반찬통갯수, location=냉장고 여러 곳, 이렇게 하나로 묶어서 반환해라."
                        # "인식불가해서 알수없는것들만 name=알 수 없음, category=기타, count=모든알수없는것의갯수, location=냉장고 여러 곳, 이렇게 하나로 묶어서 반환해라."

                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{b64_image}"
                    }
                ]
            }
        ]
    )

    output = response.output_text
    print("[VISION OUTPUT RAW]", output)

    # 코드블럭 제거
    clean = (
        output.replace("```json", "")
              .replace("```", "")
              .strip()
    )

    # JSON 파싱
    items = json.loads(clean)

    return {
        "filename": image.filename,
        "detected_items": items
    }