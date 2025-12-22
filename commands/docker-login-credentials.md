---
type: command
executor: bash
data: docker login -u $_USERNAME -p $_PASSWORD $_REGISTRY_HOST
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - auth
  - docker
verified: true
validated: true
---

# docker-login-credentials

## Command

```bash
docker login -u $_USERNAME -p $_PASSWORD $_REGISTRY_HOST
```

## Description

Authenticates the Docker client to a private or insecure registry using basic credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | Registry username | Yes |
| $_PASSWORD | Registry password | Yes |
| $_REGISTRY_HOST | Host or URL (e.g., docker.registry.local) | Yes |

## Examples

### Default Creds

```bash
docker login -u admin -p admin docker.registry.local
```

## Expected Output

```
Login Succeeded
```

Stores creds in ~/.docker/config.json.

## Related

- [[procedures/Insecure-Docker-Registry-Pentest]]
