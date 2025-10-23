---
id: 6128009a-ea72-464c-996e-bed06164c089
name: Jinja2 Config Information Extraction
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:39.666575+00:00'
updated_at: '2023-04-10T20:23:44.671291+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Impact|TA0040 - Impact]]'
techniques:
- '[[Command-Line Interface|T1059 - Command-Line Interface]]'
- '[[System Shutdown/Reboot|T1529 - System Shutdown/Reboot]]'
tags:
- '[[Jinja2]]'
- '[[Jinja2 - Dump all config variables]]'
- '[[Server Side Template Injection]]'
---

# Jinja2 Config Information Extraction

## Summary

Jinja2 is a popular templating engine used by many web applications. It allows developers to create dynamic web pages by inserting variables into templates. However, Server Side Template Injection (SSTI) vulnerabilities can allow attackers to execute arbitrary code on the server. This procedure foc

## Description

# Description

Jinja2 is a popular templating engine used by many web applications. It allows developers to create dynamic web pages by inserting variables into templates. However, Server Side Template Injection (SSTI) vulnerabilities can allow attackers to execute arbitrary code on the server. This procedure focuses on extracting all configuration variables from a Jinja2 template. By dumping all config variables, an attacker can gain valuable information about the application's infrastructure and potentially identify additional attack vectors.

To extract all config variables, the 'Config Information' command is used. This command exploits a vulnerability in Jinja2 that allows for arbitrary code execution. By injecting a payload that dumps all config variables, the attacker can retrieve sensitive information such as database credentials, secret keys, and more.

This procedure can be used by attackers to gain a better understanding of the target environment and potentially identify additional attack vectors. It can also be used as a reconnaissance tool for red team engagements.

 

## Requirements

1. Access to a web application that uses Jinja2 templating engine

1. Ability to inject payloads into the application

 

## Defense

1. Ensure that all web applications are updated to the latest version of Jinja2

1. Implement input validation and sanitization to prevent injection attacks

1. Monitor web application logs for suspicious activity

 

## Objectives

1. Extract all configuration variables from a Jinja2 template

1. Identify sensitive information such as database credentials and secret keys

1. Reconnaissance for red team engagements

 

# Instructions

1. Use this command to retrieve configuration information.

 



**Code**: [[{% for key, value in config.iteritems() %}
    <dt]]



> The config information is returned as a dictionary where the keys represent the configuration options and the values represent the corresponding values of those options. The 'config' variable should be defined in the code before using this command.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Impact|TA0040 - Impact]]

### Techniques

- [[Command-Line Interface|T1059 - Command-Line Interface]]
- [[System Shutdown/Reboot|T1529 - System Shutdown/Reboot]]

## Tags

- [[Jinja2]]
- [[Jinja2 - Dump all config variables]]
- [[Server Side Template Injection]]


