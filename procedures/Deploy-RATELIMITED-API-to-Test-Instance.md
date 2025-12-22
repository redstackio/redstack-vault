---
id: proc-uuid-1
tags:
  - setup
  - deployment
  - test-environment
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:37.401Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Deploy-RATELIMITED-API-to-Test-Instance

## Summary

This procedure sets up a local or test instance of the RATELIMITED API v3 using the open-source codebase from GitHub, enabling safe reproduction of the XSS vulnerability without affecting production systems.

## Description

The RATELIMITED API v3 is a PHP-based web application. To test the reflected XSS in the /users/[id]/set_tier endpoint, deploy the RLAPI-v3-OOP codebase. This involves cloning the repository, configuring a PHP web server, and setting up the database. The vulnerability stems from UserController.php line 93, where responses lack the proper Content-Type header, allowing JSON to be parsed as HTML.

## Requirements

1. Git access to clone the RLAPI-v3-OOP repository from GitHub
2. PHP environment (e.g., PHP 7+ with web server like Apache/Nginx)
3. Database server (e.g., MySQL) for storing user data
4. Local network access for testing

## Defense

Defensive measures and detection strategies:

- Use containerization (e.g., Docker) to isolate test environments
- Monitor for unauthorized codebase deployments via CI/CD logs
- Implement WAF rules to block anomalous setup traffic

## Objectives

1. Establish a functional replica of the vulnerable API
2. Verify endpoint accessibility
3. Prepare for authenticated testing

## Instructions

### Step 1: Clone and Install Codebase

**Context**: Retrieve the source code and set up the PHP application.

No specific command; manually clone via Git:

```bash
git clone https://github.com/repo/RLAPI-v3-OOP.git
cd RLAPI-v3-OOP
composer install  # If dependencies exist
```

> Clone the repository and install any PHP dependencies. Start the web server with `php -S localhost:8000` or configure Apache/Nginx.

### Step 2: Initialize Database

**Context**: Set up the database schema for the API.

Run database migration or import schema:

```bash
mysql -u root -p < database/schema.sql
```

> Import the database structure. Ensure the users table exists for later steps.

### Step 3: Verify Deployment

**Context**: Confirm the API is running and endpoints respond.

Use curl to test:

```bash
curl -X GET http://localhost:8000/users
```

> Expect a JSON response listing users or an auth error, indicating successful setup.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[setup]]
- [[deployment]]
