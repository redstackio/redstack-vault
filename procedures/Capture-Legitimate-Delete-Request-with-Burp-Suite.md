---
id: proc-capture-delete-request
tags:
  - burp-suite
  - request-capture
  - api-interception
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:25:47.467Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Capture-Legitimate-Delete-Request-with-Burp-Suite

## Summary

This procedure uses Burp Suite to intercept and capture a legitimate DELETE request for a featured image on the attacker's own LinkedIn account, providing a template for IDOR exploitation.

## Description

To exploit the IDOR, a baseline request must be obtained by performing a deletion on the attacker's profile while proxying traffic through Burp Suite. The request targets the endpoint /voyager/api/voyagerIdentityDashProfileTreasuryMedia/urn:li:fsd_profileTreasuryMedia:(ImageId,ProfileId)?sectionUrn=urn:li:fsd_profile:ProfileId. This step assumes Burp is configured as a proxy and focuses on isolating the key parameters for later modification. Prerequisites include an active featured image and Burp Suite running.

## Requirements

1. Burp Suite installed and configured as browser proxy
2. Logged-in attacker LinkedIn session
3. Featured image present on attacker's profile

## Defense

Defensive measures and detection strategies:

- Log and monitor unusual API request patterns from authenticated sessions
- Rate-limit deletion endpoints to prevent replay attacks

## Objectives

1. Obtain authentic DELETE request structure
2. Identify modifiable parameters (ProfileId, ImageId)
3. Store request in Burp Repeater for editing

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp to intercept browser requests to LinkedIn.

In Burp Suite, ensure the proxy listener is active on 127.0.0.1:8080 and configure the browser to use this proxy.

### Step 2: Perform Deletion and Intercept

**Context**: Trigger the deletion action to capture the API call.

Log in to the attacker account, navigate to the featured image, select delete, and confirm while Burp intercepts. Forward the request to Repeater.

**Expected Output**: DELETE request visible in Repeater with headers, URL, and parameters populated from attacker's account.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[tools/Burp-Suite]]
- [[request-capture]]
- [[api-interception]]
