---
id: proc-identify-xss-endpoint
tags:
  - xss
  - recon
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-endpoint-inspect]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T00:11:16.022Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Vulnerable Endpoint for XSS

## Summary

This procedure involves examining a web endpoint to identify input parameters that may be vulnerable to cross-site scripting (XSS) attacks by checking for reflection of user input.

## Description

In the context of the Glassdoor help page, this step targets the https://help.glassdoor.com/gd_requestsubmitpage endpoint. The attacker inspects the page for parameters like 'lang' that are reflected back in the response without proper sanitization, setting the stage for XSS exploitation. Prerequisites include basic web knowledge and tools for HTTP requests. Expected outcomes include confirmation of parameter reflection, enabling further testing.

## Requirements

1. Public access to the target URL
2. HTTP client like curl or browser
3. Knowledge of common injection points

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to restrict script execution
- Log and monitor unusual parameter values in requests
- Use web application firewalls (WAF) to detect injection patterns

## Objectives

1. Locate user-controlled input parameters on the endpoint
2. Verify if inputs are echoed in the response
3. Identify potential XSS entry points

## Instructions

### Step 1: Request the Endpoint

**Context**: Send a basic request to the endpoint to observe its structure and parameters.

**Command** ([[commands/curl-endpoint-inspect]]):
```bash
curl "https://help.glassdoor.com/gd_requestsubmitpage"
```

> This command fetches the page content. Look for forms or query parameters in the response.

### Step 2: Inspect for Parameters

**Context**: Modify the request to include a test parameter and check for reflection.

**Command** ([[commands/curl-endpoint-inspect]]):
```bash
curl "https://help.glassdoor.com/gd_requestsubmitpage?lang=test"
```

> Search the HTML response for 'test' to confirm reflection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-endpoint-inspect]]

## Tools Used


## Tags

- [[xss]]
- [[recon]]
