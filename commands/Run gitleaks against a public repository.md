---
id: 9ad3cba9-b022-49be-aeed-5df6e7cae905
name: Run gitleaks against a public repository
type: command
executor: bash
data: docker run --rm --name=gitleaks zricethezav/gitleaks -v -r https://github.com/zricethezav/gitleaks.git
output: null
created_at: '2023-04-06T03:56:00.200118+00:00'
updated_at: '2023-04-10T20:33:56.272566+00:00'
---

# Run gitleaks against a public repository

```bash
docker run --rm --name=gitleaks zricethezav/gitleaks -v -r https://github.com/zricethezav/gitleaks.git
```
