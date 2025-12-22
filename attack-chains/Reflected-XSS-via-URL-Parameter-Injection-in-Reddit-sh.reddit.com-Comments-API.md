---
id: ac-reddit-xss-reflected-001
tags:
  - xss
  - reflected-xss
  - javascript-injection
  - reddit
  - client-side-execution
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Inject-Malicious-URL-for-Reflected-XSS]]'
  - '[[procedures/Trigger-XSS-via-User-Interaction]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:56:19.897Z'
description: >-
  A multi-step attack exploiting a reflected XSS vulnerability in Reddit's
  sh.reddit.com endpoint by injecting malicious JavaScript via unsanitized URL
  parameters, leading to arbitrary code execution on user interaction.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Reflected XSS via URL Parameter Injection in Reddit sh.reddit.com Comments API

Multi-stage attack chain demonstrating exploitation of a reflected XSS vulnerability in Reddit's mobile web API endpoint.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Craft Malicious URL] --> B[Execution: Trigger XSS Payload]
    B --> C[Objective: Arbitrary JS Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome, Firefox)

### Target Environment

- Target Platform: Web
- Required Services: sh.reddit.com API
- Network Access: Public internet access to sh.reddit.com

### Initial Access Requirements

- No credentials required
- Victim must visit the malicious URL (e.g., via phishing)
- No prior access needed

## Detailed Attack Procedures

### Step 1: Craft and Navigate to Malicious URL
procedure: [[procedures/Inject-Malicious-URL-for-Reflected-XSS]]

**Objective**: Inject a malicious JavaScript payload into the URL parameter to embed an HTML event attribute in the page response.

**Instructions**: Construct the target URL by appending the XSS payload to the thread ID parameter. For example, use the following URL structure:

Navigate to: `https://sh.reddit.com/svc/shreddit/api/comments/askreddit/t3_u9po1l%20onmouseover=alert(document.domain)%20y=/t1_i5sxroa`

This injects the `onmouseover=alert(document.domain)` event handler into the page content via the unsanitized URL parameter.

**Expected Output**: The page loads with the injected attribute present in the DOM, visible upon inspection (e.g., via browser dev tools).

**Success Indicators**:
- Page loads without errors
- Payload reflected in HTML source (e.g., search for 'onmouseover' in dev tools)

### Step 2: Trigger Payload Execution
procedure: [[procedures/Trigger-XSS-via-User-Interaction]]

**Objective**: Execute the injected JavaScript by simulating user interaction to trigger the event handler.

**Instructions**: Scroll down to the end of the comments page where the 'see more' option appears. Hover the mouse over the 'see more' link to activate the onmouseover event.

No specific command needed; this is a client-side interaction.

**Expected Output**: A JavaScript alert dialog pops up displaying the document domain (e.g., 'sh.reddit.com').

**Success Indicators**:
- Alert box appears on hover
- JavaScript executes in the victim's browser context

## Attack Chain Summary

### Key Achievements

1. Successful injection of HTML event attributes via URL parameters
2. Arbitrary JavaScript execution upon user hover interaction
3. Potential for cookie theft or session hijacking in a real attack

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
