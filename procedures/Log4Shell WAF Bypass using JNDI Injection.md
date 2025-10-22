---
id: fedfbf43-1c56-443c-b011-43fef9b10362
name: Log4Shell WAF Bypass using JNDI Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:56.546016+00:00'
updated_at: '2023-04-06T03:55:56.556735+00:00'
tags:
- '[[CVE-2021-44228 Log4Shell]]'
- '[[WAF Bypass]]'
---

# Log4Shell WAF Bypass using JNDI Injection

## Summary

This procedure outlines how to bypass a Web Application Firewall (WAF) using JNDI Injection to exploit the Log4Shell vulnerability (CVE-2021-44228). The Log4Shell vulnerability allows an attacker to execute arbitrary code remotely on a server running a vulnerable version of Apache Log4j. By using J

## Description

# Description

This procedure outlines how to bypass a Web Application Firewall (WAF) using JNDI Injection to exploit the Log4Shell vulnerability (CVE-2021-44228). The Log4Shell vulnerability allows an attacker to execute arbitrary code remotely on a server running a vulnerable version of Apache Log4j. By using JNDI Injection, an attacker can bypass WAF protections and execute arbitrary code on the target system. This technique is commonly used by attackers to evade detection and successfully compromise a system.

## Requirements

1. Access to a Log4j vulnerable server

1. Knowledge of JNDI Injection

1. Ability to modify HTTP requests to bypass WAF protections

## Defense

1. Ensure that all systems are patched and up-to-date to prevent exploitation of the Log4Shell vulnerability

1. Implement proper WAF protections to prevent JNDI Injection attacks

1. Monitor network traffic for suspicious activity, such as unusual HTTP requests

## Objectives

1. Bypass WAF protections to successfully execute arbitrary code on a target system

1. Exploit the Log4Shell vulnerability (CVE-2021-44228)

# Instructions

1. Copy and paste the commands into a PowerShell console to execute them.

**Code**: [[${${::-j}${::-n}${::-d}${::-i}:${::-r}${::-m}${::-]]

> The commands use JNDI Injection to bypass WAF protections and execute arbitrary code on a Log4j vulnerable server. The commands include variations using lower and upper case, as well as using the 'env' command to create the letter 'j' to evade detection. The attacker can modify the commands to suit their specific needs.

## Tags

- [[CVE-2021-44228 Log4Shell]]
- [[WAF Bypass]]
