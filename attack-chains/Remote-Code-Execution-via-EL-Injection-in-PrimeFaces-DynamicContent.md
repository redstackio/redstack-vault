---
tags:
  - rce
  - el-injection
  - primefaces
  - jsf
  - java
  - dns-exfiltration
type: attack_chain
tools:
  - '[[tools/curl]]'
  - '[[tools/dnsbin-zhack-ca]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Java
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Generate-Encrypted-EL-Payload-for-PrimeFaces-RCE]]'
  - '[[procedures/Construct-EL-Injection-Exploit-URL]]'
  - '[[procedures/Send-EL-Injection-Payload-via-Curl]]'
  - '[[procedures/Observe-DNS-Exfiltration-from-RCE]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:07.866Z'
description: >-
  This attack chain exploits an Expression Language (EL) injection vulnerability
  in PrimeFaces 5.3's DynamicContent generator to achieve remote code execution
  (RCE) on a JavaServer Faces (JSF) application, demonstrated through DNS
  exfiltration to a controlled domain.
skill_level: intermediate
impact_level: high
id: 45d281ba-a15a-420c-b310-b4006f7a406f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Remote Code Execution via EL Injection in PrimeFaces DynamicContent

Multi-stage attack chain demonstrating exploitation of EL injection in PrimeFaces 5.3 for RCE on a JSF web application, leading to DNS-based exfiltration without direct file access to minimize impact.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Payload Generation] --> B[URL Construction]
    B --> C[Payload Delivery]
    C --> D[Exfiltration Observation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]
- [[tools/dnsbin-zhack-ca]]
- Java development environment with PrimeFaces 5.3 JAR

### Target Environment

- JSF web application running PrimeFaces 5.3
- Accessible over HTTP/HTTPS on port 80/443
- No authentication required for the vulnerable endpoint

### Initial Access Requirements

- Network access to the target web server
- Knowledge of the application's PrimeFaces version (via source inspection or error messages)
- Controlled DNS server for exfiltration observation

## Detailed Attack Procedures

### Step 1: Payload Generation
procedure: [[procedures/Generate-Encrypted-EL-Payload-for-PrimeFaces-RCE]]

**Objective**: Create an encrypted EL payload that triggers RCE via DNS resolution when injected into the pfdrid parameter.

**Instructions**: Compile and run the custom Java program with PrimeFaces 5.3 JAR in the classpath. Modify the remoteMalJarUrl to point to your controlled DNS domain (e.g., dnsbin.zhack.ca). The program generates an encrypted string for the payload.

```bash
javac -cp PrimeFaces-5.3.jar PayloadGenerator.java
java -cp .:PrimeFaces-5.3.jar PayloadGenerator
```

**Expected Output**: Encrypted payload string, e.g., a base64-like encoded value ready for URL insertion.

**Success Indicators**:
- Payload generated without compilation errors
- remoteMalJarUrl customized to controlled domain

### Step 2: URL Construction
procedure: [[procedures/Construct-EL-Injection-Exploit-URL]]

**Objective**: Build the full exploit URL targeting the DynamicContent endpoint with the generated payload.

**Instructions**: Append the encrypted payload to the base vulnerable URL. The endpoint is /javax.faces.resource/dynamiccontent.properties.xhtml with parameters pfdrt=sc&ln=primefaces&pfdrid=<payload>.

Example constructed URL:

```bash
https://target.com/javax.faces.resource/dynamiccontent.properties.xhtml?pfdrt=sc&ln=primefaces&pfdrid=<YOUR_GENERATED_PAYLOAD>
```

**Expected Output**: Valid URL ready for transmission.

**Success Indicators**:
- URL parameters correctly formatted
- Payload properly URL-encoded if necessary

### Step 3: Payload Delivery
procedure: [[procedures/Send-EL-Injection-Payload-via-Curl]]

**Objective**: Deliver the payload via HTTP GET to trigger EL injection and RCE.

**Instructions**: Use [[commands/curl-primefaces-exploit]] to send the request to the constructed URL, bypassing SSL verification if needed.

```bash
curl -vk "https://target.com/javax.faces.resource/dynamiccontent.properties.xhtml?pfdrt=sc&ln=primefaces&pfdrid=<YOUR_GENERATED_PAYLOAD>"
```

**Expected Output**: HTTP response from the server (e.g., 200 OK or resource content); no direct error indicating failure.

**Success Indicators**:
- Request sent successfully
- No immediate server error (e.g., 500) from malformed payload

### Step 4: Exfiltration Observation
procedure: [[procedures/Observe-DNS-Exfiltration-from-RCE]]

**Objective**: Confirm RCE by monitoring DNS queries to the controlled domain.

**Instructions**: Access your DNS logging service (e.g., dnsbin.zhack.ca) to watch for incoming resolution requests from the target server.

No command needed; monitor the dashboard for queries matching the payload's domain.

**Expected Output**: DNS query log entry from the target's IP attempting to resolve the malicious domain.

**Success Indicators**:
- DNS resolution observed
- Source IP matches target server

## Attack Chain Summary

### Key Achievements

1. Identified PrimeFaces 5.3 vulnerability via source code inspection
2. Generated and delivered encrypted EL payload for RCE
3. Demonstrated control via DNS exfiltration without file modifications

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
