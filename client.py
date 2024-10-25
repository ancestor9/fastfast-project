import requests
response = requests.get("http://127.0.0.1:8000/hi")
response = requests.get("http://127.0.0.1:8000")

import httpx
response = httpx.get("http://127.0.0.1:8000/hi")
response = httpx.get("http://127.0.0.1:8000")

print(response.json)
print(response.json())

# 서버로부터 받은 응답의 Response 객체 형태를 확인하려면, 
# Python의 requests 라이브러리에서 제공하는 다양한 속성들을 사용하여 응답에 대한 여러 정보를 출력해 볼 수 있습니다. 
# 여기서 Response 객체의 주요 속성들을 활용하면 응답의 상태 코드, 본문, 헤더, URL 등을 확인할 수 있습니다.
# Response 객체의 다양한 속성들을 출력하여 확인합니다.

print("응답 상태 코드:", response.status_code)  # HTTP 상태 코드 (예: 200, 404)
print("응답 헤더:", response.headers)          # 응답 헤더
print("응답 본문:", response.text)              # 응답의 텍스트 형태 (보통 HTML 또는 JSON)
print("응답 JSON:", response.json())            # 응답이 JSON 형식인 경우, Python 딕셔너리로 변환
print("응답 URL:", response.url)                # 요청이 보내진 URL

# Response 객체 자체를 출력해도 객체에 대한 정보가 나옵니다.
print("Response 객체:", response)