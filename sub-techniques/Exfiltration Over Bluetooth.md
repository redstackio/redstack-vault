---
id: 403293de-8e64-41c0-888b-acce1c95f02f
name: Exfiltration Over Bluetooth
type: sub-technique
mitre_id: T1011.001
mitre_url: null
created_at: '2023-04-06T00:31:26.216072+00:00'
updated_at: '2023-04-06T00:31:26.216072+00:00'
parent_technique: '[[Exfiltration Over Other Network Medium|T1011 - Exfiltration Over
  Other Network Medium]]'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
---

# Exfiltration Over Bluetooth

**MITRE ID**: T1011.001

**Parent Technique**: [[Exfiltration Over Other Network Medium|T1011 - Exfiltration Over Other Network Medium]]

This is a sub-technique of T1011 - Exfiltration Over Other Network Medium.

## Summary

Adversaries may attempt to exfiltrate data over Bluetooth rather than the command and control channel. If the command and control network is a wired Internet connection, an adversary may opt to exfiltrate data using a Bluetooth communication channel.

Adversaries may choose to do this if they have s

## Description

Adversaries may attempt to exfiltrate data over Bluetooth rather than the command and control channel. If the command and control network is a wired Internet connection, an adversary may opt to exfiltrate data using a Bluetooth communication channel.

Adversaries may choose to do this if they have sufficient access and proximity. Bluetooth connections might not be secured or defended as well as the primary Internet-connected channel because it is not routed through the same enterprise network.

## Tactics

This sub-technique is used in the following tactics:

- [[Exfiltration|TA0010 - Exfiltration]]
