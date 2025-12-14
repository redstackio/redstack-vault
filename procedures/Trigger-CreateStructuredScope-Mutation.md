---
id: proc-trigger-graphql-mutation
tags:
  - graphql
  - mutation-trigger
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:56.724Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger CreateStructuredScope Mutation

## Summary

This procedure initiates the GraphQL mutation for creating a structured scope in a web application like HackerOne, generating a POST request that can be intercepted for further exploitation in a DoS attack.

## Description

In the context of exploiting validation flaws, this step navigates the application's scope management interface to trigger the CreateStructuredScope mutation. It sets up the baseline request with standard variables (e.g., asset_type: URL, instruction as empty or small string), which is then proxied for modification. The target environment is a web app with GraphQL over HTTPS on port 443, requiring authenticated access. Expected outcome is a capturable HTTP POST without errors, confirming the mutation path.

## Requirements

1. Authenticated session with access to scope management (valid X-Auth-Token and cookies)
2. Proxy tool like Burp Suite configured to intercept traffic
3. Network access to the /graphql endpoint

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on GraphQL mutations
- Log and monitor mutation invocations for anomalous patterns
- Enforce client-side and server-side authentication checks

## Objectives

1. Generate a legitimate CreateStructuredScope request for interception
2. Verify authenticated access to the endpoint
3. Prepare for payload modification without alerting defenses

## Instructions

### Step 1: Navigate to Scope Management

**Context**: Access the application's interface to initiate scope creation, triggering the mutation.

**Instructions**: Log in to the target application, go to the scope management page (e.g., /testingfordos/scopes/new), and enter a domain to create a structured scope.

> This generates a POST request to /graphql with operationName: CreateStructuredScope and variables including team_id, asset_identifier (e.g., example.com), asset_type: URL, and instruction.

### Step 2: Confirm Request Generation

**Context**: Ensure the request is ready for proxy interception.

**Instructions**: Submit the form and verify in the browser developer tools or proxy that the request includes the full GraphQL query and variables.

> Expected output: JSON payload with mutation query string and variables object; status 200 or 201 if unproxied.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[graphql]]
- [[mutation-trigger]]
