---
id: uuid-1
tags:
  - hive
  - jdbc
  - setup
type: procedure
tools:
  - '[[tools/Gradle]]'
  - '[[tools/javac]]'
  - '[[tools/DataGrip]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/gradle-getdeps]]'
  - '[[commands/javac-queryhive]]'
verified: false
platforms:
  - Linux
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:55.646Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Select-and-Configure-Hive-JDBC-Client

## Summary

This procedure prepares a compatible JDBC client for connecting to Apache Hive version 1.1.0, avoiding protocol errors, either via a custom Java POC or tools like DataGrip, enabling subsequent database interactions in the attack chain.

## Description

In the context of exploiting an open Apache Hive server in a GCP environment, selecting the right client is crucial due to version-specific compatibility. This involves downloading Hive JDBC and Hadoop dependencies using Gradle, compiling a custom Java client, or configuring a GUI tool like DataGrip. The target is an unauthenticated Hive instance on port 10000, allowing anonymous SQL execution.

## Requirements

1. Java Development Kit (JDK) installed
2. Gradle build tool available
3. Access to the target's public IP on port 10000
4. build.gradle file with Hive 1.1.0 and Hadoop 1.1.0 dependencies

## Defense

Defensive measures and detection strategies:

- Restrict database ports with firewalls (e.g., GCP VPC rules)
- Monitor for unusual JDBC connection attempts in cloud logs
- Enforce authentication on all database services

## Objectives

1. Establish a functional client for Hive interaction
2. Avoid version mismatches causing connection failures
3. Prepare for SQL payload execution

## Instructions

### Step 1: Download Dependencies

**Context**: Use Gradle to fetch required JARs for the Hive JDBC driver.

**Command** ([[commands/gradle-getdeps]]):
```bash
gradle getDeps
```

> This custom task copies Hive JDBC 1.1.0 and Hadoop client JARs to a 'runtime/' directory, creating the classpath needed for execution.

### Step 2: Compile Custom Java Client

**Context**: Build the QueryHive.java source file that handles JDBC connections and query execution.

**Command** ([[commands/javac-queryhive]]):
```bash
javac QueryHive.java
```

> Compiles the class using imports like org.apache.hive.jdbc.HiveDriver, generating QueryHive.class for running test and exploit queries.

### Step 3: Configure DataGrip Alternative

**Context**: For GUI-based access, add the Hive JDBC driver in DataGrip.

**Instructions**: Download DataGrip, create a new driver for Hive 1.1.0, and set URI format to jdbc:hive2://host:10000.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/gradle-getdeps]]
- [[commands/javac-queryhive]]

## Tools Used

- [[tools/Gradle]]
- [[tools/javac]]
- [[tools/DataGrip]]

## Tags

- [[hive]]
- [[jdbc]]
- [[setup]]
