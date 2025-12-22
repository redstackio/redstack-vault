---
tags:
  - enumeration
  - reconnaissance
  - web
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
techniques:
  - '[[Active Scanning]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: c78375ba-3a96-4a64-911b-65c86ff92d17
created_at: '2025-12-14T17:29:10.071Z'
updated_at: '2025-12-14T17:29:10.071Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Enumerate-Subdomains-and-Admin-Endpoints

## Summary

This procedure involves manually discovering subdomains and enumerating potential admin endpoints on a web application, such as identifying the /pagespeed-global-admin/ path on webtools.paloalto.com, to uncover access control weaknesses.

## Description

In this attack scenario, the target is a web platform like Palo Alto Networks' webtools subdomain. The procedure relies on passive and active reconnaissance to explore publicly accessible paths without authentication. Expected outcomes include identifying unprotected admin interfaces that could lead to unauthorized access. Prerequisites include basic web browsing knowledge and no special tools beyond a standard browser.

## Requirements

1. Internet access to the target domain (e.g., paloalto.com)
2. Web browser for manual navigation and inspection
3. Knowledge of common admin path patterns (e.g., /admin, /pagespeed-global-admin)

## Defense

Defensive measures and detection strategies:

- Implement proper access controls with authentication on all admin endpoints
- Use web application firewalls (WAF) to monitor and block unusual path enumerations
- Regularly audit subdomain exposures and path accessibility

## Objectives

1. Discover hidden or unprotected subdomains
2. Identify admin endpoints vulnerable to unauthorized access
3. Map the attack surface for further exploitation

## Instructions

### Step 1: Access the Main Domain and Guess Subdomains

**Context**: Begin by targeting the root domain and common subdomain patterns to find accessible entry points.

Navigate to https://paloalto.com in your web browser and explore linked resources or use browser search to test subdomains like webtools.paloalto.com.

> Manually enter the URL https://webtools.paloalto.com/ and confirm it loads a functional page.

### Step 2: Enumerate Endpoints on the Subdomain

**Context**: Once on the subdomain, probe for admin paths by appending common directories.

In the browser, append potential paths like /admin or /pagespeed-global-admin to the subdomain URL and check for accessibility.

> Test https://webtools.paloalto.com/pagespeed-global-admin/ – it should load without authentication if vulnerable.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[enumeration]]
- [[Reconnaissance]]
