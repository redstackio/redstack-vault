---
id: 5ee07459-d1be-4bc0-a83c-faf969c44b85
name: Implant Internal Image
type: technique
mitre_id: T1525
mitre_url: null
created_at: '2023-04-06T00:31:26.079288+00:00'
updated_at: '2023-04-06T00:31:27.813832+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
---

# Implant Internal Image

**MITRE ID**: T1525

## Description

Adversaries may implant cloud or container images with malicious code to establish persistence after gaining access to an environment. Amazon Web Services (AWS) Amazon Machine Images (AMIs), Google Cloud Platform (GCP) Images, and Azure Images as well as popular container runtimes such as Docker can be implanted or backdoored. Unlike [Upload Malware](https://attack.mitre.org/techniques/T1608/001), this technique focuses on adversaries implanting an image in a registry within a victim’s environment. Depending on how the infrastructure is provisioned, this could provide persistent access if the infrastructure provisioning tool is instructed to always use the latest image.(Citation: Rhino Labs Cloud Image Backdoor Technique Sept 2019)

A tool has been developed to facilitate planting backdoors in cloud container images.(Citation: Rhino Labs Cloud Backdoor September 2019) If an adversary has access to a compromised AWS instance, and permissions to list the available container images, they may implant a backdoor such as a [Web Shell](https://attack.mitre.org/techniques/T1505/003).(Citation: Rhino Labs Cloud Image Backdoor Technique Sept 2019)

## Tactics

- [[Persistence|TA0003 - Persistence]]
