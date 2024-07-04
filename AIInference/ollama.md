run ollama:
```shell
# use 0.0.0.0 rather than localhost, otherwise other device in same LAN cant access it
OLLAMA_HOST=0.0.0.0 OLLAMA_ORIGINS=* ollama serve
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
