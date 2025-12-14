---
id: p3c4d5e6-f7g8-9012-cdef-345678901234
name: Trigger-API-Request-to-Expose-Hashes
tags:
  - api-exposure
  - hash-extraction
  - information-disclosure
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-api-users-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:29:20.373Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Credentials In Files]]'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Trigger-API-Request-to-Expose-Hashes

## Summary

This procedure exploits the /api/users endpoint by submitting a search query, which returns all user data including password hashes due to lack of filtering, allowing collection of sensitive credentials.

## Description

The user search feature sends a GET request to /api/users with parameters like page=1 and search terms, but the backend includes password hashes in the response for all users. This can be observed via browser dev tools or replicated with curl using the admin session token. The attack scenario targets web apps with insecure API responses accessible to admins, leading to potential offline cracking if hashes are weak (e.g., MD5 or unsalted).

## Requirements

1. Admin authentication token or session cookie
2. Knowledge of the API endpoint and parameters
3. Tool for HTTP requests (browser or curl)

## Defense

Defensive measures and detection strategies:

- Remove sensitive fields like passwordHash from API responses
- Implement field-level authorization and filtering
- Monitor API calls for unusual parameter usage or high data volume
- Use strong hashing (e.g., bcrypt) and salting to mitigate cracking

## Objectives

1. Invoke the vulnerable API endpoint
2. Capture and extract password hashes
3. Enable offline analysis for weak password cracking

## Instructions

### Step 1: Prepare Search Input

**Context**: Set up minimal search parameters to trigger the full user dump.

In the search form, enter "test" in firstName and leave others blank.

### Step 2: Submit and Inspect Request

**Context**: Trigger the API call and capture the response.

Submit the form. Open browser dev tools > Network tab, filter for /api/users, and view the response JSON.

Execute [[commands/curl-api-users-request]] to replicate:

```bash
curl -H "Authorization: Bearer <admin-token>" "https://target.com/api/users?page=1&userId=&firstName=test&lastName=&email=&partnerOrg=&highSchool=" -o users.json
```

> The command fetches the response and saves it to users.json. Replace <admin-token> with the actual Bearer token from login.

### Step 3: Extract Hashes

**Context**: Parse the response for sensitive data.

Review users.json for array of user objects, each containing "passwordHash".

**Expected Output**: JSON like {"users": [{"id": 1, "firstName": "John", "passwordHash": "hashedvalue"}, ...]} with all users exposed.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques

- [[Credentials In Files]] Credentials In Files

## Commands Used

- [[commands/curl-api-users-request]]

## Tools Used

- [[tools/curl]]

## Tags

- [[api-exposure]]
- [[hash-extraction]]
- [[information-disclosure]]
