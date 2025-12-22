---
tags:
  - xss
  - stored-xss
  - wordpress
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/inject-xss-payload]]'
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Inject-Stored-XSS-Payload-in-WordPress]]'
step_count: 4
techniques:
  - '[[JavaScript]]'
description: >-
  Exploitation of a stored XSS vulnerability in WordPress.com to inject
  malicious HTML payloads into comments or posts, enabling arbitrary JavaScript
  execution.
skill_level: beginner
impact_level: high
id: 669a7d09-2121-4074-a9f5-f5641c4e585d
created_at: '2025-12-14T00:11:25.143Z'
updated_at: '2025-12-14T00:11:25.143Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored XSS in WordPress via Comments or Posts

Multi-stage attack chain demonstrating the exploitation of a stored XSS vulnerability in WordPress.com, allowing attackers to inject malicious HTML into comments or posts, leading to arbitrary JavaScript execution in the victim's browser under the wordpress.com domain context.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access] --> B[Payload Injection]
    B --> C[Publish or Preview]
    C --> D[Trigger XSS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (web browser required)

### Target Environment

- Platform: Web (WordPress.com)
- Required services/ports: HTTPS access to wordpress.com
- Network access requirements: Internet access

### Initial Access Requirements

- Credential requirements: Valid WordPress.com account
- Network position: Any internet-connected device
- Prior access needed: Logged-in user access

## Detailed Attack Procedures

### Step 1: Log in to WordPress.com
procedure: [[procedures/Inject-Stored-XSS-Payload-in-WordPress]]

**Objective**: Gain authenticated access to the WordPress.com platform to enable posting comments or creating posts.

**Instructions**: Navigate to wordpress.com and log in with valid credentials.

**Expected Output**: Successful login and access to dashboard or feeds.

**Success Indicators**:
- Authenticated session established
- Ability to view or create posts

### Step 2: Choose a Post or Create New
procedure: [[procedures/Inject-Stored-XSS-Payload-in-WordPress]]

**Objective**: Select or create a target location for payload injection.

**Instructions**: Navigate to https://wordpress.com/read/feeds/{blog_id}/posts/{post_id} for an existing post or create a new blog post on https://yoursubdomain.wordpress.com.

**Expected Output**: Access to a post or new post editor.

**Success Indicators**:
- Post page loaded
- Editing interface available

### Step 3: Inject the XSS Payload
procedure: [[procedures/Inject-Stored-XSS-Payload-in-WordPress]]

**Objective**: Insert the malicious HTML payload into a comment or post body/title.

**Instructions**: Use [[commands/inject-xss-payload]] to add the payload <iframe <><a href=javascript&colon;alert(document.cookie)>Click Here</a>=&gt;&lt;/iframe&gt; into the comment field or post body/title.

```html
<iframe <><a href=javascript&colon;alert(document.cookie)>Click Here</a>=&gt;&lt;/iframe&gt;
```

**Expected Output**: Payload successfully submitted without sanitization errors.

**Success Indicators**:
- Payload appears in the comment or post
- No validation errors from WordPress

### Step 4: Preview or Publish and Trigger XSS
procedure: [[procedures/Inject-Stored-XSS-Payload-in-WordPress]]

**Objective**: View the injected content and execute the JavaScript.

**Instructions**: Preview or publish the post/comment, then view the page and click on 'Click Here' to trigger the alert(document.cookie) under the domain's context.

**Expected Output**: JavaScript alert displaying document.cookie.

**Success Indicators**:
- Alert box appears with cookie data
- Execution in wordpress.com context confirmed

## Attack Chain Summary

### Key Achievements

1. Successful injection of stored XSS payload
2. Bypassing of HTML filters in WordPress
3. Arbitrary JavaScript execution leading to potential data theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

*Last updated: 2023-10-01*
