---
tags:
  - xss
  - endpoint-access
  - exploit
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
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:37.507Z'
sub_techniques: []
id: d169693b-1d21-45f1-b0c9-1508c2386b2c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Access-Redditmedia-GTM-Jail-Endpoint

## Summary

This procedure triggers the stored XSS vulnerability by accessing the redditmedia.com/gtm/jail endpoint with a malicious GTM container ID in the 'id' parameter, causing the server to fetch and execute unsanitized HTML from GTM in the browser context.

## Description

The /gtm/jail endpoint loads HTML from the specified GTM container without validation, rendering it directly and allowing JavaScript execution. Use a URL like https://redditmedia.com/gtm/jail?id=GTM-MS246QG&cb=aa to execute a cookie bomb payload, setting thousands of large cookies for .redditmedia.com. This occurs in the redditmedia.com origin, enabling domain-specific impacts like DoS on related subdomains.

## Requirements

1. Malicious GTM container ID from prior setup
2. Web browser with developer tools
3. Public access to redditmedia.com

## Defense

Defensive measures and detection strategies:

- Validate and sanitize GTM content before rendering
- Use iframe sandboxing or no-script fallbacks
- Log and rate-limit accesses to /gtm/jail endpoint

## Objectives

1. Execute arbitrary JavaScript in redditmedia.com context
2. Manipulate cookies for the target domain
3. Chain to impact services like reddit.com media loading

## Instructions

### Step 1: Prepare the Malicious URL

**Context**: Construct the endpoint URL with the GTM ID.

Use the format https://redditmedia.com/gtm/jail?id=<YOUR_GTM_ID>&cb=aa, replacing <YOUR_GTM_ID> with the container ID (e.g., GTM-MS246QG for cookie bomb).

### Step 2: Access the Endpoint

**Context**: Load the URL in a browser to trigger the fetch and execution.

Navigate to the URL. The endpoint will request the GTM HTML and render it, firing onerror handlers in img tags to run JavaScript.

> Monitor the network tab for the GTM fetch and console for execution.

### Step 3: Verify Execution

**Context**: Confirm payload impact.

Check browser cookies for .redditmedia.com; for basic XSS, an alert should pop up.

**Expected Output**: JavaScript runs; cookies set or alert displayed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Tag-Manager]]

## Tags

- [[xss]]
- [[endpoint-access]]
- [[exploit]]
