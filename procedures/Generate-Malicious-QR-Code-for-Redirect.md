---
id: proc-qr-generate-001
tags:
  - qr-code
  - phishing
  - open-redirect
type: procedure
tools:
  - '[[tools/QR-Code-Generator]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Phishing]]'
updated_at: '2025-12-14T17:24:34.873Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Generate-Malicious-QR-Code-for-Redirect

## Summary

This procedure outlines how to create a QR code image that encodes a malicious URL, which can be used to exploit open redirect vulnerabilities in applications like Brave Browser's QR scanner, leading to automatic navigation to phishing or malware sites.

## Description

Attackers generate QR codes using online tools to embed arbitrary URLs, such as those pointing to phishing pages or malware hosts. When scanned by a vulnerable scanner like Brave's, the URL is decoded and opened without confirmation, bypassing user awareness. This is particularly effective in mobile environments where QR codes are commonly shared via images, emails, or physical media. Prerequisites include internet access for the generator tool; no special credentials are needed. Expected outcomes include a scannable image that triggers redirects, potentially resulting in credential theft or device compromise.

## Requirements

1. Internet access to an online QR code generator
2. A target malicious URL (e.g., http://www.evil.com/ hosting phishing content)
3. Image viewing capability to verify the QR code

## Defense

Defensive measures and detection strategies:

- Educate users to preview QR code contents using safe scanners like Google Lens before using built-in browser tools
- Browser vendors should implement URL previews and confirmation prompts for QR scans
- Network monitoring for sudden redirects to unknown domains from mobile traffic
- Endpoint detection rules for anomalous browser navigations triggered by QR scans

## Objectives

1. Create an embeddable malicious payload in QR format for social engineering attacks
2. Enable stealthy delivery of phishing links via common image sharing
3. Facilitate automatic exploitation without user interaction beyond scanning

## Instructions

### Step 1: Select QR Code Generator Tool

**Context**: Choose a reliable online tool to encode the URL into a QR image.

Use [[tools/QR-Code-Generator]] by visiting https://app.qr-code-generator.com/.

> No command required; this is a web-based interface.

### Step 2: Input Malicious URL and Generate

**Context**: Encode the target URL to create the QR code.

Enter the malicious URL (e.g., http://www.evil.com/) in the generator's input field and select 'Generate QR Code'.

> Download the resulting PNG or similar image file.

### Step 3: Verify QR Code

**Context**: Test the QR code with a safe scanner to confirm the encoded URL without triggering the redirect.

Use [[tools/Google-Lens]] to scan; it should display the URL with a 'Go to site' option but not auto-open.

> Expected: URL preview matches the input; no automatic navigation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Phishing]] Phishing

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/QR-Code-Generator]]

## Tags

- qr-code
- phishing
