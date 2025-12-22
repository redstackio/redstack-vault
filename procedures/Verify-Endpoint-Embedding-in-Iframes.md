---
tags:
  - csrf
  - cross-origin
  - iframe
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:42.441Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: aeb4e8bf-66e8-4c1e-aa57-f3f5ef93e835
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Verify-Endpoint-Embedding-in-Iframes

## Summary

This procedure confirms that the VK.com endpoint can be embedded in iframes on external sites without cross-origin restrictions, paving the way for CSRF exploitation.

## Description

By embedding https://vk.com/al_groups.php?act=to_public_box&al=1&gid=<group_id> in an iframe on a third-party site like http://lincoln-shop.ru/, attackers verify loadability. Admins see silence, non-admins see errors, all without CORS blocks. Requires a controlled web server for testing.

## Requirements

1. Controlled website for hosting iframe (e.g., simple HTML server)
2. Victim's VK session (via visit while logged in)
3. Browser for testing embedding

## Defense

Defensive measures and detection strategies:

- Deploy X-Frame-Options: SAMEORIGIN or DENY
- Monitor for unusual cross-origin requests to internal endpoints
- Use CSP frame-ancestors directive

## Objectives

1. Validate embedding feasibility
2. Observe response rendering cross-origin
3. Confirm no blocking headers

## Instructions

### Step 1: Create Test HTML Page

**Context**: Build a page with iframe targeting the endpoint.

Create index.html:

```html
<iframe src="https://vk.com/al_groups.php?act=to_public_box&al=1&gid=147481259" width="800" height="600"></iframe>
<iframe src="https://vk.com/al_groups.php?act=to_public_box&al=1&gid=111" width="800" height="600"></iframe>
```

Host on local server or demo site.

> Load page while logged into VK; inspect iframes.

### Step 2: Observe Responses

**Context**: Check for load success and content visibility.

View source or console for errors.

> Success: Iframes load; admin silent, non-admin shows error.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[iframe]]
