---
id: 7c5decbf-b31d-4dd9-90d3-80802e86ee77
name: Run gitleaks against a local repository
type: command
executor: bash
data: 'docker run --rm --name=gitleaks -v /tmp/:/code/  zricethezav/gitleaks -v --repo-path=/code/gitleaks

  '
output: null
created_at: '2023-04-06T03:56:00.200245+00:00'
updated_at: '2023-04-10T20:33:56.272566+00:00'
---

# Run gitleaks against a local repository

```bash
docker run --rm --name=gitleaks -v /tmp/:/code/  zricethezav/gitleaks -v --repo-path=/code/gitleaks

```
