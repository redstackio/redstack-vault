---
id: cmd-uuid-002
data: 'echo "banner_string" | grep -oP ''OpenSSH_\K[^ ]+'''
tags:
  - parsing
  - reconnaissance
type: command
output: 5.5p1
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:55.783Z'
verified: false
validated: true
submitted: true
---
# grep-version-parse

## Command

```bash
echo "banner_string" | grep -oP 'OpenSSH_\K[^ ]+'
```

## Description

This command parses an SSH banner string using grep with Perl-compatible regex to extract the OpenSSH version number, aiding in vulnerability assessment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `banner_string` | The full banner output from SSH connection | Yes |
| `-oP` | Output only the match with PCRE | Yes |
| `'OpenSSH_\K[^ ]+'` | Regex to capture version after 'OpenSSH_' | Yes |

## Examples

### Basic Usage

```bash
echo "SSH-2.0-OpenSSH_5.5p1 Debian-6+squeeze5" | grep -oP 'OpenSSH_\K[^ ]+'
```

### Advanced Usage

```bash
nc target 22 | head -1 | grep -oP 'OpenSSH_\K[^ ]+'
```

## Expected Output

Extracted version, e.g., "5.5p1", which can be compared to CVE thresholds.

## Related

- [[Related Procedure|Gather-SSH-Server-Version-via-Banner-Grabbing]]
- [[Related Command|netcat-banner-grab]]
