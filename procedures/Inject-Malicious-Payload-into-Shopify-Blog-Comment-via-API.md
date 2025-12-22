---
tags:
  - xss
  - stored-xss
  - shopify
  - api
type: procedure
tools:
  - '[[tools/Web-Browser]]'
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/shopify-update-comment-api]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:32:29.349Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: a41c1740-94fa-4177-8782-5c04fdd7316b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Shopify-Blog-Comment-via-API

## Summary

This procedure exploits a stored XSS vulnerability in Shopify's blog comments by posting a comment via the web interface, extracting its ID, setting up a custom app with comment permissions, and updating the comment through the REST API using the undocumented 'body_html' field to inject unsanitized HTML and JavaScript, which executes when the blog post is viewed in the storefront or comments are checked in the admin panel.

## Description

The attack targets Shopify stores with enabled blog comments. Normal comment submission via the web sanitizes input to prevent XSS, but the API's PUT endpoint for comments accepts an undocumented 'body_html' parameter without sanitization. By combining web posting for ID acquisition and API update for payload injection, attackers can store malicious JS that executes client-side, potentially leading to session theft, phishing, or data exfiltration for any user viewing the post, including admins. This was reported in HackerOne #192210 and affects unauthenticated users for execution but requires app setup for injection.

## Requirements

1. Access to a Shopify storefront with blog comments enabled
2. Shopify admin or partner account to create apps with read/write comment scopes
3. API access token from the installed app
4. Tools for web interaction and API requests (e.g., browser and curl)

## Defense

Defensive measures and detection strategies:

- Sanitize all API inputs, especially undocumented fields like 'body_html', using libraries like DOMPurify
- Remove or deprecate undocumented API parameters and enforce strict schema validation
- Monitor API logs for unusual PUT requests to /admin/comments with HTML content
- Implement Content Security Policy (CSP) to restrict inline JS execution in storefront and admin
- Rate-limit comment updates and require CAPTCHA for web comments

## Objectives

1. Inject and store unsanitized JavaScript in a blog comment
2. Achieve arbitrary code execution on victim browsers viewing the affected post
3. Demonstrate impact on both customers and admins for account takeover or data theft

## Instructions

### Step 1: Post Benign Comment and Extract ID

**Context**: Submit a safe comment via the web to get a valid comment ID, as the web interface handles sanitization but provides the necessary identifier.

Use [[tools/Web-Browser]] to navigate to a blog post and submit a comment like "Test comment". Then, use [[tools/Browser-Developer-Tools]] to inspect the comment element.

**Expected Output**: Comment ID visible in HTML, e.g., id="comment-2929551246".

### Step 2: Create and Install Shopify App

**Context**: Set up authentication for API access by creating an app with comment permissions.

In Shopify admin, go to Apps > Develop apps > Create app, add scopes read_comments and write_comments, install, and copy the admin API access token.

**Expected Output**: App installed; token ready for use in requests.

### Step 3: Update Comment with Malicious Payload

**Context**: Use the API to overwrite the comment, injecting JS via 'body_html' which bypasses sanitization.

Execute [[commands/shopify-update-comment-api]] with the extracted ID and token. Repeat the request if the update doesn't persist immediately.

> This step requires replacing placeholders with real values; the payload <img src=x onerror=alert(0);> triggers a simple alert but can be escalated to steal cookies or redirect.

### Step 4: Verify Execution

**Context**: Load the page to confirm the XSS fires in the target contexts.

Visit the blog post URL or admin comments page; observe JS execution.

**Expected Output**: Alert or console logs indicating successful JS run.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/shopify-update-comment-api]]

## Tools Used

- [[tools/Web-Browser]]
- [[tools/Browser-Developer-Tools]]

## Tags

- xss
- stored-xss
- shopify
- api
- javascript
