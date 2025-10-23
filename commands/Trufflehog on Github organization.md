---
id: 3c3cf251-7f1a-49fd-acaa-eb6cf108a777
name: Trufflehog on Github organization
type: command
executor: bash
data: docker run -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --org=trufflesecurity
output: null
created_at: '2023-04-06T03:55:52.060243+00:00'
updated_at: '2023-04-06T03:55:52.080901+00:00'
---

# Trufflehog on Github organization

```bash
docker run -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --org=trufflesecurity
```


