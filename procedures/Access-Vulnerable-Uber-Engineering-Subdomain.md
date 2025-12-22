---
id: proc-access-uber-subdomain
tags:
  - web
  - access
  - subdomain
type: procedure
tools:
  - '[[tools/DominatorPro]]'
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
updated_at: '2025-12-14T03:15:47.353Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Vulnerable-Uber-Engineering-Subdomain

## Summary

This procedure involves navigating to the eng.uber.com subdomain to load the page and initialize the vulnerable prettyPhoto plugin, enabling subsequent URL hash manipulations for DOM-based XSS exploitation.

## Description

The prettyPhoto plugin on eng.uber.com processes URL fragments (hashes) without proper sanitization, allowing attackers to inject payloads that alter the DOM client-side. This step establishes the attack surface by accessing the site in a compatible browser, where the plugin is active. No server-side interaction occurs beyond initial page load, making it stealthy. Expected outcomes include plugin readiness for payload injection, potentially leading to JavaScript execution for data theft or session hijacking.

## Requirements

1. Web browser with JavaScript enabled (e.g., Firefox, Chrome, IE)
2. Internet access to reach eng.uber.com
3. Optional: XSS testing tool like DominatorPro for payload validation

## Defense

Defensive measures and detection strategies:

- Update or remove outdated plugins like prettyPhoto
- Implement Content Security Policy (CSP) to restrict inline script execution
- Monitor browser developer tools for unexpected DOM changes or alerts

## Objectives

1. Load the vulnerable page to activate the prettyPhoto plugin
2. Verify plugin presence without triggering defenses
3. Prepare for hash-based payload injection

## Instructions

### Step 1: Navigate to Target URL

**Context**: Directly access the subdomain to load the vulnerable script, ensuring the plugin initializes in the browser context.

No command required; use browser navigation:

Open `http://eng.uber.com/` in your browser.

> This loads the page, injecting the prettyPhoto JavaScript. Inspect the DOM (F12) to confirm prettyPhoto elements or scripts are present.

### Step 2: Verify Plugin Loading

**Context**: Confirm the vulnerability context is active before proceeding to payload injection.

Use browser console to check:

```javascript
if (typeof $.fn.prettyPhoto !== 'undefined') { console.log('Plugin loaded'); }
```

> Expected output: "Plugin loaded" in console, indicating readiness for exploitation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/DominatorPro]]

## Tags

- [[web]]
- [[access]]
