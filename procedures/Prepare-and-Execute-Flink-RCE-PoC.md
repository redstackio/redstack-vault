---
id: proc-flink-rce-poc
tags:
  - rce
  - api-exploitation
  - javascript-gadget
  - poc
type: procedure
tools:
  - '[[tools/python]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/python-poc-execution]]'
verified: false
platforms:
  - Web
  - Java
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:32:48.422Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Prepare-and-Execute-Flink-RCE-PoC

## Summary

This procedure involves customizing a Python PoC script and executing it to exploit the unrestricted /jars/{jar_id}/plan API endpoint in Apache Flink, using a JavaScript gadget for RCE and reverse shell deployment.

## Description

The vulnerability allows arbitrary Java class specification (e.g., com.sun.tools.script.shell.Main) and arguments to load remote JavaScript from a URL, executing code on the Flink server. The PoC sends a GET request with malicious parameters, causing RCE that connects back to the netcat listener. This crashes the Flink instance. Target: Aiven Flink API; prerequisites: jar ID from prior step, listener setup.

## Requirements

1. Python 3 installed with requests library
2. poc.py script (customized with host, jar_id, listener_ip/port)
3. Valid jar ID from Flink job
4. Network access to Flink API endpoint

## Defense

Defensive measures and detection strategies:

- Validate and restrict entry-class and programArg parameters in Flink API
- Enable authentication and authorization on Flink REST API endpoints
- Monitor API logs for anomalous requests to /jars/* endpoints
- Use WAF to block gadget class invocations

## Objectives

1. Trigger RCE via API gadget chain
2. Establish reverse shell connection
3. Achieve command execution on Flink server

## Instructions

### Step 1: Update PoC Script Variables

**Context**: Customize the script for the target environment.

No command; edit poc.py to set Flink host, jar ID (e.g., 145df7ff-c71a-4f3a-b77a-ee4055b1bede_a.jar), and listener IP/port (e.g., attacker_ip:8888). The script uses requests.get with params: entry-class=com.sun.tools.script.shell.Main, programArg=-script <remote_js_url> where JS loads and executes shell.

> Script ready with target-specific values.

### Step 2: Execute the PoC Script

**Context**: Send the malicious API request to trigger RCE.

**Command** ([[commands/python-poc-execution]]):
```bash
python3 poc.py
```

> Runs the script to issue GET /jars/{jar_id}/plan. Expected output: HTTP response (200 or error), RCE execution, connection to listener; Flink crashes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/python-poc-execution]]

## Tools Used

- [[tools/python]]

## Tags

- rce
- api-exploitation
- javascript-gadget
- poc
