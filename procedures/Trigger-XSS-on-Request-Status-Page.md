---
tags:
  - xss-execution
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exfiltration Over Command and Control Channel]]'
updated_at: '2025-12-14T03:16:02.450Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 1ac368de-83e0-4784-8467-c0d486c40237
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exfiltration Over Command and Control Channel]]'
---
# Trigger-XSS-on-Request-Status-Page

## Summary

This procedure covers accessing the request status page to trigger the stored XSS payload, resulting in the execution of JavaScript that exfiltrates administrator credentials when reviewed by privileged users.

## Description

Once the payload is stored, it remains dormant until the request is viewed on the status page at https://█████████, where it is rendered unsanitized. Execution occurs in the viewer's browser, capturing session details like cookies and sending them to the attacker. This blind XSS relies on admin interaction, making it stealthy. Outcomes include logged admin sessions for potential takeover.

## Requirements

1. Submitted request ID from prior injection
2. Monitoring setup on attacker endpoint for incoming data
3. Patience for admin review (may take time in real scenarios)

## Defense

Defensive measures and detection strategies:

- Escape output on all dynamic pages using libraries like DOMPurify
- Review request queues manually or with automated scanning for malicious patterns
- Network monitoring for unexpected outbound requests from application servers or user browsers

## Objectives

1. Render the stored payload to initiate JavaScript execution
2. Capture and exfiltrate sensitive session data from admin viewers
3. Validate the vulnerability's impact through received data

## Instructions

### Step 1: Access Status Page

**Context**: Locate the vulnerable display area.

No specific command; navigate to https://█████████ and search for or select the submitted request by ID.

> Page loads with request details, including the description.

### Step 2: View Request Details

**Context**: Trigger rendering of the description field.

No specific command; click to expand or view the full request, focusing on the description section.

> If you are the submitter, execution may not yield admin data; wait for admin access. Monitor your server logs for incoming requests.

### Step 3: Confirm Exfiltration

**Context**: Verify payload success via received data.

No specific command; check your logging endpoint for HTTP GET requests containing cookie data.

> Successful trigger shows logs like '/log?data=sessionid=admin_token;user=admin'.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Exfiltration Over Command and Control Channel]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[credential-theft]]
