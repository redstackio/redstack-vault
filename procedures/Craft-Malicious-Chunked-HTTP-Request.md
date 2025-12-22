---
id: proc-craft-chunked-request
tags:
  - dos
  - http
  - chunked-encoding
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:26:48.984Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Craft-Malicious-Chunked-HTTP-Request

## Summary

This procedure crafts a malicious HTTP request exploiting the unbounded chunk extension in Node.js HTTP parsing to initiate unlimited byte reading without transferring actual data, setting up a denial of service condition.

## Description

The attack targets the http module in Node.js where chunked transfer encoding allows extensions after the chunk size. By specifying an extension that causes the parser to expect unbounded bytes without providing them, the server enters a loop of reading from the connection, exhausting CPU on parsing and holding network resources. This affects versions 18.x, 20.x, and 21.x, bypassing typical limits. Prerequisites include understanding HTTP/1.1 specs (RFC 7230) and access to craft raw requests.

## Requirements

1. Knowledge of HTTP chunked encoding and extensions
2. Text editor or script to generate the request payload
3. Target Node.js server details (host, port)

## Defense

Defensive measures and detection strategies:

- Implement limits on chunk extension length in HTTP parsers (patched in Node.js post-vulnerability)
- Use rate limiting and connection timeouts stricter than default
- Monitor for long-lived connections with low data transfer and high CPU in web processes

## Objectives

1. Generate a valid yet malicious HTTP request payload
2. Ensure the payload triggers unbounded reading
3. Prepare for transmission without alerting basic validators

## Instructions

### Step 1: Define Request Headers

**Context**: Start with standard HTTP/1.1 headers indicating chunked transfer encoding.

Create the initial part of the request:

```http
POST / HTTP/1.1
Host: target-server:3000
Transfer-Encoding: chunked

```

> This sets up the request for chunked body without Content-Length.

### Step 2: Add Malicious Chunk with Extension

**Context**: Append a chunk header with an unbounded extension to exploit the parsing flaw.

Add the chunk line:

```http
0;chunk-extension=unbounded-read-here

```

Follow with no data and end chunk if needed, but the extension causes the hang:

```http
0

```

> The ';chunk-extension=unbounded-read-here' tricks the parser into expecting more bytes indefinitely. Adjust extension to maximize effect based on Node.js version.

### Step 3: Save and Validate Payload

**Context**: Combine into a file and verify syntax.

Save as `malicious_request.txt` and test parse with tools like `curl --head` or a local server.

**Expected Output**: Syntactically valid HTTP request file.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Network Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dos
- http-crafting
