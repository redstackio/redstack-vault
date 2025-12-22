---
type: code
language: bash
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Web
tags:
  - command-injection
  - bypass
  - url-encoded
  - payload
validated: true
---

# url-encoded-backslash-newline-bypass-payload-for-cat-etc-passwd

## Code

```bash
cat%20/et%5C%0Ac/pa%5C%0Asswd
```

## Description

This is the URL-encoded version of the backslash-newline bypass payload for injecting 'cat /etc/passwd'. Encoding ensures compatibility with HTTP requests, where the server decodes it before shell execution, allowing the line continuation to take effect and evade filters.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Static encoded payload; adjust for specific command splits | N/A |

## Usage

Append or POST this string to the vulnerable parameter in a web request (e.g., ?cmd=cat%20/et%5C%0Ac/pa%5C%0Asswd). Use tools like curl or Burp Suite for delivery. Suitable for browser-based or API testing in command injection scenarios.

## Detection

- URL decoding logs revealing backslash (%5C) and newline (%0A) patterns.
- Anomaly detection in web traffic for encoded shell commands.
- Server-side logging of decoded inputs triggering file reads.

## Related

- [[procedures/Command-Injection-Filter-Bypass-with-Backslash-Newline]]
