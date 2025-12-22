---
type: command
executor: bash
data: ip link show
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - network
  - recon
verified: true
validated: true
---

# List Network Interfaces

## Command

```bash
ip link show
```

## Description

This command displays all network interfaces on the system, including their states (UP/DOWN), MAC addresses, and MTU settings. Use it to identify the interface connected to the target network before launching passive tools like p0f for fingerprinting or other network attacks like spoofing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; shows all interfaces | No |

## Examples

### Basic Usage

```bash
ip link show
```

### Advanced Usage

Filter for a specific interface:

```bash
ip link show eth0
```

## Expected Output

Description of what output to expect when the command runs successfully.

Sample output:

```
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 08:00:27:12:34:56 brd ff:ff:ff:ff:ff:ff
```

Look for interfaces in "UP" state with your network's IP range.

## Related

- [[commands/p0f-passive-os-fingerprinting]]
- [[tools/p0f]]
