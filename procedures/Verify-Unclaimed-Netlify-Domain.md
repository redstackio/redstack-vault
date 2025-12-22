---
id: uuid-for-proc2
tags:
  - netlify
  - hosting
  - verification
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-netlify-check]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:38:49.427Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Verify-Unclaimed-Netlify-Domain

## Summary

This procedure checks if a Netlify domain referenced by a dangling CNAME is unclaimed, confirming availability for takeover by attempting to access or probe the site.

## Description

Following DNS identification, this step involves probing the third-party hosting platform (Netlify) to ensure the domain alias or site ID is not actively used. In the Uber case, this revealed the Netlify site was expired and free, enabling the next takeover phase. It combines HTTP probing with manual platform checks to assess claim status.

## Requirements

1. Web browser or HTTP client for probing
2. Knowledge of the CNAME target (e.g., unclaimed-site.netlify.app)
3. Access to Netlify signup (free account optional for verification)

## Defense

Defensive measures and detection strategies:

- Monitor third-party hosting dashboards for dangling domains
- Automate alerts for expired aliases via API integrations
- Conduct periodic subdomain audits with tools like Subjack or Takeover

## Objectives

1. Confirm domain availability on hosting platform
2. Assess risk of takeover
3. Gather evidence for reporting or exploitation

## Instructions

### Step 1: Probe Site Availability

**Context**: Use HTTP requests to check if the Netlify site is live or shows unclaimed indicators.

**Command** ([[commands/curl-netlify-check]]):
```bash
curl -I https://unclaimed-site.netlify.app
```

> Expected output: HTTP 200 with Netlify's default unclaimed page or 404. If it loads custom content, the domain is claimed; otherwise, it's available.

### Step 2: Manual Netlify Dashboard Check

**Context**: Log into Netlify (or simulate) to search for the domain alias.

No command; use browser to navigate to app.netlify.com and attempt to add the domain. Success if it's free to claim.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-netlify-check]]

## Tools Used

- [[tools/curl]]

## Tags

- [[netlify]]
- [[hosting]]
- [[verification]]
