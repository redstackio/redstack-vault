---
id: ac-hackerone-idor-hackathons
tags:
  - idor
  - web
  - discovery
  - hackerone
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-IDOR-in-HackerOne-Bugs-Hackathons-Parameter]]'
step_count: 3
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:33.538Z'
description: >-
  Multi-stage attack exploiting an Insecure Direct Object Reference (IDOR) in
  the HackerOne /bugs endpoint to infer the active date ranges of private
  hackathons by analyzing submission dates of filtered reports.
skill_level: intermediate
impact_level: low
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# IDOR in HackerOne Bugs Endpoint to Infer Private Hackathon Date Ranges

Multi-stage attack chain demonstrating a complete attack workflow exploiting an IDOR vulnerability in HackerOne's bug reporting platform.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Bugs Endpoint] --> B[Inject Private Hackathon IDs]
    B --> C[Analyze Submission Dates]
    C --> D[Infer Hackathon Period]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser or [[commands/curl-query-hackerone-bugs]]

### Target Environment

- HackerOne platform (web application)
- No specific ports or services required beyond standard HTTPS access
- Network access to https://hackerone.com

### Initial Access Requirements

- Public access to HackerOne (no authentication needed for /bugs endpoint filters)
- Knowledge of hackathon IDs (public ones can be enumerated, private ones guessed or known from other sources)

## Detailed Attack Procedures

### Step 1: Access the Bugs Overview Endpoint
procedure: [[procedures/Exploit-IDOR-in-HackerOne-Bugs-Hackathons-Parameter]]

**Objective**: Gain access to the /bugs endpoint and apply basic filters to understand the response structure.

**Instructions**: Navigate to the HackerOne /bugs page or use a tool to query the endpoint with initial filters like subject=security to retrieve public bug reports.

Use [[commands/curl-query-hackerone-bugs]] for programmatic access:

```bash
curl "https://hackerone.com/bugs?subject=security" -o bugs_response.html
```

**Expected Output**: HTML or JSON response containing a list of bug reports with submission dates.

**Success Indicators**:
- Successful retrieval of bug reports
- Visible submission dates in the response

### Step 2: Inject Hackathon IDs Including Private Ones
procedure: [[procedures/Exploit-IDOR-in-HackerOne-Bugs-Hackathons-Parameter]]

**Objective**: Exploit the IDOR by including private hackathon IDs in the hackathons[] parameter to apply unauthorized filters.

**Instructions**: Modify the query to include an array of hackathon IDs, such as public ID 28 and a suspected private ID. The endpoint accepts the array without access validation, applying a date range filter based on the private hackathon's period.

Execute with [[commands/curl-query-hackerone-bugs]]:

```bash
curl "https://hackerone.com/bugs?subject=security&hackathons[]=28&hackathons[]=999" -o filtered_bugs.html
```

Replace 999 with a private hackathon ID.

**Expected Output**: Filtered bug reports from the date range of the private hackathon, even if the user lacks access.

**Success Indicators**:
- Response includes reports only from a specific date range
- No access denied errors for private IDs

### Step 3: Analyze Returned Reports for Date Extremes
procedure: [[procedures/Exploit-IDOR-in-HackerOne-Bugs-Hackathons-Parameter]]

**Objective**: Examine the submission dates of the returned reports to infer the active period of the private hackathon.

**Instructions**: Parse the response to identify the earliest and latest submission dates. These extremes correspond to the hackathon's start and end dates. This is more effective if the program has reports submitted on various days.

Manually inspect the HTML or use scripting to extract dates from the response file.

**Expected Output**: Identified min and max submission dates revealing the hackathon's date range.

**Success Indicators**:
- Clear date range inferred from report dates
- Correlation with known public hackathon periods for validation

## Attack Chain Summary

### Key Achievements

1. Unauthorized application of private hackathon filters via IDOR
2. Inference of private hackathon active periods through date analysis
3. Demonstration of missing access controls in the /bugs endpoint

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---

*Last updated: 2023-10-01T00:00:00Z*
