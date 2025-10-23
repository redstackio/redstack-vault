---
id: 4a9bbb14-13b6-4ab6-80aa-5efa52ef14c7
name: Scan GitHub repository for secrets using TruffleHog
type: command
executor: bash
data: docker run -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --repo
  https://github.com/trufflesecurity/test_keys
output: null
created_at: '2023-04-06T03:55:50.999239+00:00'
updated_at: '2023-04-10T20:21:07.107069+00:00'
---

# Scan GitHub repository for secrets using TruffleHog

```bash
docker run -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --repo https://github.com/trufflesecurity/test_keys
```


