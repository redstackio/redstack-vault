---
id: 2fc1b204-742b-41b5-9df2-5cde71aeb3d4
name: Remote Code Execution via Springboot-Actuator /env
type: procedure
verified: true
submitted: true
created_at: '2023-04-06T03:55:59.666424+00:00'
updated_at: '2023-05-26T18:52:37.745092+00:00'
tags:
- '[[Insecure Management Interface]]'
- '[[Remote Code Execution via `/env`]]'
- '[[Springboot-Actuator]]'
- '[[Steps]]'
commands:
- '[[Change directory to yaml-payload]]'
- '[[Clone yaml-payload repository]]'
- '[[Compile AwesomeScriptEngineFactory.java]]'
- '[[Create jar file]]'
---

# Remote Code Execution via Springboot-Actuator /env

**Status**: ✓ Verified

## Summary

The Springboot-Actuator is a management interface that provides a number of endpoints for monitoring and managing a Spring Boot application. One of these endpoints is `/env` which is used to view the current environment properties. However, this endpoint is susceptible to a deserialization attack v

## Description

# Description

The Springboot-Actuator is a management interface that provides a number of endpoints for monitoring and managing a Spring Boot application. One of these endpoints is `/env` which is used to view the current environment properties. However, this endpoint is susceptible to a deserialization attack via the SnakeYAML library used to parse the YAML formatted properties. An attacker can use this vulnerability to execute arbitrary code on the target system.

Technical Description: An attacker can craft a malicious YAML file that contains a specially crafted payload in one of the properties. When the target system loads this file via the `/env` endpoint, the SnakeYAML library will deserialize the payload and execute the attacker's code.

Business Value: An attacker can use this vulnerability to gain complete control of the target system, allowing them to steal sensitive data, install malware, or use the system as a jumping-off point for further attacks.

## Requirements

1. Access to the Springboot-Actuator endpoint

## Defense

1. Ensure that the Springboot-Actuator endpoint is not exposed to the public internet.

1. Implement proper input validation and output encoding to prevent deserialization attacks.

1. Regularly update the SnakeYAML library to the latest version to patch any known vulnerabilities.

## Objectives

1. Execute arbitrary code on the target system

# Instructions

1. Execute the following commands:

**Code**: [[git clone https://github.com/artsploit/yaml-payloa]]

> 
- `git clone https://github.com/artsploit/yaml-payload.git`: Clone the yaml-payload repository from GitHub.
- `cd yaml-payload`: Change into the yaml-payload directory.
- `javac src/artsploit/AwesomeScriptEngineFactory.java`: Compile the AwesomeScriptEngineFactory.java class.
- `jar -cvf yaml-payload.jar -C src/ .`: Create a JAR file containing the compiled class.

**Command** ([[Clone yaml-payload repository]]):

```bash
git clone https://github.com/artsploit/yaml-payload.git
```

**Command** ([[Change directory to yaml-payload]]):

```bash
cd yaml-payload
```

**Command** ([[Compile AwesomeScriptEngineFactory.java]]):

```bash
javac src/artsploit/AwesomeScriptEngineFactory.java
```

**Command** ([[Create jar file]]):

```bash
jar -cvf yaml-payload.jar -C src/ .
```

## Commands Used

- [[Change directory to yaml-payload]]
- [[Clone yaml-payload repository]]
- [[Compile AwesomeScriptEngineFactory.java]]
- [[Create jar file]]

## Tags

- [[Insecure Management Interface]]
- [[Remote Code Execution via `/env`]]
- [[Springboot-Actuator]]
- [[Steps]]
