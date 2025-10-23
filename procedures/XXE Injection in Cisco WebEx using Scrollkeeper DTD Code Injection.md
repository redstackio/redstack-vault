---
id: b7441718-56b4-4cb9-bdd4-a884b635d931
name: XXE Injection in Cisco WebEx using Scrollkeeper DTD Code Injection
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:44.479480+00:00'
updated_at: '2023-04-10T20:24:39.529287+00:00'
tags:
- '[[Cisco WebEx]]'
- '[[XML External Entity]]'
- '[[XXE with local DTD]]'
---

# XXE Injection in Cisco WebEx using Scrollkeeper DTD Code Injection

## Summary

The Scrollkeeper DTD Code Injection vulnerability in Cisco WebEx allows an attacker to execute arbitrary code on the target system. This vulnerability can be exploited by injecting a specially crafted XML file that contains an external entity reference which points to a local DTD file. When the vul

## Description

# Description

The Scrollkeeper DTD Code Injection vulnerability in Cisco WebEx allows an attacker to execute arbitrary code on the target system. This vulnerability can be exploited by injecting a specially crafted XML file that contains an external entity reference which points to a local DTD file. When the vulnerable application parses the XML file, it will attempt to resolve the external entity reference and will load the DTD file. The attacker can then include malicious code in the DTD file which will be executed by the vulnerable application.

This attack can be carried out remotely, allowing an attacker to gain initial access to the target system. By exploiting this vulnerability, an attacker can bypass security controls and execute arbitrary code on the target system.

 

## Requirements

1. Access to the vulnerable Cisco WebEx application

1. Knowledge of the target system's file system structure and configuration

1. Ability to craft a specially crafted XML file

 

## Defense

1. Ensure that the Cisco WebEx application is up-to-date with the latest security patches

1. Implement network segmentation to prevent remote access to critical systems

1. Use a web application firewall to detect and block XXE attacks

 

## Objectives

1. Gain remote access to the target system

1. Execute arbitrary code on the target system

1. Bypass security controls

 

# Instructions

1. This command allows the injection of DTD code into the Scrollkeeper XML file. The DTD code can be used to specify the structure and format of the XML file.

 

The first line of the data field imports the Scrollkeeper DTD file. The second line defines a new entity called "url.attribute.set" that can be used to inject the DTD code. The injected DTD code should replace the "Your DTD code" placeholder. The injected code can be used to define new elements, attributes, and entities in the Scrollkeeper XML file.

## Tags

- [[Cisco WebEx]]
- [[XML External Entity]]
- [[XXE with local DTD]]


