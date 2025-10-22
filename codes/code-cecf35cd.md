---
id: cecf35cd-5e74-434f-b656-828af8814a01
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:55:52.060073+00:00'
updated_at: '2023-04-06T03:55:52.080707+00:00'
---

# Code Snippet cecf35cd

**Language**: ps1

```ps1
docker run -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --repo https://github.com/trufflesecurity/test_keys
docker run -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --org=trufflesecurity
trufflehog git https://github.com/trufflesecurity/trufflehog.git
trufflehog github --endpoint https://api.github.com --org trufflesecurity --token GITHUB_TOKEN --debug --concurrency 2
```
