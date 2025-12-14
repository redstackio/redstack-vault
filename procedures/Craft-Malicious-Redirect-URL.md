---
tags:
  - xss
  - url-crafting
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/craft-xss-payload-url]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 063fa3d0-cb6a-4b7d-bb66-85c810078b1c
created_at: '2025-12-14T00:11:25.244Z'
updated_at: '2025-12-14T00:11:25.244Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft Malicious Redirect URL

## Summary

This procedure involves crafting a URL with a malicious dest parameter set to a javascript: URI to prepare for XSS exploitation on accounts.reddit.com.

## Description

The procedure focuses on manually or programmatically creating a URL that exploits improper sanitization of the dest parameter, allowing javascript: schemes to execute code in the victim's browser. This is typically used in phishing or direct link attacks targeting logged-in users.

## Requirements

1. Access to a text editor or scripting environment
2. Knowledge of the target URL structure
3. No special credentials required

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization on redirect parameters to block javascript: URIs
- Use Content Security Policy (CSP) to restrict script execution

## Objectives

1. Create a functional malicious URL
2. Ensure the payload is correctly encoded
3. Prepare for delivery to victim

## Instructions

### Step 1: Construct the Base URL

**Context**: Start with the base Reddit accounts URL and append the dest parameter.

**Command** ([[commands/craft-xss-payload-url]]):
```bash
echo 'https://accounts.reddit.com/?dest=javascript:alert(document.domain)' > malicious_url.txt
```

> This creates a file with the crafted URL, which can be shared or tested.

### Step 2: Test Payload Syntax

**Context**: Verify the javascript: payload is valid and will execute as intended.

> Manually inspect the URL or test in a safe environment to ensure no encoding issues.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/craft-xss-payload-url]]

## Tools Used



## Tags

- [[xss]]
- [[url-crafting]]
