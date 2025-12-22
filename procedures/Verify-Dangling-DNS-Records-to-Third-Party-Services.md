---
id: proc-verify-dangling-dns
tags:
  - dns-verification
  - dangling-records
  - third-party-services
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:51:26.323Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Verify Dangling DNS Records to Third-Party Services

## Summary

This procedure checks if a subdomain's DNS record points to an inactive third-party service configuration, confirming a dangling record ripe for takeover.

## Description

For course.oberlo.com, DNS points to Kajabi, but the associated Kajabi site is deleted. Verification involves resolving DNS and attempting access to confirm abandonment, enabling the attacker to claim it without conflicts.

## Requirements

1. DNS resolution capability
2. Web access to test the resolved URL
3. Knowledge of the third-party service (e.g., Kajabi)

## Defense

Defensive measures and detection strategies:

- Automate checks for third-party DNS integrations post-deletion
- Use subdomain monitoring tools to alert on inactive pointers
- Rotate or remove DNS records promptly after service decommissioning

## Objectives

1. Confirm DNS resolution to third-party infrastructure
2. Validate site inactivity
3. Assess takeover feasibility

## Instructions

### Step 1: Resolve and Inspect DNS

**Context**: Query the subdomain's DNS to identify the target service.

```bash
dig course.oberlo.com CNAME
```

> Output shows CNAME to Kajabi, e.g., something.kajabi.com.

### Step 2: Test Service Accessibility

**Context**: Access the resolved endpoint to check for activity.

Use browser or curl:

```bash
curl -v https://course.oberlo.com
```

> Look for 404, 410, or Kajabi-specific errors indicating deleted site.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[dns-verification]]
- [[dangling-records]]
