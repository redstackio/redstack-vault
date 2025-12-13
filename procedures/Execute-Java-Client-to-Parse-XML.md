---
tags:
  - java-execution
  - xxe
type: procedure
tools:
  - '[[tools/Java-JDK]]'
tactics:
  - '[[Lateral Movement]]'
commands:
  - '[[commands/run-java-client]]'
platforms:
  - Java
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Service Exhaustion Flood]]'
id: 0d56bcd3-ce8d-4739-ae0f-0f6b8d19d7fb
created_at: '2025-12-13T09:00:27.234Z'
updated_at: '2025-12-13T09:00:27.234Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Execute Java Client to Parse XML

## Summary

This procedure runs a Java client program to parse malicious XML using the vulnerable Pippo JAXB engine, triggering the entity expansion.

## Description

By supplying the XML to JaxbEngine.fromString(), the unsafe parsing with DTD enabled causes recursive expansion. This is demonstrated in a simple Java program acting as a client.

## Requirements

1. Java JDK installed
2. Pippo JAXB library in classpath
3. Malicious XML payload prepared

## Defense

Defensive measures and detection strategies:

- Bound JVM memory limits
- Use secure XML parsers with DTD disabled

## Objectives

1. Load and parse the XML
2. Trigger the vulnerability
3. Initiate memory consumption

## Instructions

### Step 1: Compile Java Client

**Context**: Prepare the Java code that loads XML and calls fromString().

Compile the client code with JAXB dependencies.

> Ensure Person.class is defined for unmarshalling.

### Step 2: Run the Client

**Context**: Execute the program with the payload.

Execute [[commands/run-java-client]] to run the program:

```bash
java -cp .:pippo-jaxb.jar ClientProgram malicious.xml Person.class
```

> This loads the payload and parses it.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques

- [[Service Exhaustion Flood]]

## Commands Used

- [[commands/run-java-client]]

## Tools Used

- [[tools/Java-JDK]]

## Tags

- [[java-execution]]
- [[xxe]]
