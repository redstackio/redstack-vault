---
tags:
  - xss
  - persistence
  - deployment
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chromium]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:20.436Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 152d4572-8a68-4fa9-ac03-7fbadad06ca6
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Deploy-and-Persist-XSS-Payload

## Summary

This procedure deploys the flow containing the XSS payload, storing it persistently and enabling execution for all users accessing the Node-RED dashboard.

## Description

Deployment saves the flow configuration, including malicious node/flow names, to the backend. Upon reload or access by other users, the unsanitized names render as HTML, executing the script. This turns reflected XSS into stored, broadening impact to session hijacking or data theft. Alternative injection via flow names uses the same mechanism.

## Requirements

1. Node-RED UI open with injected payload
2. Browser session active
3. No authentication barriers in local setup

## Defense

Defensive measures and detection strategies:

- Validate and escape user inputs server-side before storage
- Audit flow deployments for suspicious content (e.g., script tags)
- Use browser extensions to detect and block XSS payloads

## Objectives

1. Store the XSS payload in the flow configuration
2. Ensure persistence across sessions and users
3. Demonstrate impact on dashboard access

## Instructions

### Step 1: Deploy Flow

**Context**: Save the workspace to persist the injected node name payload.

**Instructions**: With the payload node in the workspace, click the red 'Deploy' button in the top-right of the UI.

> Expected output: 'Deploy successful' message; the flow is now stored, and accessing the node tab triggers the alert.

### Step 2: Alternative Flow Name Injection

**Context**: Test persistence via top-level flow name for broader execution.

**Instructions**: Click the '+' tab to add a new flow, enter `<script>alert('xss')</script>` in the name field, then deploy. Double-click the flow tab to view.

> The alert executes on render, confirming stored nature affecting all viewers.

### Step 3: Validate Persistence

**Context**: Restart the server and re-access to confirm.

**Instructions**: Stop the server (Ctrl+C), restart with [[commands/node-red-start-server]], and navigate to http://localhost:1880. Select the flow/node.

> Alert triggers again, proving persistence.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Chromium]]

## Tags

- xss
- persistence
- deployment
