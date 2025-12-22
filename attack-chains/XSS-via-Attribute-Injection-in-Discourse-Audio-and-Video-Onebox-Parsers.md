---
id: ac-uuid-001
tags:
  - xss
  - discourse
  - onebox
  - audio-parser
  - video-parser
  - attribute-injection
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Ruby
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Review-Discourse-Onebox-Source-Code-for-Sanitization-Issues]]'
  - '[[procedures/Craft-Malicious-Audio-URL-for-XSS]]'
  - '[[procedures/Craft-Malicious-Video-URL-for-XSS]]'
  - '[[procedures/Report-Vulnerability-with-Reproduction-Details]]'
step_count: 4
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:37.914Z'
description: >-
  A multi-stage attack chain exploiting insufficient URL sanitization in
  Discourse's onebox engine audio and video parsers, allowing JavaScript
  execution through crafted malicious URLs.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# XSS via Attribute Injection in Discourse Audio and Video Onebox Parsers

Multi-stage attack chain demonstrating the discovery and exploitation of a Cross-Site Scripting (XSS) vulnerability in Discourse's onebox engine, specifically in the audio and video parsers. The chain involves code review to identify sanitization flaws, crafting malicious payloads for attribute injection, and reporting the issue, but focuses on the exploitation path leading to arbitrary JavaScript execution in the victim's browser.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Code Review] --> B[Craft Audio Payload]
    B --> C[Craft Video Payload]
    C --> D[Inject and Execute JS]
    D --> E[Report and Verify]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools for testing
- Access to a Discourse forum instance

### Target Environment

- Discourse forum using onebox engine
- Ruby-based web application
- No specific ports required; web access only

### Initial Access Requirements

- Ability to post links in the forum (user account)
- Network access to the target Discourse instance
- No prior credentials needed beyond forum access

## Detailed Attack Procedures

### Step 1: Code Review
procedure: [[procedures/Review-Discourse-Onebox-Source-Code-for-Sanitization-Issues]]

**Objective**: Identify improper URL handling in audio and video parsers to find injection points.

**Instructions**: Examine the source code on GitHub for the audio_onebox.rb and video_onebox.rb files. Look for URL parsing logic that does not escape single quotes, allowing attribute injection.

**Expected Output**: Confirmation of unsanitized URL processing leading to potential XSS.

**Success Indicators**:
- Identified failure to sanitize single quotes in URLs
- Noted similarity to known Image parser XSS

### Step 2: Craft Audio Payload
procedure: [[procedures/Craft-Malicious-Audio-URL-for-XSS]]

**Objective**: Create a malicious audio URL that injects an onerror attribute to execute JavaScript.

**Instructions**: Construct a URL like `http://host/path'onerror=alert(1);//k.mp3` and post it in a Discourse forum thread. The parser will render it as an audio element with injected `onerror=alert(1)`.

**Expected Output**: When the victim loads the page, an alert box pops up executing the JavaScript.

**Success Indicators**:
- Alert executed in browser console
- Arbitrary JS runs in forum context

### Step 3: Craft Video Payload
procedure: [[procedures/Craft-Malicious-Video-URL-for-XSS]]

**Objective**: Create a similar malicious video URL for XSS injection.

**Instructions**: Construct a URL like `http://host/path'onerror=alert(1);//k.mp4` and post it in the forum. The video parser will inject the onerror handler similarly.

**Expected Output**: JavaScript execution via alert on video element load failure.

**Success Indicators**:
- JS alert triggered on video parsing
- Confirmed attribute injection success

### Step 4: Report and Verify
procedure: [[procedures/Report-Vulnerability-with-Reproduction-Details]]

**Objective**: Document and submit the vulnerability for remediation while verifying impact.

**Instructions**: Compile reproduction steps, including payloads and code references, and submit via HackerOne. Test in a controlled environment to confirm session hijacking or data theft potential.

**Expected Output**: Vulnerability acknowledged and fixed in upstream Discourse.

**Success Indicators**:
- Report accepted on HackerOne
- Patch applied to parsers

## Attack Chain Summary

### Key Achievements

1. Discovered XSS in audio and video parsers via code review
2. Demonstrated attribute injection with crafted URLs leading to JS execution
3. Highlighted similarity to prior Image parser flaw for broader context
4. Enabled remediation through detailed reporting

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
