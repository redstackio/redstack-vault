---
id: p3b2c3d4-e5f6-7890-abcd-ef1234567893
name: Inject-Payload-into-ThumbnailsAccessToken-Header
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:23:54.109Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - rce
  - deserialization
  - injection
platforms:
  - Web
commands:
  - '[[commands/curl-inject-deserialization-payload]]'
tools: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Inject-Payload-into-ThumbnailsAccessToken-Header

## Summary

This procedure injects the malicious serialized payload into the ThumbnailsAccessToken header of a Sitecore request, triggering deserialization and remote code execution on the server.

## Description

The injection targets Sitecore's thumbnail API endpoints, where the header is deserialized without validation. Using HTTP tools, the base64-encoded payload is sent, exploiting BinaryFormatter to execute the embedded gadget chain. This occurs in web environments with public-facing Sitecore instances. Prerequisites include the generated payload from ysoserial.net. Expected outcomes: Server-side code execution without authentication, leading to potential compromise.

## Requirements

1. Generated payload file (base64-encoded)
2. URL of the Sitecore thumbnail endpoint
3. HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Remove public access to vulnerable endpoints; place behind authentication or WAF
- Log and alert on unusual header values or deserialization attempts
- Use request size limits to block large payloads

## Objectives

1. Deliver the payload to the deserialization sink
2. Trigger RCE without detection
3. Confirm execution via side effects

## Instructions

### Step 1: Prepare the Request

**Context**: Identify the exact endpoint, typically /api/thumbnails or similar in Sitecore.

No command; confirm via prior reconnaissance.

### Step 2: Send the Injection

**Context**: Use curl to inject the payload into the header.

Execute [[commands/curl-inject-deserialization-payload]]:

```bash
curl -H "ThumbnailsAccessToken: $(cat payload.b64)" https://target-sitecore.com/api/thumbnails -v
```

> The -v flag shows verbose output; expect a 200 OK or similar, with potential delays for command execution.

### Step 3: Verify Injection

**Context**: Check for execution indicators, like a spawned process on the server if accessible.

Monitor network or use a payload that exfils data.

> Expected output: No errors; server processes the header.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-inject-deserialization-payload]]

## Tools Used


## Tags

- [[rce]]
- [[deserialization]]
- [[injection]]
