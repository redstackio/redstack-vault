---
id: proc-test-base-post-001
tags:
  - testing
  - api
  - post-request
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-base-post-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:28.886Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Endpoint-with-Base-POST-Request

## Summary

This procedure tests the accessibility of the user operations API endpoint by sending a basic POST request with the 'sendingForm' parameter, confirming it processes requests without authentication and preparing for IDOR parameter addition.

## Description

In the DoD system, the endpoint requires a 'sendingForm' parameter (e.g., a value indicating user info retrieval) to function. This test verifies the endpoint's responsiveness in an ASP.NET environment, exposing the lack of security checks that allow subsequent UID manipulation for data scraping.

## Requirements

1. Identified API endpoint URL from prior reconnaissance
2. curl tool installed for HTTP requests
3. Knowledge of the specific 'sendingForm' value used in the target application

## Defense

Defensive measures and detection strategies:

- Require authentication tokens in all POST requests
- Log and alert on anomalous POST payloads missing expected parameters
- Implement input validation to reject incomplete form data

## Objectives

1. Confirm endpoint processes POST requests unauthenticated
2. Establish a baseline response for comparison in exploitation
3. Identify any rate limits or basic protections

## Instructions

### Step 1: Prepare Base Request

**Context**: Construct the POST data with the required 'sendingForm' parameter to mimic legitimate user interactions.

Execute [[commands/curl-base-post-request]]:

```bash
curl 'https://target.gov/userops.aspx' --data-raw 'sendingForm=userInfo'
```

> This sends the base request; expect a success code (e.g., 200) with minimal or no data, indicating accessibility.

### Step 2: Analyze Response

**Context**: Review the output for signs of vulnerability, such as no auth errors.

No additional command; parse the curl output manually.

> Successful execution shows the endpoint is ready for parameter injection like UID.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-base-post-request]]

## Tools Used

- [[tools/curl]]

## Tags

- [[testing]]
- [[post-request]]
