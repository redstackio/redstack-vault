---
type: code
language: text
verified: true
created_at: '2023-04-06T03:56:37.445034+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Web
tags:
  - ssrf
  - payload
  - memcached
  - bypassing-filters
validated: true
---

# Memcached-SSRF-Malformed-URL-Payloads

## Code

```powershell
localhost:+11211aaa
localhost:00011211aaaa
```

## Description

These are example malformed URL payloads designed to bypass URL validation filters in SSRF-vulnerable applications, forcing a connection to a local Memcached server on port 11211. The extra characters (e.g., '+aaa' or leading zeros) exploit parser inconsistencies, allowing resolution to localhost while evading blacklists that block plain 'localhost:11211'.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | These are static payloads; substitute directly into request parameters like 'url=' | localhost:+11211aaa |

## Usage

Inject these payloads into SSRF endpoints (e.g., via curl or Burp Repeater) to target internal Memcached instances. Used in procedures like [[procedures/Exploit-Memcached-for-SSRF-Attack]] during the payload crafting step. Start with external tests before internal probes to avoid detection.

## Detection

- WAF logs showing requests with multiple colons or unusual localhost variants.
- Application error logs with Memcached protocol responses (e.g., 'VERSION' keyword).
- Network monitoring for unexpected connections from web servers to port 11211.
- IDS signatures for SSRF patterns like '127.0.0.1' or 'localhost' in URL parameters.

## Related

- [[procedures/Exploit-Memcached-for-SSRF-Attack]]
- [[tools/Burp-Suite]]
