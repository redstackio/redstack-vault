---
tags:
  - xss
  - execution
  - mouseover
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '[TIMESTAMP]'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:31.680Z'
sub_techniques: []
id: 1c36f81f-d20f-421d-bace-b0f99b1c4aa8
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Payload-via-Mouseover

## Summary

This procedure loads the crafted PoC in a browser and performs user interaction to execute the injected JavaScript, verifying the DOM-based XSS.

## Description

After redirection, the vulnerable page loads with the malicious referrer embedded in the 'Search Results' link href. Hovering over the link triggers the onmouseover event, executing alert(document.domain) in the browser context, potentially allowing session hijacking or data theft.

## Requirements

1. Compatible browser (e.g., Internet Explorer for legacy support)
2. PoC URL from previous step
3. No ad blockers or strict security settings

## Defense

Defensive measures and detection strategies:

- Disable or restrict mouseover events in generated HTML
- Employ XSS auditors or WAF rules for client-side injections
- Educate users on phishing via referrers
- Regularly audit JS for DOM sinks

## Objectives

1. Confirm payload execution on interaction
2. Validate arbitrary JS in victim context
3. Assess impact (e.g., domain alert)

## Instructions

### Step 1: Load PoC URL

**Context**: Navigate to the redirector link to set referrer and load target.

Open https://kb.informatica.com/solution/4/Pages/17377.aspx?myk=xxx via the PoC in Internet Explorer and wait for full load.

### Step 2: Inspect Breadcrumb

**Context**: Verify the 'Search Results' link contains injected href.

Use dev tools to check the anchor tag for the payload in href attribute.

### Step 3: Trigger Interaction

**Context**: Perform mouseover to execute.

Hover mouse over the 'Search Results' breadcrumb; observe alert popup with domain.

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
- [[Execution]]
- [[mouseover]]
