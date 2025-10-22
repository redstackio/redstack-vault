---
id: 58ba8da5-c735-49c6-b8e7-690feea47252
name: Exfiltration to Cloud Storage
type: sub-technique
mitre_id: T1567.002
mitre_url: null
created_at: '2023-04-06T00:31:26.846587+00:00'
updated_at: '2023-04-06T00:31:26.846587+00:00'
parent_technique: '[[Exfiltration Over Web Service|T1567 - Exfiltration Over Web Service]]'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
---

# Exfiltration to Cloud Storage

**MITRE ID**: T1567.002

**Parent Technique**: [[Exfiltration Over Web Service|T1567 - Exfiltration Over Web Service]]

This is a sub-technique of T1567 - Exfiltration Over Web Service.

## Summary

Adversaries may exfiltrate data to a cloud storage service rather than over their primary command and control channel. Cloud storage services allow for the storage, edit, and retrieval of data from a remote cloud storage server over the Internet.

Examples of cloud storage services include Dropbox a

## Description

Adversaries may exfiltrate data to a cloud storage service rather than over their primary command and control channel. Cloud storage services allow for the storage, edit, and retrieval of data from a remote cloud storage server over the Internet.

Examples of cloud storage services include Dropbox and Google Docs. Exfiltration to these cloud storage services can provide a significant amount of cover to the adversary if hosts within the network are already communicating with the service. 

## Tactics

This sub-technique is used in the following tactics:

- [[Exfiltration|TA0010 - Exfiltration]]
