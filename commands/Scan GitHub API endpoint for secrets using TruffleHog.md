---
id: b891a8ee-5ab3-473a-ba14-dc5ed3bbe477
name: Scan GitHub API endpoint for secrets using TruffleHog
type: command
executor: bash
data: trufflehog github --endpoint https://api.github.com --org trufflesecurity --token
  GITHUB_TOKEN --debug --concurrency 2
output: null
created_at: '2023-04-06T03:55:51.007202+00:00'
updated_at: '2023-04-10T20:21:07.107069+00:00'
---

# Scan GitHub API endpoint for secrets using TruffleHog

```bash
trufflehog github --endpoint https://api.github.com --org trufflesecurity --token GITHUB_TOKEN --debug --concurrency 2
```
