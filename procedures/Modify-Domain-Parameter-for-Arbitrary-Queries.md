---
tags:
  - idor
  - parameter-manipulation
  - data-exfiltration
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 814eec63-6e29-4f8a-9f68-5dd410160583
created_at: '2025-12-14T17:32:01.670Z'
updated_at: '2025-12-14T17:32:01.670Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Domain-Parameter-for-Arbitrary-Queries

## Summary

This procedure exploits IDOR in Semrush API by altering the 'domain' parameter to access rank data for any target domain without paying for API access.

## Description

On Semrush subdomains, the API accepts direct URL parameter changes without validating user authorization, enabling arbitrary domain queries. This web-based attack targets the domain_rank report type. Prerequisites: Accessible endpoint. Outcomes: Free access to subscription-only data, undermining revenue.

## Requirements

1. Working API endpoint URL
2. Browser for URL editing
3. Target domains to query (e.g., semrush.com, hackerone.com)

## Defense

Defensive measures and detection strategies:

- Validate all input parameters against authenticated user scopes
- Implement session-based access controls for API calls
- Monitor for rapid parameter changes or unusual domain queries in logs

## Objectives

1. Bypass domain restrictions via direct reference manipulation
2. Retrieve detailed analytics for arbitrary domains
3. Demonstrate business impact of unauthenticated access

## Instructions

### Step 1: Edit Domain Parameter

**Context**: Change the 'domain' value in the URL to target a new site.

No specific command; in Firefox address bar, modify to: `http://us.api.semrush.com/?action=report&type=domain_rank&domain=hackerone.com`

> This triggers a new API query. Expected output: Response with hackerone.com's rank data.

### Step 2: Add Export and Database Parameters

**Context**: Enhance the query for more detailed output using additional parameters.

No specific command; append to URL: `&export_columns=Db,Dn,Rk,Or,Ot,Oc,Ad,At,Ac,Sv,Sh&database=us`

> Specifies columns and US database. Expected output: Comprehensive report with traffic, ad, and search volume metrics.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[idor]]
- [[api-bypass]]
