---
id: 57646bad-2e7c-4e24-8849-a5053126435c
name: Springboot-Actuator Insecure Management Interface
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:59.632410+00:00'
updated_at: '2023-04-10T20:22:29.414931+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
tags:
- '[[Insecure Management Interface]]'
- '[[Springboot-Actuator]]'
commands:
- '[[Check system health]]'
- '[[System Information]]'
---

# Springboot-Actuator Insecure Management Interface

## Summary

Spring Boot Actuator provides endpoints that allow you to monitor and interact with your application. These endpoints can be used for both diagnostic and production purposes. However, if not properly secured, an attacker could exploit these endpoints to gain sensitive information about the applicat

## Description

# Description

Spring Boot Actuator provides endpoints that allow you to monitor and interact with your application. These endpoints can be used for both diagnostic and production purposes. However, if not properly secured, an attacker could exploit these endpoints to gain sensitive information about the application, such as system configuration, environment variables, and more. An attacker could also use these endpoints to disrupt the application's normal functionality, causing a denial of service. By accessing /health and /info endpoints, an attacker can get a lot of information about the application and use it for further attacks. 

## Requirements

1. Access to the management interface of a Springboot application

## Defense

1. Properly secure the management interface by enabling authentication and authorization.

1. Restrict access to the management interface to only authorized personnel.

1. Regularly monitor the logs and network traffic for any suspicious activity.

## Objectives

1. To obtain sensitive information about the application

1. To disrupt the application's normal functionality

# Instructions

1. Send an HTTP GET request to the /health endpoint of the target application.

**Code**: [[/health]]

> This endpoint returns the health status of the application. An attacker can use this information to determine if the application is vulnerable to certain attacks or not. For example, if the health status is 'DOWN', it could indicate that the application is experiencing issues and may be more susceptible to a denial of service attack.

**Command** ([[Check system health]]):

```bash
/health
```

2. Send an HTTP GET request to the /info endpoint of the target application.

**Code**: [[/info]]

> This endpoint returns information about the application, such as its name, version, and environment variables. An attacker can use this information to better understand the target environment and tailor their attack accordingly.

**Command** ([[System Information]]):

```bash
systeminfo
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]

## Commands Used

- [[Check system health]]
- [[System Information]]

## Tags

- [[Insecure Management Interface]]
- [[Springboot-Actuator]]
