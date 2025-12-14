---
tags:
  - wordpress
  - privilege-escalation
  - logic-flaw
  - nonce-bypass
  - business-logic
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Authenticate-as-WordPress-Author]]'
  - '[[procedures/Create-Arbitrary-Post-Type-in-WordPress]]'
step_count: 2
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:28.517Z'
description: >-
  Authenticated authors exploit a logic flaw in WordPress post creation to
  bypass nonce verification and create posts of unauthorized types, leading to
  privilege escalation.
skill_level: intermediate
impact_level: high
id: dc6e5d5b-987f-4d08-861c-6c474e471f7a
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# WordPress Privilege Escalation via Arbitrary Post Type Creation Without Nonce

Multi-stage attack chain demonstrating a complete attack workflow exploiting a logic flaw in WordPress's post creation process.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Authenticate as Author] --> B[Submit Crafted Post Data]
    B --> C[Privilege Escalation]
    C --> D[Unauthorized Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser with developer tools (e.g., Chrome DevTools for form manipulation)

### Target Environment

- WordPress instance (version vulnerable to the logic flaw, e.g., pre-patch versions)
- PHP backend
- Access to wp-admin interface

### Initial Access Requirements

- Valid author-level credentials
- Network access to the WordPress admin panel
- No prior elevated access needed beyond author role

## Detailed Attack Procedures

### Step 1: Authenticate as Author
procedure: [[procedures/Authenticate-as-WordPress-Author]]

**Objective**: Gain access to the WordPress post creation interface as an authenticated author user.

**Instructions**: Log in to the WordPress admin dashboard using author credentials. Navigate to the 'Posts > Add New' section to access the post creation form.

**Expected Output**: Successful login and visibility of the post creation interface.

**Success Indicators**:
- Admin dashboard loads without errors
- Post creation form is accessible

### Step 2: Submit Crafted Post Data
procedure: [[procedures/Create-Arbitrary-Post-Type-in-WordPress]]

**Objective**: Exploit the logic flaw by submitting form data for an unauthorized post type without the required nonce, achieving privilege escalation.

**Instructions**: Use browser developer tools to inspect and modify the post creation form. Alter the 'post_type' field to an unauthorized type (e.g., 'page' or custom type) and submit without the corresponding nonce. Monitor the response for successful creation.

**Expected Output**: Post created successfully in the specified unauthorized type, confirming bypass.

**Success Indicators**:
- New post appears in the unauthorized type's admin list
- No nonce verification error occurs

## Attack Chain Summary

### Key Achievements

1. Authenticated access to post creation
2. Bypassed nonce for arbitrary post types
3. Escalated privileges to manage unauthorized content

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]]

### MITRE ATT&CK Tactics

- [[Privilege Escalation]]

---
*Last updated: 2023-10-01T00:00:00Z*
