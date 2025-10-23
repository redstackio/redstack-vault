---
id: 4baee421-8af2-47ae-b0b0-a81e9f1d32ab
name: Scan Github Organization for Secrets using TruffleHog with API Token
type: command
executor: bash
data: trufflehog github --endpoint https://api.github.com --org trufflesecurity --token
  GITHUB_TOKEN --debug --concurrency 2
output: null
created_at: '2023-04-06T03:55:53.003050+00:00'
updated_at: '2023-04-06T03:55:53.014675+00:00'
---

# Scan Github Organization for Secrets using TruffleHog with API Token

```bash
trufflehog github --endpoint https://api.github.com --org trufflesecurity --token GITHUB_TOKEN --debug --concurrency 2
```


