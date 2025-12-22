---
tags:
  - ssrf
  - ghost-cms
  - admin-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:53:38.716Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: d0913293-5f95-4e8a-b87c-cb45649d8128
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Ghost-Admin-and-Identify-oEmbed-Endpoint

## Summary

This procedure involves logging into the Ghost CMS admin interface as a publisher and locating the oEmbed URL input field used for embedding external content, setting the stage for SSRF testing.

## Description

In Ghost CMS 3.5.2, the admin panel at /ghost/ allows authenticated users with publisher roles to embed content via URLs. Selecting 'Other...' in the embed options reveals an input that sends requests to the /ghost/api/v3/admin/oembed/ endpoint. This is the entry point for the SSRF vulnerability, as the backend fetches the provided URL without sufficient validation in certain paths.

## Requirements

1. Publisher role credentials for Ghost CMS
2. Web browser or HTTP client for admin access
3. Network connectivity to the Ghost instance

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls to limit embed features
- Monitor admin panel access logs for unusual embed attempts
- Use web application firewalls to inspect oEmbed requests

## Objectives

1. Confirm access to the admin embed interface
2. Identify the exact endpoint and parameters used
3. Prepare for subsequent SSRF testing

## Instructions

### Step 1: Log In to Ghost Admin

**Context**: Authenticate to the admin panel to access embedding features.

Navigate to https://your-ghost-instance/ghost/ and log in with publisher credentials.

> Successful login grants access to the dashboard.

### Step 2: Locate oEmbed Input

**Context**: Find the URL input for custom embeds.

In the editor or content section, attempt to embed content and select 'Other...' to reveal the URL field, which constructs requests to /ghost/api/v3/admin/oembed/?url=<input>&type=embed.

> The input field appears, confirming the feature is active.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- ghost-cms
- admin-access
