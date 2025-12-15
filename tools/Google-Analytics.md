---
id: tool-google-analytics
url: 'https://analytics.google.com'
tags:
  - tracking
  - exfiltration
  - analytics
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.414Z'
validated: true
submitted: true
---
# Google Analytics

**Status**: Unverified

## Overview

Google Analytics is a web analytics service that tracks and reports website traffic, used here for capturing query parameters like leaked OAuth codes from redirected URLs in real-time.

## Description

In offensive security, Google Analytics can be abused on attacker-controlled pages to passively exfiltrate data from URL query strings without custom logging. It integrates easily into platforms like Booth.pm via tracking IDs and provides real-time dashboards for monitoring. Common in OAuth theft scenarios where sensitive tokens appear in redirects.

## Features

- Feature 1: Real-time reporting of page views and parameters
- Feature 2: Query string tracking via URL dimensions
- Feature 3: Custom events for advanced data capture

## Installation

### Requirements

- Google account
- Website or page for integration (e.g., Booth.pm product)

### Install Commands

No installation; web-based. Embed script:

```html
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-XXXXX-Y"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA-XXXXX-Y');
</script>
```

## Basic Usage

Access via https://analytics.google.com; select property and view Realtime reports.

### Common Options

| Option | Description |
|--------|-------------|
| Realtime | Live user activity |
| Events | Tracked interactions |
| Dimensions | Custom URL/query filters |

## Examples

### Example 1: Basic Usage

View real-time traffic:

Navigate to Reports > Realtime.

### Example 2: Advanced Usage

Filter for query params:

In Realtime, add secondary dimension: Page path + query.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Sniffing]] Network Sniffing
- [[Steal Application Access Token]] Steal Application Access Token

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual GA tracking scripts on non-standard pages
- High real-time traffic from OAuth domains
- Query logging anomalies in GA exports

## Related Procedures


## Related Tools

- [[tools/Mixpanel]]
- [[tools/Adobe-Analytics]]

## References

- Official documentation: https://support.google.com/analytics
- Related resources: OAuth security guides
