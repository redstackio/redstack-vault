---
id: ac-idor-hackerone-embedded-forms
tags:
  - idor
  - graphql
  - reconnaissance
  - uuid
  - access-control
type: attack_chain
tools:
  - '[[tools/waybackurls]]'
tactics:
  - '[[Reconnaissance]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Private-Form-UUIDs-Using-Waybackurls]]'
  - '[[procedures/Exploit-IDOR-with-GraphQL-Queries-on-UUIDs]]'
step_count: 2
techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:30:47.014Z'
description: >-
  Multi-stage attack exploiting IDOR in HackerOne's embedded submission forms by
  discovering historical UUIDs and querying sensitive private program data via
  GraphQL.
skill_level: intermediate
impact_level: low
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# IDOR in HackerOne Embedded Submission Forms for Unauthorized Access to Private Programs

Multi-stage attack chain demonstrating a complete attack workflow exploiting insecure direct object references in HackerOne's system to access private program details.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Discover UUIDs] --> B[Exploitation: Query GraphQL]
    B --> C[Access Private Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/waybackurls]]

### Target Environment

- Web platform with GraphQL endpoints
- Access to HackerOne's public-facing embedded forms
- No special ports required; standard HTTPS (443)

### Initial Access Requirements

- Public internet access
- No credentials needed; relies on publicly archived data
- Prior knowledge of target domain (hackerone.com)

## Detailed Attack Procedures

### Step 1: Reconnaissance to Discover UUIDs
procedure: [[procedures/Discover-Private-Form-UUIDs-Using-Waybackurls]]

**Objective**: Identify UUIDs of private or inactive embedded submission forms from historical web archives.

**Instructions**: Use [[tools/waybackurls]] to fetch archived URLs from the Wayback Machine for the target domain, focusing on paths that previously hosted public embedded forms. Pipe the output to grep for UUID patterns (e.g., 32-character hex strings).

```bash
echo "https://hackerone.com" | waybackurls | grep -E '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
```

Extract and save unique UUIDs to a file for the next step.

**Expected Output**: A list of UUIDs from old, now-private form URLs.

**Success Indicators**:
- UUIDs extracted from historical URLs
- At least one UUID corresponds to a non-public form

### Step 2: Exploitation via GraphQL Queries
procedure: [[procedures/Exploit-IDOR-with-GraphQL-Queries-on-UUIDs]]

**Objective**: Use discovered UUIDs in GraphQL requests to retrieve sensitive details from private programs.

**Instructions**: Craft a GraphQL query incorporating the UUID to fetch program data. Use curl to send a POST request to the HackerOne GraphQL endpoint, including the UUID in the query variables.

```bash
curl -X POST https://hackerone.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"query": "query($uuid: ID!) { embeddedForm(uuid: $uuid) { responseEfficiencyPercentage introText structuredScopes } }", "variables": {"uuid": "discovered-uuid-here"}}'
```

Replace "discovered-uuid-here" with a UUID from Step 1. Parse the JSON response for sensitive fields.

**Expected Output**: JSON response containing private program details like response efficiency percentage, intro text, and scopes.

**Success Indicators**:
- Unauthorized data retrieved (e.g., private program info)
- No authentication errors; direct access granted

## Attack Chain Summary

### Key Achievements

1. Discovered hidden UUIDs through web archive reconnaissance
2. Bypassed access controls to query private program data via IDOR
3. Retrieved sensitive information leading to vulnerability disclosure and bounty

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Account Discovery]] Account Discovery

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Discovery]] Discovery

---

*Last updated: 2023-10-01T00:00:00Z*
