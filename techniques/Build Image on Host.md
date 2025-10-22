---
id: aa4b48b9-e071-4674-8a5b-8fee585f6ff0
name: Build Image on Host
type: technique
mitre_id: T1612
mitre_url: null
created_at: '2023-04-06T00:31:26.466737+00:00'
updated_at: '2023-04-06T00:31:27.836053+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
---

# Build Image on Host

**MITRE ID**: T1612

## Description

Adversaries may build a container image directly on a host to bypass defenses that monitor for the retrieval of malicious images from a public registry. A remote <code>build</code> request may be sent to the Docker API that includes a Dockerfile that pulls a vanilla base image, such as alpine, from a public or local registry and then builds a custom image upon it.(Citation: Docker Build Image)

An adversary may take advantage of that <code>build</code> API to build a custom image on the host that includes malware downloaded from their C2 server, and then they then may utilize [Deploy Container](https://attack.mitre.org/techniques/T1610) using that custom image.(Citation: Aqua Build Images on Hosts)(Citation: Aqua Security Cloud Native Threat Report June 2021) If the base image is pulled from a public registry, defenses will likely not detect the image as malicious since it’s a vanilla image. If the base image already resides in a local registry, the pull may be considered even less suspicious since the image is already in the environment. 

## Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
