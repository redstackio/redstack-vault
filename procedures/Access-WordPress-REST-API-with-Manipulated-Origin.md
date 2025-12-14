---
tags:
  - wordpress
  - cors-bypass
  - api-access
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-wordpress-rest-api-cors-bypass]]'
platforms:
  - Web
  - WordPress
techniques:
  - '[[Client Configurations]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: e5aaa893-33c2-4d29-9b33-c60426377686
created_at: '2025-12-14T17:29:36.425Z'
updated_at: '2025-12-14T17:29:36.425Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Client Configurations]]'
---
# Access-WordPress-REST-API-with-Manipulated-Origin

## Summary

This procedure demonstrates how to access the WordPress REST API endpoint (/wp-json/) without authentication by manipulating the Origin header to exploit CORS misconfigurations, revealing sensitive site metadata and available routes for user enumeration.

## Description

WordPress sites often expose the REST API publicly by default, allowing unauthenticated queries to /wp-json/ which returns JSON with site details, namespaces, and routes like /wp/v2/users. CORS policies, if not properly configured, fail to validate the Origin header, permitting requests from arbitrary domains. This procedure uses a local Origin (e.g., 127.0.0.1) to simulate a cross-origin attack, retrieving data that can lead to admin username disclosure and further reconnaissance.

## Requirements

1. Network access to the target WordPress site (e.g., https://blog.yelp.com)
2. curl or similar HTTP client installed
3. No authentication credentials needed

## Defense

Defensive measures and detection strategies:

- Restrict REST API access via plugins like Disable REST API or authentication requirements
- Configure strict CORS policies in .htaccess or server config to validate allowed origins
- Monitor access logs for anomalous Origin headers from non-standard IPs

## Objectives

1. Retrieve site metadata and API routes without authentication
2. Identify user enumeration endpoints for admin discovery
3. Validate CORS bypass for cross-origin exploitation

## Instructions

### Step 1: Craft and Send the Request

**Context**: Prepare a GET request to the /wp-json/ endpoint with a manipulated Origin header to bypass CORS checks and fetch initial data.

**Command** ([[commands/curl-wordpress-rest-api-cors-bypass]]):
```bash
curl -H "Origin: http://127.0.0.1:8080" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0" https://blog.yelp.com/wp-json/
```

> This command simulates a browser request from a local server, tricking the server into allowing the cross-origin response. Expected output is a JSON object with keys like 'name', 'description', 'namespaces' (including 'wp/v2'), and 'routes' listing endpoints such as /wp/v2/users.

### Step 2: Analyze Response for User Endpoints

**Context**: Parse the JSON to confirm exposure of sensitive routes, particularly those allowing user data access.

**Command** ([[commands/curl-wordpress-rest-api-cors-bypass]]):
```bash
curl -H "Origin: http://127.0.0.1:8080" https://blog.yelp.com/wp-json/wp/v2/users
```

> If the users endpoint is accessible, it returns an array of user objects with IDs, names, and slugs (usernames). Success confirms information disclosure vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Client Configurations]] Gather Victim Identity Information

### Sub-Techniques

- N/A

## Commands Used

- [[commands/curl-wordpress-rest-api-cors-bypass]]

## Tools Used

- N/A

## Tags

- [[wordpress]]
- [[cors-bypass]]
- [[api-access]]
