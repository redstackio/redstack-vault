---
id: 50de325e-3382-43b1-bb3d-ed3626a6c7c6
name: Run Docker Container
type: command
executor: bash
data: docker run --name vulnerable-app -p 8080:8080 ghcr.io/christophetd/log4shell-vulnerable-app
output: null
created_at: '2023-04-06T03:55:56.831624+00:00'
updated_at: '2023-04-06T03:55:56.838440+00:00'
---

# Run Docker Container

```bash
docker run --name vulnerable-app -p 8080:8080 ghcr.io/christophetd/log4shell-vulnerable-app
```


