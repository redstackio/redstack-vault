---
id: proc-recon-mtn-domains-001
tags:
  - reconnaissance
  - domain-discovery
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
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:24:44.958Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Reconnaissance-and-Target-Identification-on-MTN-Domains

## Summary

This procedure involves initial reconnaissance by signing into accessible applications and performing search queries to identify target domains associated with MTN Group, leading to discovery of a vulnerable Cisco IOS XE instance.

## Description

In the attack scenario, reconnaissance targets MTN Group's infrastructure. By logging into any user account in related web applications and searching for terms like 'MTN Innovation Centre', attackers discover subdomains and hostnames owned by entities such as MTN Cameroon. This identifies the redacted hostname hosting the Cisco IOS XE web UI, setting the stage for further exploitation. Prerequisites include basic network access to MTN-related portals; no special tools are needed beyond a browser.

## Requirements

1. Access to a web application or portal associated with the target organization (e.g., MTN Group internal search)
2. Valid low-privilege user credentials for initial sign-in
3. Network connectivity to resolve and access target domains

## Defense

Defensive measures and detection strategies:

- Implement web application firewalls (WAF) to monitor anomalous search queries
- Log and alert on domain enumeration attempts from internal searches
- Restrict search functionalities to authenticated, role-based access

## Objectives

1. Discover target domains and hostnames linked to the organization
2. Identify potential Cisco IOS XE web UI endpoints
3. Gather initial intelligence for targeted fuzzing

## Instructions

### Step 1: Sign In and Perform Search Query

**Context**: Gain initial foothold in the target's web environment to leverage search functionality for domain discovery.

No specific command; use browser to log in and search for 'MTN Innovation Centre'.

> Expected output: Search results revealing associated domains, including the redacted hostname for MTN Cameroon.

### Step 2: Verify Target Domain Ownership

**Context**: Confirm the identified hostname points to a Cisco IOS XE device.

Manually resolve the domain (e.g., via nslookup or browser access) to check for web UI login page.

> Expected output: Web UI interface confirming Cisco IOS XE presence.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[Reconnaissance]]
- [[domain-discovery]]
