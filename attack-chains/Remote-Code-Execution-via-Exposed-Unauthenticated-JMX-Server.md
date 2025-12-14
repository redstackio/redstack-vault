---
tags:
  - rce
  - jmx
  - java
  - deserialization
  - exposed-service
type: attack_chain
tools:
  - '[[tools/nmap]]'
  - '[[tools/ysoserial]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Java
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Probe-Exposed-JMX-Server]]'
  - '[[procedures/Exploit-JMX-Deserialization-RCE]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:41.546Z'
description: >-
  Attack chain exploiting an exposed unauthenticated Java JMX server on port
  555, leading to remote code execution through deserialization of untrusted
  data on decommissioned but DNS-resolvable domains.
skill_level: intermediate
impact_level: high
id: 87e8d4e0-4ed7-42a3-937b-ad1a3b6a1013
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Client Execution]]'
---
# Remote Code Execution via Exposed Unauthenticated JMX Server

Multi-stage attack chain demonstrating discovery and exploitation of an unauthenticated Java JMX server vulnerable to remote code execution via deserialization. This vulnerability was found on decommissioned domains jabber.37signals.com and jabber.basecamp.com, where lingering DNS records pointed to an old IP with an exposed JMX interface on port 555. The attack allows unauthenticated remote code execution on the target server, potentially compromising the entire infrastructure if active.

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
    A[Reconnaissance: Probe for Exposed Services] --> B[Execution: Exploit Deserialization for RCE]
    B --> C[Objective: Remote Code Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/nmap]]
- [[tools/ysoserial]]

### Target Environment

- Java-based JMX server on port 555
- Unauthenticated JMX interface
- Network access to the target IP/domain on port 555

### Initial Access Requirements

- No credentials required due to lack of authentication
- Direct network connectivity to the target port
- Resolver for DNS to IP mapping

## Detailed Attack Procedures

### Step 1: Reconnaissance - Probe for Exposed JMX Server
procedure: [[procedures/Probe-Exposed-JMX-Server]]

**Objective**: Identify if the target domain resolves to an IP with an open JMX server on port 555, confirming exposure of an unauthenticated Java Management Extensions interface.

**Instructions**: Start by resolving the domain and scanning the specific port using [[commands/nmap-jmx-probe]] to detect the JMX service:

```bash
nmap -p 555 --script=jmx-info jabber.37signals.com
```

If the port is open, attempt a basic connection test with [[commands/telnet-port-check]] to verify responsiveness:

```bash
telnet jabber.37signals.com 555
```

**Expected Output**: Nmap output showing port 555 open with JMX service details, such as "JMX service detected" or banner information indicating Java version. Telnet should connect without authentication prompts.

**Success Indicators**:
- Port 555 reported as open
- JMX banner or service identified without auth challenges

### Step 2: Execution - Exploit Deserialization for RCE
procedure: [[procedures/Exploit-JMX-Deserialization-RCE]]

**Objective**: Leverage the unauthenticated JMX interface to send a malicious serialized payload, achieving remote code execution on the target server.

**Instructions**: Generate a deserialization payload using [[tools/ysoserial]] for a CommonsCollections gadget chain, then connect via JMX and invoke the vulnerable method with [[commands/ysoserial-jmx-exploit]]:

```bash
java -jar ysoserial.jar CommonsCollections6 'touch /tmp/pwned' > payload.ser
```

Use a JMX client like jconsole or a custom script to connect and deserialize the payload on the target:

```bash
# Example using jmxterm or similar client
jmxterm -l jabber.37signals.com:555 -n -v silent -c "bean java.lang:type=Runtime;op=deserializePayload payload.ser"
```

**Expected Output**: Successful deserialization leading to command execution; check for file creation or other indicators on the target if access is available.

**Success Indicators**:
- Payload deserialized without errors
- Evidence of code execution, e.g., file created or process spawned

## Attack Chain Summary

### Key Achievements

1. Discovery of exposed JMX server via port probing on decommissioned domains
2. Confirmation of unauthenticated access enabling deserialization attacks
3. Achievement of remote code execution, compromising server control

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Exploitation for Client Execution]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
