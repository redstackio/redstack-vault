---
tags:
  - csp-bypass
  - script-injection
  - analytics-exploit
type: procedure
tools: []
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
updated_at: '2025-12-13T23:52:44.101Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 14dc70fe-b21e-40bf-b822-06d90d967e12
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Bypass-CSP-via-Analytics-Endpoint

## Summary

This procedure exploits a vulnerability in the Twitter analytics endpoint (https://analytics.twitter.com/tpm) to bypass Content Security Policy restrictions, allowing the loading and execution of external scripts that would otherwise be blocked.

## Description

The CSP on Twitter domains typically restricts script sources, but the /tpm endpoint on analytics.twitter.com permits callback functions that execute JavaScript, effectively bypassing the policy. This is based on a known issue from report #126464. The procedure involves crafting script tags that source from this endpoint with a callback parameter containing the payload. In the context of an XSS attack, this enables execution of arbitrary code like alerts or data exfiltration. Prerequisites include awareness of the endpoint's behavior and a vector for injection, such as the reflected XSS in the careers page.

## Requirements

1. Knowledge of the target site's CSP policy via browser inspection
2. Access to the analytics subdomain
3. A injection point (e.g., from prior XSS identification)

## Defense

Defensive measures and detection strategies:

- Audit and restrict analytics endpoints to prevent unauthorized script execution
- Implement nonce or hash-based CSP for scripts to block external sources
- Monitor for anomalous script loads from analytics domains in logs

## Objectives

1. Load a script from the vulnerable analytics endpoint
2. Execute JavaScript payload via the tpm_cb parameter
3. Confirm bypass by running a test alert

## Instructions

### Step 1: Inspect CSP Policy

**Context**: Use browser tools to view the current CSP header on the target page.

Load https://careers.twitter.com and check Network tab or console for CSP directives like script-src.

> Note restrictions (e.g., 'self' only); identify if analytics.twitter.com is whitelisted.

### Step 2: Craft Bypass Payload

**Context**: Build a script tag using the /tpm endpoint with a callback.

Payload: <script src="//analytics.twitter.com/tpm?tpm_cb=alert(document.domain)"></script>

Test in a local HTML file or console to verify execution.

> Success if alert fires without CSP violation.

### Step 3: Validate in Target Context

**Context**: Inject the payload into a reflected parameter and observe.

Combine with location parameter: ?location=1%22%3E%3Cscript%20src=//analytics.twitter.com/tpm?tpm_cb=alert(document.domain)%3E%3C/script%3E

Visit and check console for execution.

> Expected: Payload runs, confirming bypass integration.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csp-bypass]]
- [[script-injection]]
