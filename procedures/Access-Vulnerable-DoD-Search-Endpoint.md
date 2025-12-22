---
id: proc-uuid-1
tags:
  - xss
  - web
  - recon
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:25.931Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Vulnerable-DoD-Search-Endpoint

## Summary

This procedure involves navigating to the search functionality on a U.S. Department of Defense website to identify the vulnerable endpoint for reflected XSS exploitation. It sets the stage for payload injection by confirming the reflection of user-supplied input in search parameters.

## Description

In the context of exploiting a reflected XSS vulnerability, the attacker first accesses the public-facing search page on the DoD website. The endpoint uses parameters like 'what' and 'where' that are directly reflected in the HTML response without sanitization, allowing subsequent injection of malicious scripts. This step requires no special privileges and can be performed via a standard web browser. Expected outcomes include verification of the site's accessibility and input reflection, preparing for the exploitation phase.

## Requirements

1. Internet access to reach the public DoD website.
2. A modern web browser to interact with the search form.
3. Basic understanding of URL parameters and HTTP requests.

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to restrict script execution.
- Sanitize and encode all user inputs in search parameters using HTML entity encoding.
- Monitor for unusual search queries containing script tags or event handlers.

## Objectives

1. Confirm access to the vulnerable search endpoint.
2. Verify reflection of parameters in the page output.
3. Establish baseline for payload testing without triggering alerts.

## Instructions

### Step 1: Navigate to the Base Endpoint

**Context**: Locate the search functionality to inspect parameter handling.

Open your web browser and enter the URL https://█████████/7/0/33/1d/ with sample search parameters, such as http://www.citysearch.com/search?what=x&where=.

> This loads the search page. Inspect the HTML source (right-click > View Page Source) to confirm that the 'where' parameter value appears unescaped in the response.

### Step 2: Test Basic Reflection

**Context**: Submit a benign query to ensure parameters are reflected.

Enter a simple search like 'what=test&where=location' and submit. Check the resulting page for direct reflection of the input.

> Successful reflection indicates vulnerability to injection; no alerts or errors should appear.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[web]]
- [[recon]]
