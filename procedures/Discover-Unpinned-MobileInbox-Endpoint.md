---
id: proc-discover-unpinned-endpoint
tags:
  - ssl-pinning-bypass
  - endpoint-discovery
  - mobile
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/get-mobileinbox-limit]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Sniffing]]'
updated_at: '2025-12-14T17:32:20.541Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Sniffing]]'
---
# Discover-Unpinned-MobileInbox-Endpoint

## Summary

This procedure involves manually exploring the Starbucks app to trigger and intercept requests to unpinned endpoints like /MobileInbox/, bypassing SSL pinning limitations.

## Description

Developers overlooked pinning the /MobileInbox/ path, allowing interception via Burp Suite when the app's messages tab is accessed. This exposes requests that can be analyzed for auth tokens.

## Requirements

1. Burp Suite proxy active from prior setup.
2. Starbucks app installed and functional.
3. Knowledge of app UI to trigger specific requests.

## Defense

Defensive measures and detection strategies:

- Audit SSL pinning implementation to cover all endpoints.
- Log and alert on anomalous app requests to internal paths.
- Use app integrity checks to detect proxy usage.

## Objectives

1. Trigger unpinned requests through app navigation.
2. Capture successful interceptions in Burp.
3. Identify vulnerable paths for further exploitation.

## Instructions

### Step 1: Navigate App Messages Tab

**Context**: Access the messages/inbox feature to generate API calls.

In the app, go to the messages tab and interact (e.g., refresh inbox).

> This triggers a GET to /api/v1/MobileInbox/Limit/20, which succeeds in Burp due to missing pinning.

### Step 2: Monitor Burp History

**Context**: Check for intercepted requests post-navigation.

Execute [[commands/get-mobileinbox-limit]] equivalent in Burp or replay the captured request.

```bash
curl -k -H "Authorization: Basic QVBSTlhXTFpUUTo4NGY0NDlmMWYzOWEyMDUz" https://crmproxy.protel.com.tr/api/v1/MobileInbox/Limit/20
```

> Expected: JSON response with inbox data; confirms unpinned path.

### Step 3: Verify Response

**Context**: Ensure the endpoint returns data without pinning interference.

Inspect the response in Burp for content like message lists.

> Success: No SSL errors; request fully intercepted.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Network Sniffing]] Network Sniffing

### Sub-Techniques

- None

## Commands Used

- [[commands/get-mobileinbox-limit]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- ssl-pinning-bypass
- endpoint-discovery
