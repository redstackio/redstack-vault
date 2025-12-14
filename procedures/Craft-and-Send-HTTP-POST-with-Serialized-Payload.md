---
id: p-craft-send-post-payload
tags:
  - http-exploit
  - burp-suite
  - deserialization
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:42.649Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft and Send HTTP POST with Serialized Payload

## Summary

This procedure crafts an HTTP POST request containing a ysoserial-generated payload and sends it to the JBoss invoker servlet to trigger deserialization and RCE.

## Description

Using Burp Suite's Repeater, configure a POST to the vulnerable endpoint with the correct Content-Type header for serialized objects. The body is the binary payload file. This exploits the lack of validation in JBoss invokers, leading to command execution on deserialization.

## Requirements

1. Access to Burp Suite Professional or Community
2. Generated payload file from ysoserial
3. Target URL and HTTPS connectivity

## Defense

Defensive measures and detection strategies:

- Enforce TLS and validate Content-Type strictly
- Block binary uploads to sensitive endpoints
- WAF rules to detect ysoserial-like payloads or anomalous serialization

## Objectives

1. Deliver payload without rejection
2. Trigger server-side deserialization
3. Initiate command execution

## Instructions

### Step 1: Configure Request in Burp Repeater

**Context**: Set up the POST request with proper headers and body.

No command; manually enter:
- Method: POST
- URL: https://card.starbucks.in/invoker/EJBInvokerServlet
- Header: Content-Type: application/x-java-serialized-object; class=org.jboss.invocation.MarshalledInvocation
- Body: Paste binary from serialdata file using 'Paste from file'.

> Expected: Request ready; send to observe server response.

### Step 2: Send and Monitor

**Context**: Transmit the request and check for success.

Click 'Send' in Repeater.

> Expected: HTTP 200 or 500 with no explicit deserialization error, indicating potential execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- web-exploit
- rce
