---
tags:
  - information-disclosure
  - google-dorking
  - sso
  - reconnaissance
type: attack_chain
tools:
  - '[[tools/Google-Search]]'
  - '[[tools/Google-Chrome]]'
  - '[[tools/Google-Toolbar]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/google-dork-query]]'
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Perform-Google-Search-for-Indexed-SSO-URLs]]'
  - '[[procedures/Analyze-Search-Results-for-Valid-Login-Names]]'
step_count: 2
techniques:
  - '[[Search Open Websites-Domains]]'
description: >-
  Exploiting an information disclosure vulnerability in an SSO gateway by
  leveraging Google search to retrieve indexed internal URLs containing valid
  employee login names.
skill_level: beginner
impact_level: medium
id: d3436f22-5d72-49f5-bc03-d64f2beeb392
created_at: '2025-12-13T09:01:26.446Z'
updated_at: '2025-12-13T09:01:26.446Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Search Open Websites-Domains]]'
---
# Information Disclosure via Google Indexing of SSO Login Names

Multi-stage attack chain demonstrating how to exploit an information disclosure vulnerability on an SSO gateway domain due to the absence of a robots.txt file, allowing web crawlers to index internal URLs with valid employee login names.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance via Google Search] --> B[Analysis of Search Results]
    B --> C[Exposure of Login Names]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Google-Search]]
- [[tools/Google-Chrome]] (optional, for understanding indexing mechanism)
- [[tools/Google-Toolbar]] (optional, for understanding indexing mechanism)

### Target Environment

- Web-based SSO gateway
- Required services/ports: HTTP/HTTPS on the target domain
- Network access requirements: Public internet access to Google Search

### Initial Access Requirements

- No credentials required
- Public network position
- No prior access needed

## Detailed Attack Procedures

### Step 1: Perform Google Search for Indexed SSO URLs
procedure: [[procedures/Perform-Google-Search-for-Indexed-SSO-URLs]]

**Objective**: Identify indexed internal URLs from the SSO domain that have been inadvertently exposed to Google.

**Instructions**: Use [[commands/google-dork-query]] to search for the specific site:

```bash
echo "site:██████████&filter=0" | xargs -I {} curl -s "https://www.google.com/search?q={}"
```

Alternatively, perform the search directly in a web browser using the query 'site:██████████&filter=0' to retrieve URLs structured as https://████/people/[username].

**Expected Output**: A list of Google search results showing indexed URLs with usernames.

**Success Indicators**:
- Indexed URLs appear in search results
- URLs contain patterns like /people/[username]

### Step 2: Analyze Search Results for Valid Login Names
procedure: [[procedures/Analyze-Search-Results-for-Valid-Login-Names]]

**Objective**: Extract and validate the login names from the search results to identify valid SSO accounts.

**Instructions**: Review the Google SERP results manually or script the extraction. For example, parse the results for usernames like alice_brown, which correspond to valid SSO accounts and email addresses. No specific command is needed, but you can use tools like grep on saved results:

```bash
grep -oE 'https://████/people/[a-z_]+' results.html
```

**Expected Output**: A list of extracted usernames such as alice_brown.

**Success Indicators**:
- Valid usernames extracted
- Confirmation that usernames map to email formats (e.g., alice_brown@airbnb.com)

## Attack Chain Summary

### Key Achievements

1. Discovery of indexed internal SSO URLs via Google
2. Extraction of valid employee login names
3. Potential for further attacks like password guessing or social engineering

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Search Open Websites-Domains]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]

*Last updated: 2023-10-01*
