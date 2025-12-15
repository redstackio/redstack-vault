---
id: proc-tiktok-obtain-campaign-id-001
tags:
  - enumeration
  - campaign-id
  - tiktok
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:12.254Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Obtain-TikTok-Campaign-ID

## Summary

This procedure involves acquiring a valid campaign ID from TikTok's Ads platform, which is necessary for targeting the vulnerable endpoint in a clickjacking attack. It relies on enumeration or prior access to expose IDs used in API calls.

## Description

In the context of exploiting TikTok's Ads endpoint, the attacker first needs a legitimate campaign ID to construct the targeted iframe URL. This can be obtained by signing up for a TikTok Ads account, creating a sample campaign, and inspecting the ID from the dashboard or network requests. Without proper access controls, IDs can also be enumerated via predictable patterns or leaked sources. The procedure assumes basic web inspection skills and targets the web-based Ads interface.

## Requirements

1. Access to a TikTok account with Ads permissions.
2. Browser with developer tools (e.g., Chrome DevTools).
3. Basic knowledge of inspecting HTTP requests.

## Defense

Defensive measures and detection strategies:

- Implement ID obfuscation or non-sequential numbering for campaigns.
- Monitor for unusual enumeration attempts on Ads APIs via rate limiting and logging.

## Objectives

1. Retrieve a functional campaign ID for use in attack construction.
2. Verify the ID enables access to the vulnerable endpoint.
3. Minimize detection by using legitimate account access.

## Instructions

### Step 1: Access TikTok Ads Dashboard

**Context**: Log in to TikTok Ads and navigate to campaign management to expose IDs.

No specific command; use browser to visit https://ads.tiktok.com and create or view a campaign. Open DevTools (F12), go to Network tab, and reload the campaigns page to capture API requests containing the ID.

> Inspect requests to endpoints like /campaigns/ for JSON responses with 'id' fields.

### Step 2: Extract and Verify ID

**Context**: Copy the ID and test direct access to confirm validity.

Paste the ID into a URL like https://ads.tiktok.com/campaigns/{ID} and ensure it loads the campaign page without errors.

> Expected output: Campaign details page loads successfully.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[enumeration]]
- [[tiktok]]
- [[ads]]
