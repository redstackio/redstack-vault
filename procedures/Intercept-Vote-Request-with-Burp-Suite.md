---
tags:
  - race-condition
  - web
  - interception
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/urbandictionary-vote-get]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:22.731Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: c3683b1d-f93d-4648-b7a1-0070f9b68b5e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Vote-Request-with-Burp-Suite

## Summary

This procedure uses Burp Suite to intercept and capture a vote request from Urban Dictionary's API, extracting parameters for replay in a race condition exploit.

## Description

Burp Suite acts as a proxy to capture the GET request sent when a vote is triggered. The attack scenario involves a public web app vulnerable to concurrent requests due to lack of locking. Prerequisites include Burp Suite running and browser proxy set to 127.0.0.1:8080. Expected outcomes: Full request details including headers, defid=3889203, direction=up, and key=ab71d33b15d36506acf1e379b0ed07ee.

## Requirements

1. Burp Suite installed and running
2. Browser proxy configured to Burp
3. Initial vote triggered from website

## Defense

Defensive measures and detection strategies:

- Monitor for proxy interception patterns in traffic logs
- Enforce HTTPS to complicate interception
- Rate limit API calls per IP/session

## Objectives

1. Capture the exact vote API request
2. Extract authentication key and parameters
3. Prepare for concurrent replay

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up interception in Burp Suite.

No command; in Burp, go to Proxy > Intercept and turn on Intercept is on.

> Ensure browser traffic routes through Burp.

### Step 2: Trigger and Intercept Request

**Context**: Perform the vote action to capture the request.

Execute the vote via UI, which sends [[commands/urbandictionary-vote-get]]:

```http
GET /v0/vote?defid=3889203&direction=up&key=ab71d33b15d36506acf1e379b0ed07ee HTTP/1.1
Host: api.urbandictionary.com
Cache-Control: max-age=0
Accept: application/json, text/javascript, */*; q=0.01
Origin: http://www.urbandictionary.com/
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36
Referer: http://www.urbandictionary.com/define.php?term=alicia
Accept-Encoding: gzip, deflate, sdch
Accept-Language: en-US,en;q=0.8
Connection: close
```

> Burp displays the request; forward it. Expected: 200 OK with initial vote counts.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/urbandictionary-vote-get]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- race-condition
- web
- interception
