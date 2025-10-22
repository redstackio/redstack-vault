---
id: 9f13f679-0d7b-4261-940d-def4223c08ac
name: External Proxy
type: sub-technique
mitre_id: T1090.002
mitre_url: null
created_at: '2023-04-06T00:31:26.291941+00:00'
updated_at: '2023-04-06T00:31:26.291941+00:00'
parent_technique: '[[Connection Proxy|T1090 - Connection Proxy]]'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
---

# External Proxy

**MITRE ID**: T1090.002

**Parent Technique**: [[Connection Proxy|T1090 - Connection Proxy]]

This is a sub-technique of T1090 - Connection Proxy.

## Summary

Adversaries may use an external proxy to act as an intermediary for network communications to a command and control server to avoid direct connections to their infrastructure. Many tools exist that enable traffic redirection through proxies or port redirection, including [HTRAN](https://attack.mitre

## Description

Adversaries may use an external proxy to act as an intermediary for network communications to a command and control server to avoid direct connections to their infrastructure. Many tools exist that enable traffic redirection through proxies or port redirection, including [HTRAN](https://attack.mitre.org/software/S0040), ZXProxy, and ZXPortMap. (Citation: Trend Micro APT Attack Tools) Adversaries use these types of proxies to manage command and control communications, to provide resiliency in the face of connection loss, or to ride over existing trusted communications paths to avoid suspicion.

External connection proxies are used to mask the destination of C2 traffic and are typically implemented with port redirectors. Compromised systems outside of the victim environment may be used for these purposes, as well as purchased infrastructure such as cloud-based resources or virtual private servers. Proxies may be chosen based on the low likelihood that a connection to them from a compromised system would be investigated. Victim systems would communicate directly with the external proxy on the Internet and then the proxy would forward communications to the C2 server.

## Tactics

This sub-technique is used in the following tactics:

- [[Command and Control|TA0011 - Command and Control]]
