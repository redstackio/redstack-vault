---
tags:
  - subdomain-takeover
  - poc
  - aws
  - ec2
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:26.554Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 534ac897-1276-4d84-a04f-4b90e2aa98ef
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Host and Verify Proof-of-Concept on Taken Over Subdomain

## Summary

This procedure demonstrates control over a taken-over subdomain by hosting a proof-of-concept page on the claimed EC2 instance, verifying the ability to serve arbitrary content and potentially bypass security controls like CORS.

## Description

Following subdomain takeover, the attacker deploys content to the EC2 instance to showcase ownership. This involves uploading an HTML file and configuring a web server (e.g., Apache or Nginx) on the instance. The target environment is the newly launched EC2 instance resolving via the dangling DNS. Outcomes include serving malicious pages for phishing, redirects, or exploiting trust in the subdomain. Prerequisites: SSH access to the EC2 instance and basic web server setup knowledge.

## Requirements

1. SSH access to the claimed EC2 instance
2. Web server software installed on the instance (e.g., via yum or apt)
3. The subdomain must resolve to the instance's IP

## Defense

Defensive measures and detection strategies:

- Monitor for unexpected web content on subdomains via certificate transparency logs or content scanners
- Implement subdomain isolation with strict CORS policies
- Use AWS WAF to detect anomalous traffic to subdomains

## Objectives

1. Deploy a PoC page to the EC2 instance
2. Configure the web server to serve the content
3. Verify accessibility via the subdomain URL

## Instructions

### Step 1: Access and Configure the EC2 Instance

**Context**: SSH into the instance and install a web server if not present.

Connect via SSH and set up a simple HTTP server.

> SSH command example:
> ```bash
ssh -i key.pem ec2-user@instance-ip
```
> Then install and start server: ```bash
sudo yum install httpd -y && sudo systemctl start httpd
```
> Expected output: Web server running on port 80.

### Step 2: Upload and Host PoC Content

**Context**: Create and place the PoC HTML file in the web root.

Upload a file like poc.html containing a message proving control (e.g., "Subdomain Taken Over").

> Use SCP or edit directly: ```bash
sudo nano /var/www/html/poc.html
```
> Expected output: File saved in document root.

### Step 3: Verify Exploitation

**Context**: Access the subdomain to confirm the PoC loads.

Open a browser or use curl to visit http://subdomain.target.com/poc.html.

> Verification command:
> ```bash
curl http://subdomain.target.com/poc.html
```
> Expected output: HTML content from the PoC page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[poc]]
- [[aws]]
- [[ec2]]
