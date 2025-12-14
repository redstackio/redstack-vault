---
tags:
  - race-condition
  - toctou
  - libcurl
  - file-overwrite
  - data-leak
  - privilege-escalation
type: attack_chain
tools:
  - '[[tools/rename-custom-swapper]]'
  - '[[tools/curl]]'
  - '[[tools/pgrep]]'
  - '[[tools/cut]]'
  - '[[tools/cat]]'
tactics:
  - '[[Privilege Escalation]]'
  - '[[Defense Evasion]]'
  - '[[Collection]]'
commands:
  - '[[commands/stat-and-fopen-in-curlfopen]]'
  - '[[commands/run-rename-swap]]'
  - '[[commands/curl-cookie-jar-exploit]]'
  - '[[commands/cat-flag-verify]]'
  - '[[commands/monitor-curl-processes]]'
platforms:
  - Linux
complexity: medium
procedures:
  - '[[procedures/Prepare-Environment-for-libcurl-Race]]'
  - '[[procedures/Execute-Continuous-File-Swapping]]'
  - '[[procedures/Trigger-libcurl-with-Cookie-Jar]]'
  - '[[procedures/Verify-Exploit-Success]]'
  - '[[procedures/Monitor-Curl-Processes-for-Automation]]'
step_count: 5
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[NTFS File Attributes]]'
description: >-
  Exploits a Time-of-Check Time-of-Use race condition in libcurl's Curl_fopen
  function to trick a victim into overwriting protected files or leaking
  sensitive data like cookies via manipulated symlinks and directories.
skill_level: intermediate
impact_level: high
id: 3e0ca794-d207-4608-8de9-c58deb57ab54
created_at: '2025-12-14T17:24:22.202Z'
updated_at: '2025-12-14T17:24:22.202Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
  - '[[Defense Evasion]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[NTFS File Attributes]]'
---
# TOCTOU Race Condition in libcurl to Overwrite Protected Files and Leak Data

Multi-stage attack chain demonstrating exploitation of CVE-2023-32001, a TOCTOU race in libcurl's Curl_fopen, allowing local attackers to overwrite victim-owned files like /etc/passwd or leak sensitive data such as cookies and HSTS cache.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare Files and Symlink] --> B[Start Continuous Swapping]
    B --> C[Victim Triggers Curl]
    C --> D[Race Hits, Overwrite/Leak Occurs]
    D --> E[Verify and Automate Monitoring]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#e67e22
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/rename-custom-swapper]]
- [[tools/curl]]
- [[tools/pgrep]]
- [[tools/cut]]
- [[tools/cat]]

### Target Environment

- Linux OS with libcurl versions 7.84.0 to 8.1.2
- Local access to shared filesystem
- Victim process using curl with file-saving options like --cookie-jar
- No specific ports or services required

### Initial Access Requirements

- Local attacker access on the same system as victim
- Ability to create files/symlinks in a shared directory
- No network credentials needed; exploits local file operations

## Detailed Attack Procedures

### Step 1: Prepare Environment
procedure: [[procedures/Prepare-Environment-for-libcurl-Race]]

**Objective**: Set up symlinks, directories, and protected files to create the race condition setup.

**Instructions**: Create a symlink 'a' pointing to a victim-owned file like 'flag', a directory 'b' owned by attacker, and compile the rename tool.

Use standard Linux commands to prepare:

```bash
ln -s flag a
mkdir b
# Compile rename.c (source from GitHub)
gcc rename.c -o rename
```

**Expected Output**: Directory listing shows lrwxrwxrwx a -> flag, drwxrwxrwx b, -rw-r--r-- flag (root-owned), -rwxr-x--- rename.

**Success Indicators**:
- Symlink and directory created successfully
- Rename tool compiled without errors

### Step 2: Start Continuous File Swapping
procedure: [[procedures/Execute-Continuous-File-Swapping]]

**Objective**: Initiate atomic swaps between symlink and directory to open the TOCTOU window.

**Instructions**: Run the custom rename program to swap 'a' and 'b' in an infinite loop using [[commands/run-rename-swap]].

```bash
./rename a b
```

**Expected Output**: Continuous atomic exchanges via renameat2 syscall, creating race opportunities.

**Success Indicators**:
- Process runs indefinitely without interruption
- File names swap rapidly (observable via ls in another terminal)

### Step 3: Trigger libcurl Vulnerability
procedure: [[procedures/Trigger-libcurl-with-Cookie-Jar]]

**Objective**: Have the victim execute curl to save data to the manipulated file, hitting the race.

**Instructions**: Simulate victim running curl with --cookie-jar on 'a', triggering Curl_fopen's stat/fopen sequence using [[commands/curl-cookie-jar-exploit]].

```bash
curl --cookie-jar a google.com
```

**Expected Output**: If race hits, 'a' appears as directory to stat but symlink to fopen, writing to 'flag'.

**Success Indicators**:
- Curl completes without error
- File 'flag' modified (size changes to ~131 bytes with cookie data)

### Step 4: Verify Exploit Success
procedure: [[procedures/Verify-Exploit-Success]]

**Objective**: Check if overwrite or leak occurred by inspecting the protected file.

**Instructions**: Use [[commands/cat-flag-verify]] to display contents of 'flag'.

```bash
cat flag
```

**Expected Output**: Netscape HTTP Cookie File headers and cookie data written to 'flag'.

**Success Indicators**:
- 'flag' contains unexpected cookie data
- Original content overwritten or appended

### Step 5: Automate with Process Monitoring
procedure: [[procedures/Monitor-Curl-Processes-for-Automation]]

**Objective**: Detect victim curl executions to dynamically extract paths and target exploits.

**Instructions**: Run the monitoring script using [[commands/monitor-curl-processes]] to watch for curl PIDs and args.

```bash
while true; do TEST_VAR=`pgrep -l -f curl | cut -f 1 -d " "` && if [ -n "$TEST_VAR" ]; then cat /proc/$TEST_VAR/cmdline && echo ; fi; done
```

**Expected Output**: Prints PID and full curl command line (e.g., including --cookie-jar path) when detected.

**Success Indicators**:
- Script detects curl processes
- Extracts arguments for targeted swapping

## Attack Chain Summary

### Key Achievements

1. Setup race environment with symlink and directory manipulation
2. Exploit TOCTOU in libcurl to overwrite protected files like /etc/passwd
3. Leak sensitive data (cookies, HSTS) to attacker-controlled locations
4. Automate detection for real-world persistence

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[NTFS File Attributes]] Hide Artifacts: NTFS File Attributes (adapted for Linux file type hiding)

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation
- [[Defense Evasion]] Defense Evasion
- [[Collection]] Collection

---
*Last updated: 2023-10-01*
