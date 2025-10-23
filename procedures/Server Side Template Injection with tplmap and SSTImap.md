---
id: 642fdcb3-9f4c-410b-86eb-cee139ccaaaa
name: Server Side Template Injection with tplmap and SSTImap
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:38.844369+00:00'
updated_at: '2023-04-10T20:23:28.887650+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Template Injection|T1221 - Template Injection]]'
tags:
- '[[Server Side Template Injection]]'
- '[[Tools]]'
commands:
- '[[Directory Traversal Vulnerability Check]]'
- '[[HTTP Authorization Header Injection Vulnerability Check]]'
- '[[Jade Template Injection Vulnerability Check]]'
- '[[tplmap - inject parameter]]'
- '[[tplmap - inject parameter with level and extension]]'
- '[[tplmap - os-shell]]'
---

# Server Side Template Injection with tplmap and SSTImap

## Summary

Server Side Template Injection is a vulnerability that occurs when user input is embedded in a server-side template, which is then executed by the server. Attackers can exploit this vulnerability to execute arbitrary code on the server. The tplmap and SSTImap tools are designed to automate the expl

## Description

# Description

Server Side Template Injection is a vulnerability that occurs when user input is embedded in a server-side template, which is then executed by the server. Attackers can exploit this vulnerability to execute arbitrary code on the server. The tplmap and SSTImap tools are designed to automate the exploitation of SSTI vulnerabilities in web applications. The tools can be used to identify and exploit SSTI vulnerabilities in a variety of web application frameworks, including Flask, Django, and Jinja2.

From an offensive perspective, exploiting SSTI vulnerabilities can provide attackers with access to sensitive information or allow them to execute arbitrary code on the server. This can lead to data theft, system compromise, or even complete system takeover. From a defensive perspective, it's important to identify and remediate SSTI vulnerabilities in web applications to prevent attackers from exploiting them.

Business value: By identifying and remediating SSTI vulnerabilities in web applications, organizations can reduce the risk of data theft, system compromise, and reputation damage.

 

## Requirements

1. Access to a vulnerable web application

1. Authentication credentials if required

1. tplmap and SSTImap tools

 

## Defense

1. Secure coding practices can prevent SSTI vulnerabilities from being introduced into web applications

1. Regular vulnerability assessments and penetration testing can identify SSTI vulnerabilities before attackers can exploit them

1. Implementing web application firewalls can help detect and block SSTI attacks

 

## Objectives

1. Identify and exploit SSTI vulnerabilities in web applications

1. Gain access to sensitive information or execute arbitrary code on the server

 

# Instructions

1. Use the tplmap tool to exploit web application vulnerabilities by injecting payloads into template engines. The '-u' option specifies the target URL with a payload injection point. The '--os-shell' option is used to execute a shell command on the target operating system. The '--level' option specifies the level of injection to use (default is 3). The '-e' option specifies the template engine to use (default is jinja2).

 



**Code**: [[python2.7 ./tplmap.py -u 'http://www.target.com/pa]]



> -u: target URL with payload injection point
--os-shell: execute a shell command on target operating system
--level: level of injection to use (default is 3)
-e: template engine to use (default is jinja2)



**Command** ([[tplmap - os-shell]]):

```bash
python2.7 ./tplmap.py -u 'http://www.target.com/page?name=John*' --os-shell
```





**Command** ([[tplmap - inject parameter]]):

```bash
python2.7 ./tplmap.py -u "http://192.168.56.101:3000/ti?user=*&comment=supercomment&link"
```





**Command** ([[tplmap - inject parameter with level and extension]]):

```bash
python2.7 ./tplmap.py -u "http://192.168.56.101:3000/ti?user=InjectHere*&comment=A&link" --level 5 -e jade
```



2. The SSTImap command is used to automatically detect SSTI vulnerabilities in web applications. This command takes multiple arguments that are used to configure the tool and perform the scan. The -u argument is used to specify the target URL. The -s argument is used to perform a simple scan. The -l argument is used to specify the level of the scan. The -e argument is used to specify the extension of the file to be scanned. The -i argument is used to enable the interactive mode. The -A argument is used to enable all plugins. The -m argument is used to specify the HTTP method. The -H argument is used to specify the headers to be sent with the request.

 



**Code**: [[python3 ./sstimap.py -u 'https://example.com/page?]]



> The SSTImap command is used to scan web applications for SSTI vulnerabilities. The -u argument is used to specify the target URL. The -s argument is used to perform a simple scan. The -l argument is used to specify the level of the scan. The -e argument is used to specify the extension of the file to be scanned. The -i argument is used to enable the interactive mode, which allows the user to manually select the payloads to be sent. The -A argument is used to enable all plugins, which allows the tool to use all available payloads. The -m argument is used to specify the HTTP method to be used. The -H argument is used to specify the headers to be sent with the request.



**Command** ([[Directory Traversal Vulnerability Check]]):

```bash
python3 ./sstimap.py -u 'https://example.com/page?name=John' -s
```





**Command** ([[Jade Template Injection Vulnerability Check]]):

```bash
python3 ./sstimap.py -u 'https://example.com/page?name=Vulnerable*&message=My_message' -l 5 -e jade
```





**Command** ([[HTTP Authorization Header Injection Vulnerability Check]]):

```bash
python3 ./sstimap.py -i -A -m POST -l 5 -H 'Authorization: Basic bG9naW46c2VjcmV0X3Bhc3N3b3Jk'
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Template Injection|T1221 - Template Injection]]

## Commands Used

- [[Directory Traversal Vulnerability Check]]
- [[HTTP Authorization Header Injection Vulnerability Check]]
- [[Jade Template Injection Vulnerability Check]]
- [[tplmap - inject parameter]]
- [[tplmap - inject parameter with level and extension]]
- [[tplmap - os-shell]]

## Tags

- [[Server Side Template Injection]]
- [[Tools]]


