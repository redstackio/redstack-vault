---
id: proc-002
tags:
  - ip-conversion
  - bypass
  - redirect
type: procedure
tools:
  - '[[tools/site24x7-ip-finder]]'
  - '[[tools/smart-conversion-ip-address-converter]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:23.226Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Convert Domain to Dotless IP for Redirect Bypass

## Summary

This procedure converts a target domain to its IP address and then to a dotless decimal representation to bypass path validation restrictions in the Twitter mobile open redirect, enabling redirects to arbitrary IPs without using blocked dot notation.

## Description

Twitter's validation blocks dots in URL paths to prevent easy domain specification, but allows numeric paths that resolve as IPs. By resolving a domain (e.g., example.com) to an IP (93.184.216.34) and converting it to a single decimal (1572395042), the path //1572395042/messages redirects form submission to the target without triggering filters. This is key for chaining to token leakage.

## Requirements

1. Internet access for online tools.
2. Target domain under attacker control or for testing.
3. Basic knowledge of IP addressing.

## Defense

Defensive measures and detection strategies:

- Validate and normalize all URL paths to reject numeric sequences mimicking IPs.
- Implement allow-lists for redirect targets.
- Log and alert on unusual path encodings in requests.

## Objectives

1. Resolve domain to usable IP.
2. Encode IP to avoid detection filters.
3. Prepare encoded value for redirect exploitation.

## Instructions

### Step 1: Resolve Domain to IP

**Context**: Use an online tool to find the target's IP address.

No command; visit [[tools/site24x7-ip-finder]] and enter example.com.

> Tool outputs IP 93.184.216.34; copy this value.

### Step 2: Convert IP to Dotless Decimal

**Context**: Transform the dotted IP into a single integer.

No command; use [[tools/smart-conversion-ip-address-converter]] with input 93.184.216.34.

> Converter returns 1572395042; verify by reversing (e.g., 1572395042 / 256^3 = 93, etc.).

### Step 3: Validate Encoding

**Context**: Test the numeric path in a simple redirect.

Construct https://mobile.twitter.com//1572395042/messages and load.

> Ensure page loads without validation errors; proceed to exploitation if successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/site24x7-ip-finder]]
- [[tools/smart-conversion-ip-address-converter]]

## Tags

- ip-encoding
- domain-resolution
- bypass-technique
