---
id: 9b4a4e31-7ee0-4673-b3fb-90714db56aed
name: Internet Connection Discovery
type: sub-technique
mitre_id: T1016.001
mitre_url: null
created_at: '2023-04-06T00:31:25.580555+00:00'
updated_at: '2023-04-06T00:31:25.580555+00:00'
parent_technique: '[[System Network Configuration Discovery|T1016 - System Network
  Configuration Discovery]]'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
---

# Internet Connection Discovery

**MITRE ID**: T1016.001

**Parent Technique**: [[System Network Configuration Discovery|T1016 - System Network Configuration Discovery]]

This is a sub-technique of T1016 - System Network Configuration Discovery.

## Summary

Adversaries may check for Internet connectivity on compromised systems. This may be performed during automated discovery and can be accomplished in numerous ways such as using [Ping](https://attack.mitre.org/software/S0097), <code>tracert</code>, and GET requests to websites.

Adversaries may use th

## Description

Adversaries may check for Internet connectivity on compromised systems. This may be performed during automated discovery and can be accomplished in numerous ways such as using [Ping](https://attack.mitre.org/software/S0097), <code>tracert</code>, and GET requests to websites.

Adversaries may use the results and responses from these requests to determine if the system is capable of communicating with their C2 servers before attempting to connect to them. The results may also be used to identify routes, redirectors, and proxy servers.

## Tactics

This sub-technique is used in the following tactics:

- [[Discovery|TA0007 - Discovery]]
