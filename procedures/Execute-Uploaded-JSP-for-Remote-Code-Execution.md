---
tags:
  - rce
  - execution
  - jsp
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:23:37.065Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 57331387-886b-4e25-b8f1-ff5adab80b91
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute Uploaded JSP for Remote Code Execution

## Summary

This procedure triggers the execution of an uploaded JSP file in Tomcat to run arbitrary commands on the server, achieving full RCE post-upload bypass.

## Description

Once a JSP file with uppercase extension is uploaded via the race condition, accessing it via HTTP GET with parameters executes embedded Java code, such as command invocation via Runtime.exec(). This leverages Tomcat's JSP processing on case-insensitive systems, leading to server-side execution. Outcomes include command output in responses, enabling further attacks like data exfiltration.

## Requirements

1. Successfully uploaded JSP from prior step
2. HTTP client for GET requests with query parameters
3. Target path knowledge (e.g., /shell.JSP)

## Defense

Defensive measures and detection strategies:

- Scan for and remove uploaded .JSP files periodically
- Enable strict MIME type checking and disable JSP processing for uploads
- Log and alert on suspicious parameter usage in JSP requests (e.g., 'cmd')

## Objectives

1. Execute arbitrary commands on the server
2. Confirm RCE capability
3. Leverage for persistence or escalation

## Instructions

### Step 1: Trigger JSP Execution

**Context**: Send a GET request to the uploaded JSP with a command parameter to invoke execution.

Execute with curl:

```bash
curl "http://target:8080/shell.JSP?cmd=whoami"
```

> This runs 'whoami' via the JSP; output appears in the response body, confirming RCE.

### Step 2: Validate and Escalate

**Context**: Test with a more impactful command, like listing directories.

Execute:

```bash
curl "http://target:8080/shell.JSP?cmd=ls -la /"
```

> Expected: Directory listing; use for further reconnaissance or exploitation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[rce]]
- [[Execution]]
