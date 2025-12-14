---
id: proc-uuid-placeholder-002
tags:
  - python
  - xml-rpc
  - setup
type: procedure
tools: []
tactics: []
commands: []
verified: false
platforms:
  - Python
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-13T23:56:03.441Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
---
# Setup Vulnerable DocXMLRPCServer

## Summary

This procedure sets up a test Python XML-RPC server using the vulnerable DocXMLRPCServer module to demonstrate the reflected XSS vulnerability, allowing reproduction of CVE-2019-16935 in a controlled environment.

## Description

DocXMLRPCServer extends SimpleXMLRPCServer to provide HTML documentation. In vulnerable versions, it fails to sanitize inputs reflected into the HTML. This setup creates a minimal server exposing methods, accessible via HTTP, to test payload injection. Use for educational or proof-of-concept purposes only; patch in production.

## Requirements

1. Python 2.7 or 3.x (unpatched for vulnerability)
2. Local or remote server environment
3. Basic Python scripting knowledge

## Defense

Defensive measures and detection strategies:

- Avoid using DocXMLRPCServer in production; opt for patched versions or alternatives like Flask-RESTful
- Run servers behind authentication or firewalls
- Log all HTTP requests for anomaly detection

## Objectives

1. Deploy a functional XML-RPC server with documentation endpoint
2. Verify exposure of the vulnerable HTML generation
3. Prepare environment for XSS testing

## Instructions

### Step 1: Create Server Script

**Context**: Write a Python script to instantiate the server and register a sample method.

No command; use a text editor to create server.py:

```python
# server.py
import SimpleXMLRPCServer
from DocXMLRPCServer import DocXMLRPCServer

def hello():
    return 'Hello World'

server = DocXMLRPCServer(('0.0.0.0', 8000))
server.register_function(hello, 'hello')
print('Server starting on port 8000')
server.serve_forever()
```

> Save the file and ensure DocXMLRPCServer is available (standard library).

### Step 2: Launch the Server

**Context**: Execute the script to start listening for requests.

**Command** (python server.py):
```bash
python server.py
```

> Expected output: 'Server starting on port 8000'. Access http://localhost:8000/RPC2 to see documentation.

### Step 3: Verify Vulnerability

**Context**: Load the documentation page to confirm reflection points.

Use browser or curl to visit /RPC2 and inspect for unsanitized params.

> Success if page generates without errors and reflects query params.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- python
- xml-rpc
- setup
