---
tags:
  - xss
  - monitoring
  - confirmation
type: procedure
tools:
  - '[[tools/XSS-Hunter]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:49.911Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 2473bb50-f676-41c0-917c-6fb8c6c44356
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Monitor-and-Confirm-XSS-Execution-in-Admin-Dashboard

## Summary

This procedure outlines monitoring for the execution of a stored XSS payload in Zomato's admin dashboard, confirming compromise when a support agent views the tainted order details.

## Description

After payload injection, the attack relies on legitimate workflows where support agents access order information. The unsanitized address field renders the JavaScript in the admin interface, executing in the agent's browser. Tools like XSS Hunter capture execution details, including IP, user-agent, and potential session data, enabling further attacks like phishing or token theft.

## Requirements

1. Active XSS Hunter hunt from the injection step
2. Patience for business process triggering (may take minutes to hours)
3. Access to XSS Hunter dashboard for real-time monitoring

## Defense

Defensive measures and detection strategies:

- Sanitize all outputs in admin panels using libraries like DOMPurify
- Implement role-based access controls and audit logs for admin views
- Deploy endpoint detection for anomalous script loads in admin sessions

## Objectives

1. Detect payload execution in privileged context
2. Gather evidence of vulnerability (e.g., execution logs)
3. Assess impact on admin users for reporting or escalation

## Instructions

### Step 1: Set Up Monitoring

**Context**: Prepare the tracking tool to receive callbacks upon execution.

Log in to [[tools/XSS-Hunter]] and ensure the hunt is active. Note the callback URL and expected alert behavior.

### Step 2: Wait for Trigger

**Context**: Rely on support agents to view the order, which renders the payload.

No active input required; monitor passively. Execution occurs when the admin dashboard loads the address field, e.g., in HTML: `<div>Order Address: Valid Address"><script>...</script></div>`.

### Step 3: Confirm Execution

**Context**: Validate success via tool reports.

Check XSS Hunter for hits: Look for alert(0) or custom reports showing execution details like victim IP and referrer (admin dashboard URL).

> Successful output includes timestamp, user-agent indicating admin browser, and potential DOM context.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/XSS-Hunter]]

## Tags

- xss
- monitoring
