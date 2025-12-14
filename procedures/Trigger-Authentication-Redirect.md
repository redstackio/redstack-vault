---
tags:
  - auth-bypass
  - redirect-trigger
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:18.077Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 091848d9-2d9d-4dbb-a89f-53d6d489d576
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-Authentication-Redirect

## Summary

This procedure initiates the authentication flow in a web application to trigger a vulnerable redirect response that includes protected admin content, setting up the EAR exploitation.

## Description

In vulnerable PHP-based applications, attempting to access protected areas without authentication results in a 302 redirect, but the response body erroneously contains the full HTML of the admin panel due to improper script termination (e.g., no 'die()' or 'exit()' after header()). This allows subsequent modification to expose the content. The target is a DoD-related web app with S3 integration, where this leads to unauthorized file management.

## Requirements

1. Network access to the target URL (e.g., https://target.com)
2. Browser or HTTP client capable of following redirects
3. Proxy tool like Burp Suite for interception

## Defense

Defensive measures and detection strategies:

- Implement proper script termination after redirects (e.g., 'exit;' in PHP)
- Validate authentication on all admin endpoints server-side
- Monitor for anomalous 200 responses on redirect endpoints

## Objectives

1. Generate the vulnerable redirect response
2. Capture the response containing admin HTML
3. Prepare for status code modification

## Instructions

### Step 1: Access Main Application and Login Entry

**Context**: Navigate to the application's entry point to simulate an unauthenticated login attempt, triggering the redirect chain.

Browse to the main page `https://████/` and click the login button, which sends a POST to `https://█████████/█████`. This redirects to `https://█████/█████` and then to `https://███████/█████████`.

**Expected Output**: 302 redirect response with admin panel HTML in the body.

### Step 2: Intercept the Redirect Chain

**Context**: Use a proxy to capture the full redirect sequence for analysis.

Configure your browser to proxy through Burp Suite and repeat the login interaction to log the requests.

**Expected Output**: Logged HTTP traffic showing the 302 status and embedded HTML.

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

- [[auth-bypass]]
- [[redirect-trigger]]
