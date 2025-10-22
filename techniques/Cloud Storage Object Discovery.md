---
id: a40a17a5-4c84-43a0-95e5-fbf971cd7737
name: Cloud Storage Object Discovery
type: technique
mitre_id: T1619
mitre_url: null
created_at: '2023-04-06T00:31:26.518228+00:00'
updated_at: '2023-04-06T00:31:27.843146+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
---

# Cloud Storage Object Discovery

**MITRE ID**: T1619

## Description

Adversaries may enumerate objects in cloud storage infrastructure. Adversaries may use this information during automated discovery to shape follow-on behaviors, including requesting all or specific objects from cloud storage.  Similar to [File and Directory Discovery](https://attack.mitre.org/techniques/T1083) on a local host, after identifying available storage services (i.e. [Cloud Infrastructure Discovery](https://attack.mitre.org/techniques/T1580)) adversaries may access the contents/objects stored in cloud infrastructure.

Cloud service providers offer APIs allowing users to enumerate objects stored within cloud storage. Examples include ListObjectsV2 in AWS (Citation: ListObjectsV2) and List Blobs in Azure(Citation: List Blobs) .

## Tactics

- [[Discovery|TA0007 - Discovery]]
