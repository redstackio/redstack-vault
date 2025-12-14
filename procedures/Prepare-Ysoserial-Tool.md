---
id: proc-prepare-ysoserial
tags:
  - ysoserial
  - setup
type: procedure
tools:
  - '[[tools/git]]'
  - '[[tools/mvn]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/git-clone-ysoserial]]'
  - '[[commands/cd-ysoserial]]'
  - '[[commands/mvn-build-ysoserial]]'
  - '[[commands/cd-target]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Audio Capture]]'
updated_at: '2025-12-14T17:23:27.740Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Audio Capture]]'
---
# Prepare-Ysoserial-Tool

## Summary

This procedure sets up the ysoserial tool by cloning its GitHub repository and building it with Maven, enabling the generation of Java deserialization payloads for exploiting vulnerabilities like CWE-502 in Java-based applications.

## Description

Ysoserial is a proof-of-concept tool for generating serialized Java payloads that exploit unsafe deserialization. In this attack on the Oracle PeopleSoft monitor service, it is used to create gadget chains for RCE or DoS. The procedure requires Git and Maven installed on a Linux environment with Java JDK. Prerequisites include internet access for cloning and no prior ysoserial installation.

## Requirements

1. Linux system with Git and Maven installed
2. Java JDK (version 8 or compatible with target)
3. Internet connectivity for GitHub access

## Defense

Defensive measures and detection strategies:

- Monitor for unusual Git clones or Maven builds in build logs
- Restrict outbound connections to GitHub in secure environments
- Use containerized builds to isolate tool preparation

## Objectives

1. Obtain ysoserial source code
2. Compile into executable JAR
3. Prepare for payload generation

## Instructions

### Step 1: Clone Ysoserial Repository

**Context**: Download the ysoserial source from GitHub to start setup.

**Command** ([[commands/git-clone-ysoserial]]):
```bash
git clone https://github.com/frohoff/ysoserial.git
```

> Clones the repository; expected output is a local ysoserial directory with source files.

### Step 2: Navigate to Directory

**Context**: Enter the cloned directory for building.

**Command** ([[commands/cd-ysoserial]]):
```bash
cd ysoserial
```

> Changes working directory; verify with pwd showing /path/to/ysoserial.

### Step 3: Build with Maven

**Context**: Compile and package the tool, skipping tests for speed.

**Command** ([[commands/mvn-build-ysoserial]]):
```bash
mvn clean package –DskipTests
```

> Builds the JAR; success indicated by 'BUILD SUCCESS' message.

### Step 4: Access Build Output

**Context**: Move to the target directory containing the JAR.

**Command** ([[commands/cd-target]]):
```bash
cd target
```

> Directory change; ls should show ysoserial-0.0.6-SNAPSHOT-all.jar.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Audio Capture]]

### Sub-Techniques


## Commands Used

- [[commands/git-clone-ysoserial]]
- [[commands/cd-ysoserial]]
- [[commands/mvn-build-ysoserial]]
- [[commands/cd-target]]

## Tools Used

- [[tools/git]]
- [[tools/mvn]]

## Tags

- ysoserial
- setup
