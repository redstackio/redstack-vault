---
id: 67165108-0b68-4752-b7f5-35e60b8e1cfe
name: Run gitleaks against a specific Github Pull request using Docker
type: command
executor: bash
data: docker run --rm --name=gitleaks -e GITHUB_TOKEN={your token} zricethezav/gitleaks
  --github-pr=https://github.com/owner/repo/pull/9000
output: null
created_at: '2023-04-06T03:56:00.200361+00:00'
updated_at: '2023-04-10T20:33:56.272566+00:00'
---

# Run gitleaks against a specific Github Pull request using Docker

```bash
docker run --rm --name=gitleaks -e GITHUB_TOKEN={your token} zricethezav/gitleaks --github-pr=https://github.com/owner/repo/pull/9000
```


