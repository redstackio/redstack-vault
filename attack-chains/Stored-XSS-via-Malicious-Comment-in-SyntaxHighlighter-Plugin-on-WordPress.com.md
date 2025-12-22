---
id: ac-stored-xss-syntaxhighlighter-wordpress
tags:
  - xss
  - stored-xss
  - wordpress
  - syntaxhighlighter
  - javascript-injection
type: attack_chain
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Visit-Target-WordPress-Post]]'
  - '[[procedures/Submit-Malicious-XSS-Comment]]'
  - '[[procedures/Trigger-Stored-XSS-via-Link-Click]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.342Z'
description: >-
  A multi-step attack exploiting a stored XSS vulnerability in the
  SyntaxHighlighter plugin on WordPress.com sites, allowing arbitrary JavaScript
  execution via crafted comments that auto-link to javascript: protocols.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Stored XSS via Malicious Comment in SyntaxHighlighter Plugin on WordPress.com

Multi-stage attack chain demonstrating a stored XSS exploit in the SyntaxHighlighter plugin on WordPress.com, where a permissive regex allows javascript: URLs in code blocks to become clickable links, leading to arbitrary JavaScript execution in the victim's browser.

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
    A[Visit Target Post] --> B[Submit Malicious Comment]
    B --> C[Trigger XSS via Click]
    C --> D[Execute JavaScript]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Firefox]]
- [[tools/Chrome]]

### Target Environment

- Web platform
- WordPress.com site with SyntaxHighlighter plugin enabled
- Access to post comments section

### Initial Access Requirements

- Public access to the WordPress post (no authentication needed for commenting if enabled)
- Ability to post comments on the target site

## Detailed Attack Procedures

### Step 1: Visit Target WordPress Post
procedure: [[procedures/Visit-Target-WordPress-Post]]

**Objective**: Navigate to a vulnerable WordPress post to prepare for comment submission.

**Instructions**: Open a web browser and load the target post URL, such as https://mattstestsite128160580.wordpress.com/2019/10/03/test-post/.

**Expected Output**: The post loads, displaying the comments section.

**Success Indicators**:
- Post page renders successfully
- Comments form is visible and accessible

### Step 2: Submit Malicious Comment
procedure: [[procedures/Submit-Malicious-XSS-Comment]]

**Objective**: Inject a crafted payload into a comment that exploits the SyntaxHighlighter's auto-linking feature.

**Instructions**: In the comments section, enter the payload wrapped in [code] tags: [code]javascript://%0dalert%28document.cookie%29[/code]. Submit the comment.

**Expected Output**: Comment posts and gets processed by SyntaxHighlighter, rendering the code block with a clickable javascript: link.

**Success Indicators**:
- Comment appears on the page
- Code block highlights with auto-linked URL

### Step 3: Trigger Stored XSS via Link Click
procedure: [[procedures/Trigger-Stored-XSS-via-Link-Click]]

**Objective**: Execute the injected JavaScript by interacting with the rendered link, simulating victim behavior.

**Instructions**: Click on the 'javascript://' portion of the highlighted code in the comment to trigger the payload.

**Expected Output**: Alert box displays document.cookie, confirming JavaScript execution.

**Success Indicators**:
- JavaScript alert or console output executes
- Potential cookie theft or other actions succeed

## Attack Chain Summary

### Key Achievements

1. Successful injection of javascript: payload via comment
2. Auto-linking renders it as a clickable element due to loose regex
3. Arbitrary JS execution in site context, enabling session hijacking

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
