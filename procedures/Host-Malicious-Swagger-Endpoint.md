---
id: proc-host-malicious-swagger-endpoint
tags:
  - hosting
  - web-server
  - xss-delivery
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.379Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Host-Malicious-Swagger-Endpoint

## Summary

This procedure sets up a simple web endpoint to serve the malicious Swagger JSON file, making it accessible for loading into the target Swagger UI.

## Description

To deliver the XSS payload, the modified JSON must be hosted on a server that Swagger UI can fetch via URL. This simulates an external API documentation endpoint, allowing the vulnerable UI to pull and render the spec, triggering the reflection.

## Requirements

1. Local or cloud server capable of HTTP serving
2. Publicly accessible URL (e.g., via ngrok for local testing)
3. The crafted malicious JSON file

## Defense

Defensive measures and detection strategies:

- Monitor for anomalous JSON files on servers
- Restrict Swagger UI to load specs only from trusted domains
- Log and inspect API spec fetches for malicious content

## Objectives

1. Serve the JSON over HTTP without authentication
2. Ensure endpoint mimics a legitimate API docs URL
3. Verify accessibility from the target network

## Instructions

### Step 1: Prepare Server Directory

**Context**: Place the JSON in a web-accessible path.

Create a directory for hosting and save the malicious JSON as 'swagger.json' or similar.

### Step 2: Start Web Server

**Context**: Launch a basic HTTP server to expose the file.

Use a tool like Python's http.server: run it on port 8000, serving the directory. For public access, use ngrok to tunnel the local server.

> The endpoint URL should be something like http://yourserver.com/api-docs.

### Step 3: Test Accessibility

**Context**: Confirm the JSON can be fetched remotely.

Access the URL in a browser or via curl; it should return the JSON with the payload intact.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[hosting]]
- [[web-server]]
