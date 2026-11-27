import json
import urllib.request

API_BASE = "http://127.0.0.1:3001/v1"
API_KEY = "freellmapi-8aa2aa9beea85ea2f4eea4c21ae0b97e4fb460521fa7fd77"

def chat_test(model_name, prompt):
    print(f"\n[TESTING FREELLMAPI MODEL: {model_name}]")
    payload = {
        "model": model_name,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{API_BASE}/chat/completions",
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=25) as resp:
            res_json = json.loads(resp.read().decode("utf-8"))
            choice = res_json["choices"][0]
            content = choice["message"]["content"].strip()
            reasoning = choice["message"].get("reasoning", "")
            routed_via = res_json.get("_routed_via", {})
            tokens = res_json.get("usage", {})
            print(f"-> Phản hồi: {content}")
            if reasoning:
                print(f"-> Suy luận (Thinking): {reasoning[:120]}...")
            print(f"-> Nhà mạng tự động định tuyến (_routed_via): {routed_via}")
            print(f"-> Usage Tokens: {tokens}")
            return True
    except Exception as e:
        print(f"-> Lỗi: {e}")
        return False

if __name__ == "__main__":
    print("=== TEST KẾT NỐI FREELLMAPI GATEWAY (PORT 3001) ===")
    chat_test("auto", "1 + 1 bằng mấy?")
    chat_test("auto", "Giới thiệu ngắn gọn 1 câu về năng lực của bạn bằng tiếng Việt.")
