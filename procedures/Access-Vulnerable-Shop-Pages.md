---
tags:
  - web
  - recon
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:12.239Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 75780d18-ad74-4f5f-838a-01bd370ed153
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Vulnerable-Shop-Pages

## Summary

This procedure involves navigating to the shop pages on marthastewart.com and bhg.com to access the vulnerable search parameter, setting the stage for XSS testing.

## Description

The shop pages at https://marthastewart.com/shop/all.html?s= and https://bhg.com/shop/all.html?s= reflect user input from the ?s= parameter without sanitization. Accessing these pages allows inspection of the search functionality and preparation for payload injection. No tools are required beyond a standard web browser.

## Requirements

1. Internet access to public websites
2. Web browser with developer tools
3. No authentication or special permissions needed

## Defense

Defensive measures and detection strategies:

- Implement web application firewalls (WAF) to monitor access patterns
- Log unusual URL parameter lengths or characters

## Objectives

1. Confirm page accessibility and search parameter presence
2. Identify reflection points for input
3. Prepare for subsequent exploitation steps

## Instructions

### Step 1: Navigate to Target URLs

**Context**: Directly access the shop pages to load the vulnerable endpoints.

Open a web browser and enter the URLs:

```url
https://marthastewart.com/shop/all.html?s=
https://bhg.com/shop/all.html?s=
```

> The pages should load, displaying shop items with an empty search. Inspect the page source to see how the ?s= value is reflected, typically in a script tag or HTML attribute.

### Step 2: Inspect Page for Reflection

**Context**: Use browser tools to locate where the search input is echoed back.

Right-click and select "Inspect Element" or press F12, then search for the ?s= value in the DOM or scripts.

> Expected output: The input appears unsanitized, e.g., in a JavaScript string like var search = '?s=value';, vulnerable to breakout.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web
- recon
