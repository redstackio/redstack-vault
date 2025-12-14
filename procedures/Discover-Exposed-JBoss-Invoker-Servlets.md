---
id: p-discover-jboss-invokers
tags:
  - recon
  - jboss
  - deserialization
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T17:23:42.668Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Discover Exposed JBoss Invoker Servlets

## Summary

This procedure identifies openly accessible JBoss invoker servlets, such as EJBInvokerServlet and JMXInvokerServlet, which are prone to Java deserialization attacks when accepting untrusted input.

## Description

In JBoss environments, invoker servlets are management endpoints that process serialized Java objects. If exposed without authentication, they can be exploited for RCE using gadget chains like CommonsCollections. This step involves scanning or manually checking for these endpoints on the target domain, confirming vulnerability by observing acceptance of serialized payloads.

## Requirements

1. Network access to the target domain over HTTPS
2. Basic knowledge of web application structure and JBoss defaults
3. Tools like browser or curl for endpoint probing

## Defense

Defensive measures and detection strategies:

- Remove or disable invoker servlets in production JBoss configurations
- Implement input validation and deserialization blacklisting
- Monitor for anomalous POST requests to /invoker/ paths with binary content

## Objectives

1. Locate vulnerable endpoints
2. Confirm exposure without authentication
3. Assess potential for deserialization exploits

## Instructions

### Step 1: Probe Target Domain

**Context**: Manually or automatically enumerate common JBoss paths to find exposed invokers.

No specific command; use browser or curl to GET https://target/invoker/EJBInvokerServlet and https://target/invoker/JMXInvokerServlet.

> Expected: HTTP response indicating the servlet is active, often with a stack trace or default message if no payload sent.

### Step 2: Validate Serialized Input Acceptance

**Context**: Send a minimal serialized object to confirm the endpoint processes it.

Use a simple tool like curl to POST empty binary data with appropriate Content-Type.

> Expected: No rejection; server attempts deserialization.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Active Scanning: Vulnerability Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- recon
- jboss
