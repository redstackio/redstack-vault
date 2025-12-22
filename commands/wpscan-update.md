---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
data: wpscan --update
tags:
  - maintenance
  - wordpress
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:27:49.752Z'
verified: false
validated: true
submitted: true
---
# wpscan-update

## Command

```bash
wpscan --update
```

## Description

Updates the WPScan vulnerability database to ensure scans use the latest known issues.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--update` | Trigger database update | Yes |

## Examples

### Basic Usage

```bash
wpscan --update
```

### Advanced Usage

N/A

## Expected Output

'[+] WPScan database updated successfully' or progress bars showing download completion.

## Related

- [[Related Procedure: Scan-WordPress-Site-for-Vulnerabilities-Using-WPScan]]
