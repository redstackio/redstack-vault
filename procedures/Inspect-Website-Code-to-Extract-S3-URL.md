---
id: proc-uuid-004
tags:
  - inspection
  - developer-tools
  - s3-url
type: procedure
tools:
  - '[[tools/Web-Browser-Developer-Tools]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Process Discovery]]'
updated_at: '2025-12-14T17:25:18.269Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[T1057.001]]'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Process Discovery]]'
---
# Inspect-Website-Code-to-Extract-S3-URL

## Summary

This procedure examines the customer-side HTML on the Shopify website to extract the S3 image URL after an upload, revealing the bucket details.

## Description

Using browser developer tools, attackers inspect the rendered chat HTML to find the `<img>` src attribute pointing to the S3 object. The URL format is `https://ping-api-production.s3.us-west-2.amazonaws.com/[object-key]`, partially redacted in reports. This step leverages client-side rendering flaws. Prerequisite: Recent image upload visible in chat.

## Requirements

1. Active chat with uploaded image visible
2. Web browser with dev tools (e.g., Chrome Inspector)
3. Basic HTML knowledge

## Defense

Defensive measures and detection strategies:

- Obfuscate or proxy S3 URLs in client-side code
- Monitor for dev tools usage via JavaScript detection
- Use signed URLs with short expiration

## Objectives

1. Locate image src in DOM
2. Extract full S3 path and bucket info
3. Identify misconfiguration indicators

## Instructions

### Step 1: Return to Customer View

**Context**: Refresh chat display.

Navigate back to the Shopify store website and ensure the image is loaded in the chat.

> Expected: Image renders on page.

### Step 2: Open Developer Tools and Inspect

**Context**: Analyze HTML source.

Right-click the image, select "Inspect Element," and search for the src attribute in [[tools/Web-Browser-Developer-Tools]].

> Expected: URL like `https://ping-api-production.s3.us-west-2.amazonaws.com/oks██████` appears.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Process Discovery]] Process Discovery

### Sub-Techniques

- [[T1057.001]] Browser Information Discovery

## Commands Used


## Tools Used

- [[tools/Web-Browser-Developer-Tools]]

## Tags

- code-inspection
- url-extraction
