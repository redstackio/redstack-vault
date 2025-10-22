---
id: 4fbf68db-6838-47ea-9bd7-b603446fbcf5
name: Scan Github Repo for Secrets using TruffleHog
type: command
executor: bash
data: docker run -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --repo
  https://github.com/trufflesecurity/test_keys
output: null
created_at: '2023-04-06T03:55:53.002936+00:00'
updated_at: '2023-04-06T03:55:53.014429+00:00'
---

# Scan Github Repo for Secrets using TruffleHog

```bash
docker run -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --repo https://github.com/trufflesecurity/test_keys
```
