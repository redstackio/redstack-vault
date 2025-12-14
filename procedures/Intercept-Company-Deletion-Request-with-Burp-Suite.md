---
tags:
  - interception
  - burp-suite
  - discovery
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:25:28.806Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 91c4e7f1-f1bd-4c28-a46c-0cc24936471f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Intercept-Company-Deletion-Request-with-Burp-Suite

## Summary

This procedure uses Burp Suite to capture and analyze the company deletion request from the DoD vendor portal, revealing the structure of the vulnerable GET endpoint for IDOR exploitation.

## Description

Targeting an ASP.NET Core web application, this step involves proxying traffic through Burp Suite to intercept the deletion action on a test company. It allows observation of request parameters, headers, and cookies, identifying the IDOR flaw where no authorization checks occur. Prerequisites include a configured Burp proxy and an active vendor session. Outcomes include a detailed request log, enabling precise manipulation in the next phase.

## Requirements

1. Burp Suite installed and running with proxy listener on port 8080
2. Browser configured to use Burp as proxy (e.g., via FoxyProxy extension)
3. Active vendor session with test company created

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS and monitor for proxy interception via certificate pinning
- Log all deletion requests with user-context validation
- Use WAF rules to detect unusual request patterns or tool signatures like Burp

## Objectives

1. Capture the exact format of the deletion GET request
2. Verify authentication tokens and headers
3. Hold the request for safe modification without executing on the test company

## Instructions

### Step 1: Activate Burp Proxy

**Context**: Ensure all traffic routes through Burp for interception.

Launch Burp Suite and confirm the proxy tab is intercepting on the default port.

> Browser requests should pause in Burp's Intercept tab upon triggering actions.

### Step 2: Trigger Deletion

**Context**: Initiate the delete action on the test company to generate the request.

With proxy active, click the delete button on the test company page (e.g., https://██████/████/Vendor/Companies/{ID}).

> The request will be held in Burp; do not forward yet to avoid deleting the test company.

### Step 3: Observe Request Details

**Context**: Analyze the captured GET request for endpoint and parameters.

Examine the URL (/██████/Vendor/Companies/Delete/71712), headers (e.g., Host: ██████, Cookie: .AspNetCore.Antiforgery=..., .AspNetAuth=..., User-Agent: Mozilla/5.0...), and any body if present.

> Note the ID parameter and confirm no additional auth checks; this reveals the IDOR potential.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[interception]]
- [[tools/Burp-Suite]]
- [[Discovery]]
