---
tags:
  - ntlm
  - information-disclosure
  - eternalblue
  - rce
  - windows-auth
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Metasploit]]'
tactics:
  - '[[Reconnaissance]]'
  - '[[Discovery]]'
  - '[[Execution]]'
commands:
  - '[[commands/ntlm-trigger-get-request]]'
platforms:
  - Web
  - Windows
complexity: medium
procedures:
  - '[[procedures/Trigger-NTLM-Challenge-via-HTTP-Request]]'
  - '[[procedures/Decode-NTLM-Challenge-for-Internal-Info]]'
  - '[[procedures/Repeat-NTLM-Extraction-on-Additional-Endpoints]]'
  - '[[procedures/Analyze-for-EternalBlue-Vulnerability]]'
step_count: 4
techniques:
  - '[[Gather Victim Network Information]]'
  - '[[Exploitation of Remote Services]]'
description: >-
  Exploits misconfigured NTLM authentication on internal web servers to disclose
  sensitive network details, enabling identification of unpatched Windows
  systems vulnerable to EternalBlue remote code execution.
skill_level: intermediate
impact_level: high
id: 8d0677a6-6d07-49d3-b791-ad0d01a4366b
created_at: '2025-12-14T17:31:19.118Z'
updated_at: '2025-12-14T17:31:19.118Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Discovery]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Gather Victim Network Information]]'
  - '[[Exploitation of Remote Services]]'
---
# NTLM Authentication Misconfiguration Leading to Internal Network Disclosure and EternalBlue RCE

Multi-stage attack chain demonstrating exploitation of hidden NTLM authentication on MTN Group's internal web servers to extract sensitive internal information, revealing vulnerable Windows systems for potential remote code execution via EternalBlue.

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
    A[Trigger NTLM Challenge] --> B[Decode Internal Info]
    B --> C[Repeat on Endpoints]
    C --> D[Analyze for RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- [[tools/Metasploit]]

### Target Environment

- Windows Server 2012 R2 with IIS and Windows Authentication enabled
- Protected web endpoints (e.g., internal blogs)
- Network access to internal servers (e.g., ports 80/443 for HTTP/HTTPS)

### Initial Access Requirements

- No credentials required due to misconfiguration
- Direct network connectivity to target web servers
- No prior access needed beyond reachability

## Detailed Attack Procedures

### Step 1: Trigger NTLM Challenge
procedure: [[procedures/Trigger-NTLM-Challenge-via-HTTP-Request]]

**Objective**: Invoke hidden NTLM authentication to receive a challenge response without a login prompt.

**Instructions**: Use Burp Suite to intercept and send a crafted HTTP GET request to a protected endpoint, including an Authorization: NTLM header to start the handshake.

Execute [[commands/ntlm-trigger-get-request]]:

```bash
GET /fr/Pages/ HTTP/1.1
Host: target-internal-server
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Authorization: NTLM
```

**Expected Output**: HTTP response with WWW-Authenticate: NTLM header containing an encoded challenge.

**Success Indicators**:
- Presence of WWW-Authenticate header in response
- No login prompt triggered

### Step 2: Decode Internal Info
procedure: [[procedures/Decode-NTLM-Challenge-for-Internal-Info]]

**Objective**: Extract domain names, computer names, DNS details, and OS versions from the NTLM challenge.

**Instructions**: Capture the response in Burp Suite and use its NTLM decoder to parse the challenge blob.

**Expected Output**: Decoded details such as Target: MTNICT, MsvAvNbComputerName: ZACNVSPRWSBS01, MsvAvDnsDomainName: mtnict.local, OS: Windows Server 2012 R2.

**Success Indicators**:
- Internal hostnames and domains revealed
- OS version information obtained

### Step 3: Repeat on Additional Endpoints
procedure: [[procedures/Repeat-NTLM-Extraction-on-Additional-Endpoints]]

**Objective**: Gather more internal information from other protected paths to map the network.

**Instructions**: Send similar requests to additional blog endpoints using Burp Suite, then decode responses.

Execute a variant of [[commands/ntlm-trigger-get-request]] targeting another path:

```bash
GET /blog/protected HTTP/1.1
Host: another-internal-server
Authorization: NTLM
```

**Expected Output**: Additional decoded info like Target: MTNGROUPSA, MsvAvNbComputerName: PSWSPEMVA21, MsvAvDnsDomainName: mtn.co.za.

**Success Indicators**:
- Multiple internal systems identified
- Broader network topology exposed

### Step 4: Analyze for RCE
procedure: [[procedures/Analyze-for-EternalBlue-Vulnerability]]

**Objective**: Identify exploitable vulnerabilities like MS17-010 based on disclosed OS details.

**Instructions**: Use the extracted info to check against known vulnerabilities in Metasploit without executing.

**Expected Output**: Confirmation of Windows Server 2012 R2 vulnerability to EternalBlue (CVE-2017-0144).

**Success Indicators**:
- Vulnerable hosts pinpointed
- Potential for SMB RCE assessed

## Attack Chain Summary

### Key Achievements

1. Unauthorized disclosure of internal NTLM details without authentication
2. Mapping of multiple Windows servers and domains
3. Identification of unpatched systems for EternalBlue exploitation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Gather Victim Network Information]] Gather Victim Network Information
- [[Exploitation of Remote Services]] Exploitation of Remote Services

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Discovery]] Discovery
- [[Execution]] Execution

---
*Last updated: 2023-10-01*
