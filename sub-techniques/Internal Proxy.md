---
id: 31440bdd-df94-49fb-b3c8-d5f5e6015388
name: Internal Proxy
type: sub-technique
mitre_id: T1090.001
mitre_url: null
created_at: '2023-04-06T00:31:27.208031+00:00'
updated_at: '2023-04-06T00:31:27.208031+00:00'
parent_technique: '[[Connection Proxy|T1090 - Connection Proxy]]'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
---

# Internal Proxy

**MITRE ID**: T1090.001

**Parent Technique**: [[Connection Proxy|T1090 - Connection Proxy]]

This is a sub-technique of T1090 - Connection Proxy.

## Summary

Adversaries may use an internal proxy to direct command and control traffic between two or more systems in a compromised environment. Many tools exist that enable traffic redirection through proxies or port redirection, including [HTRAN](https://attack.mitre.org/software/S0040), ZXProxy, and ZXPortM

## Description

Adversaries may use an internal proxy to direct command and control traffic between two or more systems in a compromised environment. Many tools exist that enable traffic redirection through proxies or port redirection, including [HTRAN](https://attack.mitre.org/software/S0040), ZXProxy, and ZXPortMap. (Citation: Trend Micro APT Attack Tools) Adversaries use internal proxies to manage command and control communications inside a compromised environment, to reduce the number of simultaneous outbound network connections, to provide resiliency in the face of connection loss, or to ride over existing trusted communications paths between infected systems to avoid suspicion. Internal proxy connections may use common peer-to-peer (p2p) networking protocols, such as SMB, to better blend in with the environment.

By using a compromised internal system as a proxy, adversaries may conceal the true destination of C2 traffic while reducing the need for numerous connections to external systems.

## Tactics

This sub-technique is used in the following tactics:

- [[Command and Control|TA0011 - Command and Control]]
