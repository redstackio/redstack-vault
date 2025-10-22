---
id: 8ebe7dee-cd8b-4007-a4cb-31cfed1dcbba
name: Security Software Discovery
type: sub-technique
mitre_id: T1518.001
mitre_url: null
created_at: '2023-04-06T00:31:26.934078+00:00'
updated_at: '2023-04-06T00:31:26.934078+00:00'
parent_technique: '[[Software Discovery|T1518 - Software Discovery]]'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
---

# Security Software Discovery

**MITRE ID**: T1518.001

**Parent Technique**: [[Software Discovery|T1518 - Software Discovery]]

This is a sub-technique of T1518 - Software Discovery.

## Summary

Adversaries may attempt to get a listing of security software, configurations, defensive tools, and sensors that are installed on a system or in a cloud environment. This may include things such as firewall rules and anti-virus. Adversaries may use the information from [Security Software Discovery](

## Description

Adversaries may attempt to get a listing of security software, configurations, defensive tools, and sensors that are installed on a system or in a cloud environment. This may include things such as firewall rules and anti-virus. Adversaries may use the information from [Security Software Discovery](https://attack.mitre.org/techniques/T1518/001) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Example commands that can be used to obtain security software information are [netsh](https://attack.mitre.org/software/S0108), <code>reg query</code> with [Reg](https://attack.mitre.org/software/S0075), <code>dir</code> with [cmd](https://attack.mitre.org/software/S0106), and [Tasklist](https://attack.mitre.org/software/S0057), but other indicators of discovery behavior may be more specific to the type of software or security system the adversary is looking for. It is becoming more common to see macOS malware perform checks for LittleSnitch and KnockKnock software.

Adversaries may also utilize cloud APIs to discover the configurations of firewall rules within an environment.(Citation: Expel IO Evil in AWS) For example, the permitted IP ranges, ports or user accounts for the inbound/outbound rules of security groups, virtual firewalls established within AWS for EC2 and/or VPC instances, can be revealed by the <code>DescribeSecurityGroups</code> action with various request parameters. (Citation: DescribeSecurityGroups - Amazon Elastic Compute Cloud)

## Tactics

This sub-technique is used in the following tactics:

- [[Discovery|TA0007 - Discovery]]
