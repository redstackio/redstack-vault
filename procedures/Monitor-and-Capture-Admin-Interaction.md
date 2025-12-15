---
id: proc-monitor-admin-xss
tags:
  - monitoring
  - exfiltration
  - xss
  - admin-capture
type: procedure
tools:
  - '[[tools/zomato-php-callback]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exfiltration Over Command and Control Channel]]'
updated_at: '2025-12-14T17:30:47.064Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exfiltration Over Command and Control Channel]]'
---
# Monitor-and-Capture-Admin-Interaction

## Summary

This procedure involves waiting for and capturing data from admin browsers that execute the injected Blind XSS payload, logging details like IP and referrer to facilitate further attacks such as session theft.

## Description

After payload injection, admins viewing the stored data in the Zomato dashboard trigger the XSS, causing their browser to request the callback server. The procedure focuses on monitoring logs for these events, which confirm exploitation and provide reconnaissance on admin environments. In the report, this captured two Indian IPs, highlighting the blind nature—no immediate feedback, but eventual hits.

## Requirements

1. Deployed callback server from previous procedure
2. Access to server logs (e.g., tail -f log.txt)
3. Patience for admin interaction (may take minutes to hours)
4. Tools for log analysis if scaling (e.g., grep for IPs)

## Defense

Defensive measures and detection strategies:

- Sanitize admin dashboard outputs to prevent XSS execution
- Enable browser sandboxing and disable auto-loading of external images in admin tools
- Monitor admin access logs for views of user-submitted content
- Alert on external requests from admin sessions to unknown hosts

## Objectives

1. Detect when the XSS payload executes in admin context
2. Collect victim metadata (IP, referrer) for targeting
3. Validate the blind exploitation success

## Instructions

### Step 1: Initiate Monitoring

**Context**: Set up real-time log watching.

On the server, run tail -f log.txt to monitor for new entries in real-time.

**Expected Output**: Live view of log file; initial empty or test entries.

### Step 2: Wait for Trigger

**Context**: Allow time for backend processing and admin review.

Submit the payload and wait; the stored data must reach the admin dashboard for viewing, triggering the img src request.

**Expected Output**: No immediate output; success is asynchronous.

### Step 3: Capture and Analyze Logs

**Context**: Review incoming callbacks.

Upon hits, logs show entries like 'Time: 2018-12-12 13:49:25 IP: █████ Referer: C: zomato_xss'. Note IPs (e.g., two Indian ones) and referrers confirming admin origin.

**Expected Output**: Log entries with remote IPs and Zomato referrers.

### Step 4: Validate and Plan Next Steps

**Context**: Confirm exploitation and assess data.

Verify the 'c' parameter is 'zomato_xss' and referrer indicates dashboard. Use captured IPs for further recon (e.g., geolocation).

**Expected Output**: Evidence of admin compromise; potential for cookie theft via advanced payloads.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Exfiltration Over Command and Control Channel]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/zomato-php-callback]]

## Tags

- [[monitoring]]
- [[Exfiltration]]
- [[xss]]
- [[admin-capture]]
