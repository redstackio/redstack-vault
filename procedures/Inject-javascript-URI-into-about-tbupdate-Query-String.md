---
tags:
  - xss
  - javascript-uri
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Browser
  - Tor Browser
submitted: true
created_at: '[TIMESTAMP]'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:39.403Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 26274dab-398c-4c03-80c3-0debbe721f05
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-javascript-URI-into-about-tbupdate-Query-String

## Summary

This procedure injects a javascript: URI into the query string of the Tor Browser's about:tbupdate page, exploiting a lack of validation to prepare for reflected XSS execution.

## Description

The about:tbupdate page in Tor Browser (a Firefox-based browser) processes query string parameters without validation, allowing javascript: URIs to be accepted. This sets up the payload for execution upon user interaction. The vulnerability is limited by the nsIAboutModule::URI_SAFE_FOR_UNTRUSTED_CONTENT flag, preventing chrome privileges, but enables JS on a NoScript-whitelisted page for potential tracking or fingerprinting.

## Requirements

1. Tor Browser installed and running
2. Direct access to the browser's address bar
3. No additional tools or network access needed

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all query string inputs in about: pages
- Enforce strict URI scheme whitelisting (e.g., block javascript:)
- Monitor for unexpected JS execution in trusted pages via browser logs

## Objectives

1. Deliver the XSS payload via URL manipulation
2. Load the vulnerable page with injected parameter
3. Prepare for payload trigger without immediate detection

## Instructions

### Step 1: Navigate to Vulnerable URL

**Context**: Directly access the about:tbupdate page with the malicious query string to inject the javascript: URI.

Enter the following URL in the Tor Browser address bar:

```plaintext
about:tbupdate?javascript:alert(1)
```

> This injects the javascript:alert(1) URI into the query string. The page loads, displaying Tor update information, but the payload is not yet executed. Verify the URL in the address bar to confirm the parameter is present.

**Expected Output**: about:tbupdate page loads successfully with the query string visible.

### Step 2: Verify Injection

**Context**: Confirm the injection without triggering execution to assess setup.

Inspect the page source or URL to ensure the javascript: parameter is processed but inert until interaction.

> No command needed; manual inspection. Look for any immediate errors or warnings in the browser console (if developer tools are enabled).

**Expected Output**: No JS execution yet; page renders normally.

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
- [[javascript-uri]]
