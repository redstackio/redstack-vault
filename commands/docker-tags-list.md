---
data: >-
  curl -X GET 'https://TARGET_IP/v2/NAMESPACE/REPO/tags/list' -H 'Host:
  TARGET_IP' -H 'Accept: */*'
tags:
  - docker
  - tags
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:30.917Z'
id: 08f7d941-ec8a-4cee-9305-23e3c5e7d082
verified: false
validated: true
submitted: true
---
# docker-tags-list

## Command

```bash
curl -X GET 'https://TARGET_IP/v2/NAMESPACE/REPO/tags/list' -H 'Host: TARGET_IP' -H 'Accept: */*'
```

## Description

Lists tags for a Docker repository in an unauthenticated registry.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| NAMESPACE/REPO | Repository path | Yes |
| TARGET_IP | Registry host | Yes |

## Examples

### Basic Usage

```bash
curl https://example.com/v2/ns/repo/tags/list
```

### Advanced Usage

```bash
curl -s https://TARGET_IP/v2/ns/repo/tags/list | jq '.tags[]'
```

## Expected Output

JSON: {"tags":["3.0.1","latest"]}.

## Related

- [[Related Procedure: List-Tags-for-Docker-Repository]]
