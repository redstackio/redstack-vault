---
tags:
  - http-request-smuggling
  - ajp
  - apache
  - file-disclosure
  - rce
type: attack_chain
tools:
  - '[[tools/xxd]]'
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Discovery]]'
commands:
  - '[[commands/xxd-dump-payload]]'
  - '[[commands/curl-send-smuggled-request]]'
platforms:
  - Web
  - Linux
complexity: medium
procedures:
  - '[[procedures/Analyze-mod_proxy_ajp-Source-Code-for-Vulnerabilities]]'
  - '[[procedures/Create-Crafted-AJP-Payload-for-Smuggling]]'
  - '[[procedures/Exploit-HTTP-Request-Smuggling-with-Crafted-Request]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
description: >-
  Multi-stage attack exploiting HTTP Request Smuggling in Apache HTTP Server's
  mod_proxy_ajp to smuggle requests, disclose files, and potentially achieve
  remote code execution.
skill_level: advanced
impact_level: high
id: 1da0407c-14e7-42ab-9b2d-f33fd1501de2
created_at: '2025-12-13T09:01:21.840Z'
updated_at: '2025-12-13T09:01:21.840Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# HTTP Request Smuggling via mod_proxy_ajp for File Disclosure and Potential RCE

Multi-stage attack chain demonstrating how to exploit an HTTP Request Smuggling vulnerability in Apache HTTP Server's mod_proxy_ajp module. This allows attackers to smuggle requests to the backend AJP server by exploiting inconsistent handling of chunked Transfer-Encoding headers, leading to impacts such as setting request attributes, reading files in the application context, information disclosure, and potential remote code execution.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Advanced |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Source Code Analysis] --> B[Payload Creation]
    B --> C[Request Smuggling Exploitation]
    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools
- [[tools/xxd]]
- [[tools/curl]]

### Target Environment
- Apache HTTP Server with mod_proxy_ajp enabled
- Backend AJP server (e.g., Apache Tomcat)
- Linux platform
- Exposed proxy_ajp endpoint

### Initial Access Requirements
- Network access to the target server
- Ability to send HTTP requests
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Source Code Analysis
procedure: [[procedures/Analyze-mod_proxy_ajp-Source-Code-for-Vulnerabilities]]

**Objective**: Identify the vulnerability in mod_proxy_ajp by analyzing the source code to understand how chunked Transfer-Encoding leads to request smuggling.

**Instructions**: Examine the code in modules/proxy/mod_proxy_ajp.c to find that chunked requests cause the server to enter the else branch and immediately send POST data without waiting for the AJP protocol flow.

**Expected Output**: Confirmation of the vulnerability logic, such as the code path that flattens and sends the input brigade prematurely.

**Success Indicators**:
- Vulnerability root cause identified
- Understanding of smuggling mechanism

### Step 2: Payload Creation
procedure: [[procedures/Create-Crafted-AJP-Payload-for-Smuggling]]

**Objective**: Generate a binary payload file containing crafted AJP request data to smuggle attributes like javax.servlet.include.path_info for file reading.

**Instructions**: Create the payload file 'data2' with AJP protocol data. Then, use [[commands/xxd-dump-payload]] to verify its contents:

```bash
xxd data2
```

**Expected Output**: Hexadecimal dump showing AJP attributes, such as setting path_info to /WEB-INF/web.xml.

**Success Indicators**:
- Payload file created successfully
- Hex dump confirms correct AJP structure

### Step 3: Request Smuggling Exploitation
procedure: [[procedures/Exploit-HTTP-Request-Smuggling-with-Crafted-Request]]

**Objective**: Send the crafted request to the vulnerable server to exploit the smuggling and achieve file disclosure or other impacts.

**Instructions**: Use [[commands/curl-send-smuggled-request]] to send the POST request with the payload:

```bash
curl -i 10.211.55.3/proxy_ajp/ -H 'Transfer-Encoding: chunked' --data-binary @data2
```

**Expected Output**: HTTP/1.1 200 response containing the contents of /WEB-INF/web.xml or similar disclosed file.

**Success Indicators**:
- Successful response with disclosed information
- Confirmation of request smuggling impact

## Attack Chain Summary

### Key Achievements
1. Identification of smuggling vulnerability through code analysis
2. Creation of exploitable AJP payload
3. Successful smuggling leading to file disclosure and potential RCE

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques
- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics
- [[Initial Access]]
- [[Execution]]

*Last updated: [TIMESTAMP]*
