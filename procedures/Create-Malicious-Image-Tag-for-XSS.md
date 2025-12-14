---
tags:
  - xss
  - payload-creation
  - web
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:31.835Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 78475d30-c886-4e4a-ba03-1f35dd2e5666
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Image-Tag-for-XSS

## Summary

This procedure involves embedding a malicious <img> tag with an onerror JavaScript payload in the src attribute on a controlled website, setting up the payload for reflection in vulnerable tools like the Shopify Ecommerce Store Grader.

## Description

In the context of exploiting reflected XSS, this step prepares the attack by hosting user-controlled content on a site you control. The payload uses an invalid src to trigger an error, executing JavaScript when the attribute is echoed without sanitization. This targets web applications that fetch and display page elements, such as image attributes, in their output. Prerequisites include access to a web server or static hosting for the controlled domain.

## Requirements

1. Controlled website (e.g., personal domain with editable HTML)
2. Basic HTML editing knowledge
3. Public accessibility of the site over HTTPS/HTTP

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to restrict inline scripts
- Sanitize all reflected user input, especially HTML attributes like src
- Use HTML parsers to validate and escape image tags before display

## Objectives

1. Inject XSS payload into a fetchable webpage
2. Ensure payload survives fetching and echoing
3. Prepare for JavaScript execution on error

## Instructions

### Step 1: Edit Website HTML

**Context**: Modify the homepage or a target page to include the malicious image tag, ensuring it's parsed as part of the DOM.

No specific command; use a text editor or CMS to add:

```html
<img src="111<img src=1 onerror=alert(123)>">
```

> This creates a nested img tag where the inner src=1 fails to load, triggering onerror with alert(123). Save and upload the changes to your server.

### Step 2: Verify Payload Hosting

**Context**: Confirm the tag is live and accessible without immediate execution on your site.

Navigate to your controlled URL (e.g., http://imdb.jurgens.lv) in a browser and inspect the page source.

> Expected: The malicious src attribute appears in the HTML. No alert should trigger yet, as the context is not error-prone on your site.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- payload-injection
