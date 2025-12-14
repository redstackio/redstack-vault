---
tags:
  - automation
  - javascript-poc
  - cache-poisoning
type: procedure
tools:
  - '[[tools/Custom-POC-HTML-JS-Script]]'
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
updated_at: '2025-12-14T17:25:13.486Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: ce890777-f4e9-4fa2-9143-52e88b7996b3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Automate-Cache-Poisoning-Using-JavaScript-PoC

## Summary

This procedure uses a custom JavaScript-based PoC to automate the generation of random .css URLs and poison the cache while authenticated, scaling the attack for multiple endpoints.

## Description

The PoC runs in a browser, generating random 10-character IDs from an alphanumeric set, constructing URLs like `https://www.lyst.com/[random].css`, and opening them in popups to trigger caching. It closes popups after 3 seconds and logs URLs for retrieval. This targets cache poisoning vulns in web apps, enabling efficient data exfiltration.

## Requirements

1. Authenticated browser session on the target site
2. Local HTML file with the PoC script
3. Browser allowing popups and JavaScript execution

## Defense

Defensive measures and detection strategies:

- Block or monitor popup-based requests to cacheable endpoints
- Rate-limit requests to unusual URL patterns (e.g., random .css)
- Implement client-side CSP to restrict dynamic script behaviors

## Objectives

1. Generate and poison multiple cache entries automatically
2. Collect URLs for subsequent unauthenticated retrieval
3. Demonstrate scalable impact on user data exposure

## Instructions

### Step 1: Prepare and Load PoC

**Context**: Set up the automation script in an authenticated session.

Save the PoC as an HTML file and open it in a browser while logged into the target site. The script uses `alphaWithNumber = 'QWERTZUIOPASDFGHJUKLYXCVBNM1234567890';` for ID generation.

> Expected output: Script initializes without errors.

### Step 2: Execute Poisoning

**Context**: Trigger URL generation, popup opening, and caching.

Run the script's main function. It generates a random ID (e.g., 'A1B2C3D4E5'), builds `https://www.lyst.com/A1B2C3D4E5.css`, opens in a popup (interval check every 200ms), waits 3000ms, closes, and alerts the full URL.

> Expected output: Alert with URL like `https://www.lyst.com/A1B2C3D4E5.css`; cache poisoned for that endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Custom-POC-HTML-JS-Script]]

## Tags

- [[web-cache-poisoning]]
- [[automation]]
