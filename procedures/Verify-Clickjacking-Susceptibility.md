---
id: proc-verify-clickjacking
tags:
  - clickjacking
  - verification
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:05.069Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploit Public-Facing Application]]'
---
# Verify-Clickjacking-Susceptibility

## Summary

This procedure tests the created HTML file in a browser to confirm if the Mavenlink login page can be loaded in an iframe without restrictions, indicating clickjacking vulnerability.

## Description

By opening the test HTML locally, this step validates the absence of protections against framing. If the login page renders in the iframe, attackers can proceed to exploit it for UI redressing, where users are tricked into actions on the legitimate site while believing they interact with a benign page. This is particularly dangerous for login pages, enabling credential phishing or forced logins leading to CSRF.

## Requirements

1. Web browser (e.g., Chrome)
2. The created HTML test file
3. Internet connection to access the target URL

## Defense

Defensive measures and detection strategies:

- Enable browser developer tools to inspect for unexpected iframes
- Use security extensions like NoScript to block framing
- Server-side logging of referer headers to detect anomalous embeds

## Objectives

1. Confirm the target page loads in the iframe
2. Observe overlay behavior for exploitation potential
3. Identify any partial protections (e.g., partial frame-busting)

## Instructions

### Step 1: Load HTML File

**Context**: Open the test file in a browser to initiate the iframe load.

**Instructions**:

Open 'pen-test-for-clickjacking.html' in your web browser by double-clicking or using file:// protocol.

> The page should display the warning text with the semi-transparent login form underneath. Interact with the overlaid area to ensure clicks propagate to the iframe.

### Step 2: Inspect and Validate

**Context**: Use browser tools to verify no errors occur during framing.

**Instructions**:

Right-click the iframe and select 'Inspect Element'. Check the console for any frame-busting JavaScript errors or CSP violations.

> Expected: No errors; the login form is fully interactive. If blocked, the vulnerability is mitigated.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[testing]]
