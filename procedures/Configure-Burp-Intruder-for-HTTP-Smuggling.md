---
tags:
  - http-request-smuggling
  - web-exploit
type: procedure
tools:
  - '[[tools/Burp-Suite-Intruder]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
id: df2f5637-2b6a-4eb1-b759-45f11cb35998
created_at: '2025-12-13T09:01:17.705Z'
updated_at: '2025-12-13T09:01:17.705Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure Burp Intruder for HTTP Smuggling

## Summary

This procedure configures Burp Suite Intruder with a crafted payload for exploiting HTTP Request Smuggling vulnerabilities, focusing on chunked transfer encoding with tab characters to smuggle malicious requests that alter headers like Host for arbitrary redirects.

## Description

The procedure involves setting up a base64-encoded or decoded HTTP request in Burp Intruder to exploit desynchronization between front-end and back-end servers. It targets paths like /sf on https://consumer.acronis.com, allowing header manipulation without validation. Expected outcomes include successful payload preparation for smuggling attacks, leading to potential redirects to malicious domains.

## Requirements

1. Access to Burp Suite Professional
2. Network access to the target domain https://consumer.acronis.com
3. Base64-encoded payload or ability to decode it

## Defense

Defensive measures and detection strategies:

- Implement strict HTTP request parsing and validation on servers
- Monitor for anomalous Transfer-Encoding headers and chunked requests in logs

## Objectives

1. Prepare exploitable payload for HTTP smuggling
2. Ensure chunk sizes match smuggled content
3. Set up for automated request sending

## Instructions

### Step 1: Decode and Load Payload

**Context**: Decode the base64 payload if needed and load it into Burp Intruder for configuration.

> The payload includes POST / HTTP/1.1 with Transfer-Encoding: chunked (tab), Host: consumer.acronis.com, and smuggled POST /sf with malicious Host.

### Step 2: Adjust Chunk Size

**Context**: Modify the hex chunk size (e.g., '64') to match the exact length of the smuggled request.

> Ensure no mismatches to avoid detection or failure.

### Step 3: Configure Intruder Settings

**Context**: Set attack type to Sniper or similar, with positions for varying the malicious Host if needed.

> Target the request to https://consumer.acronis.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite-Intruder]]

## Tags

- [[http-request-smuggling]]
- [[web-exploit]]
