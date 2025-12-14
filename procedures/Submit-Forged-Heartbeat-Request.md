---
id: proc-wakatime-submit-forged-001
tags:
  - csrf
  - exploitation
  - injection
type: procedure
tools:
  - '[[tools/jQuery]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:20.779Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit Forged Heartbeat Request

## Summary

This procedure deploys the crafted HTML POC to submit a forged JSON request to WakaTime's API, injecting fake heartbeat data using the victim's session cookies.

## Description

In a social engineering attack, the malicious page is hosted and delivered to victims (e.g., via email link). Upon loading, it auto-submits the form, causing the server to accept and process the text/plain JSON as legitimate activity. Prerequisites: Hosted POC and victim interaction; outcomes include altered coding logs, potentially for deception or account compromise.

## Requirements

1. Web server to host the HTML file (e.g., GitHub Pages, local server)
2. Phishing vector to direct victim to the page
3. Access to victim's WakaTime dashboard for verification

## Defense

Defensive measures and detection strategies:

- Implement anti-phishing training for users
- Rate-limit heartbeat submissions per user/session
- Audit logs for unusual activity patterns (e.g., zero-duration heartbeats)

## Objectives

1. Trigger form submission in victim's browser
2. Confirm server acceptance of forged data
3. Validate injection in account logs

## Instructions

### Step 1: Host and Distribute POC

**Context**: Make the HTML accessible and lure the victim.

Upload the POC to a hosting service and send a link via email or social engineering.

> Ensure the page loads over HTTP/HTTPS; victim's cookies are sent automatically.

### Step 2: Monitor Submission and Verify

**Context**: Observe the request and check for success.

In a test environment, load the page with an authenticated session; use dev tools to confirm POST to /heartbeats with 200 response.

> Then, log into WakaTime dashboard to see new fake entry (e.g., coding time for "FakeProject").

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/jQuery]]

## Tags

- [[exploitation]]
- [[injection]]
