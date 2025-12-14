---
tags:
  - xss
  - rce
  - wordpress
  - php
  - iframe
  - plugin-editor
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/define-php-payload]]'
  - '[[commands/access-iframe-document]]'
  - '[[commands/select-newcontent-textarea]]'
  - '[[commands/select-submit-button]]'
  - '[[commands/set-textarea-value]]'
  - '[[commands/click-submit-button]]'
  - '[[commands/redirect-to-plugin-file]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Login-as-WordPress-Editor]]'
  - '[[procedures/Craft-and-Post-Malicious-XSS-Payload]]'
  - '[[procedures/Trigger-XSS-on-Admin-Visit]]'
  - '[[procedures/Inject-PHP-Code-via-Iframe-Manipulation]]'
  - '[[procedures/Execute-Injected-PHP-for-RCE]]'
step_count: 5
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
description: >-
  An editor exploits unfiltered HTML posting to deliver XSS that manipulates the
  WordPress plugin editor via an invisible iframe, injecting PHP code for remote
  code execution when an admin views the content.
skill_level: intermediate
impact_level: high
id: e081b7ae-226c-4205-bd68-68c166047afb
created_at: '2025-12-14T17:23:20.713Z'
updated_at: '2025-12-14T17:23:20.713Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# WordPress Editor XSS to RCE via Same-Origin Iframe Plugin Manipulation

## Overview

This attack chain exploits a vulnerability in WordPress 4.8.1 where editors can post unfiltered HTML, including JavaScript, enabling stored XSS. The XSS payload creates an invisible iframe loading the plugin editor page and uses same-origin scripting to inject arbitrary PHP code into a plugin file. When an administrator views the malicious post, the payload executes, allowing the editor to escalate privileges to full site compromise via remote code execution (RCE). The attack relies on the absence of frame protections and re-authentication for admin actions, making it a severe privilege escalation from a trusted editor role.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Login as Editor] --> B[Post XSS Payload]
    B --> C[Admin Views Content]
    C --> D[Inject PHP via Iframe]
    D --> E[Execute RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#f39c12
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser with JavaScript enabled (e.g., Chrome Developer Tools for testing)

### Target Environment

- WordPress 4.8.1 or similar vulnerable version
- Required services/ports: HTTP on port 8090
- Network access requirements: Local or same-network access to WordPress instance

### Initial Access Requirements

- Valid editor role credentials
- Network position: Internal or direct access to the WordPress site
- Prior access needed: None, assuming editor login

## Detailed Attack Procedures

### Step 1: Login as Editor
procedure: [[procedures/Login-as-WordPress-Editor]]

**Objective**: Authenticate as an editor to gain permission to post unfiltered HTML content.

**Instructions**: Use the WordPress login form to authenticate with editor credentials. No specific commands are needed beyond standard login.

**Expected Output**: Successful dashboard access with editor privileges.

**Success Indicators**:
- Access to Posts > Add New with unfiltered HTML option enabled
- Editor role confirmed in user profile

### Step 2: Craft and Post Malicious XSS Payload
procedure: [[procedures/Craft-and-Post-Malicious-XSS-Payload]]

**Objective**: Create and publish a post containing the XSS payload that loads an invisible iframe to the plugin editor.

**Instructions**: In the WordPress editor, switch to Text/HTML mode and insert the payload: an iframe sourcing `/wp-admin/plugin-editor.php?file=hello.php` with JavaScript to manipulate it after loading. Publish the post and share the link with the admin.

**Expected Output**: Post published successfully, visible to administrators.

**Success Indicators**:
- Post contains unfiltered HTML without sanitization errors
- Link to post is accessible

### Step 3: Trigger XSS on Admin Visit
procedure: [[procedures/Trigger-XSS-on-Admin-Visit]]

**Objective**: Have the administrator load the malicious post, executing the XSS payload.

**Instructions**: Direct the admin to view the post. Upon loading, the JavaScript executes, creating and loading the invisible iframe after a short delay.

**Expected Output**: Iframe loads the plugin editor page silently in the background.

**Success Indicators**:
- Admin browser executes JavaScript without alerts
- Network request to `/wp-admin/plugin-editor.php?file=hello.php` observed in dev tools

### Step 4: Inject PHP Code via Iframe Manipulation
procedure: [[procedures/Inject-PHP-Code-via-Iframe-Manipulation]]

**Objective**: Use JavaScript to access the iframe's DOM, inject PHP code into the editor textarea, and submit the form.

**Instructions**: After a 2-second delay, access the iframe document using [[commands/access-iframe-document]], select the textarea with [[commands/select-newcontent-textarea]], set its value with [[commands/set-textarea-value]] to the PHP payload defined in [[commands/define-php-payload]], select the submit button with [[commands/select-submit-button]], and click it with [[commands/click-submit-button]].

```javascript
var p = "<?php phpinfo(); ?>";
var d = document.querySelector("iframe").contentWindow.document;
var c = d.querySelector("#newcontent");
var s = d.querySelector("#submit");
c.value = p;
s.click();
```

**Expected Output**: Plugin file `hello.php` updated with the injected PHP code.

**Success Indicators**:
- Form submission succeeds without errors
- File modification confirmed by checking plugin directory (if accessible)

### Step 5: Execute Injected PHP for RCE
procedure: [[procedures/Execute-Injected-PHP-for-RCE]]

**Objective**: Redirect to the modified plugin file to trigger execution of the injected code.

**Instructions**: After another 2-second delay, redirect the browser using [[commands/redirect-to-plugin-file]] to `/wp-content/plugins/hello.php`.

```javascript
window.location.href = "http://127.0.0.1:8090/wp-content/plugins/hello.php";
```

**Expected Output**: PHP `phpinfo()` output displayed, confirming RCE.

**Success Indicators**:
- Server-side PHP execution with info dump
- Full admin compromise, enabling further actions like backdoor installation

## Attack Chain Summary

### Key Achievements

1. Privilege escalation from editor to admin via stored XSS
2. Arbitrary PHP injection into plugins without direct access
3. Remote code execution, compromising the entire WordPress site

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01*
