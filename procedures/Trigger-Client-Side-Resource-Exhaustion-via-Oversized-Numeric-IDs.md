---
tags:
  - wordpress
  - resource-exhaustion
  - dos
  - client-side
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 5375237f-0980-4c13-92e1-da91b8d69a17
created_at: '2025-12-14T17:24:23.417Z'
updated_at: '2025-12-14T17:24:23.417Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Trigger-Client-Side-Resource-Exhaustion-via-Oversized-Numeric-IDs

## Summary

This procedure exploits a resource exhaustion vulnerability in WordPress.com by crafting URLs with extremely long numeric IDs for posts, designs, or pages, causing an exception that triggers unlimited requests to the pixel tracking endpoint (pixel.wp.com/g.gif), resulting in 99% CPU usage and browser unresponsiveness. It targets the trust in legitimate WordPress URLs to deliver a denial-of-service effect on the client side.

## Description

The vulnerability stems from variables in WordPress.com that cannot handle oversized numeric values for IDs. When a URL like /post/<very long number> is accessed, it throws an exception, leading to an infinite loop of tracking pixel requests. This spikes CPU on the victim's machine, rendering the browser unusable. No authentication is required, making it suitable for drive-by attacks via shared links. Expected outcomes include degraded performance, potentially frustrating users or disrupting workflows on WordPress.com.

## Requirements

1. Web browser with developer tools enabled for monitoring network requests
2. Access to any WordPress.com site (public URLs suffice)
3. No special network access; standard internet connectivity

## Defense

Defensive measures and detection strategies:

- Implement server-side validation on ID lengths and types to prevent oversized inputs
- Rate-limit requests to tracking endpoints like pixel.wp.com to avoid floods
- Monitor for anomalous request patterns to pixel endpoints from single sessions
- Educate users on avoiding unverified links, even from trusted domains

## Objectives

1. Cause immediate client-side denial of service through resource exhaustion
2. Demonstrate impact on user experience without server compromise
3. Highlight risks of unvalidated URL parameters in web applications

## Instructions

### Step 1: Craft the Oversized ID URL

**Context**: Generate a URL that exceeds the numeric ID limits to trigger the exception. Use legitimate WordPress.com path structures but append an excessively long number (e.g., 100+ digits).

Navigate to one of the following example URLs in your browser:

```url
https://wordpress.com/post/20000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```

or

```url
https://wordpress.com/design/1000000000000000000000
```

or for pages:

```url
https://wordpress.com/pages/example.wordpress.com/-10000000000000000000000000000000000000000000000
```

> These URLs mimic valid resources but cause the ID parsing to fail, initiating the loop.

### Step 2: Access the URL and Monitor Impact

**Context**: Visit the crafted URL to trigger the vulnerability and observe the resource exhaustion.

Open the URL in a web browser. Open the browser's developer tools (F12) and monitor the Network tab for requests to https://pixel.wp.com/g.gif?v=wpcom-no-pv&x_newdash_pageviews=route&t=<timestamp>.

Check the system's task manager or activity monitor for CPU usage.

> The exception leads to unlimited pixel requests, causing CPU to hit 99% and the browser to freeze.

### Step 3: Validate the Exhaustion Effect

**Context**: Confirm the denial-of-service impact to ensure exploitation success.

Observe the browser becoming unresponsive. Attempt to close tabs or switch applications; the high CPU should hinder normal operation.

> Success is indicated by persistent high CPU and stalled browser processes.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[wordpress]]
- [[dos]]
- [[resource-exhaustion]]
