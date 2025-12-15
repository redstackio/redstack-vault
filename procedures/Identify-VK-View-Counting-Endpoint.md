---
id: proc-uuid-1
tags:
  - recon
  - web
  - endpoint-discovery
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
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:35.774Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify VK View Counting Endpoint

## Summary

This procedure involves inspecting network traffic on VK.com to locate the backend endpoint used for registering post views, revealing the structure needed for further exploitation.

## Description

In the context of analyzing VK.com for vulnerabilities, this step uses browser developer tools to monitor requests during normal post viewing. The target environment is the VK.com web application, where views are incremented via AJAX-like calls. Prerequisites include access to VK.com and basic knowledge of web debugging. Expected outcome is the endpoint URL and parameter details, setting the stage for CSRF analysis.

## Requirements

1. Web browser with developer tools (e.g., Chrome DevTools)
2. Access to a VK.com account to view posts
3. Basic understanding of HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement web application firewalls (WAF) to log unusual endpoint access patterns
- Monitor for anomalous network inspection tools in user sessions

## Objectives

1. Locate the exact URL for view registration
2. Document request parameters like 'data'
3. Confirm endpoint behavior on post views

## Instructions

### Step 1: Monitor Network Traffic

**Context**: Open VK.com in a browser and navigate to a post to trigger view registration.

**Instructions**: In developer tools, go to the Network tab, filter for XHR/Fetch requests, and reload the post page. Identify requests to al_page.php with act=seen.

> The request will show parameters like act=seen&al=1&data=[post_id_details]. Note the full URL: https://vk.com/al_page.php?act=seen&al=1&data=.

### Step 2: Document Endpoint Details

**Context**: Extract and record the endpoint structure for replication.

**Instructions**: Copy the request URL and payload. Test by viewing multiple posts to see how 'data' parameter varies with post IDs.

> Successful identification confirms the endpoint handles view increments without additional auth beyond session cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[web]]
