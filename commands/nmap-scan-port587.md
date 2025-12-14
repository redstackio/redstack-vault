---
data: nmap 50.30.33.235 -p 587
tags:
  - port-scan
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:11.040Z'
id: a624a631-9d45-4300-9865-b0c8a452b4e8
verified: false
validated: true
submitted: true
---
# nmap-scan-port587

## Command

```bash
nmap 50.30.33.235 -p 587
```

## Description

Scans a specific port on the target IP to check SMTP service status.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p | Port to scan | Yes |
| target | IP/hostname | Yes |

## Examples

### Basic Usage

```bash
nmap target -p 587
```

### Advanced Usage

```bash
nmap target -p 587 -sV
```

## Expected Output

"587/tcp open submission" if available.

## Related

- [[procedures/Verify-SMTP-Port-Availability-with-Nmap]]
- [[commands/sslyze-analyze-smtp]]
