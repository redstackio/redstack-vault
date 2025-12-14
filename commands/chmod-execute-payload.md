---
id: 123e4567-e89b-12d3-a456-426614174007
data: chmod +x payload.sh && ./payload.sh
tags:
  - chmod
  - rce
type: command
output: |-
  RCE via Unzip
  uid=1000(user)
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.220Z'
verified: false
validated: true
submitted: true
---
---
id: 123e4567-e89b-12d3-a456-426614174007
name: chmod-execute-payload
type: command
executor: bash
data: |
  chmod +x payload.sh && ./payload.sh
output: RCE via Unzip
uid=1000(user)
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
platforms: ["Linux", "macOS"]
tags: ["chmod", "rce"]
---

# chmod execute-payload

## Command

```bash
chmod +x payload.sh && ./payload.sh
```

## Description

Makes an extracted script executable and runs it, simulating RCE from malicious ZIP in vulnerable environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `+x` | Add execute permission | Yes |
| `payload.sh` | Target script | Yes |

## Examples

### Basic Usage

```bash
chmod +x malicious.sh && ./malicious.sh
```

### Advanced Usage

```bash
chmod +x payload.sh && sudo ./payload.sh  # Escalate if possible
```

## Expected Output

Script output, e.g., "RCE via Unzip\nuid=1000(user)".

## Related

- [[commands/unzip-extract-malicious]]
- [[procedures/Exploit-Unsafe-Unzip-in-Mason-Repository-for-RCE]]
