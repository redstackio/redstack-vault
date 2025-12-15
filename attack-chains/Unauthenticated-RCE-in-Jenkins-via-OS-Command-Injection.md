---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: Unauthenticated RCE in Jenkins via OS Command Injection
tags:
  - rce
  - jenkins
  - command-injection
  - unauthenticated
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Jenkins-Unauthenticated-RCE]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:36.890Z'
description: >-
  Exploits unauthenticated OS command injection vulnerabilities in a publicly
  accessible Jenkins instance to achieve remote code execution on the server.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# Unauthenticated RCE in Jenkins via OS Command Injection

Multi-stage attack chain demonstrating exploitation of unauthenticated OS command injection in Jenkins to achieve remote code execution.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Public Jenkins] --> B[Execute Arbitrary Commands]
    B --> C[RCE Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl)

### Target Environment

- Publicly accessible Jenkins instance on port 80/443
- Web platform with Jenkins CI/CD server
- No authentication required

### Initial Access Requirements

- Internet access to the target URL (e.g., https://djangoci.com/)
- No credentials needed due to unauthenticated nature
- Basic knowledge of Jenkins endpoints

## Detailed Attack Procedures

### Step 1: Exploit Unauthenticated RCE
procedure: [[procedures/Exploit-Jenkins-Unauthenticated-RCE]]

**Objective**: Leverage OS command injection vulnerabilities in Jenkins to execute arbitrary commands on the server without authentication.

**Instructions**: Identify the vulnerable Jenkins instance and send a crafted payload to a susceptible endpoint, such as a build trigger or script console, exploiting CVEs like CVE-2018-1000861, CVE-2019-1003005, or CVE-2019-1003029. Use [[commands/curl-jenkins-rce-payload]] to inject and execute a command like 'id' to verify RCE:

```bash
curl -X POST 'https://djangoci.com/scriptText' --data 'import subprocess; subprocess.call("id", shell=True)'
```

Monitor the response or server logs for command output. If successful, escalate to more destructive actions.

**Expected Output**: Command execution result, e.g., server returns output like 'uid=1000(jenkins) gid=1000(jenkins)' or evidence of execution in Jenkins logs.

**Success Indicators**:
- Arbitrary command output visible in response or logs
- No authentication prompt during access
- Server-side effects observable (e.g., file creation or process listing)

## Attack Chain Summary

### Key Achievements

1. Gained unauthenticated access to execute OS commands on the Jenkins server
2. Demonstrated critical impact allowing full server compromise
3. Highlighted risks of exposed CI/CD tools without proper security controls

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
