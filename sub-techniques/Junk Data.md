---
id: 19427d67-4f2b-41ae-8cdb-43a7548524db
name: Junk Data
type: sub-technique
mitre_id: T1001.001
mitre_url: null
created_at: '2023-04-06T00:31:27.216618+00:00'
updated_at: '2023-04-06T00:31:27.216618+00:00'
parent_technique: '[[Data Obfuscation|T1001 - Data Obfuscation]]'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
---

# Junk Data

**MITRE ID**: T1001.001

**Parent Technique**: [[Data Obfuscation|T1001 - Data Obfuscation]]

This is a sub-technique of T1001 - Data Obfuscation.

## Summary

Adversaries may add junk data to protocols used for command and control to make detection more difficult. By adding random or meaningless data to the protocols used for command and control, adversaries can prevent trivial methods for decoding, deciphering, or otherwise analyzing the traffic. Example

## Description

Adversaries may add junk data to protocols used for command and control to make detection more difficult. By adding random or meaningless data to the protocols used for command and control, adversaries can prevent trivial methods for decoding, deciphering, or otherwise analyzing the traffic. Examples may include appending/prepending data with junk characters or writing junk characters between significant characters. 

## Tactics

This sub-technique is used in the following tactics:

- [[Command and Control|TA0011 - Command and Control]]
