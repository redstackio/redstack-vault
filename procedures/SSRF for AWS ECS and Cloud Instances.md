---
id: 7db0f1e5-9c8c-4928-9e27-577d91281b9c
name: SSRF for AWS ECS and Cloud Instances
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:38.247088+00:00'
updated_at: '2023-04-10T20:24:01.243541+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Cloud Service Discovery|T1526 - Cloud Service Discovery]]'
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
tags:
- '[[Server-Side Request Forgery]]'
- '[[SSRF URL for AWS ECS]]'
- '[[SSRF URL for Cloud Instances]]'
commands:
- '[[Read /proc/self/environ]]'
- '[[Retrieve credentials from AWS metadata service]]'
---

# SSRF for AWS ECS and Cloud Instances

## Summary

Server-Side Request Forgery (SSRF) is a vulnerability that allows an attacker to manipulate the server into making requests to other servers on behalf of the attacker. In this scenario, the attacker is targeting cloud instances, specifically AWS ECS. By extracting environment variables from /proc/s

## Description

# Description

Server-Side Request Forgery (SSRF) is a vulnerability that allows an attacker to manipulate the server into making requests to other servers on behalf of the attacker. In this scenario, the attacker is targeting cloud instances, specifically AWS ECS. By extracting environment variables from /proc/self/environ and retrieving AWS credentials, the attacker can gain access to the target cloud instance and its resources. The attacker can then use this access to steal data, launch further attacks, or cause damage to the target's infrastructure. This attack can be used for reconnaissance, data exfiltration, or to gain a foothold in the target's environment.

 

## Requirements

1. Access to the target server

1. Knowledge of the target's cloud infrastructure

1. Tools for extracting environment variables and retrieving AWS credentials

 

## Defense

1. Implement proper input validation to prevent SSRF attacks

1. Restrict access to sensitive data and resources

1. Monitor network traffic for suspicious activity

 

## Objectives

1. Gain access to the target cloud instance

1. Retrieve AWS credentials

1. Perform reconnaissance or data exfiltration

 

# Instructions

1. To extract environment variables from the /proc/self/environ file, follow these steps:
1. Open the /proc/self/environ file using a text editor or by running the 'cat /proc/self/environ' command.
2. The file contains a list of null-separated environment variables in the format 'VARNAME=value'.
3. Parse the file to extract the environment variables and their values.
4. Use the extracted information to further exploit the SSRF vulnerability.

 



**Code**: [[/proc/self/environ]]



> The /proc/self/environ file contains a list of environment variables for the current process. If an attacker has an SSRF vulnerability that allows them to read files on the target system, they can extract sensitive information such as API keys, database credentials, and other secrets from this file. By understanding the format of this file, an attacker can quickly extract the necessary information to further exploit the SSRF vulnerability.



**Command** ([[Read /proc/self/environ]]):

```bash
/proc/self/environ
```



2. To retrieve AWS credentials, use the following command:

 



**Code**: [[curl http://169.254.170.2/v2/credentials/<UUID>]]



> The 'curl' command is used to transfer data from or to a server, using one of the supported protocols. In this case, it is used to retrieve the AWS credentials. The 'http://169.254.170.2/v2/credentials/<UUID>' URL retrieves the credentials for the specified UUID. Replace <UUID> with the actual UUID of the instance to retrieve its credentials. This command is useful when you need to access AWS resources from within an EC2 instance without hardcoding the credentials.



**Command** ([[Retrieve credentials from AWS metadata service]]):

```bash
curl http://169.254.170.2/v2/credentials/<UUID>
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]
- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Cloud Service Discovery|T1526 - Cloud Service Discovery]]
- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

## Commands Used

- [[Read /proc/self/environ]]
- [[Retrieve credentials from AWS metadata service]]

## Tags

- [[Server-Side Request Forgery]]
- [[SSRF URL for AWS ECS]]
- [[SSRF URL for Cloud Instances]]


