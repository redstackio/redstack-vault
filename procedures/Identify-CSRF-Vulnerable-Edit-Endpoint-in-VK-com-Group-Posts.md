---
id: proc-uuid-1
tags:
  - csrf
  - recon
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:35.377Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify CSRF-Vulnerable Edit Endpoint in VK.com Group Posts

## Summary

This procedure involves inspecting VK.com's group post editing functionality to identify the request for modifying advertising carousel cards, confirming the absence of CSRF token protection that enables cross-site forgery.

## Description

In the context of VK.com, group administrators can edit posts including advertising carousel cards via web requests. The vulnerability arises because the edit endpoint does not include a CSRF hash or token, allowing attackers to forge requests from external sites. This procedure outlines using browser tools to capture and analyze the vulnerable request, setting the stage for exploitation. Prerequisites include a VK.com account with group editing privileges. Expected outcomes: Detailed request parameters and confirmation of missing protections.

## Requirements

1. Authenticated VK.com session with group admin access
2. Modern web browser with developer tools (e.g., Chrome, Firefox)
3. Access to a group post with carousel cards

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing POST requests
- Enforce same-origin policy checks and CORS headers
- Monitor for anomalous edit requests from unexpected referers

## Objectives

1. Locate and document the edit endpoint for carousel cards
2. Verify lack of CSRF protection
3. Prepare parameters for forging in subsequent exploitation

## Instructions

### Step 1: Authenticate and Prepare Test Post

**Context**: Establish a controlled environment to trigger the edit request.

Log in to VK.com and navigate to a group where you have admin rights. Create a new post or select an existing one, adding advertising carousel cards (e.g., multiple image/text slides).

### Step 2: Capture the Edit Request

**Context**: Use developer tools to inspect the network traffic during editing.

Open browser developer tools (F12), go to the Network tab, and filter for XHR/Fetch. Edit the carousel cards by changing text or images, then save/submit. Locate the POST request to the edit endpoint (e.g., https://vk.com/al/groups.php with parameters like act=a_edit_post, group_id, and carousel data).

Inspect request headers, form data, and response. Note the absence of a CSRF token (e.g., no 'hash' or 'lh' parameter typically used by VK.com).

### Step 3: Validate Vulnerability

**Context**: Confirm the request can be forged by testing cross-origin submission.

Copy the request details. In a new tab, create a simple HTML form pointing to the endpoint and submit it. If it succeeds without errors, the endpoint is vulnerable to CSRF.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[recon]]
