---
tags:
  - privilege-escalation
  - access-control
  - web-vulnerability
  - php
  - javascript
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
  - '[[procedures/Discover-Admin-Endpoint-in-JavaScript-Files]]'
  - '[[procedures/Test-Endpoint-Accessibility-as-Normal-User]]'
  - '[[procedures/Verify-Menu-Modification-Exploitation]]'
step_count: 3
techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:44.343Z'
description: >-
  A multi-step privilege escalation attack exploiting insufficient access
  controls in Zomato's restaurant menus handler endpoint, enabling any
  authenticated user to modify or delete restaurant menus.
skill_level: intermediate
impact_level: high
id: c3d170fa-9c55-4414-9b46-9344bb973f2d
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Exploit Public-Facing Application]]'
---
# Zomato Privilege Escalation Allowing Unauthorized Restaurant Menu Edits

Multi-stage attack chain demonstrating privilege escalation in Zomato's web application, where an endpoint intended for admins is accessible to all authenticated users, allowing menu edits and deletions that disrupt restaurant operations and data integrity.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discover Endpoint] --> B[Test Accessibility]
    B --> C[Exploit and Verify]
    C --> D[Menu Modification Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser Developer Tools (e.g., Chrome DevTools)

### Target Environment

- Zomato web platform (www.zomato.com)
- Authenticated user session (normal user account)
- Web browser with JavaScript console access

### Initial Access Requirements

- Valid Zomato user credentials (non-admin)
- Network access to Zomato's website
- No prior admin privileges needed

## Detailed Attack Procedures

### Step 1: Discover Admin Endpoint
procedure: [[procedures/Discover-Admin-Endpoint-in-JavaScript-Files]]

**Objective**: Identify the vulnerable admin endpoint by reviewing client-side JavaScript files.

**Instructions**: Navigate to a restaurant page on Zomato (e.g., https://www.zomato.com/[restaurant-slug]) and inspect the page source or use browser developer tools to search for references to admin endpoints. Look for JavaScript files containing strings like "/php/restaurant_menus_handler.php" and associated actions such as "menu_collected", "toggle-res-menu-type", "clear_menu_tool", or "change-menu-type".

**Expected Output**: Endpoint path and actions identified in JS source code.

**Success Indicators**:
- Endpoint "/php/restaurant_menus_handler.php" located
- Relevant actions (e.g., toggle-res-menu-type) noted

### Step 2: Test Endpoint Accessibility
procedure: [[procedures/Test-Endpoint-Accessibility-as-Normal-User]]

**Objective**: Confirm that the endpoint is accessible to non-admin authenticated users by sending an unauthorized POST request.

**Instructions**: With an authenticated session, open the browser developer console on a restaurant page. Execute the AJAX POST request using [[commands/ajax-post-toggle-res-menu-type]] to attempt toggling the menu type for a target restaurant ID.

```javascript
$.ajax({url:"/php/restaurant_menus_handler.php",type:"POST",data:{action:"toggle-res-menu-type",res_id:12345}});
```

Replace `res_id` with a valid restaurant ID (e.g., obtained from the page URL).

**Expected Output**: HTTP 200 response or successful execution without errors, indicating no access denial.

**Success Indicators**:
- Request executes without authentication errors
- Server processes the action

### Step 3: Verify Exploitation
procedure: [[procedures/Verify-Menu-Modification-Exploitation]]

**Objective**: Observe the impact of the privilege escalation by reloading the page and confirming menu changes.

**Instructions**: After executing the toggle request from Step 2, reload the restaurant page. If toggled to text mode, menu images should disappear. Re-execute the same [[commands/ajax-post-toggle-res-menu-type]] command to toggle back and verify reappearance of images. Test additional actions like "clear_menu_tool" if needed by modifying the `action` parameter.

```javascript
$.ajax({url:"/php/restaurant_menus_handler.php",type:"POST",data:{action:"toggle-res-menu-type",res_id:12345}});
```

**Expected Output**: Visible changes to menu display (e.g., images hidden/shown) upon page reload.

**Success Indicators**:
- Menu type toggles successfully as non-admin
- Changes persist and affect restaurant data

## Attack Chain Summary

### Key Achievements

1. Discovered hidden admin endpoint through client-side code review
2. Confirmed lack of access controls allowing non-admin exploitation
3. Demonstrated real impact via menu modifications, enabling potential business disruption

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation

---

*Last updated: 2023-10-01T00:00:00Z*
