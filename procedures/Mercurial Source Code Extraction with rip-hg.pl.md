---
id: 38d15d09-811d-4fe1-92e3-2404b2a94939
name: Mercurial Source Code Extraction with rip-hg.pl
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:00.394093+00:00'
updated_at: '2023-04-10T20:33:57.936879+00:00'
tactics:
- '[[Exfiltration|TA0010 - Exfiltration]]'
techniques:
- '[[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative
  Protocol]]'
- '[[Exfiltration Over Command and Control Channel|T1041 - Exfiltration Over Command
  and Control Channel]]'
tags:
- '[[Insecure Source Code Management]]'
- '[[Mercurial]]'
- '[[rip-hg.pl]]'
- '[[Tools]]'
commands:
- '[[Download rip-hg.pl script]]'
- '[[Run docker container for dvcs-ripper]]'
---

# Mercurial Source Code Extraction with rip-hg.pl

## Summary

This procedure involves using the rip-hg.pl tool to extract source code from a Mercurial repository. This can be useful for an attacker looking to exfiltrate sensitive code from a target organization. The tool works by cloning the repository and extracting the code to a local directory. This can be

## Description

# Description

This procedure involves using the rip-hg.pl tool to extract source code from a Mercurial repository. This can be useful for an attacker looking to exfiltrate sensitive code from a target organization. The tool works by cloning the repository and extracting the code to a local directory. This can be done either by running the tool on the host or in a Docker container. The business value of this attack is that an attacker can gain access to sensitive source code, which can be used for further attacks or sold on the black market.

## Requirements

1. Access to a Mercurial repository

1. Ability to run the rip-hg.pl tool on the host or in a Docker container

## Defense

1. Limit access to Mercurial repositories to authorized users only

1. Monitor network traffic for suspicious activity, such as large amounts of data being exfiltrated

1. Implement data loss prevention measures to prevent sensitive code from being exfiltrated

## Objectives

1. Extract source code from a Mercurial repository

1. Exfiltrate sensitive code from a target organization

# Instructions

1. 1. Download the rip-hg.pl tool from the GitHub repository.
2. Run the tool either on the host or in a Docker container.
3. Provide the path to the host work directory and the URL of the Mercurial repository.
4. Use the -v and -u options to enable verbose output and to update the repository if it already exists.

**Code**: [[wget https://raw.githubusercontent.com/kost/dvcs-r]]

> The rip-hg.pl tool is used to clone the Mercurial repository and extract the source code to a local directory. The -v option is used to enable verbose output, which can be useful for debugging. The -u option is used to update the repository if it already exists. The -it option is used to run the Docker container in interactive mode. The -v option is used to mount the host work directory to the container's /work directory, which is where the repository will be cloned.

**Command** ([[Download rip-hg.pl script]]):

```bash
wget https://raw.githubusercontent.com/kost/dvcs-ripper/master/rip-hg.pl
```

**Command** ([[Run docker container for dvcs-ripper]]):

```bash
docker run --rm -it -v /path/to/host/work:/work:rw k0st/alpine-dvcs-ripper rip-hg.pl -v -u
```

## MITRE ATT&CK Mapping

### Tactics

- [[Exfiltration|TA0010 - Exfiltration]]

### Techniques

- [[Exfiltration Over Alternative Protocol|T1048 - Exfiltration Over Alternative Protocol]]
- [[Exfiltration Over Command and Control Channel|T1041 - Exfiltration Over Command and Control Channel]]

## Commands Used

- [[Download rip-hg.pl script]]
- [[Run docker container for dvcs-ripper]]

## Tags

- [[Insecure Source Code Management]]
- [[Mercurial]]
- [[rip-hg.pl]]
- [[Tools]]
