---
tags:
  - rce
  - code-injection
  - custom-script
  - apache-struts
type: procedure
tools:
  - '[[tools/Custom-RCE-Demonstration-Script]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/execute-benign-rce-command]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:20.285Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 2906e88f-73ba-41bd-9747-404911fa2c08
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# Demonstrate-RCE-with-Custom-Script

## Summary

This procedure demonstrates remote code execution on a vulnerable DoD website by developing and executing a custom script that exploits the Apache Struts code injection weakness (CVE-2017-5638), running a benign command to prove capability without causing damage.

## Description

Targeting the identified vulnerability in the DoD website's web server, this procedure crafts a payload for the deserialization flaw in Apache Struts' Multipart Parser. The custom script sends a malicious request that injects and executes code remotely. The target is a public web application, and the outcome is successful command execution, such as writing a harmless file, confirming RCE. Prerequisites include knowledge of the vulnerable endpoint from prior identification.

## Requirements

1. Custom script developed in a language like Python or Java to craft the exploit payload.
2. Access to the vulnerable DoD website endpoint.
3. Basic scripting skills for payload construction.

## Defense

Defensive measures and detection strategies:

- Enable strict input validation and sanitization in Struts applications.
- Deploy runtime application self-protection (RASP) to detect and block deserialization attempts.
- Log and alert on suspicious HTTP requests with encoded payloads.

## Objectives

1. Exploit the code injection to achieve remote command execution.
2. Execute a benign command to validate the vulnerability.
3. Ensure demonstration causes no harm to the target system.

## Instructions

### Step 1: Develop Custom Exploit Script

**Context**: Create a script that targets the vulnerable Struts endpoint with a deserialization payload.

Use a framework like ysoserial to generate the payload for CVE-2017-5638, embedding the benign command.

**Expected Output**: A runnable script file ready for execution.

### Step 2: Execute Script and Trigger RCE

**Context**: Run the script to send the payload and execute the command on the server.

Execute [[commands/execute-benign-rce-command]] as part of the payload:

```bash
echo 'RCE demonstrated successfully' > /tmp/proof.txt
```

> This command writes a harmless message to a temporary file, confirming execution via response anomalies or log verification.

**Expected Output**: Server response indicating successful payload processing, with the command run on the web server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used

- [[commands/execute-benign-rce-command]]

## Tools Used

- [[tools/Custom-RCE-Demonstration-Script]]

## Tags

- [[rce]]
- [[code-injection]]
- [[custom-script]]
