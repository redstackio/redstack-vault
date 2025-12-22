---
type: command
executor: bash
data: >-
  docker login -e $_SERVICE_EMAIL -u oauth2accesstoken -p "$_ACCESS_TOKEN"
  https://gcr.io
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - gcp
  - auth
verified: true
validated: true
---

# docker-login-gcr

## Command

```bash
docker login -e $_SERVICE_EMAIL -u oauth2accesstoken -p "$_ACCESS_TOKEN" https://gcr.io
```

## Description

Logs into Google Container Registry using service account OAuth token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SERVICE_EMAIL | Service account email | Yes |
| $_ACCESS_TOKEN | OAuth access token | Yes |
| -u oauth2accesstoken | Username for OAuth | Yes |
| https://gcr.io | GCR URL | Yes |

## Examples

### OAuth Login

```bash
docker login -e 123@gsa -u oauth2accesstoken -p "ya29..." https://gcr.io
```

## Expected Output

```
Login Succeeded
```

## Related

- [[procedures/Insecure-Docker-Registry-Pentest]]
