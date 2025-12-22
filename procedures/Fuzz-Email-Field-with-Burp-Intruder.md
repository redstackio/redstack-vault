---
id: proc-3
tags:
  - fuzzing
  - dos
  - rate-limiting
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:23:24.821Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
---
# Fuzz-Email-Field-with-Burp-Intruder

## Summary

This procedure automates the submission of hundreds of payloads to the email field using Burp Intruder's fuzzing capabilities, exploiting missing rate limiting to trigger excessive email reset processes and cause denial-of-service on the backend email system.

## Description

By loading the intercepted request into Burp Intruder and positioning payloads in the data[User][email] parameter, approximately 300 variations (e.g., %26%20 for ampersand space) are sent rapidly. Certain payloads trick the system into 'success' responses, initiating email threads that retry indefinitely for invalid addresses, overwhelming the email service and potentially the servers. This targets PHP-based web apps without request throttling.

## Requirements

1. Intercepted request from previous procedure
2. Burp Suite with Intruder module
3. Payload list including URL-encoded specials like %0a, %0d, %26%20

## Defense

Defensive measures and detection strategies:

- Implement rate limiting (e.g., 5 requests per minute per IP) on forgot password endpoints
- Use CAPTCHA or secondary verification for reset requests
- Monitor for high-volume identical requests and alert on email thread spikes

## Objectives

1. Flood the endpoint to demonstrate lack of rate limiting
2. Trigger backend email processes for DoS
3. Observe system overload from retrying threads

## Instructions

### Step 1: Load Request into Intruder

**Context**: Prepare the captured request for automated attacks.

In Burp, right-click the intercepted request and select 'Send to Intruder'.

### Step 2: Configure Payload Positions

**Context**: Mark the email parameter for fuzzing.

In Intruder, go to Positions tab, clear defaults, and highlight §data[User][email]=value§ to set as payload position.

### Step 3: Load and Launch Payloads

**Context**: Inject variations to test responses and trigger processes.

In Payloads tab, load ~300 payloads (e.g., from a file with %0a, %0d, %26%20), set to Sniper mode, and start the attack.

**Expected Output**: Responses vary; some show 'Check your email for instructions', indicating triggered emails; overall, high request volume leads to backend delays.

### Step 4: Analyze Results

**Context**: Review for success indicators and impact.

Sort results by response length or code; monitor target for slowdowns.

**Expected Output**: Evidence of DoS, such as email server overload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Network Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- fuzzing
- denial-of-service
- burp-intruder
