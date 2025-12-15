---
id: 123e4567-e89b-12d3-a456-426614174006
data: unzip -o file.zip
tags:
  - unzip
  - rce
type: command
output: |-
  Archive:  file.zip
    inflating: payload.sh
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.225Z'
verified: false
validated: true
submitted: true
---
---
id: 123e4567-e89b-12d3-a456-426614174006
name: unzip-extract-malicious
type: command
executor: bash
data: |
  unzip -o file.zip
output: Archive:  file.zip
  inflating: payload.sh
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
platforms: ["Linux", "macOS"]
tags: ["unzip", "rce"]
---

# unzip extract-malicious

## Command

```bash
unzip -o file.zip
```

## Description

Extracts ZIP archives without prompting, vulnerable to malicious payloads if source is untrusted, as in unsafe script executions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-o` | Overwrite files without prompt | No |
| `file.zip` | Archive to extract | Yes |

## Examples

### Basic Usage

```bash
unzip -o postgis-dependencies.zip
```

### Advanced Usage

```bash
unzip -o -q postgis-dependencies.zip  # Quiet mode
```

## Expected Output

"Archive: postgis-dependencies.zip\n inflating: payload.sh".

## Related

- [[commands/chmod-execute-payload]]
- [[procedures/Exploit-Unsafe-Unzip-in-Mason-Repository-for-RCE]]
