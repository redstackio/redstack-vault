---
tags:
  - xss
  - gtm
  - payload-creation
type: procedure
tools:
  - '[[tools/Google-Tag-Manager]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:37.508Z'
sub_techniques: []
id: 24328e8f-b6c8-492e-bf67-cf5ffe6487b8
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-GTM-Container-with-XSS-Payload

## Summary

This procedure involves setting up a Google Tag Manager (GTM) account and container to host arbitrary HTML containing an XSS payload, such as an img tag with an onerror handler that executes JavaScript, enabling stored XSS exploitation when loaded by a vulnerable endpoint.

## Description

In the context of the redditmedia.com vulnerability, create a GTM container that serves HTML like '<html><img src=x onerror=alert(1)></html>' for basic XSS testing or a cookie bomb payload with multiple img tags setting large cookies (e.g., 1000+ cookies of 4KB each for .redditmedia.com). This payload executes in the browser when the vulnerable /gtm/jail endpoint fetches and renders the GTM content without sanitization. Prerequisites include a Google account; no special permissions are needed beyond public GTM access.

## Requirements

1. Google account for GTM access
2. Web browser for configuration
3. Basic knowledge of HTML and JavaScript for payload crafting

## Defense

Defensive measures and detection strategies:

- Sanitize or validate GTM container content before rendering HTML
- Implement Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous GTM container creations or accesses

## Objectives

1. Host executable XSS payload in a controllable external service
2. Obtain a GTM ID for use in the vulnerable parameter
3. Enable JavaScript execution in the target domain's context

## Instructions

### Step 1: Set Up GTM Account and Container

**Context**: Create a new GTM workspace to host the payload.

Log in to https://tagmanager.google.com, create a new account if needed, and add a new container for web. Note the generated container ID (e.g., GTM-KM2VT3H).

### Step 2: Add HTML Tag with XSS Payload

**Context**: Configure an HTML tag that triggers on all pages to serve the malicious content.

In the container workspace, create a new tag of type 'Custom HTML'. Set the HTML to the payload, e.g., for cookie bomb:

```html
<html><body><script>for(let i=0;i<1000;i++){document.cookie=`bomb${i}=${'a'.repeat(4000)};domain=.redditmedia.com;path=/;`}</script></body></html>
```

Or for basic alert: `<html><img src=x onerror=alert(1)></html>`. Set trigger to 'All Pages' and publish the container.

> This step ensures the GTM endpoint serves the HTML when requested.

### Step 3: Verify Payload

**Context**: Test the container's output.

Use the GTM preview mode or directly access the GTM publish URL to confirm the HTML loads and executes in a test page.

**Expected Output**: Payload HTML served; JavaScript runs (alert or cookies set).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Tag-Manager]]

## Tags

- [[xss]]
- [[gtm]]
- [[payload-creation]]
