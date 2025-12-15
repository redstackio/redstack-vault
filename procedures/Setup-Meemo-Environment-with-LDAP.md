---
tags:
  - setup
  - environment
  - ldap
  - mongodb
type: procedure
tools:
  - '[[tools/MongoDB]]'
  - '[[tools/git]]'
  - '[[tools/npm]]'
  - '[[tools/gulp]]'
  - '[[tools/node]]'
  - '[[tools/ldapjstestserver]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/start-mongodb-service]]'
  - '[[commands/create-poc-directory]]'
  - '[[commands/clone-meemo-repo]]'
  - '[[commands/install-npm-dependencies]]'
  - '[[commands/build-meemo-app]]'
  - '[[commands/start-ldap-test-server]]'
  - '[[commands/start-meemo-app-with-ldap]]'
verified: false
platforms:
  - Linux
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:30.287Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: e4c306ce-0f58-4a89-a68f-610dd42d9ac9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-Meemo-Environment-with-LDAP

## Summary

This procedure sets up a local development environment for the vulnerable meemo-app Node.js module, including MongoDB for data storage, cloning the repository, installing dependencies, building the app, and starting a simulated LDAP server and the application itself with LDAP configuration enabled, preparing for vulnerability reproduction.

## Description

The meemo app relies on MongoDB for backend storage and LDAP for user authentication. This setup simulates the vulnerable configuration where user input in profile lookups is unsanitized, allowing LDAP Injection. The environment runs on localhost with the app on port 3000 and LDAP on 3002. Prerequisites include Ubuntu or similar Linux distro with sudo access, Node.js installed, and Git. Expected outcome is a fully operational vulnerable instance ready for testing.

## Requirements

1. Linux system (Ubuntu) with administrative privileges
2. Node.js v14.2.0 or later installed
3. MongoDB installed via package manager
4. Internet access for Git clone and npm install
5. Python for later exploitation (not used here)

## Defense

Defensive measures and detection strategies:

- Use containerization (e.g., Docker) to isolate setup environments
- Monitor for unusual repository clones or service starts in logs
- Implement LDAP input validation in production apps to prevent injection

## Objectives

1. Establish a reproducible vulnerable environment
2. Enable LDAP authentication simulation
3. Prepare for DoS exploitation testing

## Instructions

### Step 1: Start MongoDB Service

**Context**: Initialize the database backend required for meemo app data storage.

**Command** ([[commands/start-mongodb-service]]):
```bash
sudo systemctl start mongod
```

> This command starts the MongoDB daemon using systemd. Expected output: Service starts silently if already running, or logs activation; verify with `sudo systemctl status mongod` showing active status.

### Step 2: Create Testing Directory

**Context**: Prepare a isolated local directory for proof-of-concept reproduction.

**Command** ([[commands/create-poc-directory]]):
```bash
mkdir poc
cd poc/
```

> Creates 'poc' directory and navigates into it. Expected output: No output; confirm with `pwd` showing /path/to/poc.

### Step 3: Clone Repository and Install Dependencies

**Context**: Obtain source code and set up Node.js modules.

**Command** ([[commands/clone-meemo-repo]]):
```bash
git clone https://github.com/nebulade/meemo.git
cd meemo
```

> Clones the repo into 'meemo' subdir and enters it. Expected output: Progress messages ending with 'Cloning into 'meemo'...'

**Command** ([[commands/install-npm-dependencies]]):
```bash
npm i
```

> Installs dependencies from package.json. Expected output: Installation logs, node_modules directory created.

### Step 4: Build the Application

**Context**: Compile and prepare the app using Gulp build task.

**Command** ([[commands/build-meemo-app]]):
```bash
./node_modules/.bin/gulp
```

> Runs the default Gulp task. Expected output: Build completion messages, no errors.

### Step 5: Start LDAP Test Server

**Context**: Simulate LDAP backend for authentication testing.

**Command** ([[commands/start-ldap-test-server]]):
```bash
node ldapjstestserver.js
```

> Executes the test server script. Expected output: Server listening on localhost:3002.

### Step 6: Start Meemo App with LDAP

**Context**: Launch the app with environment variables configuring LDAP.

**Command** ([[commands/start-meemo-app-with-ldap]]):
```bash
CLOUDRON_LDAP_BIND_DN="cn=admin,ou=users,dc=example" CLOUDRON_LDAP_BIND_PASSWORD="password" CLOUDRON_LDAP_USERS_BASE_DN="ou=users,dc=example" CLOUDRON_LDAP_URL="ldap://localhost:3002" node app.js
```

> Sets env vars and runs app.js. Expected output: App starts on http://localhost:3000, LDAP connected.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/start-mongodb-service]]
- [[commands/create-poc-directory]]
- [[commands/clone-meemo-repo]]
- [[commands/install-npm-dependencies]]
- [[commands/build-meemo-app]]
- [[commands/start-ldap-test-server]]
- [[commands/start-meemo-app-with-ldap]]

## Tools Used

- [[tools/MongoDB]]
- [[tools/git]]
- [[tools/npm]]
- [[tools/gulp]]
- [[tools/node]]
- [[tools/ldapjstestserver]]

## Tags

- setup
- environment
- ldap
- mongodb
