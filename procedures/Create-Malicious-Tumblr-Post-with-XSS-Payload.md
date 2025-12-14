---
tags:
  - xss
  - stored-xss
  - tumblr
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 347ad624-b223-4ef8-b7f7-e8d3d2203f07
created_at: '2025-12-14T03:46:26.715Z'
updated_at: '2025-12-14T03:46:26.715Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Tumblr-Post-with-XSS-Payload

## Summary

This procedure involves logging into a Tumblr account and creating a post with an embedded stored XSS payload using a malicious HTML form that executes JavaScript on interaction, targeting the reblog and edit features.

## Description

The attack exploits insufficient HTML sanitization in Tumblr's post storage. The payload is a form with a submit button using `formaction=javascript:alert(document.domain)`, which appears innocuous but triggers XSS when rendered in edit mode after reblogging. This allows arbitrary JS execution in the victim's authenticated session, potentially leading to account takeover. Prerequisites include a valid Tumblr account; no special tools are needed beyond a web browser.

## Requirements

1. Valid attacker Tumblr account with posting privileges
2. Web browser for accessing Tumblr dashboard
3. Basic knowledge of HTML and JavaScript for payload crafting

## Defense

Defensive measures and detection strategies:

- Implement strict HTML/JS sanitization in post rendering, especially in edit modes
- Use Content Security Policy (CSP) to block inline JavaScript execution
- Monitor for anomalous JS alerts or network requests from user sessions

## Objectives

1. Store malicious payload in a public post
2. Ensure payload survives reblogging
3. Set up for XSS trigger in victim context

## Instructions

### Step 1: Log In and Create Post

**Context**: Access the Tumblr dashboard to prepare the malicious content.

Log in to your Tumblr account at tumblr.com and navigate to create a new post.

### Step 2: Insert Payload

**Context**: Embed the XSS payload in the post body to store it server-side.

In the post editor, switch to HTML mode if available and insert:

```html
<form><input type=submit value="CLICK ME" formaction=javascript:alert(document.domain)></form>
```

Add any enticing text or images to encourage reblogging, then publish the post.

> The payload will be stored without execution at this stage.

### Step 3: Verify Storage

**Context**: Confirm the post contains the intact payload.

View the published post in source code to ensure the HTML form is present and unescaped.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[xss]]
- [[stored-xss]]
- [[tumblr]]
