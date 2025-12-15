---
id: cmd-basic-integration-class
data: 'classScript{ process_incoming_request({ request }){}; }'
tags:
  - integration-script
  - javascript
type: command
output: 'null'
executor: javascript
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:26.941Z'
verified: false
validated: true
submitted: true
---
# basic-integration-class-script

## Command

```javascript
classScript{ process_incoming_request({ request }){}; }
```

## Description

This basic class definition satisfies Rocket.Chat's integration script requirements, providing an empty handler for incoming requests while allowing preceding code (e.g., role adds) to execute first.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| process_incoming_request | Empty handler function for request processing | Yes |

## Examples

### Basic Usage

```javascript
classScript{ process_incoming_request({ request }){}; }
```

### Advanced Usage

Extend handler if needed: process_incoming_request({ request }){ return 'OK'; };

## Expected Output

Valid script structure; no output from empty handler, but enables overall script run.

## Related

- [[procedures/Create-Malicious-Integration-Script]]
