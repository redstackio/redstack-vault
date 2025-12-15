---
tags:
  - curl
  - cookie-jar
  - toctou
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-cookie-jar-exploit]]'
  - '[[commands/stat-and-fopen-in-curlfopen]]'
platforms:
  - Linux
techniques:
  - '[[Exploitation for Privilege Escalation]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: fd962869-9d74-4a3e-9707-01b0b23a6d32
created_at: '2025-12-14T17:24:22.189Z'
updated_at: '2025-12-14T17:24:22.189Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Trigger-libcurl-with-Cookie-Jar

## Summary

This procedure simulates the victim running curl to save cookies to a manipulated file, triggering the vulnerable Curl_fopen stat/fopen sequence during the race window.

## Description

Victim executes curl --cookie-jar a google.com, invoking lib/fopen.c where stat('a', &sb) checks file type, falling back to fopen('a', 'w') if non-regular. With swapping active, stat sees directory, but fopen follows symlink to 'flag', overwriting it. Applies to options like --hsts, --alt-svc; leads to integrity breaches on protected files.

## Requirements

1. Vulnerable libcurl (7.84.0-8.1.2)
2. Active file swapping from prior procedure
3. Victim privileges to run curl
4. Network access to target URL (e.g., google.com)

## Defense

Defensive measures and detection strategies:

- Patch libcurl to version 8.3.0+ where race is fixed with atomic checks
- Run curl in sandboxed environments (e.g., AppArmor) restricting file ops
- Log file opens in privileged paths

## Objectives

1. Hit the TOCTOU race for file overwrite
2. Leak or corrupt sensitive data
3. Achieve privilege escalation effects

## Instructions

### Step 1: Execute Curl Command

**Context**: Victim fetches URL and saves cookies, triggering Curl_fopen.

**Command** ([[commands/curl-cookie-jar-exploit]]):
```bash
curl --cookie-jar a google.com
```

> Fetches google.com, writes cookies to 'a' in Netscape format. Expected output: Curl success message; if race hits, 'flag' overwritten with 131 bytes of cookie data.

### Step 2: Vulnerable Code Execution

**Context**: Internal libcurl logic executed (for reference).

**Command** ([[commands/stat-and-fopen-in-curlfopen]]):
```c
if(stat(filename, &sb) == -1 || !S_ISREG(sb.st_mode)) { *fh = fopen(filename, FOPEN_WRITETEXT); }
```

> Checks regularity via stat; falls back to fopen if not. Expected: Opens symlink if swapped.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used

- [[commands/curl-cookie-jar-exploit]]
- [[commands/stat-and-fopen-in-curlfopen]]

## Tools Used

- [[tools/curl]]

## Tags

- [[tools/curl]]
- [[cookie-jar]]
- [[toctou]]
