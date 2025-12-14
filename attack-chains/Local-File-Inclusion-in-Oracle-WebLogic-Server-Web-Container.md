---
id: ac-lfi-weblogic-2022
tags:
  - lfi
  - oracle-weblogic
  - cve-2022-21371
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-LFI-in-Oracle-WebLogic-Server]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:21.635Z'
description: >-
  An unauthenticated attacker exploits an LFI vulnerability in the Oracle
  WebLogic Server Web Container to read sensitive local files, potentially
  gaining access to critical data or server control.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Local File Inclusion in Oracle WebLogic Server Web Container

Multi-stage attack chain demonstrating exploitation of CVE-2022-21371 for unauthorized file access in Oracle WebLogic Server.

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
    A[Discovery] --> B[Exploitation]
    B --> C[Data Exfiltration]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Oracle WebLogic Server (affected versions: specific releases as per CVE-2022-21371)
- Web platform with HTTP access to the Web Container
- No authentication required

### Initial Access Requirements

- Network access to the WebLogic server port (typically 7001 or 80/443)
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Vulnerability Discovery

procedure: [[procedures/Exploit-LFI-in-Oracle-WebLogic-Server]]

**Objective**: Identify the LFI vulnerability in the Web Container by probing for file inclusion behaviors.

**Instructions**: Send a test HTTP request using [[commands/curl-lfi-probe]] to attempt inclusion of a known file like /etc/passwd. Target the vulnerable endpoint in the WebLogic Web Container, often involving parameters like 'file' or 'include' in JSP or servlet paths.

```bash
curl "http://target-weblogic:7001/vulnerable-endpoint?file=../../../etc/passwd" -v
```

**Expected Output**: Response containing contents of /etc/passwd or error indicating traversal success.

**Success Indicators**:
- File contents leaked in response body
- HTTP 200 with readable data

### Step 2: Exploitation and Exfiltration

procedure: [[procedures/Exploit-LFI-in-Oracle-WebLogic-Server]]

**Objective**: Read sensitive files such as configuration files, data stores, or application secrets to achieve unauthorized access.

**Instructions**: Escalate by targeting critical files like weblogic.xml or database configs using path traversal. Use [[commands/curl-lfi-exploit]] to include and retrieve the file.

```bash
curl "http://target-weblogic:7001/vulnerable-endpoint?file=../../../opt/oracle/weblogic/config.xml" -o stolen-config.xml
```

**Expected Output**: Downloaded file with server configuration or sensitive data.

**Success Indicators**:
- Successful download of target file
- Exposure of credentials or data store contents
- Potential path to server control if combined with other vulns

## Attack Chain Summary

### Key Achievements

1. Unauthenticated access to local files via HTTP
2. Reading of critical configuration and data files
3. Potential for full server compromise through data exposure

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
