---
tags:
  - jira
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-basic-get]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:25:17.715Z'
sub_techniques: []
id: 5617f44b-43a2-460c-9645-0677f9951b14
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Exposed-JIRA-Instance

## Summary

This procedure involves scanning and identifying an exposed Atlassian JIRA Server instance, particularly outdated versions like 7.9.2, to confirm vulnerability to known CVEs for information disclosure.

## Description

In a reconnaissance phase, attackers target public domains to detect web applications. For JIRA Server, accessing the root URL reveals the login page and version details via HTML source or headers. This step confirms the presence of JIRA 7.9.2, which is susceptible to CVE-2019-3403 and CVE-2019-8442, enabling unauthenticated information leaks that can map users and internal configurations for further attacks.

## Requirements

1. Internet access to the target domain (e.g., sim.starbucks.com)
2. Basic HTTP client like curl or browser
3. Knowledge of JIRA indicators (e.g., /secure/Dashboard.jspa path)

## Defense

Defensive measures and detection strategies:

- Keep JIRA updated to latest versions
- Implement web application firewall (WAF) to block version disclosure
- Monitor access logs for root URL hits from suspicious IPs

## Objectives

1. Confirm JIRA Server presence and version
2. Identify potential for CVE exploitation
3. Gather initial attack surface details

## Instructions

### Step 1: Access Target Domain

**Context**: Fetch the root page to inspect for JIRA signatures.

**Command** ([[commands/curl-basic-get]]):
```bash
curl -i https://sim.starbucks.com
```

> This command retrieves headers and body. Look for 'Server: Apache' or JIRA meta tags like <meta name="application-name" content="JIRA">. Success if version 7.9.2 is visible in source.

### Step 2: Verify JIRA Paths

**Context**: Probe specific JIRA endpoints to confirm installation.

**Command** ([[commands/curl-basic-get]]):
```bash
curl -s https://sim.starbucks.com/secure/Dashboard.jspa | grep -i jira
```

> Expected output includes JIRA-specific HTML elements, confirming the instance.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-basic-get]]

## Tools Used


## Tags

- [[jira]]
- [[Reconnaissance]]
