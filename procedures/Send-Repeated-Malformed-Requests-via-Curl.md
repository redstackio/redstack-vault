---
id: proc-uuid-5
name: Send Repeated Malformed Requests via Curl
tags:
  - dos
  - rails
  - exploit
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/send-repeated-malformed-requests]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:36.509Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Send Repeated Malformed Requests via Curl

## Summary

This procedure uses curl in a loop to send malformed HTTP requests with XML headers to a non-existent path, triggering 404 exceptions and causing progressive mutation of the response body.

## Description

The malformed path like ///wp1/wp-includes/wlwmanifest.xml fails routing, invoking ShowExceptions. Each exception mutates the shared FAILSAFE_RESPONSE via lograge and request_store, building recursive Rack::BodyProxy objects until stack overflow.

## Requirements

1. Running Rails server on localhost:3000
2. Ruby interpreter for the loop
3. Curl installed

## Defense

Defensive measures and detection strategies:

- Rate limit XML-accepting endpoints
- Validate path formats with regex in routing
- Monitor for repeated 404s from same IP

## Objectives

1. Trigger exception handling repeatedly
2. Mutate response constants across requests
3. Build recursive object depth

## Instructions

### Step 1: Execute Request Loop

**Context**: Use a Ruby one-liner to loop 1000 curl requests, simulating a flood attack.

**Command** ([[commands/send-repeated-malformed-requests]]):
```bash
1000.times.each do |n| `curl -H "Accept: application/xml" -H "Content-Type: application/xml" -X GET http://localhost:3000///wp1/wp-includes/wlwmanifest.xml` end
```

> Run in terminal. Expected output: 404 responses for first ~989 requests, then crash.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/send-repeated-malformed-requests]]

## Tools Used

- [[tools/curl]]

## Tags

- dos
- rails
- exploit
