---
tags:
  - dos
  - cookie-bomb
  - impact
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T03:16:37.505Z'
sub_techniques: []
id: 09f41887-7097-44e5-b773-0debed7fc4d7
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Trigger-DoS-on-Reddit-com-via-Cookie-Overflow

## Summary

This procedure demonstrates the impact of the XSS by navigating to reddit.com after setting oversized cookies on .redditmedia.com, causing media resources to fail loading due to cookie header overflow in requests.

## Description

Following payload execution, the browser includes thousands of large cookies in all requests to redditmedia.com, exceeding limits (e.g., 4KB per cookie or total header size), leading to rejected requests and broken media on reddit.com. This is a user-specific DoS, as media embeds from redditmedia.com fail. Hypothetical JSONP chaining was noted but unexploitable.

## Requirements

1. Cookies already set from prior XSS execution
2. Access to reddit.com in the same browser session
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Cookie size limits and validation on servers
- Monitor for anomalous cookie counts/sizes in requests
- Clear cookies or use incognito for testing

## Objectives

1. Cause denial of service for media loading
2. Demonstrate cross-subdomain impact
3. Highlight resource exhaustion via client-side manipulation

## Instructions

### Step 1: Navigate to Target Site

**Context**: Load reddit.com to trigger media requests.

Open https://reddit.com/ in the affected browser. Scroll or interact to load media content.

### Step 2: Observe Failures

**Context**: Requests to redditmedia.com will include bloated cookies.

Use developer tools (Network tab) to inspect requests; expect errors like 400 Bad Request due to oversized headers.

> Media images/videos from redditmedia.com will not load.

### Step 3: Validate DoS

**Context**: Confirm service unavailability.

Check that non-media parts of reddit.com work, but media embeds are broken or slow.

**Expected Output**: Partial site functionality with media failures.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[dos]]
- [[cookie-bomb]]
- [[Impact]]
