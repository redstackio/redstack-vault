---
tags:
  - reconnaissance
  - web-vuln
  - parameter-testing
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T17:24:31.463Z'
sub_techniques: []
id: 2256f9ea-3df2-4cf4-9ac2-abcb1289e20b
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Identify Vulnerable Path Parameter Endpoints

## Summary

This procedure involves testing multiple endpoints in the Shopify Locksmith app to identify pages where the 'path' parameter is vulnerable to manipulation, setting the stage for open redirect and XSS exploits.

## Description

In the context of supporthiring.shopify.com, the Locksmith app exposes various resource pages under /apps/locksmith/resource/pages/. By appending ?path= to these URLs and observing responses, attackers can confirm if the parameter is processed without strict validation, enabling further exploitation for redirects or script injection. This reconnaissance step is crucial for targeting affected Shopify sites and requires only public access.

## Requirements

1. Public access to the target Shopify domain (e.g., supporthiring.shopify.com).
2. Browser or proxy tool for URL testing.
3. Basic understanding of web parameters and HTTP responses.

## Defense

Defensive measures and detection strategies:

- Implement parameter validation to reject or sanitize 'path' inputs.
- Monitor for unusual URL patterns in access logs, such as repeated ?path= tests.

## Objectives

1. Locate endpoints accepting the 'path' parameter.
2. Confirm lack of initial protections.
3. Prepare for payload injection.

## Instructions

### Step 1: Enumerate Target Pages

**Context**: Identify candidate URLs by navigating to Locksmith app resource pages.

Construct and load URLs like http://supporthiring.shopify.com/apps/locksmith/resource/pages/gauntlet-challenge?path= in a browser or using a proxy.

> Inspect the page source or network tab for reflection of the parameter.

### Step 2: Test Parameter Acceptance

**Context**: Verify if the parameter influences page behavior without errors.

Append empty or benign values to ?path= and observe for redirects, errors, or reflections.

> Successful test shows the parameter is parsed, e.g., no 400 errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Vulnerability Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[Reconnaissance]]
- [[web-vuln]]
