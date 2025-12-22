---
tags:
  - xss
  - execution
  - node
type: procedure
tools:
  - '[[tools/node]]'
  - '[[tools/webpack-bundle-analyzer]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/node-run-analyzer]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:36.970Z'
sub_techniques: []
id: 42102674-e52a-4882-9d1f-a407f5c6f5c7
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Run-Analyzer-on-Malicious-JSON

## Summary

This procedure executes the webpack-bundle-analyzer on a malicious stats JSON file, starting a local server that serves the vulnerable viewer interface with injected XSS payload.

## Description

The analyzer parses the provided JSON and generates an interactive treemap via a local HTTP server on port 8888. Due to unsanitized rendering in viewer.ejs, the malicious names trigger XSS upon page load. This targets a local Node.js environment, requiring the package to be installed, and results in a running server ready for browser access to execute the payload.

## Requirements

1. webpack-bundle-analyzer installed (vulnerable version)
2. Malicious poc.json file present
3. Node.js executable in PATH

## Defense

Defensive measures and detection strategies:

- Upgrade to webpack-bundle-analyzer >=3.3.2
- Run analyzer in isolated environments (e.g., Docker)
- Monitor local port 8888 for unexpected server startups

## Objectives

1. Parse malicious JSON and start local visualization server
2. Inject payload into generated HTML without detection
3. Prepare for browser-based execution

## Instructions

### Step 1: Launch the Analyzer

**Context**: Runs the analyzer binary with the malicious input to initiate the vulnerable server.

**Command** ([[commands/node-run-analyzer]]):
```bash
node ./node_modules/webpack-bundle-analyzer/lib/bin/analyzer.js poc.json
```

> This starts the server at http://127.0.0.1:8888. Expected output: "Webpack Bundle Analyzer is started at http://127.0.0.1:8888\nUse Ctrl+C to close it". The payload is now embedded in the served content.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/node-run-analyzer]]

## Tools Used

- [[tools/node]]
- [[tools/webpack-bundle-analyzer]]

## Tags

- xss
- execution
- node
