---
tags:
  - setup
  - concrete-cms
  - restricted-content
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:29.635Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: afec6d40-70ed-4c2c-9734-a9dbf5b1a1f8
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-Restricted-Blog-Post-with-Sensitive-Comment

## Summary

This procedure sets up a test environment in Concrete CMS by creating a blog post restricted to administrators and adding a comment with simulated sensitive data, enabling demonstration of the IDOR vulnerability's impact on PII disclosure.

## Description

In a Concrete CMS instance, authenticated administrators can create pages with permission restrictions. This procedure involves logging in as an admin, creating a new blog post, setting permissions to Administrators-only for read/write, and posting a comment under the associated conversation. The comment includes mock PII (e.g., "User: john.doe@example.com, SSN: 123-45-6789") to highlight data exposure risks. The resulting conversation ID (cnvID) is noted for subsequent exploitation. This setup requires administrative access but simulates real-world scenarios where sensitive discussions occur on private posts.

## Requirements

1. Administrative credentials for the Concrete CMS instance
2. Access to the CMS dashboard for page creation and permission management
3. A running Concrete CMS 5.7.5.7 environment on PHP 5.5

## Defense

Defensive measures and detection strategies:

- Enforce role-based access control (RBAC) on all content creation endpoints
- Log and monitor administrative actions for unusual permission changes
- Use web application firewalls (WAF) to detect anomalous content setup patterns

## Objectives

1. Establish a restricted conversation with sensitive data for testing
2. Obtain a valid cnvID for IDOR exploitation
3. Validate that the content is inaccessible via normal unauthenticated browsing

## Instructions

### Step 1: Create Restricted Blog Post

**Context**: Log in as admin and create a new page with administrator-only permissions to ensure it's protected.

Navigate to the CMS dashboard, create a new blog post page, and in the permissions settings, restrict READ and WRITE to the Administrators group only. Save the page.

### Step 2: Add Sensitive Comment

**Context**: Post a comment under the new page's conversation to introduce PII and generate a cnvID.

On the blog post page (as admin), add a comment containing sensitive data, e.g., "Test PII: Email - user@example.com, Phone - 555-1234". Submit the comment and note the generated conversation ID from the page source or backend logs.

**Expected Output**: Comment is added, and the page remains hidden from non-admin users.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[concrete-cms]]
- [[restricted-content]]
