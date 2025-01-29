from openai import OpenAI
import base64
import json
import time

import os
# 开启代理
# os.environ['http_proxy']='http://127.0.0.1:10808'
# os.environ['https_proxy']='http://127.0.0.1:10808'

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# 常用模型:
## 支持多模态 openai需代理
### openai/o1                           200K context,$15/M input tokens,$60/M output tokens,$21.68/K input imgs   (需代理)
### openai/gpt-4o-2024-11-20            128K context,$2.5/M input tokens,$10/M output tokens,$3.613/K input imgs  (需代理)
### google/gemini-2.0-flash-exp:free    1.05M context                                                             (需开启隐私)
### google/gemini-exp-1206:free         2.1M context                                                              (需开启隐私)
### google/gemini-flash-1.5             1M context,$0.075/M input tokens,$0.3/M output tokens,$0.04/K input imgs  (便宜)
### anthropic/claude-3.5-sonnet:beta    200K context,$3/M input tokens,$15/M output tokens,$4.8/K input imgs      (比4o贵)
### anthropic/claude-3-haiku            200K context,$0.25/M input tokens,$1.25/M output tokens,$0.4/K input imgs (便宜)

## 纯文本
### microsoft/wizardlm-2-8x22b          66K context,$0.5/M input tokens,$0.5/M output tokens                      (角色扮演nb)
### deepseek-reasoner                   64K context,$0.55/M input tokens,$2.19/M output tokens                    (R1:推理)
### deepseek-chat                       64K context,$0.14/M input tokens,$0.28/M output tokens                    (便宜)


def support_show_cot(model):
    if model in ['deepseek-reasoner']:
        return True
    return False

o_client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.environ.get("OPENROUTER_API_KEY"),
)
ds_client = OpenAI(
  base_url="https://api.deepseek.com",
  api_key=os.environ.get("DEEPSEEK_API_KEY"),
)

def get_client(model):
    if model in ['deepseek-reasoner']:
        return ds_client
    return o_client

def chat(model, prompt, img_path, log=True):
    client = get_client(model)
    start_time = time.time()
    if img_path and len(img_path.strip()) > 0: # 多模态问答
        base64_image = encode_image(img_path)
        completion = client.chat.completions.create(
            # extra_headers={
            #    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
            #    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
            # },
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ]
        )
    else: # 纯文本问答
        completion = client.chat.completions.create(
            # extra_headers={
            #     "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
            #     "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
            # },
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ]
        )

    
    # print(completion)

    if log:
        log_id = completion.id
        usage = completion.usage
        duration = "{:.2f}s".format(time.time() - start_time)
        usage_str = f"\033[92m{log_id} Prompt tokens: {usage.prompt_tokens}, Completion tokens: {usage.completion_tokens}, Total tokens: {usage.total_tokens}, duration: {duration}, Completion tokens details: {usage.completion_tokens_details}, Prompt tokens details: {usage.prompt_tokens_details}\033[0m"
        print(usage_str)
        if support_show_cot(model):
            print(f"\033[94m{completion.choices[0].message.reasoning_content}\033[0m")
    

    return completion.choices[0].message.content

if __name__ == '__main__':
    model = 'google/gemini-flash-1.5'
    prompt = '解释下这张图片'
    img_path = '/Users/zhouyi9/Pictures/Picture1.png' # 为空则为纯文本问答

    resp_text = chat(model, prompt, img_path)
    print(resp_text)


