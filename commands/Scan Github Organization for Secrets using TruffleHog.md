---
id: 6e15bcf8-e341-42d2-bf73-8f3e675cf465
name: Scan GitHub organization for secrets using TruffleHog
type: command
executor: bash
data: docker run -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --org=trufflesecurity
output: null
created_at: '2023-04-06T03:55:51.000548+00:00'
updated_at: '2023-04-10T20:21:07.107069+00:00'
---

# Scan GitHub organization for secrets using TruffleHog

```bash
docker run -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --org=trufflesecurity
```
