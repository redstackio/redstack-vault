---
tags:
  - setup
  - tooling
  - java
type: procedure
tools:
  - '[[tools/Git]]'
  - '[[tools/Maven]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/git-clone-ysoserial]]'
  - '[[commands/cd-ysoserial]]'
  - '[[commands/mvn-build-ysoserial]]'
  - '[[commands/cd-target]]'
verified: false
platforms:
  - Linux
  - Java
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Audio Capture]]'
updated_at: '2025-12-14T17:23:27.271Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 96669a4a-6373-4ba1-b703-2da239ccb5c5
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Audio Capture]]'
---
---

# Setup-Ysoserial-Tool

## Summary

This procedure sets up the ysoserial tool by cloning its repository and building it with Maven, preparing it for generating Java deserialization payloads used in exploiting vulnerabilities like the one in Oracle PeopleSoft.

## Description

Ysoserial is a proof-of-concept tool for generating payloads that exploit unsafe Java object deserialization. In this attack scenario, it is used against a DoD web system's PeopleSoft platform where the /monitor endpoint deserializes untrusted data via readObject() without validation. Prerequisites include Java and Maven installed on a Linux environment with internet access.

## Requirements

1. Java Development Kit (JDK) installed
2. Maven build tool installed
3. Git installed
4. Internet access for cloning repository

## Defense

Defensive measures and detection strategies:

- Monitor for unusual git clones or Maven builds in environments (e.g., via endpoint detection tools)
- Block access to known exploit tool repositories in corporate networks

## Objectives

1. Acquire ysoserial source code
2. Compile into executable JAR
3. Prepare for payload generation

## Instructions

### Step 1: Clone Ysoserial Repository

**Context**: Download the ysoserial tool from GitHub to obtain the source for building payloads.

**Command** ([[commands/git-clone-ysoserial]]):
```bash
git clone https://github.com/frohoff/ysoserial.git
```

> Clones the repository into a local 'ysoserial' directory. Expected output: Progress messages ending with 'Cloning into 'ysoserial'...'

### Step 2: Navigate to Directory

**Context**: Change into the cloned directory to run the build.

**Command** ([[commands/cd-ysoserial]]):
```bash
cd ysoserial
```

> Changes working directory. Expected output: Prompt updates to ysoserial/.

### Step 3: Build with Maven

**Context**: Compile and package the tool, skipping tests for speed.

**Command** ([[commands/mvn-build-ysoserial]]):
```bash
mvn clean package –DskipTests
```

> Builds the JAR. Expected output: '[INFO] BUILD SUCCESS' and JAR in target/.

### Step 4: Navigate to Target Directory

**Context**: Access the built artifacts.

**Command** ([[commands/cd-target]]):
```bash
cd target
```

> Changes to target/. Expected output: Prompt updates.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Audio Capture]] Audio Capture (adapted for tool acquisition; primarily tooling setup)

### Sub-Techniques


## Commands Used

- [[commands/git-clone-ysoserial]]
- [[commands/cd-ysoserial]]
- [[commands/mvn-build-ysoserial]]
- [[commands/cd-target]]

## Tools Used

- [[tools/Git]]
- [[tools/Maven]]

## Tags

- setup
- tooling
- java
