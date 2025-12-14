---
tags:
  - wordpress
  - privilege-escalation
  - logic-flaw
  - nonce-bypass
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:28.512Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 44b65af4-d54c-4a77-b1cf-5c945ff4c692
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Create-Arbitrary-Post-Type-in-WordPress

## Summary

This procedure exploits a business logic error in WordPress's post submission mechanism, allowing authenticated authors to create posts of arbitrary types without the required nonce verification, resulting in privilege escalation to unauthorized content management.

## Description

WordPress's post creation process (handled via wp-admin/post-new.php) inadequately verifies nonces for arbitrary post types, enabling authors to modify form inputs and bypass restrictions. This leads to creation of posts in types like 'pages' or custom post types reserved for higher roles, potentially exposing sensitive data or functionalities. The attack requires an authenticated session and uses browser-based form tampering. Outcomes include unauthorized post creation and modification, with risks of data leakage if sensitive types are targeted.

## Requirements

1. Authenticated session as a WordPress author
2. Access to the post creation form (wp-admin/post-new.php)
3. Browser with developer tools for inspecting and modifying HTML forms

## Defense

Defensive measures and detection strategies:

- Implement proper nonce checks for all post types in custom code or plugins
- Use capability checks to restrict post type creation based on user roles
- Monitor audit logs for unusual post creations (e.g., authors creating pages) via plugins like Activity Log
- Regularly update WordPress core and plugins to patch known logic flaws

## Objectives

1. Bypass nonce verification for unauthorized post types
2. Escalate privileges to create and manage restricted content
3. Gain potential access to sensitive data through escalated post types

## Instructions

### Step 1: Access Post Creation Form

**Context**: Load the vulnerable post creation interface to prepare for input manipulation.

Navigate to `https://target.com/wp-admin/post-new.php` in the authenticated browser session.

> The form should load with default fields for a standard 'post' type. Inspect the HTML using developer tools (F12) to locate the 'post_type' hidden input or related fields.

### Step 2: Modify Form Data

**Context**: Alter the post type parameter to an unauthorized value without adding the nonce.

In the developer tools console or Elements tab, change the value of the 'post_type' field (e.g., from 'post' to 'page' or a custom type like 'attachment'). Ensure no nonce field for the target type is included.

> Example modification: Set `<input type="hidden" name="post_type" value="page">`. Fill in other required fields like title and content, then submit the form via POST to the same endpoint.

### Step 3: Submit and Verify

**Context**: Execute the submission and confirm the bypass.

Click 'Publish' or simulate the POST request. Check the admin lists for the new post in the targeted type.

> Successful response: Redirect to edit screen or success message. Verify in wp-admin by navigating to the post type's list (e.g., Pages > All Pages).

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[wordpress]]
- [[privilege-escalation]]
- [[logic-flaw]]
