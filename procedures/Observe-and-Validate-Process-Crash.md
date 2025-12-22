---
tags:
  - dos
  - validation
  - crash
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:37.433Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 61f4b44d-e233-4517-878b-c6d614b07127
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Observe-and-Validate-Process-Crash

## Summary

This procedure monitors and confirms the success of the DoS exploit by observing the Node.js process crash resulting from the nghttp2 NULL pointer dereference.

## Description

After sending malformed frames, the target Node.js process crashes due to the unhandled NULL pointer in nghttp2's ALTSVC handling. This procedure details validation through logs, monitoring, and service checks, confirming the denial of service impact. It applies to both server and client scenarios in HTTP/2 environments.

## Requirements

1. Access to target server logs or monitoring (e.g., via SSH or remote logging)
2. Tools for service health checks (e.g., curl or netcat)
3. Knowledge of the target process PID

## Defense

Defensive measures and detection strategies:

- Enable process monitoring with tools like Prometheus to alert on crashes
- Use application-level error handling to prevent full crashes from frame errors
- Rotate logs and review for segfault patterns post-incident

## Objectives

1. Confirm process termination from the exploit
2. Verify service unavailability (DoS)
3. Document crash details for reporting

## Instructions

### Step 1: Monitor Process State

**Context**: Check if the Node.js process has crashed post-frame sending.

Use `ps aux | grep node` on the target to verify PID disappearance, or tail crash logs: `tail -f /var/log/node.log` looking for "Segmentation fault" or nghttp2 errors.

### Step 2: Validate Service Downtime

**Context**: Test if the HTTP/2 service is unresponsive.

Attempt connections: `curl -v --http2 https://target.com` should timeout or fail. Confirm no new streams can be established.

### Step 3: Analyze Crash Logs

**Context**: Review details to attribute the crash to the NULL pointer.

Examine core dumps or logs for references to nghttp2_altsvc_frame.c and uninitialized pointers, confirming the exploit success.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- dos
- validation
