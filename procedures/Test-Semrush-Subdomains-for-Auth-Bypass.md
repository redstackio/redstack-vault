---
tags:
  - auth-bypass
  - subdomain-testing
  - validation
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: c602717a-172e-452f-8acc-c64045e126f5
created_at: '2025-12-14T17:32:01.669Z'
updated_at: '2025-12-14T17:32:01.669Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Test-Semrush-Subdomains-for-Auth-Bypass

## Summary

This procedure tests multiple Semrush regional subdomains to confirm the authentication bypass vulnerability and its scope, contrasting with the main domain's enforcement.

## Description

Semrush's regional subdomains (e.g., uk, us, fr) fail to require API keys, unlike the root api.semrush.com. This web procedure validates the IDOR and auth bypass across instances. Prerequisites: Base endpoint knowledge. Outcomes: Proof of widespread exposure to unauthorized queries.

## Requirements

1. List of subdomains (uk.api.semrush.com, us.api.semrush.com, fr.api.semrush.com)
2. Browser for repeated testing
3. Sample query parameters

## Defense

Defensive measures and detection strategies:

- Uniformly apply API key validation across all subdomains
- Use consistent authentication middleware for regional deployments
- Audit subdomain configurations for discrepancies in access controls

## Objectives

1. Verify bypass on multiple regional endpoints
2. Confirm key enforcement on main domain
3. Assess vulnerability prevalence

## Instructions

### Step 1: Test Regional Subdomains

**Context**: Apply the parameter modification to different subdomains with varying databases.

No specific command; in Firefox, load: `http://uk.api.semrush.com/?action=report&type=domain_rank&domain=semrush.com&database=uk`

> Repeat for us and fr. Expected output: Successful data for each.

### Step 2: Contrast with Main Domain

**Context**: Attempt the same query on the root to observe failure.

No specific command; load: `http://api.semrush.com/?action=report&type=domain_rank&domain=semrush.com`

> Without key. Expected output: Error 'ERROR 120 :: WRONG KEY - ID PAIR'.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[auth-bypass]]
- [[subdomain-enum]]
