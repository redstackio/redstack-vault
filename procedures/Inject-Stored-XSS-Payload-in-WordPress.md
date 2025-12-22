---
tags:
  - xss
  - stored-xss
  - wordpress
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/inject-xss-payload]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: 66f4b039-a01e-449c-b0b5-94efc1b5ecef
created_at: '2025-12-14T00:11:25.141Z'
updated_at: '2025-12-14T00:11:25.141Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject Stored XSS Payload in WordPress

## Summary

This procedure outlines the steps to exploit a stored XSS vulnerability in WordPress.com by injecting a malicious HTML payload into comments or post bodies/titles, leading to arbitrary JavaScript execution when viewed by victims.

## Description

The vulnerability stems from insufficient sanitization of user-inputted HTML in WordPress comments and posts, allowing specially crafted iframes and anchor tags to execute JavaScript. This can result in stealing cookies, performing requests on behalf of users, or reading accessible data under the wordpress.com domain. The procedure targets feeds at https://wordpress.com/read/feeds/{blog_id}/posts/{post_id} or subdomain sites like https://yoursubdomain.wordpress.com.

## Requirements

1. Valid WordPress.com account credentials
2. Web browser with internet access
3. Knowledge of target post or ability to create a new one

## Defense

Defensive measures and detection strategies:

- Implement strict HTML sanitization and Content Security Policy (CSP) on user inputs
- Monitor for suspicious HTML patterns in logs, such as malformed iframes or javascript: URIs

## Objectives

1. Inject and store malicious payload
2. Trigger XSS to execute JavaScript
3. Demonstrate potential for data exfiltration or unauthorized actions

## Instructions

### Step 1: Authenticate to WordPress.com

**Context**: Log in to gain access for injecting payloads.

Navigate to wordpress.com and log in.

> Establishes an authenticated session.

### Step 2: Select Injection Point

**Context**: Choose or create a post for payload insertion.

Navigate to a feed post or create a new one on your subdomain.

> Prepares the location for stored XSS.

### Step 3: Inject Payload

**Context**: Insert the malicious HTML.

Execute [[commands/inject-xss-payload]] by adding the following to the comment or post body/title:

```html
<iframe <><a href=javascript&colon;alert(document.cookie)>Click Here</a>=&gt;&lt;/iframe&gt;
```

> Bypasses filters to store the payload.

### Step 4: Trigger the XSS

**Context**: View and interact with the injected content.

Publish or preview, then click 'Click Here' to execute the JavaScript.

> Confirms execution with an alert showing cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/inject-xss-payload]]

## Tools Used



## Tags

- [[xss]]
- [[stored-xss]]
- [[wordpress]]
