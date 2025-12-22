---
tags:
  - xxe
  - semrush
  - exploitation
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 4546d2a8-c4ad-4aaf-a493-ef080a66b634
created_at: '2025-12-13T09:00:33.772Z'
updated_at: '2025-12-13T09:00:33.772Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger XXE in Site Audit

## Summary

This procedure starts the Site Audit in Semrush, triggering the XXE vulnerability by processing the malicious sitemap.xml, leading to arbitrary file reading and directory listing on the server.

## Description

Initiating the audit causes the Java XML processor to parse the provided sitemap, resolving external entities to access local resources like /etc/hostname or /home. This exploits the lack of restrictions on entity resolution. The target is the Semrush backend on Linux. Expected outcomes include exposure of sensitive server information.

## Requirements

1. Configured Site Audit with malicious sitemap
2. Web browser for starting the audit
3. Monitoring capability for exposed data (e.g., in audit results)

## Defense

Defensive measures and detection strategies:

- Use secure XML parsing libraries with entity resolution disabled
- Monitor server logs for unusual file access or entity resolutions

## Objectives

1. Process malicious XML
2. Resolve external entities
3. Expose server files and directories

## Instructions

### Step 1: Start the Audit

**Context**: Initiate the processing of the sitemap.

In Semrush Site Audit, click 'Start Audit' using [[tools/Firefox]] or [[tools/Google-Chrome]].

> Wait for the process to begin.

### Step 2: Observe XXE Trigger

**Context**: Monitor for vulnerability exploitation.

Check audit outputs or error responses for resolved entity data, such as file contents or directory listings.

> Verify exposure of targeted resources.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Firefox]]
- [[tools/Google-Chrome]]

## Tags

- [[xxe]]
- [[semrush]]
- [[exploitation]]
