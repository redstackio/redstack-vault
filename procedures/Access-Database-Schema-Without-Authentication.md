---
id: proc-unauth-db-access
tags:
  - access-control
  - authentication-bypass
  - database-exposure
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-access-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:11.303Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Database-Schema-Without-Authentication

## Summary

This procedure exploits an improper access control vulnerability in a web application to view the entire backend database schema, including all tables and columns, without any authentication. It targets unprotected endpoints that expose sensitive structural information, rated as medium severity due to potential for further attacks like targeted SQL injection.

## Description

In this attack scenario, the target is a web application from the U.S. Department of Defense, where the endpoint https://█████████/schema/columns.byTable.html lacks authentication or authorization checks. An attacker simply visits the URL to retrieve an HTML page detailing the database structure. This exposure reveals sensitive details such as table names, column types, and relationships, which could aid in crafting more sophisticated exploits. The procedure requires only HTTP access and no prior credentials, making it accessible to beginners. Expected outcomes include full visibility into the backend, enabling reconnaissance for deeper vulnerabilities.

## Requirements

1. Network connectivity to the target web application (public-facing URL)
2. Standard HTTP client (browser or curl; no special tools needed)
3. No authentication credentials or prior access

## Defense

Defensive measures and detection strategies:

- Implement proper authentication and authorization on all admin or schema-related endpoints using frameworks like OAuth or JWT
- Use web application firewalls (WAF) to block access to sensitive paths like /schema/
- Monitor access logs for anomalous requests to internal endpoints and enable rate limiting
- Conduct regular access control audits and apply least-privilege principles to database interfaces

## Objectives

1. Retrieve unauthorized database schema to understand backend structure
2. Identify potential sensitive data locations for follow-on attacks
3. Validate the presence of access control flaws in the application

## Instructions

### Step 1: Direct Endpoint Access

**Context**: Navigate to the vulnerable URL to fetch the database schema without triggering any auth checks, confirming the improper access control.

**Command** ([[commands/curl-access-endpoint]]):
```bash
curl -X GET "https://█████████/schema/columns.byTable.html" -o schema.html
```

> This command sends a GET request to the endpoint and saves the response to a file for inspection. Expected output is an HTML document listing all tables (e.g., users, logs) with their columns (e.g., id, username, email), revealing the database layout without errors or redirects.

### Step 2: Verify Exposure

**Context**: Open the retrieved file or response in a browser/editor to confirm sensitive details are exposed, such as column names indicating PII or confidential data.

**Command** (Manual inspection; no command needed):

> Review the HTML for table structures. Success is indicated by visible schema details without login prompts.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-endpoint]]

## Tools Used


## Tags

- access-control
- authentication-bypass
- database-exposure
