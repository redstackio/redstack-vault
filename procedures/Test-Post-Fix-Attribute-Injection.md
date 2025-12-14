---
tags:
  - xss
  - attribute-injection
  - open-redirect
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 8e53586f-6690-44c9-be21-40c501120d43
created_at: '2025-12-14T03:46:38.194Z'
updated_at: '2025-12-14T03:46:38.194Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test-Post-Fix-Attribute-Injection

## Summary

After a partial fix blocks direct script injection, this procedure tests for attribute injection in meta tags, including onclick handlers requiring interaction and open redirects via http-equiv=refresh.

## Description

Post-fix, the endpoint may still allow attribute breaks like " onclick=alert(1) accesskey=x, executable via keyboard shortcuts (e.g., SHIFT+ALT+X). Additionally, injecting into meta refresh enables phishing redirects. Testing uses encoded payloads to probe remaining flaws, with outcomes showing limited but persistent risks.

## Requirements

1. Knowledge of the partial fix status
2. Browser supporting accesskey (e.g., Chrome)
3. Target endpoint post-remediation

## Defense

Defensive measures and detection strategies:

- Strip or validate all HTML attributes on user input
- Disable meta refresh or validate redirect URLs
- Detect keyboard shortcut anomalies in session logs

## Objectives

1. Exploit attribute injection for conditional XSS
2. Demonstrate open redirect for phishing
3. Evaluate fix completeness

## Instructions

### Step 1: Test Onclick Injection

**Context**: Inject attributes into meta tag for interactive execution.

Encode %22%20onclick=alert%601%60%20accesskey=x and use in /category/[payload]. Load page, then press SHIFT+ALT+X.

> Expected: Alert on keypress, confirming injection.

### Step 2: Test Open Redirect

**Context**: Inject refresh directive for automatic redirect.

Use payload %22%20content=%220;url=http://evil.com%22 in slug. Load URL.

> Expected: Browser redirects to evil.com without prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[attribute-injection]]

