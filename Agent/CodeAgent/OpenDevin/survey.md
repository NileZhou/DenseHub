run in shell:

export WORKSPACE_BASE="/home/llm/Project/PythonProjects/workspace"

export LLM_BASE_URL="http://host.docker.internal:11434"

docker run
    -it
    --pull=always
    --add-host host.docker.internal:host-gateway
    -e SANDBOX_USER_ID=$(id -u)
    -e LLM_API_KEY="ollama"
    -e LLM_BASE_URL="http://host.docker.internal:11434"
    -e LLM_OLLAMA_BASE_URL="http://host.docker.internal:11434"
    -e WORKSPACE_MOUNT_PATH=$WORKSPACE_BASE
    -v $WORKSPACE_BASE:/opt/workspace_base
    -v /var/run/docker.sock:/var/run/docker.sock
    -p 3000:3000
    ghcr.io/opendevin/opendevin:main

# paper explained

## features

- event stream

## Insight

The author of OpenDevin was inspired by the way human using tools, and the most powerful among tools is software.

The challenges of building a software-driven agent:

- Effectively create and modify code in complex software systems
- Provide agent with tools on-the-fly to debug problems or gather task-requisite information
- Ensure that development is safe and avoids negative side effects on the users’ systems

## architecture

system architecture:
https://docs.all-hands.dev/modules/usage/architecture






```
docker run --runtime nvidia --gpus all \
  -v ~/.cache/huggingface:/root/.cache/huggingface \
  --env "HUGGING_FACE_HUB_TOKEN=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" \
  -p 8000:8000 \
  --ipc=host \
  vllm/vllm-openai:latest \
  --model hugging-quants/Meta-Llama-3.1-8B-Instruct-GPTQ-INT4
```
