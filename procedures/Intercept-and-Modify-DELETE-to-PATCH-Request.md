---
id: proc-frontegg-intercept-modify-001
tags:
  - request-interception
  - burp-suite
  - method-modification
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/frontegg-delete-api-key]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:32:29.175Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Intercept-and-Modify-DELETE-to-PATCH-Request

## Summary

This procedure intercepts an Admin's DELETE request for an Owner API key using Burp Suite, modifies the HTTP method to PATCH, and prepares it for unauthorized editing, exploiting the API's lack of method-specific authorization.

## Description

From the Admin account, initiate a delete action on the Owner's API key via UI, proxying traffic through Burp Suite to capture the DELETE request to `/frontegg/identity/resources/tenants/api-tokens/v1/<API_KEY_ID>`. Drop the original request and switch to PATCH in the Repeater tab. This bypasses UI restrictions, as the endpoint accepts PATCH without proper checks. Prerequisites: Burp Suite configured as proxy, Admin login, and known API_KEY_ID. Expected outcome: Ready-to-send PATCH request.

## Requirements

1. Burp Suite installed and browser proxied
2. Admin account logged in
3. API_KEY_ID from prior step

## Defense

Defensive measures and detection strategies:

- Validate HTTP methods per role in API gateways
- Monitor for anomalous method changes in proxy logs
- Implement request signing to prevent tampering

## Objectives

1. Capture legitimate DELETE for modification
2. Alter method to enable editing
3. Set up for payload injection

## Instructions

### Step 1: Initiate Delete from Admin UI

**Context**: Trigger the interceptable request.

Log in as Admin, select the Owner's API key, and click delete in the dashboard.

**Expected Output**: DELETE request intercepted in Burp Proxy.

### Step 2: Drop and Forward to Repeater

**Context**: Prevent actual deletion and prepare modification.

In Burp, drop the request and forward to Repeater without sending.

Execute [[commands/frontegg-delete-api-key]] equivalent via UI action:

```http
DELETE /frontegg/identity/resources/tenants/api-tokens/v1/<API_KEY_ID> HTTP/1.1
Host: your-frontegg-instance.com
Authorization: Bearer <ADMIN_TOKEN>
```

> Intercepted request shows DELETE method; drop to avoid execution.

### Step 3: Change Method to PATCH

**Context**: Exploit endpoint's acceptance of PATCH.

In Repeater, edit the method from DELETE to PATCH, keeping endpoint and headers.

**Expected Output**: Request now shows PATCH method.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript (UI manipulation proxy)

### Sub-Techniques


## Commands Used

- [[commands/frontegg-delete-api-key]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[request-interception]]
- [[tools/Burp-Suite]]
- [[method-modification]]
