---
id: proc-001
tags:
  - netrc
  - malicious-file
  - nul-byte
type: procedure
tools:
  - '[[tools/bash]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/echo-create-malicious-netrc]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:25:13.325Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Create-Malicious-netrc-File-with-NUL-Byte

## Summary

This procedure creates a proof-of-concept .netrc file containing a NUL byte (\x00) in the password token, exploiting the libcurl parsenetrc() function's failure to handle NUL terminators properly, leading to a heap over-read during token parsing.

## Description

The .netrc file is used by libcurl to store credentials for network authentication. The vulnerability arises in lib/netrc.c's parsenetrc() function, where the token parsing loop increments tok_end without checking for NUL bytes in unquoted tokens, causing reads into adjacent heap memory. By embedding \x00 in the password field followed by arbitrary data, the parser over-reads heap contents, which are then used in network requests. This procedure focuses on generating the malicious file on a Linux system with bash access.

## Requirements

1. Bash shell access on Linux
2. Write permissions in the current directory
3. No special privileges needed

## Defense

Defensive measures and detection strategies:

- Validate and sanitize .netrc files for unexpected NUL bytes using tools like `hexdump` or `strings`
- Disable .netrc usage in libcurl via `CURLOPT_NETRC` set to 0
- Monitor file creations in user directories for suspicious echo commands with escape sequences

## Objectives

1. Generate a .netrc file that triggers the heap over-read in libcurl
2. Ensure the NUL byte is correctly embedded without corrupting the file format
3. Prepare for integration with libcurl exploitation

## Instructions

### Step 1: Execute File Creation Command

**Context**: Use echo with escape interpretation to write the malicious line to a file, embedding the NUL byte in the password token to exploit the parser's boundary handling.

**Command** ([[commands/echo-create-malicious-netrc]]):

```bash
echo -en 'machine 127.0.0.1 login username password\x00 nothing-suspicious-here\n' > poc.txt
```

> This command uses `-e` to interpret backslashes (\x00 as NUL) and `-n` to suppress trailing newline. The output is redirected to `poc.txt`. Expected: File created with the exact line, verifiable by `cat poc.txt` showing the content and NUL as a non-printable character.

### Step 2: Verify File Integrity

**Context**: Confirm the NUL byte is present to ensure the exploit trigger is ready.

**Command** (Manual verification):

```bash
hexdump -C poc.txt
```

> Look for `00` byte after 'password' in the hex dump. Success: NUL byte confirmed at the expected position.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Credentials In Files]] Credentials In Files (.netrc)

### Sub-Techniques


## Commands Used

- [[commands/echo-create-malicious-netrc]]

## Tools Used

- [[tools/bash]]

## Tags

- netrc
- malicious-file
- nul-byte
