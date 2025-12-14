---
tags:
  - rce
  - exploit
type: procedure
tools:
  - '[[tools/primefaces-py]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/python-primefaces-py-exploit]]'
platforms:
  - Web
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 5361ff2f-1ea0-4b09-8882-4c89233a4b9c
created_at: '2025-12-14T17:23:27.556Z'
updated_at: '2025-12-14T17:23:27.556Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# Execute-PrimeFaces-RCE-POC

## Summary

This procedure executes the PrimeFaces POC script to exploit CVE-2017-1000486, achieving unauthenticated remote code execution by injecting and running arbitrary system commands on the target Tomcat server.

## Description

Targeting a vulnerable endpoint like /ftn-Website/ on restsvr1.ftn.research.usafa.edu, the script crafts a deserialization payload using MD5 hashing to bypass security and execute commands as the tomcat user (UID 91). This leads to full RCE, allowing potential pivoting in the DoD network. Requires the POC script and dependencies; outcomes include command output from the remote system.

## Requirements

1. Installed primefaces.py and pycryptodome
2. Target URL accessible (e.g., redacted subdomain)
3. Python 3.6+ runtime

## Defense

Defensive measures and detection strategies:

- Patch PrimeFaces to 5.3.8 or later
- Enable deserialization filters in Java applications
- Log and alert on suspicious HTTP requests to JSF endpoints

## Objectives

1. Inject malicious deserialization payload
2. Execute remote system commands
3. Confirm RCE for further exploitation

## Instructions

### Step 1: Run the Exploitation Script

**Context**: Launch the POC with the target URL and command to execute.

**Command** ([[commands/python-primefaces-py-exploit]]):
```bash
python primefaces.py ███/ftn-Website/ -c id
```

> The -c flag specifies the command ('id'); expect remote output showing tomcat user details if successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used

- [[commands/python-primefaces-py-exploit]]

## Tools Used

- [[tools/primefaces-py]]

## Tags

- [[rce]]
- [[exploit]]
