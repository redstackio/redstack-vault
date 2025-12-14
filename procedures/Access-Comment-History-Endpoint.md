---
tags:
  - access
  - web
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:05.466Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 7fadac7b-94af-4778-ab4b-80a480936919
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Comment-History-Endpoint

## Summary

This procedure navigates to the vulnerable comment history endpoint using the retrieved site ID, confirming the parameter is reachable and setting up for SQL injection.

## Description

The endpoint https://intensedebate.com/commenthistory/$YourSiteId processes the site ID in backend SQL queries without sanitization. Accessing it normally loads comment data (or empty results), but it accepts the parameter directly, making it ripe for injection. This step validates the target before payload delivery.

## Requirements

1. Retrieved site ID
2. Authenticated session
3. Web browser or HTTP client

## Defense

Defensive measures and detection strategies:

- Parameterize all SQL queries to prevent injection
- Use input validation on URL parameters
- Log endpoint accesses with parameter values for anomaly detection

## Objectives

1. Confirm endpoint accessibility
2. Verify site ID integration
3. Prepare for payload modification

## Instructions

### Step 1: Construct Base URL

**Context**: Build the legitimate request to the endpoint.

Replace $YourSiteId in https://intensedebate.com/commenthistory/$YourSiteId with the actual ID.

> Example: https://intensedebate.com/commenthistory/12345

### Step 2: Request the Endpoint

**Context**: Fetch the page to observe normal behavior.

Visit the URL in a browser.

> Page loads with comment history; inspect for any errors or reflections of the ID.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[endpoint-access]]
- [[pre-exploit]]
