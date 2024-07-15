run ollama:

```shell

# use 0.0.0.0 rather than localhost, otherwise other device in same LAN cant access it
OLLAMA_HOST=0.0.0.0 OLLAMA_ORIGINS=* ollama serve

# show the prompt in log
OLLAMA_DEBUG="1" OLLAMA_HOST=0.0.0.0 OLLAMA_ORIGINS=* ollama serve
```


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




stop ollama:

```shell
sudo systemctl stop ollama.service

```

show models:

```shell
ollama list
```

update ollama (when run some latest models but get error):

```shell
curl https://ollama.ai/install.sh | sh
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
