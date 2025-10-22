---
id: 4478d6f9-3c4a-4103-9662-a3838c4c99df
name: Windows Service Persistence with Calculator
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:27.968713+00:00'
updated_at: '2023-04-10T20:37:24.622346+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Service Execution|T1035 - Service Execution]]'
- '[[Service Registry Permissions Weakness|T1058 - Service Registry Permissions Weakness]]'
tags:
- '[[Serviceland]]'
- '[[Windows - Persistence]]'
- '[[Windows Service]]'
---

# Windows Service Persistence with Calculator

## Summary

Windows Service Persistence with Calculator is a technique used by attackers to maintain access to a compromised system. This technique involves creating a Windows service that runs a malicious executable, which is often disguised as a legitimate system process. Once the service is installed, it wi

## Description

# Description

Windows Service Persistence with Calculator is a technique used by attackers to maintain access to a compromised system. This technique involves creating a Windows service that runs a malicious executable, which is often disguised as a legitimate system process. Once the service is installed, it will run automatically whenever the system starts up, providing the attacker with persistent access to the system. This technique can be used to maintain a foothold on a system, exfiltrate data, or carry out other malicious activities.

Technical Explanation:
This technique involves using the 'sc' command to create a new Windows service, and the 'cmd.exe' command to execute a malicious executable. The service is created with a specific name, description, and startup type, and is configured to run the malicious executable when the system starts up. The attacker can then use the 'sc' command to start, stop, or delete the service as needed. 

Business Value:
This technique can be used by attackers to maintain persistent access to a compromised system, allowing them to exfiltrate sensitive data, install additional malware, or carry out other malicious activities. By using a Windows service to maintain access, the attacker can ensure that their access to the system remains undetected for an extended period of time.

## Requirements

1. Administrator-level access to the compromised system

1. The 'sc' command must be available on the system

1. The malicious executable must be present on the system

## Defense

1. Implement and enforce the principle of least privilege to restrict access to critical systems and services

1. Regularly monitor system logs and network traffic for signs of suspicious activity

1. Use endpoint protection software to detect and prevent the installation of malicious services

## Objectives

1. To maintain persistent access to a compromised system

1. To exfiltrate sensitive data

1. To install additional malware

1. To carry out other malicious activities

# Instructions

1. This command adds persistence to a service by executing the Windows calculator every time the service is started. The command uses SharPersist, a tool that helps in persistence techniques.

**Code**: [[SharPersist -t service -c "C:\Windows\System32\cmd]]

> -t: Specifies the type of persistence technique to use. In this case, it's 'service'.
-c: Specifies the command to execute. In this case, it's 'C:\Windows\System32\cmd.exe' which opens the command prompt.
-a: Specifies the arguments to the command. In this case, it's '/c calc.exe' which executes the Windows calculator.
-n: Specifies the name of the service. In this case, it's 'Some Service'.
-m: Specifies the mode of the SharPersist tool. In this case, it's 'add' which adds the persistence.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Service Execution|T1035 - Service Execution]]
- [[Service Registry Permissions Weakness|T1058 - Service Registry Permissions Weakness]]

## Tags

- [[Serviceland]]
- [[Windows - Persistence]]
- [[Windows Service]]
