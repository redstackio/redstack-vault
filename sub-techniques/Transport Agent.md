---
id: 0d61766f-abf1-4927-9d1f-a6ecf14ac4e2
name: Transport Agent
type: sub-technique
mitre_id: T1505.002
mitre_url: null
created_at: '2023-04-06T00:31:25.890793+00:00'
updated_at: '2023-04-06T00:31:25.890793+00:00'
parent_technique: '[[Server Software Component|T1505 - Server Software Component]]'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
---

# Transport Agent

**MITRE ID**: T1505.002

**Parent Technique**: [[Server Software Component|T1505 - Server Software Component]]

This is a sub-technique of T1505 - Server Software Component.

## Summary

Adversaries may abuse Microsoft transport agents to establish persistent access to systems. Microsoft Exchange transport agents can operate on email messages passing through the transport pipeline to perform various tasks such as filtering spam, filtering malicious attachments, journaling, or adding

## Description

Adversaries may abuse Microsoft transport agents to establish persistent access to systems. Microsoft Exchange transport agents can operate on email messages passing through the transport pipeline to perform various tasks such as filtering spam, filtering malicious attachments, journaling, or adding a corporate signature to the end of all outgoing emails.(Citation: Microsoft TransportAgent Jun 2016)(Citation: ESET LightNeuron May 2019) Transport agents can be written by application developers and then compiled to .NET assemblies that are subsequently registered with the Exchange server. Transport agents will be invoked during a specified stage of email processing and carry out developer defined tasks. 

Adversaries may register a malicious transport agent to provide a persistence mechanism in Exchange Server that can be triggered by adversary-specified email events.(Citation: ESET LightNeuron May 2019) Though a malicious transport agent may be invoked for all emails passing through the Exchange transport pipeline, the agent can be configured to only carry out specific tasks in response to adversary defined criteria. For example, the transport agent may only carry out an action like copying in-transit attachments and saving them for later exfiltration if the recipient email address matches an entry on a list provided by the adversary. 

## Tactics

This sub-technique is used in the following tactics:

- [[Persistence|TA0003 - Persistence]]
