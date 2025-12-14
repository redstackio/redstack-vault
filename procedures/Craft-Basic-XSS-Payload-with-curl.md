---
tags:
  - xss
  - payload-crafting
  - poc
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-reflected-xss-poc]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 7183fae1-1eb2-4962-855f-536b734bc5d4
created_at: '2025-12-14T03:47:13.097Z'
updated_at: '2025-12-14T03:47:13.097Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Basic-XSS-Payload-with-curl

## Summary

This procedure crafts and tests a basic reflected XSS payload in Revive Adserver's /www/delivery/afr.php by injecting '</script><script>alert(1)</script>' into the 'refresh' parameter, bypassing the prior fix and confirming unescaped output via curl.

## Description

The attack exploits the incomplete escaping in the JavaScript context of the endpoint's response, where the 'refresh' parameter is embedded in a setTimeout call within a script tag. By appending '&</script><script>alert(1)</script>' to 'refresh=10000', the payload closes the existing tag and opens a new one, executing alert(1) if rendered in a browser. This is tested non-interactively with curl to observe the reflected payload, useful for initial proof-of-concept in penetration testing against ad servers.

## Requirements

1. curl installed on the attacker's machine
2. HTTP access to the target Revive Adserver instance
3. Basic understanding of URL encoding and script contexts

## Defense

Defensive measures and detection strategies:

- Enforce strict URL decoding and HTML/JS entity encoding on all inputs server-side
- Deploy Web Application Firewall (WAF) rules to block payloads containing '</script>' patterns
- Log and alert on requests with suspicious query strings including script tags

## Objectives

1. Demonstrate script tag closure to bypass sanitization
2. Verify reflection without browser execution
3. Collect evidence of the vulnerability for reporting

## Instructions

### Step 1: Prepare the Payload

**Context**: Construct the payload to close the existing script and inject a test alert.

No command; manually build: refresh=10000&</script><script>alert(1)</script>

> Expected: Payload string ready for URL insertion.

### Step 2: Test with curl

**Context**: Send the request and inspect the response for unescaped payload.

**Command** ([[commands/curl-reflected-xss-poc]]):
```bash
curl "https://revive-instance/www/delivery/afr.php?refresh=10000&</script><script>alert(1)</script>"
```

> This fetches the response; grep for 'alert(1)' to confirm reflection. Expected output includes the unescaped payload in the setTimeout string, indicating successful injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-reflected-xss-poc]]

## Tools Used

- [[tools/curl]]

## Tags

- [[xss]]
- [[poc]]
