---
data: dig demo.greenhouse.io +trace
tags:
  - dns
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:49.353Z'
id: d0dc4040-f4e4-4f88-a6c8-536f3c1c7d05
verified: false
validated: true
submitted: true
---
# dig-full-lookup

## Command

```bash
dig demo.greenhouse.io +trace
```

## Description

This command traces the full DNS resolution path for a subdomain, useful for verifying if a CNAME chain leads to an inactive or dangling resource.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `+trace` | Enables tracing of the delegation path | Yes |
| `demo.greenhouse.io` | The target subdomain | Yes |

## Examples

### Basic Usage

```bash
dig demo.greenhouse.io +trace
```

### Advanced Usage

```bash
dig +trace @8.8.8.8 demo.greenhouse.io
```

## Expected Output

Full trace showing delegation and final resolution, e.g., ending in NXDOMAIN or error for dangling records.

## Related

- [[commands/dig-cname-lookup]]
- [[procedures/Verify-DNS-CNAME-Record]]
