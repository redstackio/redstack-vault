---
id: proc-intercept-scheduled-post
tags:
  - traffic-interception
  - proxy
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
  - '[[Network Sniffing]]'
updated_at: '2025-12-14T03:16:25.200Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Network Sniffing]]'
---
# Intercept-Scheduled-Post-Request

## Summary

This procedure captures the HTTP POST request used for creating or editing scheduled posts in the Kit app on Shopify, enabling subsequent modification for vulnerability exploitation.

## Description

In the context of testing for stored XSS, intercepting API requests allows visibility into form parameters like 'website_link'. This is typically done using a proxy tool while performing normal post creation/editing actions in the app's dashboard. The target endpoint is `/pages/{page_id}/manual_posts/{post_id}`, where {page_id} and {post_id} are specific to the user's Shopify store and post.

## Requirements

1. Authenticated session in the Kit app (valid Shopify user credentials)
2. Proxy tool configured to intercept HTTPS traffic (e.g., Burp Suite with CA certificate installed)
3. Network access to kitcrm.com

## Defense

Defensive measures and detection strategies:

- Monitor for unusual proxy traffic or certificate pinning bypasses
- Implement request logging at the API gateway to detect interception patterns

## Objectives

1. Capture the exact request structure for scheduled post operations
2. Identify filterable parameters like 'website_link'
3. Prepare for payload injection without alerting the application

## Instructions

### Step 1: Configure Proxy

**Context**: Set up a tool to intercept traffic from the browser to the Kit app.

No specific command; configure Burp Suite or similar to proxy browser traffic and ensure HTTPS interception is enabled.

> Expected: All requests to kitcrm.com routed through proxy.

### Step 2: Trigger Request

**Context**: Perform an action in the app to generate the target POST request.

Navigate to the scheduled posts section in the Kit app dashboard and attempt to create or edit a post.

> Expected: POST request to `/pages/{page_id}/manual_posts/{post_id}` appears in proxy history, showing multipart/form-data with fields like 'website_link'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Network Sniffing]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[traffic-interception]]
- [[proxy-setup]]
