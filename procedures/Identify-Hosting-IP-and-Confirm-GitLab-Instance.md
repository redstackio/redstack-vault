---
id: proc-uuid-1
name: Identify-Hosting-IP-and-Confirm-GitLab-Instance
tags:
  - reconnaissance
  - hostname-discovery
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
updated_at: '2025-12-14T17:28:44.341Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify Hosting IP and Confirm GitLab Instance

## Summary

This procedure involves resolving the IP address associated with a target subdomain and confirming it hosts a private GitLab Enterprise Edition instance through port checks and redirect analysis.

## Description

In scenarios where a subdomain redirects to an internal service like GitLab EE, attackers can identify the hosting IP and use TLS certificate details to uncover the true hostname. This step sets the foundation for credential searches by revealing service-specific identifiers. The target environment is a web-accessible IP with nginx proxying to GitLab on ports 80 and 443.

## Requirements

1. Access to DNS resolution tools or browser
2. Knowledge of the target subdomain
3. Network connectivity to the IP on ports 80/443

## Defense

Defensive measures and detection strategies:

- Implement certificate transparency monitoring to detect exposed internal hostnames
- Use web application firewalls to block unauthorized port scans
- Rotate TLS certificates regularly and avoid embedding internal details

## Objectives

1. Resolve and confirm the target's hosting IP
2. Extract hostname from TLS certificate
3. Verify redirection to GitLab EE

## Instructions

### Step 1: Resolve IP and Check Port 80

**Context**: Query the IP to observe the initial HTTP response and redirect.

No specific command; use browser or curl:

```bash
curl -I http://[target-ip]:80
```

> This returns a 301 redirect to HTTPS on port 443, indicating nginx proxy to GitLab.

### Step 2: Inspect TLS Certificate

**Context**: Examine the certificate to reveal the internal GitLab hostname.

Use browser developer tools or openssl:

```bash
openssl s_client -connect [target-ip]:443 -servername [subdomain]
```

> Output includes the certificate with the embedded hostname for further searches.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[hostname-discovery]]
