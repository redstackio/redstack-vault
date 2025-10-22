---
id: b413689b-9b44-45b3-9452-e34c18b71ff8
name: Malicious Image
type: sub-technique
mitre_id: T1204.003
mitre_url: null
created_at: '2023-04-06T00:31:26.734505+00:00'
updated_at: '2023-04-06T00:31:26.734505+00:00'
parent_technique: '[[User Execution|T1204 - User Execution]]'
tactics:
- '[[Execution|TA0002 - Execution]]'
procedures:
- '[[LFI to RCE via uploaded file]]'
---

# Malicious Image

**MITRE ID**: T1204.003

**Parent Technique**: [[User Execution|T1204 - User Execution]]

This is a sub-technique of T1204 - User Execution.

## Summary

Adversaries may rely on a user running a malicious image to facilitate execution. Amazon Web Services (AWS) Amazon Machine Images (AMIs), Google Cloud Platform (GCP) Images, and Azure Images as well as popular container runtimes such as Docker can be backdoored. Backdoored images may be uploaded to 

## Description

Adversaries may rely on a user running a malicious image to facilitate execution. Amazon Web Services (AWS) Amazon Machine Images (AMIs), Google Cloud Platform (GCP) Images, and Azure Images as well as popular container runtimes such as Docker can be backdoored. Backdoored images may be uploaded to a public repository via [Upload Malware](https://attack.mitre.org/techniques/T1608/001), and users may then download and deploy an instance or container from the image without realizing the image is malicious, thus bypassing techniques that specifically achieve Initial Access. This can lead to the execution of malicious code, such as code that executes cryptocurrency mining, in the instance or container.(Citation: Summit Route Malicious AMIs)

Adversaries may also name images a certain way to increase the chance of users mistakenly deploying an instance or container from the image (ex: [Match Legitimate Name or Location](https://attack.mitre.org/techniques/T1036/005)).(Citation: Aqua Security Cloud Native Threat Report June 2021)

## Tactics

This sub-technique is used in the following tactics:

- [[Execution|TA0002 - Execution]]

## Related Procedures

There are 1 procedures using this sub-technique:

- [[LFI to RCE via uploaded file]]
