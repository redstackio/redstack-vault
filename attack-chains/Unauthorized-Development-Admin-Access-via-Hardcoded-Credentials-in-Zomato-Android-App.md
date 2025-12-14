---
id: ac-uuid-001
tags:
  - hardcoded-credentials
  - android
  - basic-auth
  - subdomain-enumeration
  - unauthorized-access
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Android
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Decompile-Android-App-to-Uncover-Credentials]]'
  - '[[procedures/Identify-Hardcoded-HTTP-Basic-Credentials]]'
  - '[[procedures/Perform-Subdomain-Bruteforce-on-Target-Domain]]'
  - '[[procedures/Log-In-to-Discovered-Subdomain-Using-Hardcoded-Credentials]]'
step_count: 4
techniques:
  - '[[Credentials In Files]]'
  - '[[Valid Accounts]]'
  - '[[Hardware]]'
updated_at: '2025-12-14T17:24:44.669Z'
description: >-
  Multi-stage attack exploiting hardcoded HTTP basic authentication credentials
  embedded in the Zomato Android app, discovered through decompilation, leading
  to subdomain enumeration and unauthorized access to a development admin panel
  clone.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Credentials In Files]]'
  - '[[Valid Accounts]]'
  - '[[Hardware]]'
---
# Unauthorized Development Admin Access via Hardcoded Credentials in Zomato Android App

Multi-stage attack chain demonstrating the discovery and exploitation of hardcoded HTTP basic authentication credentials in the Zomato Android app, leading to unauthorized access to a development environment's admin panel clone.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Decompile App] --> B[Identify Credentials]
    B --> C[Subdomain Enumeration]
    C --> D[Unauthorized Login]
    D --> E[Access Dev Admin Panel]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/jadx]]
- [[tools/gobuster]]

### Target Environment

- Android mobile application (APK file)
- Web services on target domain (e.g., zomato.com subdomains)
- Required services/ports: HTTP/HTTPS on port 80/443
- Network access requirements: Internet access for downloading APK and enumerating subdomains

### Initial Access Requirements

- No prior credentials needed
- Network position: External attacker with public access to app download and domain
- Prior access needed: None, starts with app decompilation

## Detailed Attack Procedures

### Step 1: Decompile Android App
procedure: [[procedures/Decompile-Android-App-to-Uncover-Credentials]]

**Objective**: Reverse engineer the Android app to inspect its code and resources for potential secrets or endpoints.

**Instructions**: Obtain the Zomato APK from a trusted source like the Google Play Store or APKMirror. Use [[tools/jadx]] to decompile it into readable Java/Kotlin source code. Load the APK into jadx-gui for interactive browsing or use the CLI for batch decompilation.

```bash
jadx -d decompiled_app zomato.apk
```

Navigate through the decompiled code, focusing on network-related classes and configuration files while searching for API endpoints.

**Expected Output**: Directory structure with decompiled Java/Kotlin files, XML resources, and assets.

**Success Indicators**:
- Decompilation completes without errors
- Source code is readable and searchable

### Step 2: Identify Hardcoded Credentials
procedure: [[procedures/Identify-Hardcoded-HTTP-Basic-Credentials]]

**Objective**: Search the decompiled app code for embedded secrets, such as hardcoded authentication credentials.

**Instructions**: Use grep or the IDE's search function within the decompiled directory to look for strings like 'Authorization', 'Basic', or domain-related terms. Focus on HTTP client classes or configuration files.

```bash
grep -r "Basic\s*["']" decompiled_app/
```

Examine matches for base64-encoded credentials or plaintext usernames/passwords associated with the target domain.

**Expected Output**: Lines of code revealing credentials, e.g., hardcoded 'username:password' for a subdomain.

**Success Indicators**:
- Credentials found, e.g., for a domain returning 503 initially
- Credentials appear valid for HTTP basic auth

### Step 3: Perform Subdomain Bruteforce
procedure: [[procedures/Perform-Subdomain-Bruteforce-on-Target-Domain]]

**Objective**: Enumerate subdomains of the target domain to find ones where the discovered credentials apply.

**Instructions**: Use [[tools/gobuster]] with a wordlist to bruteforce subdomains. Start with common development-related terms like 'dev', 'admin', 'staging'.

```bash
gobuster dns -d zomato.com -w /path/to/subdomains-wordlist.txt -t 50
```

Test identified subdomains with a simple HTTP request to check for 503 or auth prompts, then apply credentials.

**Expected Output**: List of discovered subdomains, including one exposing an admin panel clone.

**Success Indicators**:
- Valid subdomain found where credentials work
- Access to a page resembling the main admin panel

### Step 4: Log In Using Hardcoded Credentials
procedure: [[procedures/Log-In-to-Discovered-Subdomain-Using-Hardcoded-Credentials]]

**Objective**: Authenticate to the discovered subdomain using the hardcoded credentials to gain unauthorized access.

**Instructions**: Use curl to test HTTP basic auth on the subdomain URL.

```bash
curl -u username:password http://discovered-subdomain.zomato.com/
```

If successful, browse the admin panel clone for development environment data.

**Expected Output**: Successful login response, e.g., HTML of the admin dashboard.

**Success Indicators**:
- 200 OK response with admin panel content
- Access to sensitive development features before shutdown

## Attack Chain Summary

### Key Achievements

1. Discovered embedded development credentials through app decompilation
2. Enumerated hidden subdomain exposing admin functionality
3. Achieved unauthorized access to dev environment
4. Prompted shutdown of vulnerable environment

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Credentials In Files]] Credentials In Files
- [[Valid Accounts]] Valid Accounts
- [[Hardware]] Gather Victim Host Information: Domain

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Reconnaissance]] Reconnaissance
- [[Discovery]] Discovery

---
*Last updated: 2023-10-01T00:00:00Z*
