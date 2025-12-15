---
id: proc-undici-analyze-001
name: Analyze-Proxy-Header-Leakage
tags:
  - analysis
  - leakage
  - undici
  - information-disclosure
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:29:56.619Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques:
  - '[[Credentials In Files]]'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Analyze-Proxy-Header-Leakage

## Summary

This procedure examines the output from the undici PoC execution to confirm that the Proxy-Authorization header is not cleared during cross-origin redirects, validating the information disclosure vulnerability and its potential to compromise proxy credentials.

## Description

Following PoC execution in a Node.js environment, this procedure involves logging and inspecting response details (status, headers, body) from undici requests, alongside capturing incoming requests on the attacker endpoint (port 8182). The analysis reveals if Proxy-Authorization persists post-redirect, enabling unauthorized access to proxies. This targets scenarios where applications use undici behind authenticated proxies and encounter malicious redirects.

## Requirements

1. Output from executed PoC script (console logs).
2. Logs from attacker server capturing the redirected request.
3. Knowledge of HTTP protocol and header inspection.

## Defense

Defensive measures and detection strategies:

- Patch undici to include Proxy-Authorization clearing.
- Implement logging and alerting for sensitive headers in outbound requests.
- Use network proxies that strip auth headers on redirects.

## Objectives

1. Inspect undici response for redirect behavior.
2. Verify header presence in captured attacker request.
3. Document the leakage for reporting or mitigation.

## Instructions

### Step 1: Review PoC Console Output

**Context**: Check the script's logged response to ensure redirect occurred.

Examine console output for statusCode (e.g., 200), headers, and body from the final endpoint.

> Successful redirect shows no errors; body may contain attacker page content.

### Step 2: Inspect Attacker Server Logs

**Context**: Confirm the leaked header in the incoming request.

Review logs on the server at port 8182 for the full request, including headers like Proxy-Authorization: 'xxxxxxxx'.

> Evidence of leakage: Header present and matching the sent value, uncledared.

### Step 3: Validate Against Spec

**Context**: Cross-reference with Fetch API to confirm violation.

Note that Proxy-Authorization should be forbidden and cleared, but undici fails to do so.

> Outcome: Validation of vulnerability for disclosure in applications.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques

- [[Credentials In Files]] Credentials In Files

## Commands Used


## Tools Used


## Tags

- [[analysis]]
- [[information-disclosure]]
