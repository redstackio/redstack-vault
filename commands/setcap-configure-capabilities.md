---
id: cmd-setcap-node
data: sudo setcap 'cap_net_bind_service=+ep' /usr/bin/node
tags:
  - capabilities
  - privileges
type: command
output: /usr/bin/node = cap_net_bind_service+eip
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.346Z'
verified: false
validated: true
submitted: true
---
# setcap-configure-capabilities

## Command

```bash
sudo setcap 'cap_net_bind_service=+ep' /usr/bin/node
```

## Description

This command applies the CAP_NET_BIND_SERVICE Linux capability to the Node.js binary, allowing it to perform privileged operations like binding to ports below 1024 without full root privileges. Use this in vulnerability testing setups for Node.js on Linux.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `cap_net_bind_service=+ep` | Specifies the capability (network bind service) with effective (e) and permitted (p) inheritance | Yes |
| `/usr/bin/node` | Path to the Node.js executable | Yes |

## Examples

### Basic Usage

```bash
sudo setcap 'cap_net_bind_service=+ep' /usr/bin/node
```

### Advanced Usage

```bash
sudo setcap 'cap_net_bind_service,cap_sys_admin=+ep' /usr/bin/node
```

## Expected Output

No output on success; the binary gains the specified capabilities, verifiable with getcap.

## Related

- [[commands/getcap-check-capabilities]]
- [[procedures/Configure-Node.js-with-Linux-Capabilities]]
