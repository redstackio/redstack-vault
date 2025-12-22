---
id: cmd-uuid-9
data: 'echo ''{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":true}'' | base64 -w0'
tags:
  - encoding
type: command
output: >-
  eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjp0cnVlfQo=
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:55.438Z'
verified: false
validated: true
submitted: true
---
# Base64 Encode Admin Cookie

## Command

```bash
echo '{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":true}' | base64 -w0
```

## Description

Encodes modified JSON cookie for admin privilege.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -w0 | No wrap | No |
| Input | JSON string | Yes |

## Examples

### Basic Usage

```bash
echo 'json' | base64 -w0
```

## Expected Output

Base64 string.

## Related

- [[procedures/Brute-Force-Credentials-and-Manipulate-Base64-Cookie]]
