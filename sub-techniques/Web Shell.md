---
id: b609a5d0-5395-4877-b1f1-cb2d7c729490
name: Web Shell
type: sub-technique
mitre_id: T1505.003
mitre_url: null
created_at: '2023-04-06T00:31:26.200238+00:00'
updated_at: '2023-04-06T00:31:26.200238+00:00'
parent_technique: '[[Server Software Component|T1505 - Server Software Component]]'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
procedures:
- '[[ObjectDataProvider JSON.NET Deserialization RCE]]'
---

# Web Shell

**MITRE ID**: T1505.003

**Parent Technique**: [[Server Software Component|T1505 - Server Software Component]]

This is a sub-technique of T1505 - Server Software Component.

## Summary

Adversaries may backdoor web servers with web shells to establish persistent access to systems. A Web shell is a Web script that is placed on an openly accessible Web server to allow an adversary to use the Web server as a gateway into a network. A Web shell may provide a set of functions to execute

## Description

Adversaries may backdoor web servers with web shells to establish persistent access to systems. A Web shell is a Web script that is placed on an openly accessible Web server to allow an adversary to use the Web server as a gateway into a network. A Web shell may provide a set of functions to execute or a command-line interface on the system that hosts the Web server.(Citation: volexity_0day_sophos_FW)

In addition to a server-side script, a Web shell may have a client interface program that is used to talk to the Web server (e.g. [China Chopper](https://attack.mitre.org/software/S0020) Web shell client).(Citation: Lee 2013)

## Tactics

This sub-technique is used in the following tactics:

- [[Persistence|TA0003 - Persistence]]

## Related Procedures

There are 1 procedures using this sub-technique:

- [[ObjectDataProvider JSON.NET Deserialization RCE]]
