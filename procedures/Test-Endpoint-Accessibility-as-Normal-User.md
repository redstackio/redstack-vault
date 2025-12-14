---
tags:
  - access-testing
  - privilege-escalation
  - ajax-request
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/ajax-post-toggle-res-menu-type]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:44.336Z'
sub_techniques: []
id: a3c8ad9d-1029-4235-a79c-4aeb2a1ed023
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Endpoint-Accessibility-as-Normal-User

## Summary

This procedure tests whether an admin-only endpoint, like Zomato's /php/restaurant_menus_handler.php, is accessible to standard authenticated users by sending a POST request via the browser console, confirming broken access controls.

## Description

Authenticated users on platforms like Zomato should not access admin endpoints, but insufficient checks allow privilege escalation. This involves crafting an AJAX request in the browser console to simulate admin actions. Prerequisites: Authenticated session and known endpoint from reconnaissance. Outcomes: Successful request execution without denial, paving the way for exploitation.

## Requirements

1. Active authenticated session as a non-admin user
2. Browser with developer console (e.g., on a restaurant page)
3. Valid restaurant ID (res_id) from page inspection

## Defense

Defensive measures and detection strategies:

- Enforce role-based access control (RBAC) on all endpoints
- Log and alert on unauthorized POST requests to admin paths
- Use server-side authentication tokens validated per action

## Objectives

1. Verify endpoint reachability without admin privileges
2. Confirm lack of authorization checks
3. Prepare for impact verification

## Instructions

### Step 1: Prepare the Environment

**Context**: Ensure the browser is on a restaurant page with the target loaded.

**Command** (Page Load):
Manually navigate to https://www.zomato.com/[restaurant-slug] and open console (F12).

> Verify session cookies are present; extract res_id from URL or page source (e.g., data-res-id attribute).

### Step 2: Execute Test Request

**Context**: Send the AJAX POST to test access.

**Command** ([[commands/ajax-post-toggle-res-menu-type]]):
```javascript
$.ajax({url:"/php/restaurant_menus_handler.php",type:"POST",data:{action:"toggle-res-menu-type",res_id:12345}});
```

> Replace res_id with actual value. Expected output: No error; console shows success or empty response, indicating processing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/ajax-post-toggle-res-menu-type]]

## Tools Used


## Tags

- [[access-testing]]
- [[web-exploit]]
