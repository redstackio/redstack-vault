---
id: proc-execute-stored-xss
tags:
  - xss
  - execution
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
updated_at: '2025-12-14T03:15:35.567Z'
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
# Execute Stored XSS on Search Results Page

## Summary

This procedure triggers the stored XSS payload by loading the search results page in Concrete CMS, causing the malicious JavaScript to execute in the browser context of any viewing user.

## Description

The Search Title, now containing the injected payload, is rendered without escaping on the search results page. When loaded, the HTML parses the <img> tag, fails to load src=x, and fires the onerror event to run alert(1) or advanced payloads like cookie theft. This affects all users, including admins, leading to client-side attacks such as session hijacking or phishing.

## Requirements

1. Payload persisted in search configuration
2. Access to the public or authenticated search results page
3. Victim browser (can be self for testing)

## Defense

Defensive measures and detection strategies:

- Apply output encoding (e.g., htmlspecialchars) when rendering titles in templates
- Implement browser-side CSP headers to block unsafe inline scripts
- Monitor for unexpected JavaScript execution via client-side logging or anomaly detection

## Objectives

1. Render the tainted title to trigger script execution
2. Demonstrate impact like alerts or data exfiltration
3. Highlight cross-site effects on other users

## Instructions

### Step 1: Access Search Results

**Context**: Navigate to the search functionality and perform a search to load the results page where the title is rendered.

Use the site's search bar to query any term.

> Expected: Page loads with the search title in the HTML, parsing the payload.

### Step 2: Observe Execution

**Context**: Inspect the page source or watch for JavaScript effects as the payload executes.

Open browser developer tools (F12) and monitor the console.

> Expected output: onerror event fires, showing alert(1) popup; console may log execution. In production, replace with document.cookie exfiltration.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- execution
