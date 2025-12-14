---
tags:
  - reconnaissance
  - web-endpoint
  - cgi
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-directory-traversal-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:05.668Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 7792c5be-76eb-42ee-951f-b356bc8fb1a6
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Identify-Vulnerable-CGI-Endpoint

## Summary

This procedure involves manually inspecting a web application to locate CGI script endpoints that accept directory listing parameters, such as the DIR parameter in a DoD web app's display_directory CGI script, setting the stage for path traversal exploitation.

## Description

In this attack scenario, the target is a public-facing web application on a Linux server running CGI scripts. By browsing multiple pages, attackers identify hidden or referenced endpoints like /aerosol-bin/███████/display_directory_████_t.cgi that process user-supplied directory paths without validation. This reconnaissance step reveals the attack surface for subsequent traversal tests, potentially exposing the entire server filesystem. Prerequisites include direct HTTP access to the site; no authentication is needed.

## Requirements

1. Web browser or command-line tool like curl for probing
2. Knowledge of the target domain and basic web navigation
3. Network connectivity to the public-facing web server

## Defense

Defensive measures and detection strategies:

- Implement web application firewalls (WAF) to monitor for unusual endpoint access patterns
- Log all CGI script invocations and parameter values for anomaly detection
- Restrict CGI execution to sanitized inputs only

## Objectives

1. Locate exploitable CGI endpoints accepting directory parameters
2. Confirm parameter usage across application pages
3. Prepare for traversal testing without alerting defenses

## Instructions

### Step 1: Browse Application Pages

**Context**: Navigate the target web application to find references to the vulnerable CGI script.

**Command** ([[commands/curl-directory-traversal-test]]):
```bash
curl "https://target.gov/" | grep -i "display_directory"
```

> This command fetches the homepage and greps for script references. Expected output includes paths like /aerosol-bin/███████/display_directory_████_t.cgi. Manually visit linked pages to confirm DIR parameter presence.

### Step 2: Verify Endpoint Accessibility

**Context**: Test the identified endpoint with a benign directory to ensure it responds.

**Command** ([[commands/curl-directory-traversal-test]]):
```bash
curl "https://target.gov/aerosol-bin/███████/display_directory_████_t.cgi?DIR=./"
```

> This lists the current directory if functional. Expected output: A safe directory listing within the web root, confirming the endpoint is active.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-directory-traversal-test]]

## Tools Used

- [[tools/curl]]

## Tags

- [[Reconnaissance]]
- [[web]]
- [[cgi]]
