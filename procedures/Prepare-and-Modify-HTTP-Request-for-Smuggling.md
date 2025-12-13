---
tags:
  - http-request-smuggling
  - request-modification
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Chrome-Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 42afcfb5-ba9a-4b82-9798-812e9ae6a688
created_at: '2025-12-13T09:01:21.638Z'
updated_at: '2025-12-13T09:01:21.638Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Prepare and Modify HTTP Request for Smuggling

## Summary

This procedure involves selecting a legitimate POST request from twitter.com, intercepting it with Burp Suite, and modifying it to include chunked transfer encoding in preparation for HTTP Request Smuggling exploitation.

## Description

The procedure targets inconsistencies in chunked encoding handling between front-end and back-end servers on twitter.com. It sets up the request for smuggling by removing interfering headers and adding the necessary Transfer-Encoding header and chunked body. This is a foundational step for detecting and exploiting the vulnerability, potentially leading to unauthorized actions.

## Requirements

1. Access to twitter.com via Chrome Browser proxied through Burp Suite
2. Burp Suite installed and configured with Repeater module
3. Basic knowledge of HTTP request structures

## Defense

Defensive measures and detection strategies:

- Implement consistent HTTP parsing between front-end and back-end servers
- Monitor for unusual Transfer-Encoding headers in logs

## Objectives

1. Prepare a modifiable request for smuggling tests
2. Enable chunked encoding without rejection
3. Set stage for vulnerability confirmation and exploitation

## Instructions

### Step 1: Intercept and Send Request to Repeater

**Context**: Select a legitimate HTTP POST request from twitter.com traffic and forward it to Burp Repeater for modification.

Using [[tools/Burp-Suite]], intercept the request in the proxy and right-click to send to Repeater.

> This allows detailed modification of the request headers and body.

### Step 2: Remove Specific Headers

**Context**: Remove headers that may interfere with smuggling.

In Burp Repeater, delete 'Connection: close' and 'Accept-Encoding: gzip, deflate' headers.

> This prepares the request for clean chunked encoding insertion.

### Step 3: Add Transfer-Encoding Header

**Context**: Insert the chunked encoding header.

Add 'Transfer-Encoding: chunked' to the request headers in Repeater.

> This signals the use of chunked transfer encoding.

### Step 4: Add Chunked Encoding to Body

**Context**: Encode the request body appropriately.

Modify the body to include chunked encoding, such as '0' followed by two CRLFs.

> Ensures the body is treated as chunked by the back-end.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Chrome-Browser]]

## Tags

- [[http-request-smuggling]]
- [[request-modification]]
