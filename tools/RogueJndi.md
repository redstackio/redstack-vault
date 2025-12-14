---
id: tool-roguejndi
url: 'https://github.com/veracode-research/rogue-jndi'
tags:
  - jndi
  - ldap
  - deserialization
type: tool
verified: false
platforms:
  - Linux
  - Java
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.563Z'
validated: true
submitted: true
---
# RogueJndi

**Status**: Unverified

## Overview

RogueJndi is a Java tool for creating rogue JNDI LDAP/RMI servers to exploit JNDI injection vulnerabilities by serving malicious payloads like deserialization gadgets.

## Description

Used in offensive security to simulate LDAP references that trigger code execution on vulnerable Java applications, such as in JAAS configs. Supports custom commands and gadget chains for RCE.

## Features

- Feature 1: LDAP and RMI server implementation
- Feature 2: Customizable payloads for reverse shells
- Feature 3: Support for deserialization exploits

## Installation

### Requirements

- Java 8+

### Install Commands

```bash
# Download JAR
wget https://github.com/veracode-research/rogue-jndi/releases/download/v1.1/RogueJndi-1.1.jar
```

## Basic Usage

```bash
java -jar RogueJndi-1.1.jar --help
```

### Common Options

| Option | Description |
|--------|-------------|
| --hostname | Server hostname |
| -c | Command payload |
| --commandPort | Port for command execution |

## Examples

### Example 1: Basic Usage

```bash
java -jar RogueJndi-1.1.jar --hostname 0.0.0.0
```

### Example 2: Advanced Usage

```bash
java -jar RogueJndi-1.1.jar --hostname attacker.com -c "calc.exe"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to non-standard LDAP ports
- Java processes spawning with RogueJndi JAR
- Outbound JNDI lookups to suspicious domains

## Related Procedures


## Related Tools

- [[tools/MarshallingToolkit]]
- [[tools/ysoserial]]

## References

- https://github.com/veracode-research/rogue-jndi
- JNDI Injection resources
