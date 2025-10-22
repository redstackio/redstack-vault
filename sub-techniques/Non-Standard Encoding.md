---
id: b8b20452-3ff0-4b96-ae51-38e6b9a532c9
name: Non-Standard Encoding
type: sub-technique
mitre_id: T1132.002
mitre_url: null
created_at: '2023-04-06T00:31:27.011238+00:00'
updated_at: '2023-04-06T00:31:27.011238+00:00'
parent_technique: '[[Data Encoding|T1132 - Data Encoding]]'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
---

# Non-Standard Encoding

**MITRE ID**: T1132.002

**Parent Technique**: [[Data Encoding|T1132 - Data Encoding]]

This is a sub-technique of T1132 - Data Encoding.

## Summary

Adversaries may encode data with a non-standard data encoding system to make the content of command and control traffic more difficult to detect. Command and control (C2) information can be encoded using a non-standard data encoding system that diverges from existing protocol specifications. Non-sta

## Description

Adversaries may encode data with a non-standard data encoding system to make the content of command and control traffic more difficult to detect. Command and control (C2) information can be encoded using a non-standard data encoding system that diverges from existing protocol specifications. Non-standard data encoding schemes may be based on or related to standard data encoding schemes, such as a modified Base64 encoding for the message body of an HTTP request.(Citation: Wikipedia Binary-to-text Encoding) (Citation: Wikipedia Character Encoding) 

## Tactics

This sub-technique is used in the following tactics:

- [[Command and Control|TA0011 - Command and Control]]
