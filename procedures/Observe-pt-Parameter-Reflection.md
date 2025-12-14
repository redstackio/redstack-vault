---
id: proc-789652-observe-reflection
tags:
  - recon
  - xss
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-check-reflection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:16:36.886Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Observe-pt-Parameter-Reflection

## Summary

This procedure involves accessing the Topcoder ReviewBoard URL to observe and confirm that the 'pt' parameter is directly reflected in the page without sanitization, setting the stage for XSS exploitation.

## Description

In the context of testing the Topcoder website, this step verifies the root cause of the reflected XSS vulnerability: lack of input sanitization or output encoding for the 'pt' parameter in the URL https://www.topcoder.com/tc?module=ReviewBoard&pt=1. By inspecting the page source, attackers can see the parameter value embedded raw in HTML, allowing subsequent payload injection. This is a reconnaissance step in web vulnerability assessment, requiring only public access to the site.

## Requirements

1. Web browser or curl installed for HTTP requests
2. Public internet access to https://www.topcoder.com
3. Basic knowledge of HTML inspection (e.g., View Source or Developer Tools)

## Defense

Defensive measures and detection strategies:

- Implement content security policy (CSP) to block inline scripts
- Use output encoding (e.g., HTML entity encoding) for user inputs in web apps
- Monitor for anomalous URL parameters in web logs

## Objectives

1. Confirm reflection of 'pt' parameter without escaping
2. Identify the exact location of reflection in page HTML
3. Validate no immediate WAF blocking for benign inputs

## Instructions

### Step 1: Access Target URL

**Context**: Visit the vulnerable endpoint to load the page and prepare for inspection.

**Command** ([[commands/curl-check-reflection]]):
```bash
curl "https://www.topcoder.com/tc?module=ReviewBoard&pt=1" -s | grep -i pt
```

> This command fetches the page and searches for 'pt' in the output, revealing if the value '1' is reflected. Expected output includes lines like '<div>pt=1</div>' or similar unescaped insertion.

### Step 2: Inspect Page Source

**Context**: Use browser tools to manually verify reflection.

Navigate to https://www.topcoder.com/tc?module=ReviewBoard&pt=1 in a browser, right-click, and select 'View Page Source'. Search for 'pt=1' to confirm direct embedding.

> Successful inspection shows the parameter value unaltered in the HTML structure, indicating vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-check-reflection]]

## Tools Used


## Tags

- recon
- xss
- web
