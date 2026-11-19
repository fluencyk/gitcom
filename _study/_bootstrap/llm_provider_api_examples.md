# LLM Provider API Examples

> GitCom R1 · API syntax comparison · 2026-11-17  
> Purpose: compare seven providers' minimal Python invocation patterns before designing a thin Router.

## Scope and conventions

- The examples are **independent snippets**, not a single executable program.
- All keys are read from environment variables; never commit actual credentials.
- Except for Gemini's native-SDK example, snippets use the `openai` Python package and its Chat Completions interface.
- Model availability, account permissions, geographic restrictions, and provider-specific parameters must be verified before execution.
- The **DeepSeek** pattern has been verified locally for GitCom R1; the other six are illustrative and have not been tested in this environment.
- Each example assumes the same prompt:

```python
prompt = "Reply with exactly: GITCOM_R1_OK"
```

---

## 1. OpenAI — native OpenAI SDK

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
)

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role": "user", "content": prompt}],
)

print(response.choices[0].message.content)
```

**Observation:** `base_url` is omitted; the SDK uses its OpenAI default. This example uses Chat Completions for comparison, although OpenAI also offers the Responses API.

---

## 2. DeepSeek — OpenAI-compatible API

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com",
)

response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[{"role": "user", "content": prompt}],
)

print(response.choices[0].message.content)
```

**Observation:** The client syntax is the same as OpenAI's; `base_url`, API key, and model select DeepSeek. This invocation pattern was successfully tested in GitCom R1.

---

## 3. Gemini — native Google Gen AI SDK

```python
import os
from google import genai

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"],
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)

print(response.text)
```

**Observation:** The native Gemini method is `models.generate_content`, not `chat.completions.create`. Gemini also has an OpenAI-compatible endpoint, but this example deliberately shows the native syntax.

---

## 4. Grok (xAI) — OpenAI-compatible API

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["XAI_API_KEY"],
    base_url="https://api.x.ai/v1",
)

response = client.chat.completions.create(
    model="grok-4-1-fast-reasoning",
    messages=[{"role": "user", "content": prompt}],
)

print(response.choices[0].message.content)
```

**Observation:** Same Python call shape; xAI-specific endpoint and model. Confirm model availability in the account before running.

---

## 5. Doubao Ark — Volcengine OpenAI-compatible API

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["ARK_API_KEY"],
    base_url="https://ark.cn-beijing.volces.com/api/v3",
)

response = client.chat.completions.create(
    model=os.environ["ARK_MODEL_ID"],
    messages=[{"role": "user", "content": prompt}],
)

print(response.choices[0].message.content)
```

**Observation:** `ARK_MODEL_ID` must refer to a model identifier or inference endpoint available to the account; it is not necessarily the consumer-app product name.

---

## 6. Kimi (Moonshot) — OpenAI-compatible API

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["MOONSHOT_API_KEY"],
    base_url="https://api.moonshot.ai/v1",
)

response = client.chat.completions.create(
    model=os.environ["MOONSHOT_MODEL"],
    messages=[{"role": "user", "content": prompt}],
)

print(response.choices[0].message.content)
```

**Observation:** The example uses the international Moonshot endpoint. Check the appropriate endpoint for the account and region, and set an available model ID.

---

## 7. Qwen — Alibaba Cloud Model Studio / DashScope

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["DASHSCOPE_API_KEY"],
    base_url=os.environ["QWEN_BASE_URL"],
)

response = client.chat.completions.create(
    model=os.environ["QWEN_MODEL"],
    messages=[{"role": "user", "content": prompt}],
)

print(response.choices[0].message.content)
```

**Observation:** Qwen's OpenAI-compatible endpoint varies by deployment region. Set `QWEN_BASE_URL` to the corresponding regional compatible-mode endpoint, and use a matching API key and model.

---

## Cross-provider comparison

| Provider | Python client | Explicit `base_url`? | Invocation | Model selection |
|---|---|---|---|---|
| OpenAI | `openai.OpenAI` | No (SDK default) | `chat.completions.create` | Literal or configured ID |
| DeepSeek | `openai.OpenAI` | Yes | `chat.completions.create` | `deepseek-flash` in tested example |
| Gemini | `google.genai.Client` | No (native SDK) | `models.generate_content` | Gemini model ID |
| Grok | `openai.OpenAI` | Yes | `chat.completions.create` | xAI model ID |
| Doubao Ark | `openai.OpenAI` | Yes | `chat.completions.create` | Account model/endpoint ID |
| Kimi | `openai.OpenAI` | Yes | `chat.completions.create` | Account model ID |
| Qwen | `openai.OpenAI` | Yes, from environment | `chat.completions.create` | Account model ID |

## Minimal abstraction observations (not a Router design)

1. **Provider identity is not SDK identity.** One Python SDK can target multiple remote providers.
2. **An omitted `base_url` is not an absent endpoint.** Native clients may supply their own defaults.
3. **Common call syntax does not guarantee identical semantics.** Reasoning modes, tool calls, JSON output, and usage fields may differ.
4. **Configuration and invocation are distinguishable.** `api_key`, `base_url`, and `model` identify how/where to call; `messages` or `contents` express the request.
5. **A minimal shared inference operation is plausible**, but its exact contract remains an open design question for GitCom R1.

## Official documentation entry points

- OpenAI: https://platform.openai.com/docs/api-reference/chat
- DeepSeek: https://api-docs.deepseek.com/
- Gemini: https://ai.google.dev/gemini-api/docs
- xAI: https://docs.x.ai/
- Volcengine Ark: https://www.volcengine.com/docs/82379
- Moonshot: https://platform.moonshot.ai/docs
- Alibaba Cloud Model Studio: https://www.alibabacloud.com/help/en/model-studio/
