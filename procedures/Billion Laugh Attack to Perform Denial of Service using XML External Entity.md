---
id: fbced85e-0bc0-49dc-b8f6-e24c68a6ec80
name: Billion Laugh Attack to Perform Denial of Service using XML External Entity
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:44.269725+00:00'
updated_at: '2023-04-10T20:24:37.548220+00:00'
tactics:
- '[[Impact|TA0040 - Impact]]'
techniques:
- '[[Network Denial of Service|T1498 - Network Denial of Service]]'
- '[[System Shutdown/Reboot|T1529 - System Shutdown/Reboot]]'
tags:
- '[[Billion Laugh Attack]]'
- '[[Exploiting XXE to perform a deny of service]]'
- '[[XML External Entity]]'
---

# Billion Laugh Attack to Perform Denial of Service using XML External Entity

## Summary

The Billion Laugh Attack is a type of denial of service attack that exploits a vulnerability in XML parsers. This attack is performed by creating an XML document that contains a large number of nested entities. When the XML parser attempts to parse the document, it will consume a large amount of me

## Description

# Description

The Billion Laugh Attack is a type of denial of service attack that exploits a vulnerability in XML parsers. This attack is performed by creating an XML document that contains a large number of nested entities. When the XML parser attempts to parse the document, it will consume a large amount of memory and CPU resources, eventually causing the system to crash or become unresponsive. This attack can be performed using the XML External Entity (XXE) vulnerability, which allows an attacker to include external entities in an XML document. By including a large number of nested entities, an attacker can perform a successful Billion Laugh Attack.

From a technical standpoint, the Billion Laugh Attack is a type of amplification attack. The attacker sends a small amount of data to the target system, which is then amplified by the XML parser. This amplification can be significant, with a single XML document causing the consumption of gigabytes of memory and CPU resources. The business value of this attack is that it can be used to disrupt critical services and cause downtime for an organization.

## Requirements

1. Access to a vulnerable XML parser

1. Knowledge of XML syntax and the XML External Entity vulnerability

## Defense

1. Implement input validation and sanitization to prevent the inclusion of external entities in XML documents

1. Limit the resources available to the XML parser to prevent resource exhaustion

1. Use a web application firewall (WAF) to block XML documents that contain a large number of nested entities

## Objectives

1. Perform a successful Billion Laugh Attack using the XML External Entity vulnerability

1. Cause the target system to crash or become unresponsive

# Instructions

1. To execute an XML Entity Bomb Attack, create an XML file with a DOCTYPE declaration that defines an internal DTD subset with multiple entities that reference each other recursively. Then, parse the XML file with an XML processor that expands the entities, causing the processor to consume large amounts of memory and CPU resources. This can cause a denial-of-service (DoS) attack on the system.

**Code**: [[<!DOCTYPE data [
<!ENTITY a0 "dos" >
<!ENTITY a1 "]]

> The XML Entity Bomb Attack is a type of Denial of Service (DoS) attack where an attacker sends an XML file containing a large number of recursive entity references to a vulnerable XML processor. When the XML processor attempts to expand these entities, it consumes large amounts of memory and CPU resources, which can cause the system to crash or become unresponsive. This attack can be used to disrupt the availability of a service or server, and should not be used on production systems.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact|TA0040 - Impact]]

### Techniques

- [[Network Denial of Service|T1498 - Network Denial of Service]]
- [[System Shutdown/Reboot|T1529 - System Shutdown/Reboot]]

## Tags

- [[Billion Laugh Attack]]
- [[Exploiting XXE to perform a deny of service]]
- [[XML External Entity]]
