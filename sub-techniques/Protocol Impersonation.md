---
id: e6e9eecf-c485-4a84-b8de-b386d0d22564
name: Protocol Impersonation
type: sub-technique
mitre_id: T1001.003
mitre_url: null
created_at: '2023-04-06T00:31:26.879769+00:00'
updated_at: '2023-04-06T00:31:26.879769+00:00'
parent_technique: '[[Data Obfuscation|T1001 - Data Obfuscation]]'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
---

# Protocol Impersonation

**MITRE ID**: T1001.003

**Parent Technique**: [[Data Obfuscation|T1001 - Data Obfuscation]]

This is a sub-technique of T1001 - Data Obfuscation.

## Summary

Adversaries may impersonate legitimate protocols or web service traffic to disguise command and control activity and thwart analysis efforts. By impersonating legitimate protocols or web services, adversaries can make their command and control traffic blend in with legitimate network traffic.  

Adv

## Description

Adversaries may impersonate legitimate protocols or web service traffic to disguise command and control activity and thwart analysis efforts. By impersonating legitimate protocols or web services, adversaries can make their command and control traffic blend in with legitimate network traffic.  

Adversaries may impersonate a fake SSL/TLS handshake to make it look like subsequent traffic is SSL/TLS encrypted, potentially interfering with some security tooling, or to make the traffic look like it is related with a trusted entity. 

## Tactics

This sub-technique is used in the following tactics:

- [[Command and Control|TA0011 - Command and Control]]
