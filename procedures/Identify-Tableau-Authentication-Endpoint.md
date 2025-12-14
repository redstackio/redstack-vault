---
id: proc-uuid-002
tags:
  - recon
  - endpoint-discovery
  - tableau
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:46:32.122Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Tableau-Authentication-Endpoint

## Summary

This procedure focuses on locating the vulnerable authentication redirect endpoint in Tableau software deployed on the target subdomain, setting the stage for XSS exploitation.

## Description

Tableau's embedded authentication often uses specific URLs for redirects. By examining the site's structure after accessing the subdomain, attackers can identify /en/embeddedAuthRedirect.html, which accepts an 'auth' parameter prone to XSS. This step requires manual browsing and inspection, with outcomes including the full endpoint URL for payload injection. The target is a DoD subdomain, so ethical disclosure via platforms like HackerOne is recommended post-discovery.

## Requirements

1. Access to the target subdomain from previous procedure
2. Web browser with inspection capabilities
3. Knowledge of Tableau's common URL patterns

## Defense

Defensive measures and detection strategies:

- Regularly audit web application endpoints for exposed parameters
- Use content security policies (CSP) to restrict script execution on authentication pages

## Objectives

1. Pinpoint the /en/embeddedAuthRedirect.html endpoint
2. Confirm the presence of the 'auth' parameter
3. Prepare for payload testing

## Instructions

### Step 1: Browse Subdomain Paths

**Context**: Explore URLs to find Tableau-specific functionality.

Navigate through the subdomain and look for paths under /en/ or authentication-related links.

> Manually click or append /en/embeddedAuthRedirect.html to the base URL. If it resolves, note the 'auth' parameter in the query string.

### Step 2: Inspect for Vulnerability Indicators

**Context**: Verify the endpoint's behavior.

Use browser dev tools to monitor requests when loading potential auth pages.

> Check if the 'auth' parameter is reflected in the response without sanitization. Success is indicated by the parameter appearing in HTML or JavaScript contexts.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[tableau]]
