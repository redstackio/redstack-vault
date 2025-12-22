---
id: ae13ffeb-dcf8-4bff-86d9-918fdd9f87cd
type: command
executor: bash
data: nmap --interactive
output: |-
  $ nmap --interactive
  Starting Nmap V. 4.53 ( http://insecure.org )
  Welcome to Interactive Mode -- press h <enter> for help
  nmap> 
created_at: '2019-10-09T23:36:48.475781+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - exploit
  - priv-esc
verified: true
validated: true
---

# nmap-interactive-mode

## Command

```bash
nmap --interactive
```

## Description

Launches Nmap in interactive mode, allowing scripted scans; exploitable in old versions for shell escape.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --interactive | Enter interactive prompt | Yes |

## Examples

### Basic Usage

```bash
nmap --interactive
```

### With Target

```bash
nmap --interactive 10.10.10.10
```

## Expected Output

nmap> prompt for commands.

## Related

- [[procedures/Nmap-Interactive-Mode-Shell-Escape]]
- [[tools/Nmap]]
