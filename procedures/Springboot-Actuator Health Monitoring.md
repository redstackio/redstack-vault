---
id: 74fa112f-e6a5-48f4-b9bf-412ae08b652a
name: Springboot-Actuator Health Monitoring
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:59.604670+00:00'
updated_at: '2023-04-10T20:22:30.592635+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Automated Exfiltration|T1020 - Automated Exfiltration]]'
- '[[Commonly Used Port|T1043 - Commonly Used Port]]'
tags:
- '[[Insecure Management Interface]]'
- '[[Springboot-Actuator]]'
commands:
- '[[Health Check]]'
---

# Springboot-Actuator Health Monitoring

## Summary

Spring Boot Actuator provides an endpoint /health that can be used to monitor the health of the application. This endpoint can be accessed by anyone who has network access to the application. Attackers can use this endpoint to gather information about the application and its environment. They can a

## Description

# Description

Spring Boot Actuator provides an endpoint /health that can be used to monitor the health of the application. This endpoint can be accessed by anyone who has network access to the application. Attackers can use this endpoint to gather information about the application and its environment. They can also use it to identify vulnerabilities and potential targets for further attacks. The business value of this procedure is that it allows the attacker to gain a foothold in the target environment and potentially move on to more critical systems.

## Requirements

1. Network access to the application

## Defense

1. Disable or restrict access to the /health endpoint

1. Implement authentication and authorization for accessing the /health endpoint

1. Monitor access to the /health endpoint for suspicious activity

## Objectives

1. Gather information about the application and its environment

1. Identify vulnerabilities and potential targets for further attacks

# Instructions

1. Send an HTTP GET request to the /health endpoint

**Code**: [[/health]]

> The /health endpoint can be accessed by sending an HTTP GET request to the endpoint URL. The response will contain a JSON object with information about the health of the application.

**Command** ([[Health Check]]):

```bash
/health
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Automated Exfiltration|T1020 - Automated Exfiltration]]
- [[Commonly Used Port|T1043 - Commonly Used Port]]

## Commands Used

- [[Health Check]]

## Tags

- [[Insecure Management Interface]]
- [[Springboot-Actuator]]
