---
tags:
  - setup
  - poc
  - node.js
  - express
type: procedure
tools:
  - '[[tools/npm]]'
  - '[[tools/node]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/mkdir-poc-directory]]'
  - '[[commands/cd-poc-directory]]'
  - '[[commands/npm-init-project]]'
  - '[[commands/npm-install-express]]'
  - '[[commands/npm-install-sequelize]]'
  - '[[commands/npm-install-sqlite3]]'
  - '[[commands/npm-install-express-laravel-passport]]'
  - '[[commands/node-run-app]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:31:19.043Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 2fa6695e-e033-4c62-a73f-4d88215c11ac
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Setup-Vulnerable-Express-App-with-express-laravel-passport

## Summary

This procedure sets up a proof-of-concept Node.js Express application using the vulnerable express-laravel-passport module, Sequelize ORM, and in-memory SQLite to simulate the authentication middleware flaw for testing JWT forgery.

## Description

The express-laravel-passport module (v1.1.2) implements Laravel Passport-like auth for Express but fails to verify JWT signatures, using only jwt.decode. This procedure creates an app that defines an oauth_access_tokens model, syncs an in-memory DB with test data (e.g., tokens with jti=1 and jti=2), and applies the middleware to a root route that logs the user_id from the token payload. The setup allows demonstration of the vulnerability in a controlled local environment.

## Requirements

1. Node.js installed (v8+ recommended)
2. npm package manager
3. Local port 3000 free
4. Basic knowledge of Node.js and Express

## Defense

Defensive measures and detection strategies:

- Always use jwt.verify() instead of jwt.decode() in auth middleware
- Implement token blacklisting and expiration checks
- Monitor for anomalous user_id logs in access tokens
- Use signed and encrypted JWTs with strong secrets

## Objectives

1. Establish a reproducible environment for the vulnerability
2. Simulate database-backed token validation
3. Prepare for JWT testing without signature enforcement

## Instructions

### Step 1: Create Project Directory

**Context**: Initialize the file system structure for the PoC.

**Command** ([[commands/mkdir-poc-directory]]):
```bash
mkdir poc
```

> Creates a new directory named 'poc' for the test environment.

### Step 2: Enter Directory and Initialize npm

**Context**: Set up the npm project to manage dependencies.

**Command** ([[commands/cd-poc-directory]]):
```bash
cd poc/
```

> Changes into the poc directory.

**Command** ([[commands/npm-init-project]]):
```bash
npm init -y
```

> Generates package.json for the project.

### Step 3: Install Dependencies

**Context**: Add required packages for the Express app, DB, and vulnerable module.

**Command** ([[commands/npm-install-express]]):
```bash
npm i express
```

> Installs Express framework.

**Command** ([[commands/npm-install-sequelize]]):
```bash
npm i sequelize@4.32.7
```

> Installs specific Sequelize version for ORM.

**Command** ([[commands/npm-install-sqlite3]]):
```bash
npm i sqlite3
```

> Installs SQLite driver for in-memory DB.

**Command** ([[commands/npm-install-express-laravel-passport]]):
```bash
npm i express-laravel-passport
```

> Installs the vulnerable module (v1.1.2).

### Step 4: Create Application Code

**Context**: Define the Express app in index.js with DB setup and middleware.

No command; manually create index.js with content simulating oauth_access_tokens model, sequelize.sync(), test data insertion, and app.use('/laravel-passport', require('express-laravel-passport')()) on GET '/' route logging req.user_id.

### Step 5: Run the Application

**Context**: Start the server to host the vulnerable endpoint.

**Command** ([[commands/node-run-app]]):
```bash
node index.js
```

> Launches the Express server on port 3000.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/mkdir-poc-directory]]
- [[commands/cd-poc-directory]]
- [[commands/npm-init-project]]
- [[commands/npm-install-express]]
- [[commands/npm-install-sequelize]]
- [[commands/npm-install-sqlite3]]
- [[commands/npm-install-express-laravel-passport]]
- [[commands/node-run-app]]

## Tools Used

- [[tools/npm]]
- [[tools/node]]

## Tags

- setup
- poc
- node.js
- express
