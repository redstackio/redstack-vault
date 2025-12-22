---
id: proc-tiktok-access-identify
tags:
  - access
  - endpoint-discovery
  - web
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:56.702Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access TikTok Ads Portal and Identify Endpoint

## Summary

This procedure outlines logging into the TikTok Ads Portal with an authenticated account and using browser tools to discover the vulnerable API endpoint that exposes advertiser account data via the 'aadvid' parameter.

## Description

In the context of the TikTok Ads Portal IDOR vulnerability, initial access requires a valid user account. Navigation to features like invited Ad Accounts triggers API calls. By inspecting network traffic, attackers identify the endpoint lacking proper authorization checks, setting up parameter manipulation. This step assumes the attacker has an account with access to multiple invited accounts in the same business group.

## Requirements

1. Valid TikTok Ads Portal credentials (email/password or OAuth)
2. Modern web browser (e.g., Chrome, Firefox) with developer tools enabled
3. Accounts must be in the same business group for later exploitation

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) on API endpoints
- Log and monitor parameter manipulations in API requests
- Use web application firewalls (WAF) to detect anomalous 'aadvid' changes

## Objectives

1. Establish authenticated session in the portal
2. Locate the 'aadvid'-based API endpoint
3. Prepare for IDOR exploitation

## Instructions

### Step 1: Authenticate to the Portal

**Context**: Log in to gain a session that allows access to Ad Account features.

Open https://ads.tiktok.com in your browser and log in with valid credentials. Navigate to the 'Ad Account' or 'Business Center' section to view invited accounts.

**Expected Output**: Dashboard loaded with account listings.

### Step 2: Inspect Network Traffic for Endpoint

**Context**: Identify the API call handling account retrieval.

Open browser developer tools (F12), go to the Network tab, and refresh or interact with invited accounts. Filter for XHR/Fetch requests and search for 'aadvid' in request parameters.

**Expected Output**: Endpoint URL like /api/v1/advertiser/info?aadvid=123456 visible in requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[access]]
- [[endpoint-discovery]]
- [[web]]
