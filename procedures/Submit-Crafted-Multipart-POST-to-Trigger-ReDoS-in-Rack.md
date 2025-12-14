---
id: 123e4567-e89b-12d3-a456-426614174001
name: Submit-Crafted-Multipart-POST-to-Trigger-ReDoS-in-Rack
type: procedure
verified: false
submitted: true
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.835Z'
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
sub_techniques: []
tags:
  - dos
  - redos
  - rack
  - ruby
  - rails
  - multipart
commands:
  - '[[commands/curl-multipart-redos-rack]]'
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
---

# Submit-Crafted-Multipart-POST-to-Trigger-ReDoS-in-Rack

## Summary

This procedure exploits a Regular Expression Denial of Service (ReDoS) vulnerability in Rack's multipart parsing component by submitting a crafted HTTP POST request with a malicious boundary string, causing exponential backtracking in the regex engine and leading to excessive CPU usage on vulnerable Ruby on Rails servers.

## Description

Rack, a core component of Ruby on Rails, handles multipart/form-data parsing for file uploads and form submissions according to RFC2183. The boundary parsing uses a regular expression that is vulnerable to ReDoS due to lack of safeguards like atomic grouping or memoization in Ruby versions prior to 3.2. An attacker can craft a multipart request where the boundary and body include repeating patterns (e.g., nested quantifiers like (a+)+b) that force the regex engine to explore an exponential number of states, consuming 100% CPU for minutes on end. This affects any Rails application (>= Rack 2.0.0) without mitigations, enabling remote DoS without authentication if an upload endpoint is exposed.

## Requirements

1. Access to a network-reachable Ruby on Rails application using vulnerable Rack version
2. An endpoint that processes multipart/form-data POST requests (e.g., /upload)
3. Tools to craft and send HTTP requests (e.g., curl)
4. Knowledge of ReDoS patterns to generate evil boundary strings

## Defense

Defensive measures and detection strategies:

- Upgrade to Ruby 3.2+ with built-in regex memoization or patch Rack with atomic regexes
- Implement request timeouts and rate limiting on multipart endpoints
- Monitor for sudden CPU spikes correlated with multipart requests; use WAF rules to scan for suspicious boundary patterns
- Disable or sandbox multipart parsing if not essential

## Objectives

1. Trigger ReDoS to exhaust CPU resources on the target server
2. Deny service to legitimate users by making the application unresponsive
3. Demonstrate vulnerability in Rack-based web applications

## Instructions

### Step 1: Craft the Malicious Payload

**Context**: Create a file with a multipart body using an evil boundary string that exploits the regex backtracking, such as a long string of repeating characters designed for catastrophic matching (e.g., 'a{100,}(b(a+))+'). The boundary must be unique and trigger the vulnerable pattern in Rack's parser.

**Command** ([[commands/curl-multipart-redos-rack]]):
First, prepare the payload file `crafted_payload.txt`:

```bash
echo '--evil-boundary\r\nContent-Disposition: form-data; name=\"file\"; filename=\"test.txt\"\r\n\r\nmalicious content with repeating patterns to amplify backtracking\r\n--evil-boundary--\r\n' > crafted_payload.txt
```

> This creates a basic multipart structure; customize the boundary (e.g., 'aaaaaaaaaaaaaaaa...b') to match known ReDoS triggers for the specific regex in Rack's code (lib/rack/utils.rb or similar).

### Step 2: Submit the Request to the Target Endpoint

**Context**: Send the crafted payload via POST to the vulnerable endpoint, specifying the boundary in the Content-Type header to initiate parsing and trigger the DoS.

**Command** ([[commands/curl-multipart-redos-rack]]):

```bash
curl -X POST http://target.example.com/upload \
  -H "Content-Type: multipart/form-data; boundary=evil-boundary" \
  --data-binary @crafted_payload.txt \
  -v
```

> The -v flag shows verbose output for debugging. Expect the request to hang as the server parses the boundary, with CPU usage spiking. If successful, the server may timeout or crash the worker process.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/curl-multipart-redos-rack]]

## Tools Used


## Tags

- [[dos]]
- [[redos]]
- [[rack]]
- [[ruby]]
- [[rails]]
- [[multipart]]
