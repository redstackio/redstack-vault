---
tags:
  - subdomain-takeover
  - dns-registration
  - cloud
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1583.003]]'
updated_at: '2025-12-14T04:38:39.453Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 36c9175d-3968-474c-a38a-83c65e330fc8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1583.003]]'
---
# Register and Claim Takeover Subdomain

## Summary

This procedure claims control of a dangling subdomain by registering it with a third-party DNS provider that supports takeovers of unclaimed records.

## Description

After identifying a dangling record (e.g., a CNAME to an inactive AWS service), attackers register the subdomain on a provider like Heroku, GitHub Pages, or a generic registrar. This grants full DNS and hosting control. In the mozaws.net case, the record was unclaimed, allowing registration and NS record updates for propagation.

## Requirements

1. Account on a DNS provider supporting dangling record claims
2. Identified dangling subdomain from prior reconnaissance
3. Domain registration fees if applicable

## Defense

Defensive measures and detection strategies:

- Monitor for unauthorized NS changes on subdomains
- Use CAA records to restrict certificate issuance
- Automate cleanup of DNS records during service decommissioning

## Objectives

1. Gain ownership of the subdomain
2. Update DNS to point to attacker-controlled nameservers
3. Enable subsequent hosting or redirection

## Instructions

### Step 1: Provider Selection and Registration

**Context**: Choose a provider (e.g., AWS Route 53 alternative) and create an account. Search for the subdomain availability.

No command; perform via web interface: Log in to provider dashboard, add the subdomain, and confirm it's unclaimed.

> Expected: Dashboard shows successful addition.

### Step 2: Update Nameservers

**Context**: Point the subdomain's NS records to your provider's nameservers.

No command; update in the provider's DNS settings to propagate changes (may take up to 48 hours).

> Verify with dig after propagation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1583.003]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[DNS]]
- [[takeover]]
