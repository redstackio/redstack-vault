---
data: xxd data2
tags:
  - payload-verification
  - hex-dump
type: command
executor: bash
platforms:
  - Linux
id: 556d709e-63eb-477b-9296-686d06e85dcd
created_at: '2025-12-13T09:01:21.822Z'
updated_at: '2025-12-13T09:01:21.822Z'
verified: false
validated: true
submitted: true
---
# xxd Dump Payload

## Command

```bash
xxd data2
```

## Description
Displays a hex dump of the file data2, which contains the crafted AJP smuggling payload, used to verify its contents before exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `data2` | The file containing the binary payload for the exploit | Yes |

## Examples

### Basic Usage

```bash
xxd data2
```

## Expected Output
Hexadecimal representation of the payload, including AJP protocol data and attributes like javax.servlet.include.path_info=/WEB-INF/web.xml.

## Related
- [[procedures/Create-Crafted-AJP-Payload-for-Smuggling]]
