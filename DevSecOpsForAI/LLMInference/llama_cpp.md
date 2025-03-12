
# text model API

http://localhost:8080/v1/chat/completions


```
import requests

BASE_URL = 'http://localhost:8080'
chat_url = BASE_URL + '/v1/chat/completions'
headers =  {'Content-Type': 'application/json', 
            'Accept': 'application/json', 
    'Authorization': 'Bearer no-key'
}

data = {
    "model": "llama3.1:8b",
    "messages": [
        {
            "role": "user",
            "content": "你的身份是微博的资深评论段子手，结合如下评论指南和博文信息，如何在15个字以内趣味评论该博文且有对话感？\n\n**评论指南**\n1.结合微博内容(content)、类型(blog_type)、配图(image)、领域(tagname)、性别(gender)构建评论内容，确保评论和博文、配图主题一致\n2.保持评论友好和积极，提供情绪价值\n3.评论要**真实且让人有互动的欲望**，**适度幽默有梗**\n4.**严禁发布带色情、涉政的敏感内容**\n5.不要提及特定身份和角色，不要提及“博主” \n\n**博文信息**：{\"content\": \"世界上最疼我的两个人，\\n我最爱的姥姥和奶奶，\\n已经离开我四年了，\\n您们在那边过得还好吗？[泪] ​\", \"blog_type\": \"picture\", \"gender\": \"男\", \"tagname\": \"情感\", \"author_nick\": \"破厂皮老师\", \"author_description\": \"\", \"author_region\": \"发布于 内蒙古\", \"image caption\": \"这张图片由两张照片拼接而成。左边的照片中，一位老人和一位年轻人坐在沙发上，老人双手托着脸颊，显得有些疲惫或沉思。老人穿着深色的衣服，头发花白，脸上有明显的皱纹和斑点。年轻人穿着蓝色的上衣，戴着眼镜，表情平静。沙发上有花纹的靠垫，背景是白色的墙壁。\n\n右边的照片中，同样的老人和年轻人坐在一起，但他们的表情和姿势有所不同。老人穿着红色的衣服，戴着眼镜，表情温和，似乎在微笑。年轻人穿着蓝色的上衣，戴着眼镜，表情自然，似乎在微笑。背景是白色的墙壁，光线明亮。\n\n两张照片的拼接使得整体看起来像是经过编辑处理的，但两张照片中的场景和人物表情都显得自然和谐。\"}"
        }
    ]
}

response = requests.post(chat_url, headers=headers, json=data)
print(response.choices[0].message.content)




import base64
from openai import OpenAI

client = OpenAI(
    base_url = 'http://localhost:8080/v1',
    api_key = 'llamacpp',  # 乱写的
)

response = client.chat.completions.create(
    model = "DeepSeek-R1-UD-Q2_K_XL",
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "你的身份是微博的资深评论段子手，结合如下评论指南和博文信息，如何在15个字以内趣味评论该博文且有对话感？\n\n**评论指南**\n1.结合微博内容(content)、类型(blog_type)、配图(image)、领域(tagname)、性别(gender)构建评论内容，确保评论和博文、配图主题一致\n2.保持评论友好和积极，提供情绪价值\n3.评论要**真实且让人有互动的欲望**，**适度幽默有梗**\n4.**严禁发布带色情、涉政的敏感内容**\n5.不要提及特定身份和角色，不要提及“博主” \n\n**博文信息**：{\"content\": \"世界上最疼我的两个人，\\n我最爱的姥姥和奶奶，\\n已经离开我四年了，\\n您们在那边过得还好吗？[泪] ​\", \"blog_type\": \"picture\", \"gender\": \"男\", \"tagname\": \"情感\", \"author_nick\": \"破厂皮老师\", \"author_description\": \"\", \"author_region\": \"发布于 内蒙古\", \"image caption\": \"这张图片由两张照片拼接而成。左边的照片中，一位老人和一位年轻人坐在沙发上，老人双手托着脸颊，显得有些疲惫或沉思。老人穿着深色的衣服，头发花白，脸上有明显的皱纹和斑点。年轻人穿着蓝色的上衣，戴着眼镜，表情平静。沙发上有花纹的靠垫，背景是白色的墙壁。\n\n右边的照片中，同样的老人和年轻人坐在一起，但他们的表情和姿势有所不同。老人穿着红色的衣服，戴着眼镜，表情温和，似乎在微笑。年轻人穿着蓝色的上衣，戴着眼镜，表情自然，似乎在微笑。背景是白色的墙壁，光线明亮。\n\n两张照片的拼接使得整体看起来像是经过编辑处理的，但两张照片中的场景和人物表情都显得自然和谐。\"}"
                }
            ],
        }
    ]
)

print(response.choices[0].message.content)
```



# arguments

https://github.com/ggerganov/llama.cpp/blob/master/examples/server/README.md