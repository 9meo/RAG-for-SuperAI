import requests
import json




def send_api(prompt,
             url ='http://127.0.0.1:8080/completion',
             temp = 0.7,
             n_predict= 512,
            ):
    payload = json.dumps({
    "prompt": f'''<s>[INST] <<SYS>>
    You are a question answering assistant. Answer the question as truthful and helpful as possible
    คุณคือผู้ช่วยตอบคำถาม จงตอบคำถามอย่างถูกต้องและมีประโยชน์ที่สุด<</SYS>>

    Answer the question based only on the following context:
    {prompt}

    [/INST]''',
    "n_predict": n_predict,
    'temperature': temp,
    "stop": ["</s>"]
    })

    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()