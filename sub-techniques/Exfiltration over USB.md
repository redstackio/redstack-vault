---
id: 8ca0c5b6-dcf5-4bc4-81ec-cf7b2e05e725
name: Exfiltration over USB
type: sub-technique
mitre_id: T1052.001
mitre_url: null
created_at: '2023-04-06T00:31:26.671428+00:00'
updated_at: '2023-04-06T00:31:26.671428+00:00'
parent_technique: '[[Exfiltration Over Physical Medium|T1052 - Exfiltration Over Physical
  Medium]]'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
---

# Exfiltration over USB

**MITRE ID**: T1052.001

**Parent Technique**: [[Exfiltration Over Physical Medium|T1052 - Exfiltration Over Physical Medium]]

This is a sub-technique of T1052 - Exfiltration Over Physical Medium.

## Summary

Adversaries may attempt to exfiltrate data over a USB connected physical device. In certain circumstances, such as an air-gapped network compromise, exfiltration could occur via a USB device introduced by a user. The USB device could be used as the final exfiltration point or to hop between otherwis

## Description

Adversaries may attempt to exfiltrate data over a USB connected physical device. In certain circumstances, such as an air-gapped network compromise, exfiltration could occur via a USB device introduced by a user. The USB device could be used as the final exfiltration point or to hop between otherwise disconnected systems.

## Tactics

This sub-technique is used in the following tactics:

- [[Exfiltration|TA0010 - Exfiltration]]
