---
data: >-
  curl -X GET 'https://TARGET_IP/v2/_catalog' -H 'Host: TARGET_IP' -H 'Accept:
  */*'
tags:
  - docker
  - enumeration
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:30.921Z'
id: 15ddb9f5-c844-44ba-893a-80079adb47c8
verified: false
validated: true
submitted: true
---
# docker-catalog-enumerate

## Command

```bash
curl -X GET 'https://TARGET_IP/v2/_catalog' -H 'Host: TARGET_IP' -H 'Accept: */*'
```

## Description

Enumerates repositories in a Docker Registry via the unauthenticated catalog endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| TARGET_IP | IP or domain of the registry | Yes |
| -H 'Accept: */*' | Accepts any response type | No |

## Examples

### Basic Usage

```bash
curl https://example.com/v2/_catalog
```

### Advanced Usage

```bash
curl -s https://TARGET_IP/v2/_catalog | jq .
```

## Expected Output

JSON: {"repositories":["repo1","repo2"]}. 

## Related

- [[Related Procedure: Enumerate-Repositories-in-Docker-Registry]]
