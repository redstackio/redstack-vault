---
tags:
  - xss
  - url-injection
  - flash
type: procedure
tools:
  - '[[tools/Google-Chrome]]'
  - '[[tools/Mozilla-Firefox]]'
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
updated_at: '2025-12-14T03:16:07.872Z'
sub_techniques: []
id: 36a793a7-8bef-4f5e-a858-7591e5b66917
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Access-Plupload-Flash-Vulnerable-URL

## Summary

This procedure involves navigating to a crafted URL targeting the Plupload Flash SWF file in WordPress, injecting encoded JavaScript parameters to trigger reflected XSS upon loading.

## Description

The vulnerability stems from an outdated Plupload version lacking input sanitization for Flash parameters. By accessing https://business-blog.zomato.com/wp-includes/js/plupload/plupload.flash.swf?target%g=alert&uid%g=hello&, the %g encoding (representing a space or Flash-specific delimiter) allows JavaScript injection. This executes in modern browsers when the SWF loads, bypassing typical XSS filters due to Flash's handling.

## Requirements

1. Prepared browsers (Chrome/Firefox latest)
2. Direct access to the target WordPress site
3. Knowledge of the vulnerable path /wp-includes/js/plupload/plupload.flash.swf

## Defense

Defensive measures and detection strategies:

- Update Plupload to the latest version with proper parameter sanitization
- Remove or disable legacy Flash SWF files in WordPress installations
- Implement Content Security Policy (CSP) to restrict script execution from SWF sources
- Log and alert on unusual parameter encodings in URL access logs

## Objectives

1. Deliver the XSS payload via URL parameters to the Flash SWF
2. Trigger loading of the vulnerable file with injected code
3. Set up conditions for JavaScript execution in the victim's context

## Instructions

### Step 1: Navigate in Chrome

**Context**: Use Chrome to access the vulnerable URL and load the SWF with payload.

Manually enter or paste the URL into the address bar: https://business-blog.zomato.com/wp-includes/js/plupload/plupload.flash.swf?target%g=alert&uid%g=hello&

> Expected: Page loads the SWF file; parameters are passed without sanitization.

### Step 2: Navigate in Firefox

**Context**: Repeat in Firefox to confirm cross-browser vulnerability.

Manually enter or paste the URL into the address bar: https://business-blog.zomato.com/wp-includes/js/plupload/plupload.flash.swf?target%g=alert&uid%g=hello&

> Expected: SWF loads similarly, preparing for payload execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome]]
- [[tools/Mozilla-Firefox]]

## Tags

- [[reflected-xss]]
- [[plupload]]
