---
tags:
  - xss
  - payload-injection
  - express-entities
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
updated_at: '2025-12-14T03:16:02.520Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 9a6431cd-510b-4f50-b367-e9641c9357ea
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Express-Entity-with-XSS-Payload

## Summary

This procedure involves navigating to the Express entities management in Concrete CMS, creating a new entity, and injecting a stored XSS payload into the Name field to store malicious JavaScript for later execution.

## Description

Express entities in Concrete CMS allow custom data objects. The Name field lacks proper escaping, enabling stored XSS. An authenticated admin creates an entity via the dashboard, injects HTML/JS like '</h1><script>alert(1)</script><h1>', and saves it. The payload persists and executes when rendered. This targets admin users viewing shared links, potentially leading to session theft. Prerequisites include admin access.

## Requirements

1. Authenticated admin session in Concrete CMS 8.5.2
2. Web browser for form interaction
3. Knowledge of XSS payloads
4. No client-side validation bypassing needed (server-side flaw)

## Defense

Defensive measures and detection strategies:

- Implement output encoding (e.g., htmlspecialchars) for user inputs in templates
- Use Content Security Policy (CSP) to restrict script execution
- Validate and sanitize inputs server-side; audit entity fields
- Monitor for anomalous JavaScript in database entries

## Objectives

1. Store malicious payload in the entity Name field
2. Ensure payload saves without sanitization
3. Set up for subsequent triggering and execution

## Instructions

### Step 1: Navigate to Express Entities

**Context**: Access the management interface for entities.

**Action**:

- From dashboard, go to System & Settings > Express Entities.
- URL: /index.php/dashboard/system/express/entities.

> The entities list page loads.

### Step 2: Initiate Entity Creation

**Context**: Start the form for a new entity.

**Action**:

- Click the 'Create' button.

> A form opens with fields including Name, Handle, etc.

### Step 3: Inject XSS Payload

**Context**: Enter the malicious input in the vulnerable field.

**Action**:

- In the Name field, paste: `</h1><script>alert(1)</script><h1>`.
- Fill other required fields minimally (e.g., Handle: test-entity).
- Click 'Save'.

> Entity saves; payload is stored unescaped.

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
- [[payload-injection]]
- [[express-entities]]
- [[concrete-cms]]
