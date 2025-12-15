---
id: proc-okru-video-bypass-001
tags:
  - broken-authentication
  - access-bypass
  - web-vulnerability
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:11.357Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-Access-Controls-to-View-Private-Group-Videos-on-ok.ru-Mobile

## Summary

This procedure exploits broken authentication and absent access control validations on the mobile version of ok.ru (Odноклассники), a social networking site, to directly access private group videos without logging in or being a group member. By crafting a specific URL with group and video parameters, an attacker can view restricted content, leading to privacy violations and unauthorized data exposure.

## Description

The vulnerability stems from the mobile site's failure to enforce authentication or membership checks when accessing group video endpoints via direct links. The endpoint `/dk` with parameters like `st.cmd=altGroupMovieComments`, `st.groupId`, and `st.sbj` loads video content without verifying user permissions. This affects private groups where videos are intended for members only. The attack requires no tools beyond a browser and works over standard HTTP, making it accessible to any internet user. Expected outcomes include full video playback and comments visibility, confirming the bypass success. Prerequisites include knowledge of the target group's ID and video subject ID, which may be discoverable through public sources or enumeration.

## Requirements

1. Web browser with internet access
2. Target private group ID (e.g., from public group listings or enumeration)
3. Video subject ID (e.g., from leaked or guessed identifiers)
4. No authentication or VPN needed

## Defense

Defensive measures and detection strategies:

- Implement server-side access controls to validate user authentication and group membership for all endpoints, including mobile versions
- Use token-based authorization (e.g., JWT) and validate on every request to private resources
- Monitor for anomalous direct URL accesses to restricted endpoints via web application firewalls (WAF) or logging
- Enforce HTTPS and rate-limiting on mobile APIs to prevent enumeration

## Objectives

1. Achieve unauthorized initial access to restricted web resources
2. Expose private multimedia content without detection
3. Demonstrate the impact of missing authorization checks in web applications

## Instructions

### Step 1: Identify Target Group and Video Identifiers

**Context**: Gather the necessary parameters for the vulnerable URL. Group IDs and video subject IDs can be obtained from public group pages, API responses, or trial-and-error if partial information is available.

For the example, use groupId=53605096554748 and sbj=31115578108.

### Step 2: Construct and Access the Vulnerable URL

**Context**: Build the direct link to the mobile endpoint that bypasses checks, then navigate to it in a browser to load the content.

No command execution is needed; use the browser's address bar:

```url
http://m.ok.ru/dk?st.cmd=altGroupMovieComments&st.ord=off&st.groupId=53605096554748&st.sbj=31115578108
```

> This URL invokes the altGroupMovieComments command on the mobile site (/m.ok.ru), ordering results as 'off' (likely offline or default view), and targets the specified group and video. Upon loading, the page renders the video player and comments without any auth prompt.

### Step 3: Verify Access and Extract Content

**Context**: Confirm the bypass by checking for video playback and ensure no restrictions apply.

Interact with the loaded page: play the video, scroll comments. If successful, content is fully accessible.

> Expected output includes embedded video media and user comments from the private group, indicating complete unauthorized access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- broken-authentication
- access-bypass
- web-vulnerability
