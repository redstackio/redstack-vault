---
id: proc-002
tags:
  - csrf
  - poc-generation
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:32:58.124Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Generate-CSRF-Proof-of-Concept-with-Burp-Suite

## Summary

This procedure uses Burp Suite to intercept a legitimate profile update request and generate a CSRF HTML PoC, enabling the forgery of state-changing actions like modifying user settings.

## Description

The procedure targets web applications lacking CSRF protections, such as missing tokens in POST requests to endpoints like profile save. By proxying traffic through Burp Suite, the attacker captures the request parameters (e.g., action=save_info, password fields, email) and uses built-in tools to create an HTML form that replicates the request. This PoC can then be hosted or saved for delivery to victims. The scenario assumes an authenticated session and focuses on the DoD app's profile editing vulnerability.

## Requirements

1. Burp Suite installed and running with proxy listener (default port 8080)
2. Browser configured to use Burp as proxy (e.g., via FoxyProxy extension)
3. Active authenticated session to the target application

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens (e.g., synchronizer tokens) in all state-changing forms
- Enforce same-site cookie attributes (Lax or Strict) to prevent cross-site requests
- Monitor for unusual proxy traffic or tool signatures in logs

## Objectives

1. Capture exact request structure for forgery
2. Generate a functional HTML PoC for CSRF exploitation
3. Validate PoC against the target endpoint

## Instructions

### Step 1: Configure Proxy and Intercept

**Context**: Set up traffic interception to capture the profile save request.

Launch Burp Suite and ensure the proxy is running. Configure browser to route traffic through 127.0.0.1:8080.

> With proxy active, navigate to profile edit, make a change (e.g., update email), and submit. Intercept the POST in Burp's Proxy > Intercept tab. Expected output: Request details visible, including headers, body with parameters like action=save_info.

### Step 2: Generate PoC

**Context**: Use Burp's Engagement Tools to create the CSRF HTML.

Right-click the intercepted request in Burp Repeater or Proxy history, select Engagement Tools > Generate CSRF PoC. Customize parameters for malicious changes (e.g., new password).

> Burp outputs HTML with <form> posting to the endpoint (e.g., https://█████) and hidden inputs. Copy the code. Expected output: Valid HTML file that, when loaded, submits the forged request.

### Step 3: Test PoC Locally

**Context**: Verify the PoC works before delivery.

Save HTML to a file and open in browser while authenticated.

> Form submits; check target app for changes. Success if profile updates without direct interaction.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[poc-generation]]
- [[web]]
