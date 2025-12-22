---
tags:
  - domain-setup
  - public-server
type: procedure
tools:
  - '[[tools/Docker]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:55.273Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: b5a955be-6c27-4519-9f05-4de77e1d7e31
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Acquire Domain and Setup Public Server

## Summary

This procedure involves purchasing a domain and configuring a public server to host components for SSRF exploitation, enabling control over DNS and initial HTTP requests.

## Description

In the context of the Bitwarden SSRF attack, acquire a domain to manipulate DNS resolutions for bypassing private IP checks. Point the domain to a server with a public IP where a webserver will be hosted to serve redirects. This sets up the entry point for Bitwarden's icon fetching feature to make an initial external request before chaining internally.

## Requirements

1. Access to a domain registrar (e.g., Namecheap, GoDaddy)
2. A VPS or cloud instance with public IP (e.g., AWS EC2, DigitalOcean)
3. Basic server administration knowledge

## Defense

Defensive measures and detection strategies:

- Monitor domain registrations linked to your organization
- Use DNS logging to detect anomalous resolutions
- Implement web application firewalls (WAF) to block suspicious redirects

## Objectives

1. Establish control over DNS for subdomain resolutions
2. Prepare a hosting environment for malicious payloads
3. Ensure public accessibility for external fetches

## Instructions

### Step 1: Purchase and Configure Domain

**Context**: Acquire a domain and update its nameservers to point to your control.

No specific command; use registrar UI to buy domain and set NS records to your DNS server (e.g., ns1.yourserver.com).

> Expected: Domain propagates within 1-48 hours; verify with dig or nslookup.

### Step 2: Provision Public Server

**Context**: Set up a server instance with public IP.

Launch a VPS, assign static public IP, and ensure SSH access.

> Expected: Server reachable via IP; install OS packages as needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Docker]]

## Tags

- domain-setup
- public-server
