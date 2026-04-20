# AI Feature Flag System

Dynamically route requests between different AI models/prompts using feature flags, and measure performance.

Think: \
“Which model is better?” \
“Can I safely roll out a new prompt?”\
“How do I A/B test AI in production?”

```python
Client Request
   ↓
Feature Flag Engine
   ↓
Router
   ↓
Model A / Model B
   ↓
Response Logger
   ↓
Metrics Store
```

## Repo Structure
```python
ai-feature-flag-system/
├── app/
│   ├── main.py              # FastAPI entry
│   ├── router.py            # feature flag logic
│   ├── models.py            # model implementations
│   ├── config.py            # flag config loader
│   ├── logger.py            # metrics logging
│
├── config/
│   └── flags.json           # experiment config
│
├── data/
│   └── logs.jsonl           # metrics storage
│
├── tests/
│   └── test_router.py
│
├── requirements.txt
├── train.py                 # (for MLOps simulation)
├── Dockerfile              # (later for cloud)
├── .github/workflows/ci.yml
```
