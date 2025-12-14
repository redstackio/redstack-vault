---
tags:
  - poc
  - traffic-control
  - demonstration
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Azure
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T04:38:49.687Z'
sub_techniques: []
id: b0e45659-c957-4a78-9974-6d7083d99e9a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Demonstrate-Subdomain-Control-with-PoC

## Summary

This procedure proves subdomain takeover by uploading and serving a proof-of-concept file via the controlled Azure VM, visible through the original domain.

## Description

With VM control established, host a simple text file on the subdomain's HTTP path to show ownership. This validates traffic routing and enables further demos like phishing pages. Targets usclsapipma.cv.ford.com; requires web server on VM.

## Requirements

1. Controlled Azure VM with web server (e.g., Apache)
2. File upload access to VM filesystem
3. Public access to subdomain URL

## Defense

Defensive measures and detection strategies:

- Implement certificate pinning or HSTS to detect traffic hijacks
- Monitor web logs for anomalous content on subdomains
- Use DNSSEC to prevent unauthorized resolutions

## Objectives

1. Verify traffic interception on the subdomain
2. Display evidence of control without alerting
3. Simulate real impacts like malware hosting

## Instructions

### Step 1: Upload PoC File to VM

**Context**: Create and place a file on the web root of the controlled VM.

SSH into VM and execute:
```bash
echo "Proof of Control: Subdomain Taken Over" > /var/www/html/BHJAed55oazeDAZ02dDZ.txt
systemctl restart apache2
```

> File is now served at the VM's IP; DNS propagation routes subdomain requests here.

### Step 2: Access and Verify via Subdomain

**Context**: Test accessibility from the original domain.

Browse to http://usclsapipma.cv.ford.com/BHJAed55oazeDAZ02dDZ.txt.

> Expected: File content loads, confirming takeover success.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques

- None

## Commands Used


## Tools Used


## Tags

- [[poc]]
- [[traffic-control]]
- [[demonstration]]
