---
tags:
  - subdomain-takeover
  - dns
  - recon
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
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:51:10.469Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 3ecfa0eb-fff7-4d86-a53d-f39500be1f30
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Discover-Vulnerable-Subdomain

## Summary

This procedure identifies subdomains vulnerable to takeover by checking for DNS records pointing to unclaimed third-party services like UptimeRobot, where a 'not found' error indicates an inactive or unclaimed account.

## Description

In a subdomain takeover attack, attackers scan for dangling DNS records (e.g., CNAMEs) that point to external services without an active account. Visiting the subdomain reveals service-specific errors, signaling opportunity. This targets web environments with misconfigured DNS, leading to potential control over the subdomain for phishing or malware distribution. Prerequisites include public access to the target domain's DNS.

## Requirements

1. Web browser for manual visitation
2. Knowledge of common third-party services (e.g., UptimeRobot, Heroku)
3. Access to public DNS resolution

## Defense

Defensive measures and detection strategies:

- Regularly audit DNS records for dangling pointers using tools like dnsdumpster or subfinder
- Implement DNS verification and remove unused records
- Monitor for unexpected third-party error pages on subdomains

## Objectives

1. Confirm DNS misconfiguration pointing to unclaimed services
2. Identify takeover candidates for further exploitation
3. Gather evidence of vulnerability without alerting defenders

## Instructions

### Step 1: Resolve and Visit Subdomain

**Context**: Manually check the subdomain's resolution and response to detect unclaimed service indicators.

No specific command; use a web browser:

Navigate to `https://uptime.btfs.io/` (replace with target subdomain).

> Observe the HTTP response: A 'not found' error from UptimeRobot confirms the DNS CNAME points to their infrastructure but lacks an active claim.

### Step 2: Verify DNS Record

**Context**: Confirm the DNS type and target to ensure it's a takeover vector.

Use online DNS lookup tools or dig (if available):

```bash
dig CNAME uptime.btfs.io
```

> Expected output shows CNAME to UptimeRobot's servers (e.g., cname.uptimerobot.com), indicating vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[DNS]]
- [[recon]]
