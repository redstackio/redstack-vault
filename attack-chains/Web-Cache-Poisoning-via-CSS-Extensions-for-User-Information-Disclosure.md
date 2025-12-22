---
tags:
  - web-cache-poisoning
  - information-disclosure
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Web-Browser]]'
  - '[[tools/Incognito-Mode]]'
  - '[[tools/JavaScript]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/view-source-cached-url]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Visit-Crafted-URL-While-Logged-In]]'
  - '[[procedures/Server-Caches-Dynamic-Content]]'
  - '[[procedures/Access-Cached-Content-as-Unauthenticated-User]]'
  - '[[procedures/Automate-Attack-with-JavaScript-PoC]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Multi-stage web cache poisoning attack exploiting improper caching of dynamic
  pages with static extensions to disclose sensitive user information
skill_level: intermediate
impact_level: high
id: 9d087317-30c7-4307-b841-f1f4a61de2c8
created_at: '2025-12-13T09:00:34.404Z'
updated_at: '2025-12-13T09:00:34.404Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Web Cache Poisoning via CSS Extensions for User Information Disclosure

Multi-stage attack chain demonstrating a complete workflow for exploiting a web cache poisoning vulnerability on a web application, leading to the disclosure of logged-in user information such as email, name, and member ID to unauthorized parties.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Visit Crafted URL Logged In] --> B[Server Caches Content]
    B --> C[Access as Unauthenticated]
    C --> D[Automate with PoC]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Web-Browser]]
- [[tools/Incognito-Mode]]
- [[tools/JavaScript]]

### Target Environment

- Web platform
- Web server with caching enabled
- Network access to the target URL

### Initial Access Requirements

- A logged-in user session on the target site
- Ability to visit crafted URLs
- No prior credentials needed for unauthenticated access

## Detailed Attack Procedures

### Step 1: Visit Crafted URL While Logged In
procedure: [[procedures/Visit-Crafted-URL-While-Logged-In]]

**Objective**: Trigger the server to cache dynamic page content including user session data by accessing a URL with a static file extension.

**Instructions**: Using a [[tools/Web-Browser]], while logged in, visit a crafted URL such as https://www.lyst.com/shop/trends/mens-dress-shoes/blahblah.css to cause the server to cache the response with sensitive data.

**Expected Output**: The page loads normally, but the server caches the content.

**Success Indicators**:
- Page loads without errors
- No immediate indication of caching, but proceeds to next step

### Step 2: Server Caches Dynamic Content
procedure: [[procedures/Server-Caches-Dynamic-Content]]

**Objective**: Allow the server to improperly store the dynamic content as a static resource due to the .css extension.

**Instructions**: No direct action needed; this occurs server-side after Step 1. The cache treats the response as static but includes user-specific data like email and member ID.

**Expected Output**: Cached content stored on the server.

**Success Indicators**:
- Subsequent access in Step 3 reveals cached data

### Step 3: Access Cached Content as Unauthenticated User
procedure: [[procedures/Access-Cached-Content-as-Unauthenticated-User]]

**Objective**: Retrieve the cached sensitive information without authentication.

**Instructions**: Using a [[tools/Web-Browser]] in [[tools/Incognito-Mode]], access the same crafted URL and execute [[commands/view-source-cached-url]] to inspect the page source:

```bash
view-source:https://www.lyst.com/LAVFKS53DG.css
```

**Expected Output**: Page source containing username, slug, id, email, etc.

**Success Indicators**:
- Sensitive user data visible in source
- Disclosure confirmed without login

### Step 4: Automate Attack with JavaScript PoC
procedure: [[procedures/Automate-Attack-with-JavaScript-PoC]]

**Objective**: Automate the poisoning process using a script to generate random URLs and capture data from victims.

**Instructions**: Use [[tools/JavaScript]] to run a script that generates a random 10-character ID, opens a popup to the crafted URL while the victim is logged in, closes it after caching, and provides the URL for attacker access.

**Expected Output**: Automated caching and URL for data retrieval.

**Success Indicators**:
- Script executes without errors
- Cached data accessible via generated URL

## Attack Chain Summary

### Key Achievements

1. Successful caching of dynamic user data
2. Unauthorized disclosure of email, name, and member ID
3. Automated exploitation via JavaScript PoC

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

*Last updated: [TIMESTAMP]*
