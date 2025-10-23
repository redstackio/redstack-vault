---
id: 9227a6ba-0c52-4f91-8f1e-0bc5e3c8df2b
name: Run vulnerable-app container
type: command
executor: bash
data: docker run --name vulnerable-app -p 8080:8080 ghcr.io/christophetd/log4shell-vulnerable-app
output: null
created_at: '2023-04-06T03:55:56.458257+00:00'
updated_at: '2023-04-06T03:55:56.467817+00:00'
---

# Run vulnerable-app container

```bash
docker run --name vulnerable-app -p 8080:8080 ghcr.io/christophetd/log4shell-vulnerable-app
```


