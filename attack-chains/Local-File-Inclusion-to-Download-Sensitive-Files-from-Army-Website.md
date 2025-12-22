---
id: ac-lfi-army-download
tags:
  - lfi
  - file-inclusion
  - web-vulnerability
  - army
  - dod
  - file-disclosure
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-LFI-via-URL-Traversal]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:22.768Z'
description: >-
  Exploitation of a Local File Inclusion vulnerability on a misconfigured U.S.
  Army website to remotely download local files, potentially exposing sensitive
  system or user information.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Local File Inclusion to Download Sensitive Files from Army Website

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via LFI Exploitation] --> B[File Disclosure]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser or [[commands/curl-fetch-url]]

### Target Environment

- Web application (e.g., U.S. Army website)
- No specific ports required beyond standard HTTP/HTTPS (80/443)
- Publicly accessible website

### Initial Access Requirements

- No credentials required
- Direct network access to the target website
- No prior access needed

## Detailed Attack Procedures

### Step 1: Exploit LFI for File Download
procedure: [[procedures/Exploit-LFI-via-URL-Traversal]]

**Objective**: Discover and exploit the LFI vulnerability by crafting a malicious URL to access and download local files from the server.

**Instructions**: Identify a parameter in the target website's URL that is vulnerable to LFI, such as a file inclusion endpoint. Craft a URL that traverses to sensitive local files like /etc/passwd or configuration files. Use [[commands/curl-fetch-url]] to fetch the content:

```bash
curl "https://target-army-site.com/include.php?file=../../../etc/passwd"
```

If successful, the response will contain the file contents. Test with null byte (%00) if path traversal is filtered:

```bash
curl "https://target-army-site.com/include.php?file=../../../etc/passwd%00"
```

**Expected Output**: Raw contents of the targeted local file displayed in the response body.

**Success Indicators**:
- Server responds with file contents instead of an error
- Sensitive data like usernames or paths are visible in the output

## Attack Chain Summary

### Key Achievements

1. Unauthorized remote access to local server files via web vulnerability
2. Potential exposure of sensitive system information
3. Demonstration of misconfiguration impact on a high-value target

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
