---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567894
tags:
  - xss-trigger
  - phabricator
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:31.192Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Persistent-XSS-in-Repository-Edit-Link

## Summary

This procedure triggers the stored XSS payload by clicking the 'Edit' link in a Phabricator repository, executing arbitrary JavaScript in the browser context due to the bypassed editor URL.

## Description

After injection, the user's editor setting is a malicious javascript: URI. Navigating to a repository and clicking 'Edit' invokes this URL, running the payload (e.g., alert(1)). This is self-XSS but can escalate with CSRF. Targets browsers like Chrome that parse whitespace in schemes. Outcomes: Immediate JS execution, potential for phishing or takeover.

## Requirements

1. Injected payload from prior procedure
2. Access to a Phabricator repository
3. Vulnerable browser (e.g., Chrome)

## Defense

Defensive measures and detection strategies:

- Sanitize all user-configured URLs in Phabricator
- Implement strict URI validation stripping whitespace
- Educate users on risks of external editor links

## Objectives

1. Execute the persistent payload
2. Verify XSS via alert or console
3. Demonstrate impact like data exfiltration

## Instructions

### Step 1: Navigate to Repository

**Context**: Select any repository to access the Edit functionality.

No command required; browse to a repo page like /source/<repo>/.

> Ensure the page loads with the 'Edit' link visible.

### Step 2: Click Edit Link

**Context**: Interact with the vulnerable link to trigger the editor URL.

No command required; click the 'Edit' button or link.

> The browser should execute the javascript: payload, showing an alert(1) dialog.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
- [[phabricator]]
