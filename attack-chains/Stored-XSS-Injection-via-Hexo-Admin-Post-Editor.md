---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: Stored XSS Injection via Hexo-Admin Post Editor
type: attack_chain
description: >-
  Multi-stage attack exploiting a stored XSS vulnerability in the hexo-admin
  plugin version 3.9.0, allowing injection of malicious scripts into blog posts
  that persist and execute on page views, enabling session hijacking or data
  theft.
verified: false
submitted: true
step_count: 4
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:37.053Z'
procedures:
  - '[[procedures/Setup-Hexo-Environment-with-Admin-Plugin]]'
  - '[[procedures/Start-Hexo-Server-and-Access-Admin-Panel]]'
  - '[[procedures/Create-Post-and-Inject-Stored-XSS-Payload]]'
  - '[[procedures/Save-Post-Rebuild-Site-and-Verify-Persistent-XSS]]'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
tags:
  - stored-xss
  - hexo-admin
  - node.js
  - web-vulnerability
platforms:
  - Web
  - Node.js
tools:
  - '[[tools/HexoJS]]'
  - '[[tools/Hexo-Admin]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---

# Stored XSS Injection via Hexo-Admin Post Editor

Multi-stage attack chain demonstrating exploitation of stored XSS in the hexo-admin plugin for Node.js, where unsanitized post content allows persistent script injection that executes on blog views, impacting administrators and visitors.

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
    A[Setup Environment] --> B[Access Admin Panel]
    B --> C[Inject XSS Payload]
    C --> D[Save and Verify Persistence]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/HexoJS]]
- [[tools/Hexo-Admin]]

### Target Environment

- Node.js runtime (version 14+ recommended)
- Local development setup for Hexo static site generator
- Port 4000 open for local server

### Initial Access Requirements

- Administrative access to the Hexo blog instance
- No prior network access needed; local setup suffices for demonstration
- Basic knowledge of Node.js package management

## Detailed Attack Procedures

### Step 1: Environment Setup
procedure: [[procedures/Setup-Hexo-Environment-with-Admin-Plugin]]

**Objective**: Install and configure the Hexo static site generator with the vulnerable hexo-admin plugin to prepare for XSS injection testing.

**Instructions**: Follow the setup procedure to install prerequisites via npm, including the hexo-admin plugin version 3.9.0.

**Expected Output**: Hexo project initialized with admin plugin ready for server startup.

**Success Indicators**:
- Hexo CLI available
- hexo-admin plugin listed in package.json

### Step 2: Server Startup and Admin Access
procedure: [[procedures/Start-Hexo-Server-and-Access-Admin-Panel]]

**Objective**: Launch the local Hexo server and navigate to the admin interface to gain access to the post editor.

**Instructions**: Use [[commands/hexo-server-deploy]] to start the development server, then open the browser to localhost:4000/admin.

```bash
hexo server -d
```

**Expected Output**: Local server running at http://localhost:4000, admin panel accessible.

**Success Indicators**:
- Server logs show successful startup
- Admin login page loads without errors

### Step 3: Post Creation and XSS Injection
procedure: [[procedures/Create-Post-and-Inject-Stored-XSS-Payload]]

**Objective**: Create a new blog post in the admin panel and inject a malicious XSS payload into the content field to trigger immediate execution.

**Instructions**: In the admin panel, navigate to posts, create a new post titled 'Test XSS here', and insert the payload `"><img src=x onerror=alert('XSS')>"` in the content area.

**Expected Output**: Alert popup triggers in the editor interface upon payload insertion or preview.

**Success Indicators**:
- JavaScript alert executes in the browser
- Payload visible in the post editor without sanitization

### Step 4: Persistence Verification
procedure: [[procedures/Save-Post-Rebuild-Site-and-Verify-Persistent-XSS]]

**Objective**: Save the injected post, rebuild the static site, and confirm the XSS payload persists and executes on the published post view.

**Instructions**: Save the post, then run [[commands/hexo-clean]], [[commands/hexo-generate]], and restart with [[commands/hexo-server-deploy]]. Access the post URL to observe execution.

```bash
hexo clean
hexo generate
hexo server -d
```

**Expected Output**: Rebuilt site serves the post with executing XSS alert on load.

**Success Indicators**:
- No sanitization errors during build
- Alert triggers when viewing the published post

## Attack Chain Summary

### Key Achievements

1. Successful setup of vulnerable Hexo environment with admin plugin.
2. Injection and immediate execution of XSS in the post editor.
3. Persistence of malicious script after saving and site rebuild.
4. Demonstration of impact on post viewers via client-side script execution.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
