---
id: proc-access-endpoint-001
tags:
  - web-access
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:05.297Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Target-Web-Endpoint

## Summary

This procedure involves navigating to a legitimate endpoint of the target web application to establish a baseline and identify modifiable URL path parameters for potential vulnerabilities.

## Description

In the context of testing web applications like https://corporate.admyntec.co.za/, this step accesses URLs generated during user processes such as customer registration or insurance quoting. It confirms endpoint functionality and reveals parameters like userId, customerId, and contactPersonId that may be vulnerable to injection if unsanitized. Expected outcomes include normal page load, setting the stage for manipulation.

## Requirements

1. Web browser (e.g., Chrome, Firefox)
2. Direct internet access to the target domain
3. Knowledge of application flow to obtain a valid URL

## Defense

Defensive measures and detection strategies:

- Implement web application firewall (WAF) to monitor access patterns
- Log all endpoint requests and alert on unusual parameter values

## Objectives

1. Confirm endpoint accessibility and parameter structure
2. Gather baseline response for comparison in testing
3. Identify potential injection points in path parameters

## Instructions

### Step 1: Obtain and Navigate to URL

**Context**: Use a URL from the application's normal workflow to access the endpoint without raising suspicion.

No command required; use browser to visit: https://corporate.admyntec.co.za/customerInsurance/newCustomerStep8/userId/868878/customerId/732562/contactPersonId/0

> The page should display insurance details. Note the parameters for modification in subsequent steps.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web-access
- recon
