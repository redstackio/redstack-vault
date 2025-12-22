---
id: ac-graphql-batch-bypass-001
tags:
  - graphql
  - rate-limit-bypass
  - dos
  - api-abuse
  - race-condition
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Turbo-Intruder]]'
  - '[[tools/Python]]'
  - '[[tools/race-single-packet-attack.py]]'
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-Intercepted-Request-in-Burp-Suite]]'
  - '[[procedures/Generate-Batched-GraphQL-Mutation]]'
  - '[[procedures/Configure-and-Execute-Turbo-Intruder-Race-Attack]]'
  - '[[procedures/Verify-Bulk-Report-Creation]]'
step_count: 4
techniques:
  - '[[Network Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:57.230Z'
description: >-
  Multi-stage attack exploiting GraphQL named-based batching in HackerOne's API
  to create thousands of reports, bypassing the 500-report-per-24-hours limit
  and enabling spam/DoS.
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Bypass HackerOne Report Rate Limit via GraphQL Batching and Race Condition

Multi-stage attack chain demonstrating exploitation of HackerOne's GraphQL API to bypass rate limits on report creation, allowing spam of over 6400 reports in 40 seconds.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~40 seconds |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Request] --> B[Generate Batch Query]
    B --> C[Race Condition Attack]
    C --> D[Verify Spam]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- [[tools/Turbo-Intruder]]
- [[tools/Python]]
- [[tools/race-single-packet-attack.py]]

### Target Environment

- HackerOne Platform (Web API)
- GraphQL endpoint at /graphql
- HTTP/2 support
- Valid user authentication (HackerOne cookie and CSRF token)

### Initial Access Requirements

- Authenticated HackerOne account with report submission privileges
- Network access to hackerone.com
- No prior elevated access needed; exploits public-facing API

## Detailed Attack Procedures

### Step 1: Setup Intercepted Request
procedure: [[procedures/Setup-Intercepted-Request-in-Burp-Suite]]

**Objective**: Prepare the base HTTP request for GraphQL mutation in Burp Suite, replacing placeholders with user-specific values.

**Instructions**: Launch Burp Suite and intercept a sample POST request to /graphql. Update the Cookie with your HackerOne session cookie, X-CSRF-Token with your CSRF token, and team_handle with the target program's handle. Include placeholders for the batched query.

**Expected Output**: Modified HTTP request ready for forwarding, with JSON payload containing operationName 'CreateReport' and variables for team_handle, product_area, and product_feature.

**Success Indicators**:
- Request body validates as proper JSON
- Placeholders correctly substituted without syntax errors

### Step 2: Generate Batched Query
procedure: [[procedures/Generate-Batched-GraphQL-Mutation]]

**Objective**: Use Python to craft a GraphQL mutation with 75 named createReport operations for batching.

**Instructions**: Run the Python script to generate the mutation string. Execute [[commands/generate-batched-graphql-query]] with range(75) to produce 75 batched operations, each including title, vulnerability_information, impact, and source. Insert the output as the query placeholder in the HTTP request.

```python
def generate_query(index): return('example'+str(index)+': createReport(input: {team_handle: $team_handle, ' + 'title: "Your Report Title", vulnerability_information: "Vulnerability Information", ' + 'impact: "Impact Description", source: "Report Source"}) { ' + 'was_successful errors { edges { node { id error_code field message __typename } __typename } ' + '__typename } } }')
queries =[]
for i in range(75):
    queries.append(generate_query(i))
main_mutation =('mutation BulkReports($team_handle: String!) {\n ' + '\n '.join(queries) + '\n}')
print(repr(main_mutation).replace('"','\\"').replace("'",""))
```

**Expected Output**: Escaped string of the full batched mutation query for JSON insertion.

**Success Indicators**:
- Query string contains 75 unique named operations (e.g., example0 to example74)
- No syntax errors in GraphQL format

### Step 3: Execute Race Condition Attack
procedure: [[procedures/Configure-and-Execute-Turbo-Intruder-Race-Attack]]

**Objective**: Forward the request to Turbo Intruder and run a race condition script to repeat it 100 times rapidly, creating ~7500 report attempts.

**Instructions**: From Burp Suite, send the modified request to Turbo Intruder. Load [[tools/race-single-packet-attack.py]] and adjust the loop to 100 iterations. Start the attack to send batched requests in quick succession, exploiting the lack of per-mutation limits.

**Expected Output**: Turbo Intruder console shows 100 requests sent, with many succeeding in creating 75 reports each.

**Success Indicators**:
- Requests complete in ~40 seconds
- No immediate rate limit errors due to batching

### Step 4: Verify Bulk Report Creation
procedure: [[procedures/Verify-Bulk-Report-Creation]]

**Objective**: Confirm the bypass by checking the target team's reports page for spam.

**Instructions**: After the attack completes, open a web browser, navigate to the HackerOne team reports page, and refresh. Use [[commands/post-batched-report-request]] manually if needed for single verification, but primarily observe the bulk results.

**Expected Output**: Over 6400 reports visible on the target's inbox, exceeding the 500 limit.

**Success Indicators**:
- Reports page shows thousands of new entries with the batched content
- No single-request limits enforced on batched mutations

## Attack Chain Summary

### Key Achievements

1. Bypassed 500-report daily limit using GraphQL batching up to 75 per request
2. Amplified via race condition to create 6400+ reports in 40 seconds
3. Demonstrated potential for DoS via spam on any HackerOne program

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Impact]] Impact

---
*Last updated: 2023-10-01T00:00:00Z*
