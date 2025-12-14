---
id: ac-uuid-001
name: Stored XSS in Airship Comments via JavaScript Protocol URL
tags:
  - xss
  - stored-xss
  - javascript-url
  - cms
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Submit-Malicious-Comment-with-JavaScript-URL]]'
  - '[[procedures/Trigger-XSS-via-Rendered-Link-Interaction]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:14.560Z'
description: >-
  A stored cross-site scripting attack exploiting the lack of protocol
  validation in the author's website field of Airship comments, allowing
  javascript: URLs to be stored and potentially executed on click.
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored XSS in Airship Comments via JavaScript Protocol URL

Multi-stage attack chain demonstrating a complete stored XSS workflow in the Airship PHP-based CMS.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Submit Malicious Comment] --> B[Render and Interact with Link]
    B --> C[JavaScript Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser for manual testing

### Target Environment

- Airship CMS (PHP-based)
- Web platform with comment submission feature enabled
- No specific ports or services beyond standard HTTP/HTTPS

### Initial Access Requirements

- Public access to the blog post or page with comments
- No authentication required for anonymous comments

## Detailed Attack Procedures

### Step 1: Submit Malicious Comment
procedure: [[procedures/Submit-Malicious-Comment-with-JavaScript-URL]]

**Objective**: Inject a malicious javascript: URL into the author's website field to store it in the database without filtering.

**Instructions**: Navigate to a blog post page in the Airship application that allows comments. Fill out the comment form, entering a payload like `javascript:alert(1)` in the author's website field. Submit the comment.

**Expected Output**: The comment is successfully posted and stored in the backend.

**Success Indicators**:
- Comment appears in the list after submission
- No validation errors on javascript: protocol

### Step 2: Trigger XSS via Rendered Link
procedure: [[procedures/Trigger-XSS-via-Rendered-Link-Interaction]]

**Objective**: Observe the stored URL rendered as an href in a link element and interact to execute the JavaScript.

**Instructions**: Refresh or load the blog post page where the comment was submitted. Locate the rendered comment, which includes a link with the malicious href (e.g., `<a href="javascript:alert(1)">`). Click the link to trigger execution.

**Expected Output**: If CSP allows or is absent, an alert box or arbitrary JavaScript executes in the victim's browser context.

**Success Indicators**:
- Malicious URL visible in the href attribute of the link
- JavaScript payload executes on click (alert or other code)

## Attack Chain Summary

### Key Achievements

1. Successful storage of unfiltered javascript: URL in comments
2. Rendering of the payload in link elements without sanitization
3. Potential arbitrary JavaScript execution on user interaction, bypassing basic protections

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
