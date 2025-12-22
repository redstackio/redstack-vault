---
id: ac-uuid-placeholder
tags:
  - information-disclosure
  - path-disclosure
  - web-vulnerability
  - flask
  - django
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Flask-Doc-Site-for-Path-Disclosure]]'
  - '[[procedures/Access-Django-Doc-Site-for-Path-Disclosure]]'
step_count: 2
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:00.616Z'
description: >-
  A simple information disclosure attack revealing non-sensitive server paths by
  accessing public documentation sites for Flask and Django hosted by Aspen,
  observed in error responses or page sources.
skill_level: beginner
impact_level: low
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Server Path Disclosure on Aspen Flask and Django Documentation Sites

Multi-stage attack chain demonstrating a complete attack workflow for identifying server path disclosures on public web documentation sites.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Flask Site] --> B[Observe Path Disclosure]
    B --> C[Access Django Site]
    C --> D[Observe Path Disclosure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser or [[commands/curl-fetch-url]]

### Target Environment

- Web platform
- Publicly accessible documentation sites
- No authentication required

### Initial Access Requirements

- Internet access
- No credentials needed
- Direct public URL access

## Detailed Attack Procedures

### Step 1: Access Flask Documentation Site
procedure: [[procedures/Access-Flask-Doc-Site-for-Path-Disclosure]]

**Objective**: Navigate to the Flask documentation site to trigger and observe server path disclosure in responses.

**Instructions**: Use [[commands/curl-fetch-url]] to retrieve the page content and inspect for disclosed paths:

```bash
curl -s http://flask.aspen.io/en/latest/ | grep -i path
```

Alternatively, open the URL in a browser and check error messages or page source for internal file paths like /var/www or similar non-sensitive directories.

**Expected Output**: Response containing error messages or source code revealing server paths, e.g., "/usr/local/lib/python3.x/site-packages/flask/...".

**Success Indicators**:
- Internal server paths visible in response or source
- No sensitive data like credentials exposed

### Step 2: Access Django Documentation Site
procedure: [[procedures/Access-Django-Doc-Site-for-Path-Disclosure]]

**Objective**: Navigate to the Django documentation site to trigger and observe server path disclosure in responses.

**Instructions**: Use [[commands/curl-fetch-url]] to retrieve the page content and inspect for disclosed paths:

```bash
curl -s http://django.aspen.io/en/latest/ | grep -i path
```

Alternatively, open the URL in a browser and check error messages or page source for internal file paths.

**Expected Output**: Response containing error messages or source code revealing server paths, e.g., "/usr/local/lib/python3.x/site-packages/django/...".

**Success Indicators**:
- Internal server paths visible in response or source
- Confirmation of similar disclosure pattern as Flask site

## Attack Chain Summary

### Key Achievements

1. Identified server path disclosures on two public documentation sites
2. Confirmed minimal impact with no sensitive information leaked
3. Demonstrated potential for reconnaissance in Python-based web environments

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
