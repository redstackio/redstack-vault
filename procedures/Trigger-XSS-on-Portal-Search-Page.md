---
tags:
  - xss
  - trigger
  - portal-search
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: 03bff6af-1d47-432d-81a6-948e0fa4ba8d
created_at: '2025-12-14T00:11:16.149Z'
updated_at: '2025-12-14T00:11:16.149Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-on-Portal-Search-Page

## Summary

This procedure triggers the stored XSS payload on the portal search page, executing JavaScript when users interact with search functionality.

## Description

The search page incorporates the same stored portal content, rendering the malicious HTML. This broadens impact to customer-facing views, allowing attacks on non-admin users. Execution occurs on page load or search initiation, enabling phishing, keylogging, or credential theft in the app's domain context.

## Requirements

1. Payload injected and saved previously
2. Access to the search endpoint
3. Victim browsing the portal

## Defense

Defensive measures and detection strategies:

- Apply output encoding to all rendered content
- Use strict CSP headers to prevent JS execution
- Detect anomalous script events in client-side logs
- Limit search page content to sanitized snippets

## Objectives

1. Execute JS in search context
2. Demonstrate cross-user impact
3. Highlight escalation to customer sessions

## Instructions

### Step 1: Access Search Page

**Context**: Load the search interface with embedded content.

Navigate to `https://services.alveo.io/portal/search?shop=<shop>.myshopify.com`.

### Step 2: Initiate Render

**Context**: Cause payload execution.

The page loads and displays content; the <img> tag triggers onerror and alert(2).

### Step 3: Test in Victim Session

**Context**: Simulate real-world access.

Use incognito or another account to confirm execution without prior knowledge.

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
- [[trigger]]
- [[portal-search]]
