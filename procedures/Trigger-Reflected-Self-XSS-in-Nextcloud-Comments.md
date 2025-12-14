---
tags:
  - xss
  - self-xss
  - reflected-xss
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
techniques:
  - '[[JavaScript]]'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
id: 85d2ae33-d582-4f21-8c4a-3885cfa66672
created_at: '2025-12-14T03:15:31.355Z'
updated_at: '2025-12-14T03:15:31.355Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Reflected-Self-XSS-in-Nextcloud-Comments

## Summary

This procedure exploits a reflected self-XSS vulnerability in the comment section of Nextcloud files, where user input is insufficiently sanitized. By posting a malicious JavaScript payload as a comment and then editing it, arbitrary JavaScript executes in the authenticated user's browser, typically for testing or self-inflicted attacks, with potential for social engineering escalation.

## Description

The vulnerability occurs in Nextcloud's Files app comment feature due to improper escaping of user input during rendering, especially in the edit view. Attackers with authenticated access can inject HTML/JS payloads that break out of the textarea context and execute when the comment is edited. This is a self-XSS, meaning it affects only the user who posts and edits the comment, limiting impact but useful for demonstrating flaws or in phishing scenarios where victims are tricked into editing. Discovered via payload testing in the comments box, as detailed in HackerOne report #164520. Expected outcomes include alert popups or prompts confirming JS execution.

## Requirements

1. Authenticated session in a Nextcloud instance with file commenting enabled.
2. Access to the Files app and permission to comment on at least one file.
3. Modern web browser to interact with the interface and observe JS execution.

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and HTML escaping for all user inputs in comments, using libraries like DOMPurify.
- Enforce Content Security Policy (CSP) to block inline scripts and unsafe eval.
- Monitor for unusual JS execution in browser consoles or error logs during comment interactions.
- Educate users on avoiding suspicious comments and disable edit for untrusted content.

## Objectives

1. Inject and persist a malicious payload in a file comment.
2. Trigger XSS execution via the edit functionality.
3. Demonstrate arbitrary JS execution in the victim's browser context.

## Instructions

### Step 1: Enter Malicious Payload in Comments Box

**Context**: This step injects the payload into the input field, exploiting the lack of sanitization on submission.

Navigate to a file in the Nextcloud Files app, scroll to the comments section, and type one of the following payloads into the comment input box:

- `</textarea><script>alert(1)</script>`
- `</textarea>"><img src=x onerror=prompt('XSS');>`
- `</textarea><IMG SRC=/ onerror="alert(String.fromCharCode(88,83,83))"></img>`
- `</textarea><svg/onload=alert('XSS')>`
- `</textarea>foo<script>alert(1)</script>`

> These payloads break out of the expected textarea context and inject executable HTML/JS. The input field accepts them without validation.

### Step 2: Post the Comment

**Context**: Submitting stores the payload, which is reflected back unsanitized in the comment list.

Click the 'Post comment' or equivalent submit button to save the entry.

> The comment appears in the list with the payload intact, visible but dormant until re-rendered.

### Step 3: Click Edit Comment

**Context**: Editing re-renders the comment content in an editable form, activating the payload due to escaping flaws in the edit view.

Find the posted comment in the list and click the 'Edit' icon or link.

> The edit modal opens, parsing the payload as HTML and triggering script execution.

### Step 4: Verify JavaScript Execution

**Context**: Confirm the vulnerability by observing the payload's effects in the browser.

Upon edit load, watch for execution indicators like an alert box saying '1' or 'XSS', or a prompt.

> If successful, JS runs in the current session's context. Check browser developer tools for script errors or console output to validate.

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
- [[self-xss]]
- [[reflected-xss]]
- [[nextcloud]]
