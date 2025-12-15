---
id: cmd-getcap-node
data: getcap /usr/bin/node
tags:
  - capabilities
  - verification
type: command
output: /usr/bin/node = cap_net_bind_service+eip
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.344Z'
verified: false
validated: true
submitted: true
---
# getcap-check-capabilities

## Command

```bash
getcap /usr/bin/node
```

## Description

This command queries the Linux capabilities applied to the Node.js binary, useful for verifying configurations in privilege escalation vulnerability assessments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/usr/bin/node` | Path to the executable to check | Yes |

## Examples

### Basic Usage

```bash
getcap /usr/bin/node
```

### Advanced Usage

```bash
getcap -v /usr/bin/node
```

## Expected Output

`/usr/bin/node = cap_net_bind_service+eip` or similar, listing applied capabilities.

## Related

- [[commands/setcap-configure-capabilities]]
- [[procedures/Configure-Node.js-with-Linux-Capabilities]]
