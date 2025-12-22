---
data: npm install fastify @fastify/view ejs
tags:
  - install
  - dependencies
type: command
output: null
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.764Z'
id: 4716bf7d-539f-4467-ae54-19e594087d7f
verified: false
validated: true
submitted: true
---
# npm-install-fastify-deps

## Command

```bash
npm install fastify @fastify/view ejs
```

## Description

Installs the Fastify framework, @fastify/view plugin, and EJS template engine as dependencies for the vulnerable server setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| fastify | Core Fastify package | Yes |
| @fastify/view | View rendering plugin | Yes |
| ejs | EJS template engine | Yes |

## Examples

### Basic Usage

```bash
npm install fastify @fastify/view ejs
```

### Advanced Usage

```bash
npm install fastify @fastify/view ejs --save-dev
```

## Expected Output

Packages installed in node_modules; package.json updated with dependencies.

## Related

- [[Related Procedure: Setup-Vulnerable-Fastify-Environment]]
