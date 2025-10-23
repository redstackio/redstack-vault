---
id: 5be9ab9c-7603-4913-847e-8b86f076f33a
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:55:51.004524+00:00'
updated_at: '2023-04-10T20:21:07.109645+00:00'
---

# Code Snippet 5be9ab9c

**Language**: ps1

```ps1
docker run -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --repo https://github.com/trufflesecurity/test_keys
docker run -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --org=trufflesecurity
trufflehog git https://github.com/trufflesecurity/trufflehog.git
trufflehog github --endpoint https://api.github.com --org trufflesecurity --token GITHUB_TOKEN --debug --concurrency 2
```


