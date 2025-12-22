---
id: execute-poc-kafka-rce-001
tags:
  - rce
  - kafka-connect
  - ssrf
  - file-upload
  - poc
type: procedure
tools:
  - '[[tools/Python3]]'
  - '[[tools/Kafka-Python]]'
tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
commands:
  - '[[commands/cd-to-poc-directory]]'
  - '[[commands/python-run-poc-script]]'
verified: false
platforms:
  - Cloud
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[PowerShell]]'
updated_at: '2025-12-14T03:46:09.296Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[PowerShell]]'
---
# Execute-PoC-Script-for-Kafka-Connect-RCE

## Summary

This procedure runs a Python proof-of-concept script to exploit Aiven Kafka Connect by creating malicious connectors: uploading a SQLite DB with an embedded JVM agent JAR via JdbcSinkConnector and using HttpSinkConnector for SSRF to invoke Jolokia's jvmtiAgentLoad MBean, leading to RCE and reverse shell.

## Description

The script interacts with Kafka Connect's REST API to configure the JdbcSinkConnector for unrestricted SQLite file upload (exploiting lack of BLOB validation) and HttpSinkConnector for SSRF to localhost:6725. It targets the com.sun.management:type=DiagnosticCommand MBean to load the agent, executing code that connects back to the listener. Requires access to the Connect API and kafka-python for API calls.

## Requirements

1. Kafka Connect REST API endpoint accessible (e.g., https://your-aiven-connect:8083)
2. kafka-python library: pip install kafka-python
3. PoC directory with poc.py and malicious SQLite DB (embedded JAR agent)
4. Network access to target without auth bypass needed for connector creation

## Defense

Defensive measures and detection strategies:

- Restrict JdbcSinkConnector to validated file types and scan uploads for embedded executables
- Validate HttpSinkConnector URLs to block localhost/internal IPs (e.g., deny 127.0.0.1, 0.0.0.0)
- Secure Jolokia with authentication (e.g., basic auth or IP whitelisting) and limit MBean exposure
- Monitor Connect API for anomalous connector creations and log SSRF attempts

## Objectives

1. Upload malicious SQLite DB containing JVM agent via JDBC
2. Trigger SSRF to unprotected Jolokia for agent loading
3. Achieve RCE with reverse shell to external listener

## Instructions

### Step 1: Navigate to PoC Directory

**Context**: Change to the directory containing the exploit script and assets.

**Command** ([[commands/cd-to-poc-directory]]):
```bash
cd jdbc-sqlite-jolokia-rce
```

> This sets the working directory to where poc.py and the malicious DB reside. Expected output: Prompt changes to reflect new directory.

### Step 2: Run the Exploitation Script

**Context**: Execute the script to orchestrate connector setup, upload, SSRF, and agent load.

**Command** ([[commands/python-run-poc-script]]):
```bash
python3 poc.py
```

> The script uses kafka-python to POST connector configs to /connectors, uploads the DB as a BLOB via JDBC, sends SSRF request to Jolokia (/jolokia/exec/.../jvmtiAgentLoad/...), and triggers the reverse shell. Expected output: JSON responses for connector creation, HTTP 200 for Jolokia, and confirmation of agent load; shell connects externally.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Initial Access]] Initial Access

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[PowerShell]] Command and Scripting Interpreter

### Sub-Techniques


## Commands Used

- [[commands/cd-to-poc-directory]]
- [[commands/python-run-poc-script]]

## Tools Used

- [[tools/Python3]]
- [[tools/Kafka-Python]]

## Tags

- rce
- kafka-connect
- ssrf
- file-upload
- poc
