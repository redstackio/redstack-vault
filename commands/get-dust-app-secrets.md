---
id: cmd-uuid-1
data: >-
  curl -X GET "https://dust.tt/api/w/[workspace_id]/dust_app_secrets" -H
  "Cookie: [appSession]"
tags:
  - discovery
  - api-enumeration
type: command
output: >-
  {"secrets":
  [{"id":"123","name":"API_KEY","value":"•••••••","created_at":"2023-01-01T00:00:00Z"}]}
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:46.828Z'
verified: false
validated: true
submitted: true
---
---

# get-dust-app-secrets

## Command

```bash
curl -X GET "https://dust.tt/api/w/[workspace_id]/dust_app_secrets" -H "Cookie: [appSession]"
```

## Description

This command retrieves a list of all secrets in a Dust workspace via the unprotected GET endpoint, exposing secret names to Builder users for discovery purposes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| workspace_id | The ID of the target workspace in the URL path | Yes |
| appSession | Valid session cookie for authenticated Builder access | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://dust.tt/api/w/ws_abc123/dust_app_secrets" -H "Cookie: appSession=eyJ..."
```

### Advanced Usage

```bash
curl -X GET "https://dust.tt/api/w/[workspace_id]/dust_app_secrets" -H "Cookie: [appSession]" | jq '.secrets[] | {name, created_at}'
```

## Expected Output

JSON object with a 'secrets' array, each item containing id, name, masked value (•••••••), and created_at timestamp. No errors if access is granted.

## Related

- [[Related Procedure: Enumerate-Secret-Names-as-Builder-User]]
- [[commands/post-dust-app-secrets]]
