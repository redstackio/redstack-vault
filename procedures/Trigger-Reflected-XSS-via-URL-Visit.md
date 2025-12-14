---
id: proc-003
tags:
  - xss
  - execution
  - client-side
type: procedure
tools: []
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:16:02.580Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Trigger Reflected XSS via URL Visit

## Summary

This procedure executes the reflected XSS attack by loading the crafted malicious URL in an authenticated browser session, causing the injected JavaScript payloads to reflect and run, demonstrating arbitrary code execution such as alerting cookies or domain information.

## Description

Upon visiting the PoC URL, the server reflects the unsanitized parentPageString and labelsString parameters back into the HTML response, breaking out of context with the injected <img> tags. The onerror handlers trigger JavaScript execution in the victim's browser, allowing access to client-side data. This is a classic reflected XSS, effective against signed-in users via phishing or direct access.

## Requirements

1. Authenticated session from prior steps
2. Crafted PoC URL from the injection procedure
3. Vulnerable target environment (TopCoder wiki)

## Defense

Defensive measures and detection strategies:

- Deploy browser-based protections like XSS auditors
- Log and alert on JavaScript errors or unusual alert executions
- Educate users on phishing risks with malicious links

## Objectives

1. Execute the payloads to confirm vulnerability
2. Capture sensitive data like session cookies
3. Validate impact for reporting or exploitation

## Instructions

### Step 1: Load the Malicious URL

**Context**: Visit the URL while authenticated to trigger reflection.

Paste the PoC URL into the browser address bar:

https://apps.topcoder.com/wiki/pages/createpage.action?spaceKey=tcwiki&parentPageString=powerpuff_hackerone%22%3E%3Cimg%20src=X%20onerror=alert(document.cookie)%3E&labelsString=%22%3E%3Cimg+src%3DX+onerror%3Dalert(document.domain)%3E

> The page loads, and payloads execute immediately.

### Step 2: Observe Execution

**Context**: Verify the JavaScript runs and displays data.

Look for alert dialogs showing cookie values and the domain 'topcoder.com'.

> Successful execution confirms the XSS, with potential for further payloads like keyloggers.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
- [[browser]]
