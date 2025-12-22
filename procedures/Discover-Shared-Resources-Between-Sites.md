---
id: proc-discover-shared-resources
tags:
  - recon
  - idor
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:33:34.353Z'
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
# Discover-Shared-Resources-Between-Sites

## Summary

This procedure involves reconnaissance to identify shared database and cookie credentials between an alternate site and the main application, such as card.starbucks.com.sg, setting the stage for IDOR exploitation.

## Description

In scenarios where multiple sites share backend resources without proper isolation, attackers can discover these overlaps by analyzing network traffic, cookies, and response data. This procedure targets web applications using PHP sessions, where PHPSESSID cookies are reused across sites, enabling unauthorized access. Expected outcomes include confirmation of shared infrastructure, rated as a precursor to critical vulnerabilities like account takeover.

## Requirements

1. Access to both the main site and alternate site via web browser
2. Browser with developer tools enabled (e.g., Chrome DevTools)
3. Optional: Proxy tool for traffic interception

## Defense

Defensive measures and detection strategies:

- Implement site-specific session isolation using unique session namespaces
- Monitor for anomalous cross-site requests via WAF rules
- Use environment-specific databases to prevent resource sharing

## Objectives

1. Confirm shared PHPSESSID cookie usage
2. Verify database interactions overlap
3. Establish foundation for session hijacking

## Instructions

### Step 1: Inspect Site Configurations

**Context**: Compare cookie and endpoint behaviors between sites to detect sharing.

Open developer tools on the alternate site, navigate to various pages, and inspect cookies and network requests. Look for PHPSESSID in headers and check if endpoints return data consistent with the main site's user base.

> Manually review responses for shared user IDs or database error patterns indicating common backend.

### Step 2: Test Resource Overlap

**Context**: Probe for direct object references by attempting to access main site resources via alternate endpoints.

Submit requests to alternate site APIs that might query the shared database, observing if main site user data appears in responses.

> Success is indicated by leaked session or user info without proper authorization.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[idor]]
