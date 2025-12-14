---
tags:
  - impact
  - ssrf
  - kubernetes
  - pdf-generator
  - internal-recon
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud
  - Kubernetes
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:54.955Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 38fa8476-15d5-47ec-9324-cd494314fbcb
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-SSRF-via-Template-Preview

## Summary

This procedure activates the PDF generator by previewing the tampered template, causing server-side execution of injected HTML to perform SSRF against internal endpoints or external redirects.

## Description

The preview function in Shopify's Packing Slip Template renders HTML to PDF, loading embedded resources server-side without client-side restrictions. Injected iframes trigger requests to internal Kubernetes services (e.g., /livez?verbose), enabling reconnaissance, while meta redirects can expose order data externally. This exploits the lack of URL validation in the renderer, applicable in cloud-hosted Shopify instances with Kubernetes backends.

## Requirements

1. Saved template with malicious payload
2. Ability to trigger PDF generation
3. Network tools to observe SSRF requests (optional, e.g., proxy)

## Defense

Defensive measures and detection strategies:

- Restrict PDF renderer to whitelisted domains only
- Block internal service access from application servers
- Log and alert on anomalous outbound requests from PDF processes

## Objectives

1. Initiate PDF rendering to execute injected code server-side
2. Achieve SSRF to internal Kubernetes endpoints
3. Observe potential data disclosure via redirects

## Instructions

### Step 1: Initiate Preview

**Context**: Use the preview feature to process the template.

No command required; click the 'Preview' button in the editor.

> Generator fetches and renders HTML. Expected output: PDF preview attempt starts.

### Step 2: Monitor SSRF Execution

**Context**: Verify requests to injected URLs occur server-side.

No command required; inspect browser network tab or server logs for requests to kubernetes.default.svc/version or external sites.

> Success if internal responses (e.g., version info) are processed. Expected output: SSRF confirmed via traces or redirects.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Impact]]
- [[ssrf]]
- [[kubernetes]]
- [[pdf-generator]]
- [[internal-recon]]
