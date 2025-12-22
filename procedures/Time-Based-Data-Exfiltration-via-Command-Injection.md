---
id: 24a9f3b8-d8dc-4244-8461-3dc76260f8d9
name: Time-Based-Data-Exfiltration-via-Command-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:57.455319+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - '[[techniques/Command and Scripting Interpreter|T1059.004 - Unix Shell]]'
  - >-
    [[techniques/Exfiltration Over Alternative Protocol|T1048 - Exfiltration
    Over Alternative Protocol]]
sub_techniques: []
tags:
  - '[[tags/Command Injection]]'
  - '[[tags/Time-based Data Exfiltration]]'
  - blind-exfiltration
commands:
  - '[[commands/bash-time-based-char-check]]'
platforms:
  - Linux
  - Web
tools: []
validated: true
---

# Time-Based-Data-Exfiltration-via-Command-Injection

## Summary

This procedure demonstrates time-based data exfiltration through command injection vulnerabilities, where an attacker injects shell commands that introduce measurable delays based on data characteristics, allowing bit-by-bit or character-by-character extraction of sensitive information like usernames without direct output visibility.

## Description

Time-based exfiltration exploits command injection flaws in applications (e.g., web apps executing system commands) by crafting injections that conditionally delay responses using sleep commands. For each potential character or bit in the target data (e.g., username from 'whoami'), the attacker tests guesses; a delay indicates a match. This is useful in blind scenarios where direct command output is not returned, such as filtered responses or no-echo environments. The technique targets Unix-like systems via shell interpreters and can exfiltrate data like environment variables, file contents, or database queries sequentially. It requires precise timing measurement (e.g., via network latency) and is slow but stealthy, evading output-based detection.

## Requirements

1. A vulnerable application permitting command injection (e.g., unsanitized user input passed to system() in PHP or exec() in Node.js).
2. Ability to send repeated requests and measure response times accurately (e.g., using tools like Burp Suite or custom scripts).
3. Target system running a Unix shell (bash/sh) with access to basic commands like 'whoami', 'cut', and 'sleep'.
4. Knowledge of data length or format to iterate positions (e.g., usernames typically 1-32 chars).

## Defense

- Implement strict input validation and sanitization, using whitelists for allowed characters and parameterized queries.
- Employ web application firewalls (WAFs) to detect injection patterns like semicolons, pipes, or sleep commands.
- Monitor application logs for anomalous delays in command execution and network response times.
- Use least-privilege execution for application processes to limit command impact.

## Objectives

1. Identify and exploit a command injection point to inject conditional delay commands.
2. Extract sensitive data (e.g., username) character by character via response timing.
3. Reconstruct full data payload without relying on direct output.

## Instructions

### Step 1: Identify Injection Point and Test Basic Delay

**Context**: Confirm command injection works and establish baseline response time by injecting a simple sleep command.

**Command** ([[commands/bash-time-based-char-check]]):
```bash
sleep 5;
```

> Inject this into the vulnerable parameter (e.g., via POST data or URL). Measure the response time; a 5-second delay confirms injection success. Adjust for network latency (e.g., average non-delayed responses ~200ms).

### Step 2: Determine Data Length

**Context**: First, probe the length of the target data (e.g., username) using a conditional sleep based on string length.

**Command** ([[commands/bash-time-based-char-check]]):
```bash
if [ $(whoami | wc -c) -eq 8 ]; then sleep 5; fi;
```

> Iterate the length guess (e.g., replace 8 with 1-32). A delay indicates the correct length. This sets the number of positions to probe.

### Step 3: Extract Character by Character

**Context**: For each position in the data, test possible characters (e.g., a-z, 0-9) sequentially or via binary search to find matches via delay.

**Command** ([[commands/bash-time-based-char-check]]):
```bash
if [ $(whoami | cut -c 1) == "s" ]; then sleep 5; fi;
```

> Start with position 1 (cut -c 1), guess 'a' to 'z'. Repeat for each guess until delay observed (match). Move to position 2 (cut -c 2), etc. For the example username 'swissky', position 1 delays on 's', position 2 on 'w', and so on. Document matches to reconstruct the full string.

### Step 4: Verify and Exfiltrate Full Data

**Context**: Once characters are identified, inject a command to output or further process the full data if possible, or use the reconstructed info for next steps.

> If partial exfiltration succeeds, chain to extract more (e.g., replace 'whoami' with 'cat /etc/passwd | head -1 | cut -c $_POS'). Total time scales with data length and charset size (e.g., 7-char username with 26 letters: ~182 requests).
