---
tags:
  - xss-trigger
  - javascript-execution
  - view-objects
  - concrete-cms
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
updated_at: '2025-12-14T03:16:02.518Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 97494faf-6009-4d03-bab9-5f9354364cf5
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-in-View-Objects

## Summary

This procedure demonstrates how to render the malicious Express entity in Concrete CMS to trigger the stored XSS, executing arbitrary JavaScript in the victim's browser context.

## Description

After creating the entity with the XSS payload, switching to the View Objects tab causes the Name field to render without escaping, executing the script. This can be shared via link to target other admins. Impact includes alert popups for proof-of-concept or advanced payloads for cookie theft/data exfiltration. Assumes the entity exists; targets authenticated sessions.

## Requirements

1. Created Express entity with XSS payload
2. Admin session in the same browser
3. Vulnerable Concrete CMS 8.5.2
4. Browser without XSS protections disabled for testing

## Defense

Defensive measures and detection strategies:

- Apply patches to Concrete CMS (upgrade beyond 8.5.2)
- Enable strict CSP headers to block inline scripts
- Audit rendered content for unescaped outputs; use template engines with auto-escaping
- Detect via browser dev tools or proxy for unexpected script execution

## Objectives

1. Render the entity to execute the payload
2. Confirm JavaScript runs in admin context
3. Demonstrate potential for broader compromise

## Instructions

### Step 1: Access Entity Management

**Context**: Return to the Express entities section.

**Action**:

- Ensure you're in /index.php/dashboard/system/express/entities.

> Select the malicious entity if needed.

### Step 2: Switch to View Objects Tab

**Context**: Load the view where the Name is rendered unsafely.

**Action**:

- Click on the 'View Objects' tab.

> The list of objects displays, rendering the Name field.

### Step 3: Observe Execution

**Context**: Verify the XSS triggers.

**Action**:

- The payload executes automatically upon render.

> An alert(1) box appears; inspect console for script details.

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
- [[javascript-execution]]
- [[view-objects]]
- [[concrete-cms]]
