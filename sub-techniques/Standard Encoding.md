---
id: 9d81e501-0825-4934-adab-22d5994a9835
name: Standard Encoding
type: sub-technique
mitre_id: T1132.001
mitre_url: null
created_at: '2023-04-06T00:31:25.448761+00:00'
updated_at: '2023-04-06T00:31:25.448761+00:00'
parent_technique: '[[Data Encoding|T1132 - Data Encoding]]'
tactics:
- '[[Command and Control|TA0011 - Command and Control]]'
---

# Standard Encoding

**MITRE ID**: T1132.001

**Parent Technique**: [[Data Encoding|T1132 - Data Encoding]]

This is a sub-technique of T1132 - Data Encoding.

## Summary

Adversaries may encode data with a standard data encoding system to make the content of command and control traffic more difficult to detect. Command and control (C2) information can be encoded using a standard data encoding system that adheres to existing protocol specifications. Common data encodi

## Description

Adversaries may encode data with a standard data encoding system to make the content of command and control traffic more difficult to detect. Command and control (C2) information can be encoded using a standard data encoding system that adheres to existing protocol specifications. Common data encoding schemes include ASCII, Unicode, hexadecimal, Base64, and MIME.(Citation: Wikipedia Binary-to-text Encoding) (Citation: Wikipedia Character Encoding) Some data encoding systems may also result in data compression, such as gzip.

## Tactics

This sub-technique is used in the following tactics:

- [[Command and Control|TA0011 - Command and Control]]
