---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - xss
  - stored-xss
  - wordpress
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2024-10-05T00:00:00Z'
procedures:
  - '[[procedures/Upload-Malicious-Theme-to-WordPress]]'
  - '[[procedures/Break-Theme-by-Deleting-Style-CSS]]'
  - '[[procedures/Rename-Theme-Folder-to-XSS-Payload]]'
  - '[[procedures/Trigger-XSS-on-WordPress-Themes-Page]]'
step_count: 4
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.339Z'
description: >-
  A multi-step attack exploiting a stored XSS vulnerability in WordPress's
  wp-admin themes page by uploading a broken theme with a malicious folder name,
  leading to JavaScript execution when viewed by administrators.
skill_level: intermediate
impact_level: low
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored XSS via Malicious Theme Folder Name in WordPress Admin

Multi-stage attack chain demonstrating a stored XSS vulnerability in WordPress's wp-admin themes page, where a broken theme's folder name is reflected without sanitization, allowing JavaScript execution in the administrator's browser. This exploit requires authenticated access with theme upload privileges or direct filesystem write access, making it primarily a self-XSS with limited practical impact beyond the attacker's own session.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Upload Theme] --> B[Break Theme]
    B --> C[Rename Folder]
    C --> D[Trigger XSS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses WordPress admin interface and optional filesystem access)

### Target Environment

- WordPress installation (any version prior to patch for this issue)
- Web platform with PHP backend
- Access to wp-content/themes/ directory

### Initial Access Requirements

- Authenticated WordPress administrator account with theme upload permissions
- Or direct server filesystem write access (e.g., via FTP, SSH, or hosting panel)
- Network access to the WordPress admin dashboard

## Detailed Attack Procedures

### Step 1: Upload Theme
procedure: [[procedures/Upload-Malicious-Theme-to-WordPress]]

**Objective**: Introduce a custom theme into the WordPress themes directory to set up for modification.

**Instructions**: Log in to the WordPress admin dashboard and navigate to Appearance > Themes > Add New. Upload a ZIP file containing a basic theme structure (including a style.css file initially). The theme will extract to wp-content/themes/ with its folder name.

**Expected Output**: Theme appears in the themes list as installed.

**Success Indicators**:
- Theme folder created in wp-content/themes/
- No upload errors in admin interface

### Step 2: Break Theme
procedure: [[procedures/Break-Theme-by-Deleting-Style-CSS]]

**Objective**: Render the theme malformed so WordPress displays it as broken on the themes page, triggering the vulnerable reflection.

**Instructions**: Access the server filesystem (via hosting file manager, FTP, or SSH) and navigate to the uploaded theme folder in wp-content/themes/. Delete the style.css file, which is required for valid theme detection.

**Expected Output**: Theme folder exists but lacks style.css, causing WordPress to flag it as broken.

**Success Indicators**:
- style.css file removed
- Theme no longer loads as valid in admin

### Step 3: Rename Folder
procedure: [[procedures/Rename-Theme-Folder-to-XSS-Payload]]

**Objective**: Inject the XSS payload into the theme's folder name, which will be unsanitized when displayed.

**Instructions**: Using filesystem access, rename the broken theme folder to a name containing the payload, such as '<img src=x onerror=alert(1)>'. This stores the malicious string for later reflection.

**Expected Output**: Folder renamed successfully without errors.

**Success Indicators**:
- Folder name updated to include HTML/JS payload
- No filesystem permission issues

### Step 4: View Themes Page
procedure: [[procedures/Trigger-XSS-on-WordPress-Themes-Page]]

**Objective**: Cause the payload to execute by viewing the vulnerable page.

**Instructions**: In the WordPress admin, go to Appearance > Themes. The broken theme's name will be displayed in an error message, executing the XSS payload in the browser.

**Expected Output**: Alert box or other JS execution in the admin browser.

**Success Indicators**:
- JavaScript alert (or equivalent payload) triggers
- Console logs show execution in wp-admin context

## Attack Chain Summary

### Key Achievements

1. Successful theme upload and modification with elevated privileges
2. Stored XSS payload injection via filesystem
3. JavaScript execution in authenticated admin session

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2024-10-05T00:00:00Z*
