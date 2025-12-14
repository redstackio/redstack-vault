---
id: cmd-display-interfaces
data: ifconfig
tags:
  - network
  - ipv6
type: command
output: >-
  Shows lo and venet0 interfaces with multiple IPv6 addresses like
  2a04:XXXX:0:32::1001/64, ::1010/64, etc. (SNIPped for brevity)
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.768Z'
verified: false
validated: true
submitted: true
---
# display-network-interfaces

## Command

```bash
ifconfig
```

## Description

Displays network interface configurations, including assigned IPv4 and IPv6 addresses, to verify setup for IP rotation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | N/A | No |

## Examples

### Basic Usage

```bash
ifconfig
```

### Advanced Usage

Show specific interface:

```bash
ifconfig venet0
```

## Expected Output

Shows lo and venet0 interfaces with multiple IPv6 addresses like 2a04:XXXX:0:32::1001/64, ::1010/64, etc.

## Related

- [[procedures/Verify-Network-Configuration]]
- [[procedures/Setup-VPS-with-IPv6-Addresses]]
