---
id: proc-uuid-2
tags:
  - access-control
  - database-manipulation
  - domain-takeover
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-probe-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:13.360Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Installation-Endpoint-for-Database-Manipulation

## Summary

This procedure discovers and probes an active PHP installation endpoint (e.g., install.php?step=1) that lacks authentication, potentially allowing unauthorized updates to the database, which could lead to domain takeover by modifying DNS records or application configurations.

## Description

Many PHP applications, especially CMS or custom scripts, include installation files that guide users through setup, including database configuration. If these endpoints remain active post-deployment, attackers can access them to manipulate database contents without checks. In this case, the endpoint https://███.edu/install.php?step=1 was found accessible, suggesting write capabilities to the database exposed via the prior credential leak. The procedure involves URL enumeration and response inspection to confirm vulnerability. Prerequisites include knowledge of common install paths; outcomes enable escalation from read-only disclosure to active compromise.

## Requirements

1. Access to the target domain via HTTP/HTTPS
2. Basic understanding of PHP application structures (e.g., common paths like /install.php)
3. Tool for sending HTTP requests and inspecting responses (browser or curl)

## Defense

Defensive measures and detection strategies:

- Remove or disable installation files after deployment; rename or delete scripts like install.php
- Implement authentication or IP whitelisting for admin/install paths; use role-based access control (RBAC)
- Monitor server logs for accesses to sensitive paths; deploy intrusion detection systems (IDS) to alert on parameter manipulations like ?step=1
- Conduct regular vulnerability scans with tools like OWASP ZAP to identify leftover install endpoints

## Objectives

1. Confirm the endpoint's accessibility and lack of protections
2. Identify opportunities for database writes leading to takeover
3. Chain with extracted credentials for full exploitation

## Instructions

### Step 1: Probe the Installation Endpoint

**Context**: Send a GET request to the suspected install URL to check for public access and functionality.

**Command** ([[commands/curl-probe-endpoint]]):
```bash
curl 'https://███.edu/install.php?step=1'
```

> This retrieves the page content. Successful output shows HTML forms or PHP echoes related to database setup, without login redirects, indicating vulnerability.

### Step 2: Inspect for Manipulation Potential

**Context**: Analyze the response for interactive elements that could accept input for database updates.

Use browser developer tools or pipe curl output to view source:

```bash
curl 'https://███.edu/install.php?step=1' | grep -i 'form\|input\|database'
```

> Look for form fields or parameters that suggest write access. Expected indicators include database connection tests or config update sections.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-probe-endpoint]]

## Tools Used

- [[tools/curl]]

## Tags

- [[access-control]]
- [[database-manipulation]]
- [[domain-takeover]]
