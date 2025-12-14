---
id: proc-nextcloud-analyze-filters
tags:
  - ssrf
  - code-review
  - nextcloud
  - php
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T03:53:38.313Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Analyze Nextcloud preventLocalAddress Function

## Summary

This procedure involves reviewing the Nextcloud preventLocalAddress (ThrowIfLocalAddress) function to identify deficiencies in SSRF protection, specifically gaps in local domain and IP range validation that allow bypasses to cloud metadata services.

## Description

In a code review scenario targeting Nextcloud hosted on cloud platforms, examine the function responsible for blocking local addresses. The function checks for localhost, .local, .localhost suffixes, hostname-only names, and uses PHP's filter_var with FILTER_FLAG_NO_PRIV_RANGE and FILTER_FLAG_NO_RES_RANGE for IP validation. However, it fails to block cloud-specific endpoints like http://metadata.google.internal/ (Google Cloud) or 100.100.100.200 (Alibaba Cloud), enabling SSRF to internal services. This procedure outlines manual code inspection to document these weaknesses, applicable in vulnerability research or pentesting.

## Requirements

1. Access to Nextcloud source code (Git repository or deployed files).
2. Basic PHP knowledge for understanding filter_var and domain parsing logic.
3. Code editor for navigation and annotation.

## Defense

Defensive measures and detection strategies:

- Implement comprehensive URL allowlisting instead of just blacklisting local patterns.
- Use cloud-specific WAF rules to block metadata endpoint requests.
- Monitor application logs for anomalous internal URL access attempts.

## Objectives

1. Map out all validation checks in preventLocalAddress.
2. Identify unblocked cloud metadata paths.
3. Document potential SSRF vectors for reporting or patching.

## Instructions

### Step 1: Locate and Open the Function

**Context**: Find the preventLocalAddress or ThrowIfLocalAddress function in the Nextcloud codebase to begin analysis.

Navigate to the lib/private/Http/Client/Client.php or relevant files handling URL validation. Search for 'preventLocalAddress' or 'ThrowIfLocalAddress' using your IDE's search functionality.

### Step 2: Examine Domain and Hostname Checks

**Context**: Review string-based filters for common local indicators.

Inspect code lines checking for 'localhost', '.local', '.localhost' substrings, and hostname-only validation (e.g., no dots in hostname). Note that these are case-sensitive and do not cover internal cloud domains like 'metadata.google.internal'.

### Step 3: Analyze IP Range Filtering

**Context**: Evaluate PHP filter_var usage for IP blocking.

Look for filter_var calls with FILTER_VALIDATE_URL or FILTER_VALIDATE_IP, flagged with FILTER_FLAG_NO_PRIV_RANGE (blocks 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) and FILTER_FLAG_NO_RES_RANGE (blocks 127.0.0.0/8, etc.). Confirm that Alibaba's 100.100.100.200 (documentation IP range) is not covered, allowing bypass.

### Step 4: Document Gaps

**Context**: Compile findings on bypassed endpoints.

Create notes or a report highlighting that http://metadata.google.internal/ passes domain checks (no .local suffix) and resolves to internal IPs not flagged by the filters.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssrf]]
- [[code-review]]
- [[nextcloud]]
- [[php]]
