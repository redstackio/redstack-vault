---
tags:
  - rce
  - el-injection
  - http-request
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-primefaces-exploit]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:07.848Z'
sub_techniques: []
id: 10669588-8f1d-4585-be06-06b1315ef1d1
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send EL Injection Payload via Curl

## Summary

This procedure delivers the EL injection payload to the target JSF endpoint using curl, triggering the vulnerability in PrimeFaces 5.3 to execute arbitrary code on the server.

## Description

By sending a GET request to the constructed URL with the pfdrid parameter containing the encrypted payload, the DynamicContent generator processes the EL expression without validation, leading to RCE. Flags like -v for verbose output and -k for insecure SSL help in debugging and bypassing cert issues. This step assumes the URL is ready and focuses on transmission, with success validated by subsequent DNS observation rather than response content.

## Requirements

1. Constructed exploit URL with payload
2. curl installed on the attacker's machine
3. Network connectivity to target port 80/443

## Defense

Defensive measures and detection strategies:

- Enable strict input validation in PrimeFaces resource handlers
- Monitor web server logs for GET requests to dynamiccontent with anomalous pfdrid values
- Use intrusion detection systems (IDS) to flag EL-like patterns in traffic

## Objectives

1. Successfully transmit the payload to the server
2. Trigger EL evaluation without request rejection
3. Observe no immediate failure in HTTP response

## Instructions

### Step 1: Prepare Curl Command

**Context**: Set up the curl invocation with necessary flags for the target URL.

**Command** ([[commands/curl-primefaces-exploit]]):
```bash
curl -vk "https://target.com/javax.faces.resource/dynamiccontent.properties.xhtml?pfdrt=sc&ln=primefaces&pfdrid=<YOUR_GENERATED_PAYLOAD>"
```

> Sends the GET request verbosely (-v) and insecurely (-k). Replace <YOUR_GENERATED_PAYLOAD> with the actual string. Expected output: HTTP headers and body; look for 200 OK or resource data.

### Step 2: Execute and Monitor Response

**Context**: Run the command and review output for errors.

Execute the above command.

> If SSL issues arise, -k ensures continuation. Success is indirect via DNS step.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-primefaces-exploit]]

## Tools Used

- [[tools/curl]]

## Tags

- rce
- http-request
