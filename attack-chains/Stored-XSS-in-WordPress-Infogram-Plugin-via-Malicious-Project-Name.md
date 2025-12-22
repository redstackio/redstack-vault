---
tags:
  - xss
  - stored-xss
  - wordpress
  - infogram
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2024-10-01T12:00:00Z'
procedures:
  - '[[procedures/Install-WordPress-and-Infogram-Plugin]]'
  - '[[procedures/Create-Malicious-Infogram-Project]]'
  - '[[procedures/Embed-Infogram-Graphic-in-WordPress]]'
  - '[[procedures/Trigger-XSS-in-Popup]]'
step_count: 4
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:14.273Z'
description: >-
  A multi-stage attack exploiting insufficient sanitization in the Infogram
  plugin for WordPress, allowing stored XSS through a malicious project name
  embedded via the plugin's interface.
skill_level: intermediate
impact_level: high
id: c3370746-cace-43ce-a464-da92b5c0506d
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Stored XSS in WordPress Infogram Plugin via Malicious Project Name

Multi-stage attack chain demonstrating a complete attack workflow exploiting a stored XSS vulnerability in the WordPress Infogram plugin version 1.5.1 on WordPress 4.5. The attack involves creating a malicious Infogram project name that injects JavaScript, embedding it via the plugin, and triggering execution in a popup, leading to arbitrary code execution in the victim's browser context.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Install Environment] --> B[Create Malicious Payload]
    B --> C[Embed Graphic]
    C --> D[Trigger XSS Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome or Firefox)
- Access to Infogram account

### Target Environment

- WordPress 4.5 instance
- Infogram plugin 1.5.1
- Web platform with administrative access to WordPress

### Initial Access Requirements

- Authenticated access to WordPress admin
- Infogram account credentials
- No prior network access beyond standard internet connectivity

## Detailed Attack Procedures

### Step 1: Install WordPress and Infogram Plugin
procedure: [[procedures/Install-WordPress-and-Infogram-Plugin]]

**Objective**: Set up the vulnerable environment to host the Infogram plugin.

**Instructions**: Download and install WordPress version 4.5 on a local or remote server. Once installed, log in to the WordPress admin dashboard and navigate to Plugins > Add New. Search for "Infogram" and install version 1.5.1. Activate the plugin to enable the 'Add from Infogram' functionality.

**Expected Output**: WordPress site running with Infogram plugin active, visible in the admin menu.

**Success Indicators**:
- WordPress dashboard accessible
- Infogram plugin listed as active

### Step 2: Create Malicious Infogram Project
procedure: [[procedures/Create-Malicious-Infogram-Project]]

**Objective**: Craft a project on Infogram with an XSS payload in the name field to store the malicious input.

**Instructions**: Log in to your Infogram account at infogram.com. Create a new project and set the project name to `"><img src=x onerror=prompt(0);>`. Generate a simple report or graphic within the project, then save and publish it to obtain the embed code or ID.

**Expected Output**: Infogram project created with the malicious name, ready for embedding.

**Success Indicators**:
- Project saved without errors
- Malicious name reflected in project details

### Step 3: Embed Infogram Graphic in WordPress
procedure: [[procedures/Embed-Infogram-Graphic-in-WordPress]]

**Objective**: Use the plugin to embed the malicious Infogram project into the WordPress site, storing the payload.

**Instructions**: Return to the WordPress editor for a post or page. Click the 'Add from Infogram' button provided by the plugin. In the popup interface, search for and select the malicious project created earlier. Confirm the embed to insert the graphic into the content.

**Expected Output**: Graphic embedded in the WordPress post, with the project name fetched from Infogram.

**Success Indicators**:
- Embed button functional
- Graphic appears in the editor without immediate errors

### Step 4: Trigger XSS in Popup
procedure: [[procedures/Trigger-XSS-in-Popup]]

**Objective**: Execute the stored XSS payload by interacting with the embedded content, leading to JavaScript execution.

**Instructions**: Save and view the WordPress post containing the embedded graphic. Interact with the embed by clicking the 'Add from Infogram' button again or refreshing the popup interface. The unsanitized project name will be displayed, triggering the `<img src=x onerror=prompt(0);>` payload to execute a prompt dialog in the browser.

**Expected Output**: Browser alert or prompt box appears, confirming JavaScript execution.

**Success Indicators**:
- Prompt(0) dialog opens
- No sanitization blocks the payload

## Attack Chain Summary

### Key Achievements

1. Successful setup of vulnerable WordPress environment with Infogram plugin.
2. Storage of XSS payload in Infogram project name.
3. Embedding and reflection of payload in WordPress popup.
4. Arbitrary JavaScript execution, enabling session hijacking or data theft.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Initial Access]]

---
*Last updated: 2024-10-01T12:00:00Z*
