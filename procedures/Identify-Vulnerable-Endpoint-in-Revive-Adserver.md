---
tags:
  - xss
  - vulnerability-identification
  - revive-adserver
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 7a37afbf-bc70-4692-8fd6-6d7e9d01d830
created_at: '2025-12-14T03:47:13.104Z'
updated_at: '2025-12-14T03:47:13.104Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Vulnerable-Endpoint-in-Revive-Adserver

## Summary

This procedure involves reviewing prior vulnerability reports to pinpoint incomplete sanitization in Revive Adserver's /www/delivery/afr.php endpoint, where query parameters are inserted into JavaScript without full escaping, setting the stage for XSS exploitation.

## Description

In the context of Revive Adserver, a PHP-based ad serving platform, the /www/delivery/afr.php endpoint handles ad requests and embeds user-controlled query parameters like 'refresh' and 'loc' directly into a script tag in the response. A previous fix from report #775693 addressed basic XSS but failed to handle script tag closure techniques or special characters like '/', allowing attackers to inject new script tags. This procedure focuses on static analysis of the endpoint and prior reports to identify the insertion point and bypass opportunities, applicable in web vulnerability assessments targeting ad servers.

## Requirements

1. Access to HackerOne report #775693 or equivalent vulnerability disclosure
2. Basic knowledge of PHP and JavaScript contexts in web responses
3. Network access to the target Revive Adserver instance for verification

## Defense

Defensive measures and detection strategies:

- Implement comprehensive input validation and output encoding for all query parameters in JavaScript contexts using libraries like OWASP ESAPI
- Use Content Security Policy (CSP) to restrict script execution and inline scripts
- Monitor for anomalous query parameters containing script tags in web server logs

## Objectives

1. Confirm the exact location of user input insertion in the response script tag
2. Identify gaps in the previous fix, such as unhandled tag closure
3. Prepare for payload crafting by understanding the JavaScript context

## Instructions

### Step 1: Review Prior Vulnerability Report

**Context**: Examine report #775693 to understand the original XSS and the applied fix, noting that query parameters are still directly concatenated into the script without escaping for tag closure.

No command required; perform manual review of the report and endpoint source if available.

> Expected: Documentation of the script tag structure, e.g., setTimeout('window.location.replace("..." + userInput + ...)'

### Step 2: Analyze Endpoint Response Structure

**Context**: Fetch a clean response from /www/delivery/afr.php to map where parameters like 'refresh' appear.

Use browser developer tools or a proxy to inspect the HTML/JS output.

> Expected: Identification of unescaped insertion points allowing '</script><script>' payloads.

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
- [[revive-adserver]]
