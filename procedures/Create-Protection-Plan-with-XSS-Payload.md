---
tags:
  - xss-injection
  - payload-creation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f36b3813-938a-4737-bb01-6e0b3f743f74
created_at: '2025-12-13T23:52:50.024Z'
updated_at: '2025-12-13T23:52:50.024Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Protection-Plan-with-XSS-Payload

## Summary

This procedure injects a malicious JavaScript payload into the protection plan name field during creation in the Acronis Cyber Protect Console, exploiting insufficient input sanitization to store HTML and script elements persistently.

## Description

The vulnerability stems from lack of escaping in the plan name field under PLANS > Protection > Create Plan. By using a payload like <video><source onerror="javascript:alert(document.domain)">, attackers can embed executable JavaScript that triggers on specific UI interactions. This stored XSS allows arbitrary code execution in the browser of any user viewing or acting on the plan, potentially leading to session hijacking or phishing.

## Requirements

1. Authenticated session in Acronis Console
2. Access to a device with installed agent (e.g., tester's PC)
3. Knowledge of XSS payloads exploiting onerror events

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs in plan names using HTML entity encoding
- Implement content security policy (CSP) to restrict inline JavaScript execution
- Log and review plan creation events for suspicious payloads (e.g., script tags)

## Objectives

1. Store malicious payload in plan metadata
2. Ensure payload survives creation without triggering prematurely
3. Enable later execution for impact

## Instructions

### Step 1: Navigate to Plans Section

**Context**: Access the creation interface for protection plans.

From the dashboard, click 'PLANS' > 'Protection'.

> The plans list loads; look for the 'Create Plan' button.

### Step 2: Initiate Plan Creation and Add Device

**Context**: Set up the plan structure before injecting the payload.

Click 'Create Plan', then 'Add devices' and select a target device (e.g., PC with agent).

> Device selection confirms; proceed to naming.

### Step 3: Inject Payload in Name Field

**Context**: Exploit the unsanitized input to store the XSS.

In the plan name field, enter: <video><source onerror="javascript:alert(document.domain)">

> The field accepts the HTML without validation.

### Step 4: Submit and Confirm Creation

**Context**: Persist the payload in the system.

Click 'Create' and wait for processing to complete.

> Plan appears in the list with the payload name intact.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[stored-xss]]
- [[JavaScript]]
