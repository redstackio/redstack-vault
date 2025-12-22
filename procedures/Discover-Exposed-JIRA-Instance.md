---
id: proc-discover-jira
tags:
  - reconnaissance
  - subdomain-enumeration
  - web-discovery
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-access-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:30:18.168Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Discover Exposed JIRA Instance

## Summary

This procedure involves reconnaissance to identify exposed web applications, specifically unsecured JIRA instances on test subdomains, by enumerating subdomains and probing for service fingerprints.

## Description

In scenarios like the Starbucks JIRA exposure, attackers begin with passive or active reconnaissance to uncover non-standard subdomains such as 'jiratest'. This targets misconfigured development or staging environments that lack proper access controls. The procedure assumes public domain access and focuses on web-based discovery, leading to identification of vulnerable services without prior credentials.

## Requirements

1. Access to the target's root domain (e.g., starbucks.com)
2. Basic networking tools like curl for probing
3. Knowledge of common test subdomain patterns (e.g., test, dev, staging)

## Defense

Defensive measures and detection strategies:

- Implement DNS filtering to hide internal subdomains
- Use web application firewalls (WAF) to block reconnaissance probes
- Monitor for anomalous subdomain queries in DNS logs

## Objectives

1. Uncover hidden subdomains hosting services like JIRA
2. Verify exposure without authentication
3. Map the attack surface for further exploitation

## Instructions

### Step 1: Subdomain Enumeration

**Context**: Manually or automatically guess and resolve potential test subdomains to find exposed instances.

**Command** ([[commands/curl-access-url]]):
```bash
curl -k -I https://jiratest.starbucks.com
```

> This command performs a HEAD request to check if the subdomain resolves and returns JIRA-specific headers (e.g., X-Seraph-LoginReason). Expected output includes HTTP 200 and server details indicating Atlassian JIRA.

### Step 2: Service Fingerprinting

**Context**: Confirm the presence of JIRA by accessing key endpoints and observing the interface.

**Command** ([[commands/curl-access-url]]):
```bash
curl -k https://jiratest.starbucks.com/secure/Dashboard.jspa
```

> Look for JIRA dashboard elements in the HTML response. Success is indicated by no redirect to a login page and visibility of issue navigation.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-url]]

## Tools Used


## Tags

- [[Reconnaissance]]
- [[web-discovery]]
