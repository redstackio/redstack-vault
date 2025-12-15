---
id: proc-001
tags:
  - web
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
updated_at: '2025-12-14T17:26:27.852Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Insurance-Registration-URL

## Summary

This procedure involves navigating to a generated URL in the insurance registration flow of the target web application to expose vulnerable path parameters for potential SQL injection attacks.

## Description

In the context of the https://corporate.admyntec.co.za/ application, the insurance registration process generates a URL with path parameters like userId, customerId, and contactPersonId. These parameters are directly used in backend SQL queries without sanitization, making them prime targets for injection. This step sets up the attack surface by accessing the URL during the registration workflow, allowing subsequent testing and exploitation.

## Requirements

1. Web browser with access to the internet
2. Ability to initiate the customer insurance registration process
3. No special credentials required, as the flow is public

## Defense

Defensive measures and detection strategies:

- Implement URL parameter validation and sanitization at the application layer
- Use prepared statements or parameterized queries in backend SQL code
- Monitor access logs for unusual URL modifications

## Objectives

1. Obtain the vulnerable URL with ID parameters
2. Verify the endpoint loads correctly
3. Prepare for injection testing on path parameters

## Instructions

### Step 1: Initiate Registration Flow

**Context**: Start the insurance registration to generate the target URL.

No specific command; manually navigate through the web application to the step that produces the details URL.

> Proceed via browser to https://corporate.admyntec.co.za/customerInsurance/newCustomerStep8/userId/{userId}/customerId/{customerId}/contactPersonId/{contactPersonId}, where IDs are dynamically generated.

### Step 2: Capture and Inspect URL

**Context**: Examine the URL for injectable parameters.

Copy the full URL from the browser address bar and note the values of userId, customerId, and contactPersonId.

> Expected output: URL like https://corporate.admyntec.co.za/customerInsurance/newCustomerStep8/userId/868878/customerId/732562/contactPersonId/0.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web
- recon
