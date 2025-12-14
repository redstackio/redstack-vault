---
id: proc-002
tags:
  - deserialization
  - snakeyaml
  - rce
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:31.224Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Identify-Unsafe-SnakeYAML-Parsing-Configuration

## Summary

This procedure details the identification of insecure SnakeYAML configurations in the Hyperledger Fabric SDK for Java, where the parser is instantiated without a SafeConstructor, enabling the deserialization of arbitrary Java types from untrusted YAML inputs and potentially leading to remote code execution.

## Description

The Hyperledger Fabric SDK for Java relies on SnakeYAML for parsing configuration files such as chaincode endorsement policies and network setups. Without a SafeConstructor, the parser can construct any Java class specified in the YAML, including those that execute code (e.g., via gadget chains). This vulnerability is client-side, requiring an attacker to supply malicious YAML to a client application using the SDK. Discovered through code review, it affects versions 2.0.0 and earlier, with low overall severity due to the lack of a remote attack vector.

## Requirements

1. Java runtime environment (JDK 8 or later) for testing.
2. Maven or Gradle for building a test project with the SDK dependency.
3. Sample YAML files for testing deserialization.

## Defense

Defensive measures and detection strategies:

- Configure SnakeYAML with SafeConstructor to limit deserializable classes.
- Use YAML schemas or validation libraries to enforce structure.
- Monitor for unexpected Java class instantiations in application logs.

## Objectives

1. Confirm absence of SafeConstructor in parsing code.
2. Demonstrate potential for arbitrary object creation.
3. Evaluate exploitation feasibility in a controlled environment.

## Instructions

### Step 1: Inspect Constructor Usage

**Context**: Analyze how SnakeYAML is initialized in vulnerable files.

In the IDE, navigate to the parsing lines (e.g., line 121 in ChaincodeCollectionConfiguration.java). Check for code like:

```java
Yaml yaml = new Yaml();
```

> Absence of SafeConstructor indicates vulnerability.

### Step 2: Create Test Environment

**Context**: Set up a minimal project to test deserialization.

Create a new Maven project and add the SDK dependency in pom.xml:

```xml
<dependency>
    <groupId>org.hyperledger.fabric</groupId>
    <artifactId>fabric-sdk-java</artifactId>
    <version>2.0.0</version>
</dependency>
```

Build with `mvn compile`.

> This replicates the SDK environment for testing.

### Step 3: Test Malicious YAML Parsing

**Context**: Attempt to parse YAML with arbitrary class references.

Create a test YAML file (malicious.yaml) with content like:

```yaml
!!java.lang.Runtime
exec: calc
```

In a test class, load and parse it using the SDK's methods, observing if arbitrary execution occurs.

> Expected: Successful instantiation without errors, confirming RCE potential on client-side.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- snakeyaml
- deserialization
- rce
