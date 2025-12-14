---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - xss-execution
  - redirection
  - phishing
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:37.222Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Viewing-Tainted-Project

## Summary

This procedure accesses a tainted Khan Academy project to execute the stored XSS payload, demonstrating how viewers' browsers run the injected JavaScript, such as redirecting to external sites.

## Description

After injection, the project URL (e.g., https://www.khanacademy.org/physics/woah/4740384569491456) renders the unsanitized HTML, triggering event handlers like onload in the <img> tag. This executes the script in the viewer's session, enabling attacks like phishing or cookie theft. No special tools needed beyond a browser; impacts any authenticated or guest viewer.

## Requirements

1. URL of the tainted project
2. Victim browser (can be self for testing)
3. No additional credentials if public

## Defense

Defensive measures and detection strategies:

- Render user-generated content in iframes with sandboxing
- Implement client-side XSS filters or escape outputs
- Monitor for unexpected redirects in browser logs

## Objectives

1. Load the project to trigger payload
2. Observe script execution (e.g., redirect)
3. Confirm vulnerability impact

## Instructions

### Step 1: Access the Project URL

**Context**: Navigate to the tainted project to initiate rendering.

Open a browser and visit the project URL, such as https://www.khanacademy.org/physics/woah/4740384569491456.

**Expected Output**: Page loads with project content.

### Step 2: Observe Payload Execution

**Context**: The HTML renders, firing the JavaScript event.

Watch for the onload or onerror to trigger; e.g., browser redirects to the external site.

**Expected Output**: Alert, redirect, or console log confirming execution.

### Step 3: Validate in Victim Context

**Context**: Test in an incognito or separate session to simulate another user.

Repeat access without your session cookies to ensure cross-user impact.

**Expected Output**: Consistent execution across sessions.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-execution]]
- [[redirection]]
