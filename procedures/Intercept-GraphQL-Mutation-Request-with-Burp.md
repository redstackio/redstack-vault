---
id: proc-intercept-graphql-burp
tags:
  - interception
  - graphql
  - proxy
type: procedure
tools:
  - '[[tools/Burp-Proxy]]'
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
updated_at: '2025-12-14T17:26:00.442Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-GraphQL-Mutation-Request-with-Burp

## Summary

This procedure uses Burp Proxy to capture and analyze the GraphQL mutation request triggered by editing a certification on HackerOne, revealing the structure of the CreateOrUpdateHackerCertification query for subsequent manipulation.

## Description

Targeted at web applications using GraphQL, this involves proxying traffic from the browser to intercept HTTP POST requests to the API endpoint. In the HackerOne scenario, editing one's own certification generates a mutation request lacking proper ID validation, allowing observation of parameters like 'id' and 'input'. Prerequisites include an active session and Burp configured as a proxy.

## Requirements

1. Running instance of Burp Suite with Proxy listener on 127.0.0.1:8080
2. Browser proxy settings configured to route through Burp
3. Authenticated HackerOne session

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS and certificate pinning to detect proxy interception
- Log and alert on proxied traffic or unusual request patterns
- Implement client-side request signing to prevent tampering

## Objectives

1. Capture the exact GraphQL mutation payload
2. Identify editable parameters like ID
3. Prepare for request modification without errors

## Instructions

### Step 1: Configure Proxy

**Context**: Route browser traffic through Burp to enable interception.

No command; UI-based:

In Burp, ensure Proxy tab is listening on 127.0.0.1:8080. In browser settings, set HTTP proxy to this address and port.

> Traffic now flows through Burp; turn on Intercept in Proxy > Intercept tab.

### Step 2: Trigger and Intercept Request

**Context**: Generate the mutation by editing a certification.

No command; platform action:

Navigate to certifications in HackerOne, edit an existing one, and submit. Burp intercepts the POST to /graphql or similar endpoint.

> Intercepted request shows JSON body with "query": "mutation CreateOrUpdateHackerCertification..." and variables including "id".

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Proxy]]

## Tags

- [[interception]]
- [[graphql]]
- [[proxy]]
