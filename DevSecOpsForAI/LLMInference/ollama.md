run ollama:

```shell

# customize the model directories
export OLLAMA_MODELS=/home/llm/.ollama/models

# use 0.0.0.0 rather than localhost, otherwise other device in same LAN cant access it
OLLAMA_HOST=0.0.0.0 OLLAMA_ORIGINS=* ollama serve

# show the prompt in log
OLLAMA_DEBUG="1" OLLAMA_HOST=0.0.0.0 OLLAMA_ORIGINS=* ollama serve
```

now, the path of models is located in: /usr/share/ollama/.ollama/models

PS: all args in 'ollama serve':

```go
    envVars["OLLAMA_DEBUG"],
    envVars["OLLAMA_HOST"],
    envVars["OLLAMA_KEEP_ALIVE"],
    envVars["OLLAMA_MAX_LOADED_MODELS"],
    envVars["OLLAMA_MAX_QUEUE"],
    envVars["OLLAMA_MODELS"],
    envVars["OLLAMA_NUM_PARALLEL"],
    envVars["OLLAMA_NOPRUNE"],
    envVars["OLLAMA_ORIGINS"],
    envVars["OLLAMA_TMPDIR"],
    envVars["OLLAMA_FLASH_ATTENTION"],
    envVars["OLLAMA_LLM_LIBRARY"],
    envVars["OLLAMA_MAX_VRAM"],

```

# update ollama

sudo vim /etc/systemd/system/ollama.service

sudo systemctl daemon-reload

sudo systemctl restart ollama

# stop ollama:

```shell
sudo systemctl stop ollama.service

```

show models:

```shell
ollama list
```

# update client

update ollama (when run some latest models but get error):

first stop the ollama

```shell
# pre-release
curl https://ollama.com/install.sh | sed 's#https://ollama.com/download#https://github.com/jmorganca/ollama/releases/download/v0.2.6#' | sh
curl -fsSL https://ollama.com/install.sh | sh
```

access by OPENAI-Compatible API:

# stream API

POST method:

```shell
# the model here is llama3
curl http://localhost:11434/api/generate -d '{
  "model": "llama3",
  "prompt": "Why is the sky blue?"
}'
```

# not-stream API

POST method:

```shell
# the model here is llama3
curl http://localhost:11434/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "llama3",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Hello!"
            }
        ]
    }'
```

compatible for other library:

```shell
$ export OPENAI_API_BASE='http://localhost:11434/v1'
$ export OPENAI_API_KEY='ollama'

# with aider
$ docker run -it --volume $(pwd):/app paulgauthier/aider --openai-api-key $OPENAI_API_KEY
```

# Vision model API

use the vision model:

- in cli:

```
$ ollama run llava-llama3:8b-v1.1-fp16
>>> extract text from img and notice keep indent and newline: ./Downloads/github-img-8.png
Added image './Downloads/github-img-8.png'
demo package

Module contents
------------------

class demo . foo ("a" class demo_base) : object Some headers line Variables: Somevar - some text some detailed 
docstring demo .Somevar = j Documentation for this variable
```

- in python client (need ollama version >= 0.2.6)

```python
import base64
from openai import OpenAI


def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')


client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key = 'ollama',  # required, but unused
)

base64_image = encode_image("/home/llm/Downloads/github-img-8.png")

response = client.chat.completions.create(
    model = "llava-llama3:8b-v1.1-fp16",
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "extract text from img and notice keep indent and newline"
                },
                {
                  "type": "image_url",
                  "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}",
                  },
                }
            ],
        }
    ]
)

print(response.choices[0].message.content)
```

# the model files location

~/.ollama/models

or

/usr/share/ollama/.ollama/models

# template


we can see template of models in ollama: eg: https://ollama.com/library/llama3.1:latest/blobs/11ce4ee3e170


# backend

llama.cpp

# frontend

## NextChat

![image](_imgs/next-chat.png)
