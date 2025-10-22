---
id: 4afb5099-47d8-44ef-92dc-ca9bf9681d69
name: Trufflehog on Github repo
type: command
executor: bash
data: docker run -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --repo
  https://github.com/trufflesecurity/test_keys
output: null
created_at: '2023-04-06T03:55:52.060230+00:00'
updated_at: '2023-04-06T03:55:52.080809+00:00'
---

# Trufflehog on Github repo

```bash
docker run -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --repo https://github.com/trufflesecurity/test_keys
```
