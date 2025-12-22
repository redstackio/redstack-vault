---
id: 612de3f5-fcd3-4d36-8232-715f930af6c7
name: linenum-basic-scan-for-vulnerabilities
type: command
executor: bash
data: ./LinEnum.sh
output: |-
  root@host:~$ ./LinEnum.sh
  #########################################################
  # Local Linux Enumeration & Privilege Escalation Script #
  ...
  ### SCAN COMPLETE ####################################
created_at: '2019-09-17T06:34:44.715137+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - enum
  - priv-esc
verified: true
validated: true
---

# linenum-basic-scan-for-vulnerabilities

## Command

```bash
./LinEnum.sh
```

## Description

Runs basic LinEnum scan for priv-esc vectors.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ./LinEnum.sh | Script execution | Yes |

## Examples

### Basic Run

```bash
chmod +x LinEnum.sh; ./LinEnum.sh
```

## Expected Output

Enumeration report sections.

## Related

- [[procedures/enumerate-linux-privilege-escalation-paths-with-linenum]]
