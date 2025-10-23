---
id: c7287fd1-a5a9-4137-9773-200949ae791b
name: Springboot-Actuator RCE via /env
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:59.691691+00:00'
updated_at: '2023-04-10T20:22:30.949042+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
tags:
- '[[Insecure Management Interface]]'
- '[[Remote Code Execution via `/env`]]'
- '[[Springboot-Actuator]]'
- '[[Steps]]'
---

# Springboot-Actuator RCE via /env

## Summary

Spring Boot Actuator is a sub-project of Spring Boot that adds management endpoints to the application. One of these endpoints is `/env` which displays the current environment properties. However, if the application is vulnerable to Insecure Management Interface, an attacker can execute arbitrary c

## Description

# Description

Spring Boot Actuator is a sub-project of Spring Boot that adds management endpoints to the application. One of these endpoints is `/env` which displays the current environment properties. However, if the application is vulnerable to Insecure Management Interface, an attacker can execute arbitrary code via this endpoint. The attacker can craft a malicious payload and send it as a value for an environment variable. When the `/env` endpoint is accessed, the payload is executed. The impact of this vulnerability could be severe, leading to complete compromise of the application and underlying infrastructure.

Technical Explanation: The vulnerability exists due to the fact that Spring Boot Actuator allows the execution of arbitrary code via the `/env` endpoint. The endpoint is used to display the current environment properties of the application. However, if the application is vulnerable to Insecure Management Interface, an attacker can send a malicious payload as a value for an environment variable. When the `/env` endpoint is accessed, the payload is executed.

Business Value: An attacker exploiting this vulnerability can gain complete control over the application and underlying infrastructure, leading to data theft, data loss, and system downtime.

 

## Requirements

1. Access to the target system

1. Knowledge of the target application's vulnerabilities

 

## Defense

1. Ensure that the application is not vulnerable to Insecure Management Interface by following secure coding practices and regular security assessments

1. Implement network segmentation and access controls to limit access to the application and underlying infrastructure

1. Monitor network traffic and system logs for any suspicious activity

 

## Objectives

1. Execute arbitrary code on the target system

1. Compromise the target application and underlying infrastructure

 

# Instructions

1. Replace the `COMMAND HERE` placeholder with the actual command to be executed.

 



**Code**: [[public AwesomeScriptEngineFactory() {
    try {
  ]]



> The payload is crafted in the form of a Java script that uses the `Runtime.getRuntime().exec()` method to execute the specified command. The payload is then sent as a value for an environment variable. When the `/env` endpoint is accessed, the payload is executed and the specified command is executed on the target system.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]

## Tags

- [[Insecure Management Interface]]
- [[Remote Code Execution via `/env`]]
- [[Springboot-Actuator]]
- [[Steps]]


