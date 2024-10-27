

mind the **data region** !!!   USA or EU

# quick start

references: https://docs.smith.langchain.com/

```shell
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY=<your-api-key>

# The below examples use the OpenAI API, though it's not necessary in general
export OPENAI_API_KEY=<your-openai-api-key>
```

# Alternatives: LangFuse

open source alternatives: https://github.com/langfuse/langfuse

create key in https://cloud.langfuse.com/

```shell
from langfuse import Langfuse

langfuse = Langfuse(
  secret_key="sk-lf-866b67c4-c382-4bde-a8dd-a4b55d43421a",
  public_key="pk-lf-965b63d3-32dd-474c-831d-411630cf8c63",
  host="https://cloud.langfuse.com"
)
```

https://langfuse.com/docs

other alternatives: https://www.saashub.com/langsmith-alternatives



support self-host deployment









