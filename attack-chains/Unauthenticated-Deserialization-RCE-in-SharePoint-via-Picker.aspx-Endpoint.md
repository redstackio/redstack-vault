---
id: ac-unauth-deserial-rce-sharepoint-picker
tags:
  - rce
  - deserialization
  - sharepoint
  - microsoft
  - cve-2019-0604
  - command-injection
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Vulnerable-SharePoint-Endpoint]]'
  - '[[procedures/Exploit-Deserialization-RCE-CVE-2019-0604]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:54.300Z'
description: >-
  Multi-stage attack exploiting CVE-2019-0604 in Microsoft SharePoint to achieve
  unauthenticated remote code execution through unsafe deserialization in the
  picker.aspx endpoint.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Client Execution]]'
---
# Unauthenticated Deserialization RCE in SharePoint via Picker.aspx Endpoint

Multi-stage attack chain demonstrating exploitation of CVE-2019-0604 in Microsoft SharePoint, allowing unauthenticated attackers to inject and execute arbitrary OS commands on the server via the publicly accessible picker.aspx endpoint.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discovery of Vulnerable Endpoint] --> B[Deserialization Payload Injection and RCE]
    B --> C[Server Compromise]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser for endpoint discovery
- ysoserial.net for payload generation
- curl for payload delivery

### Target Environment

- Microsoft SharePoint server (version affected by CVE-2019-0604)
- Web platform with HTTP/HTTPS access
- No authentication required for the picker.aspx endpoint

### Initial Access Requirements

- Public network access to the target SharePoint instance
- No credentials needed due to unauthenticated endpoint
- Knowledge of SharePoint directory structure (_layouts/15/)

## Detailed Attack Procedures

### Step 1: Discover Vulnerable Endpoint
procedure: [[procedures/Discover-Vulnerable-SharePoint-Endpoint]]

**Objective**: Identify the publicly accessible picker.aspx endpoint in the SharePoint application that is vulnerable to deserialization attacks.

**Instructions**: Navigate to the target SharePoint site's standard layout path using a web browser or reconnaissance tool. For example, access https://target.com/_layouts/15/picker.aspx and inspect the page source or interact with it to confirm it's unauthenticated and processes user input.

**Expected Output**: Confirmation of the endpoint loading without authentication, revealing potential input fields for serialized data.

**Success Indicators**:
- Endpoint accessible without login
- Page reveals SharePoint version or deserialization-related behaviors

### Step 2: Exploit Deserialization RCE
procedure: [[procedures/Exploit-Deserialization-RCE-CVE-2019-0604]]

**Objective**: Craft and deliver a malicious serialized payload to trigger remote code execution on the server, allowing arbitrary command injection.

**Instructions**: Generate a deserialization gadget chain payload using ysoserial targeting the vulnerable .NET deserializer in SharePoint. Then, send the payload via HTTP POST to the picker.aspx endpoint using curl. For validation, execute a simple command like 'ping' to an attacker-controlled server to confirm RCE.

**Expected Output**: Server executes the injected command, such as a ping response received on the attacker's side or evidence of command output in server logs.

**Success Indicators**:
- Ping or test command response from target server
- Arbitrary command execution confirmed (e.g., file creation or network callback)

## Attack Chain Summary

### Key Achievements

1. UnaAuthenticated access to critical SharePoint endpoint
2. Successful deserialization leading to full RCE
3. Potential for server compromise, data exfiltration, or lateral movement

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Exploitation for Client Execution]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
