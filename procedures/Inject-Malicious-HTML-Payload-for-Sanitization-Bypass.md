---
tags:
  - execution
  - html-injection
  - sanitization-bypass
  - iframe
  - ssrf
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T04:08:54.959Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 47f38abd-3a7d-43b1-9b83-4f16ea0ce6e3
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Inject-Malicious-HTML-Payload-for-Sanitization-Bypass

## Summary

This procedure crafts and inserts HTML payloads prefixed with <svg><style><h1/> to evade Shopify's iframe filter, enabling injection of malicious elements that lead to SSRF during PDF rendering.

## Description

The Shopify Packing Slip Template sanitizes plain <iframe> tags but overlooks them when obfuscated via SVG elements. By injecting such payloads targeting internal Kubernetes URLs (e.g., kubernetes.default.svc/version) or external redirects (e.g., Google via meta refresh), attackers can force server-side requests. This step requires understanding HTML structure and the filter's weaknesses, targeting web-based template editors in cloud environments.

## Requirements

1. Access to the template editor
2. Knowledge of target internal endpoints (e.g., Kubernetes services)
3. Web browser for payload testing

## Defense

Defensive measures and detection strategies:

- Enhance HTML sanitization to parse nested elements like SVG
- Validate and whitelist allowed HTML tags/attributes
- Monitor for unusual HTML patterns in template submissions

## Objectives

1. Bypass the sanitization filter with obfuscated payloads
2. Embed iframes or meta tags targeting sensitive endpoints
3. Save the template without rejection

## Instructions

### Step 1: Craft Payload

**Context**: Design HTML to prefix iframes with non-sanitized elements.

No command required; prepare strings like <svg><style><h1/><iframe src="https://kubernetes.default.svc/version" width=1001 height=1001>.

> Use large width/height to ensure rendering. Expected output: Valid HTML snippet.

### Step 2: Insert into Template

**Context**: Add the payload to the editable HTML area and save.

No command required; paste the payload into the template content field and click 'Save'.

> Filter evaded if no errors. Expected output: Template updates successfully.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Execution]]
- [[html-injection]]
- [[sanitization-bypass]]
- [[iframe]]
- [[ssrf]]
