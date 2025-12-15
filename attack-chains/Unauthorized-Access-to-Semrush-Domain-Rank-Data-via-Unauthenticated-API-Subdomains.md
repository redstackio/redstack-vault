---
tags:
  - idor
  - auth-bypass
  - api
  - reconnaissance
  - semrush
type: attack_chain
tools:
  - '[[tools/Google-Search]]'
  - '[[tools/Firefox]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Google-Dorking-for-Semrush-API-Endpoints]]'
  - '[[procedures/Access-Semrush-API-Endpoints]]'
  - '[[procedures/Modify-Domain-Parameter-for-Arbitrary-Queries]]'
  - '[[procedures/Test-Semrush-Subdomains-for-Auth-Bypass]]'
step_count: 4
techniques:
  - '[[Hardware]]'
  - '[[Exploit Public-Facing Application]]'
description: >-
  Multi-stage attack exploiting lack of API key validation on Semrush regional
  subdomains to access paid domain analytics data without authentication.
skill_level: intermediate
impact_level: high
id: 46c9b1c3-ca9f-4b12-a1bc-a3965727e3fa
created_at: '2025-12-14T17:32:01.676Z'
updated_at: '2025-12-14T17:32:01.676Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
  - '[[Exploit Public-Facing Application]]'
---
# Unauthorized Access to Semrush Domain Rank Data via Unauthenticated API Subdomains

Multi-stage attack chain demonstrating unauthorized access to Semrush's paid domain rank API features through regional subdomains that lack API key enforcement, allowing free retrieval of domain analytics data via parameter manipulation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Google Dorking] --> B[Initial Access: Endpoint Discovery]
    B --> C[Execution: Parameter Manipulation]
    C --> D[Validation: Subdomain Testing]
    D --> E[Objective: Data Exfiltration]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Google-Search]]
- [[tools/Firefox]]

### Target Environment

- Web platform
- Publicly accessible Semrush API subdomains (e.g., uk.api.semrush.com, us.api.semrush.com)
- No special ports required; standard HTTPS/HTTP

### Initial Access Requirements

- Internet access for Google searching and browsing
- No credentials needed due to the authentication bypass
- Basic knowledge of URL parameter manipulation

## Detailed Attack Procedures

### Step 1: Reconnaissance via Google Dorking
procedure: [[procedures/Google-Dorking-for-Semrush-API-Endpoints]]

**Objective**: Identify publicly indexed API endpoints on Semrush subdomains to discover potential entry points for unauthorized access.

**Instructions**: Use Google Search to perform dorking with the query `site:*.api.semrush.com` to find indexed results from regional subdomains.

**Expected Output**: Search results linking to API endpoints, such as those on uk.api.semrush.com or us.api.semrush.com, displaying raw domain rank data.

**Success Indicators**:
- At least two indexed API responses visible in search results
- Endpoints return data without prompting for authentication

### Step 2: Initial Access to Discovered Endpoints
procedure: [[procedures/Access-Semrush-API-Endpoints]]

**Objective**: Load and inspect the discovered API endpoints to confirm they return sensitive domain data without requiring an API key.

**Instructions**: In Firefox, click on the Google search result links to access the endpoints directly. Observe the JSON or formatted response containing domain rank information.

**Expected Output**: API response with domain analytics data, such as rankings, organic traffic, and ad metrics for the default domain.

**Success Indicators**:
- Data loads successfully without errors or key prompts
- Response includes fields like domain name, rank, and traffic estimates

### Step 3: Execution via Parameter Manipulation
procedure: [[procedures/Modify-Domain-Parameter-for-Arbitrary-Queries]]

**Objective**: Exploit the lack of validation by altering the 'domain' parameter to query rank data for any arbitrary domain, bypassing paid access restrictions.

**Instructions**: In the browser URL, modify the 'domain' parameter, for example, change it to `hackerone.com` in `http://us.api.semrush.com/?action=report&type=domain_rank&domain=hackerone.com`. Add optional parameters like `export_columns=Db,Dn,Rk,Or,Ot,Oc,Ad,At,Ac,Sv,Sh` and `database=us` for comprehensive reports.

**Expected Output**: Updated API response with rank data for the specified domain, including detailed metrics across the chosen database.

**Success Indicators**:
- Data for the new domain is returned accurately
- No authentication errors occur during modification

### Step 4: Validation Across Subdomains
procedure: [[procedures/Test-Semrush-Subdomains-for-Auth-Bypass]]

**Objective**: Verify the vulnerability's scope by testing multiple regional subdomains and confirming the main domain enforces keys while subdomains do not.

**Instructions**: Repeat parameter modifications on other subdomains like uk.api.semrush.com and fr.api.semrush.com, using various databases (e.g., `database=us`). Test the main api.semrush.com to observe the key enforcement error.

**Expected Output**: Successful data retrieval from subdomains; error 'ERROR 120 :: WRONG KEY - ID PAIR' on the main domain without a key.

**Success Indicators**:
- Consistent bypass on regional subdomains
- Failure on main domain confirms targeted scope

## Attack Chain Summary

### Key Achievements

1. Discovered publicly indexed unauthenticated API endpoints via Google dorking
2. Accessed and manipulated parameters to retrieve paid domain rank data for arbitrary targets
3. Validated the issue across multiple regional subdomains, exposing business logic flaws

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Hardware]] Gather Victim Host Information: Domains
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance

---
*Last updated: 2023-10-01*
