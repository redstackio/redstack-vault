---
id: proc-uuid-placeholder
tags:
  - idor
  - api
  - cloning
  - persistence
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/patch-agent-config-clone]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:35.719Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Account Manipulation]]'
  - '[[Valid Accounts]]'
---
# Clone-Admin-Agent-via-SID-Overwrite

## Summary

This procedure exploits an Insecure Direct Object Reference (IDOR) vulnerability in the Dust platform's agent configuration PATCH endpoint, allowing an authenticated member to overwrite the SID parameter of their newly created agent with an admin-owned agent's SID (e.g., 'gemini-pro'), effectively cloning it and persisting access to restricted AI models even after admin disablement.

## Description

In the Dust dashboard, agents represent configurable AI assistants backed by specific models. Admins manage global or workspace-owned agents, including enabling/disabling them. The vulnerability stems from insufficient validation in the PATCH /api/w/{w_id}/assistant/agent_configurations/{agent-id} endpoint, where the 'sid' field can be arbitrarily set without ownership checks. An attacker with member privileges creates a new agent, then patches its configuration to reference an admin SID, cloning the agent's capabilities. This leads to privilege persistence as the clone remains functional post-disablement of the original, undermining admin controls over resources like premium AI models.

## Requirements

1. Authenticated member access to a Dust workspace
2. Knowledge of an admin agent's SID (e.g., 'gemini-pro', discoverable via dashboard inspection or prior recon)
3. API client (e.g., curl) or browser dev tools for sending PATCH requests
4. Workspace ID (w_id) from the URL or API

## Defense

Defensive measures and detection strategies:

- Implement ownership validation on SID updates in PATCH endpoints to restrict edits to owned agents only
- Audit logs for SID changes and cross-reference with user permissions
- Rate-limit or monitor agent creation and configuration updates for anomalies
- Use RBAC to enforce scoped access to global/admin agents

## Objectives

1. Clone an admin-controlled agent to gain unauthorized access to its underlying resources
2. Persist usage of the agent beyond admin revocation
3. Demonstrate breakdown in access controls for AI model management

## Instructions

### Step 1: Create Base Agent

**Context**: Establish a controllable agent as the cloning target.

**Instructions**: Log in as member and create a new agent via dashboard. Note the {agent-id}.

### Step 2: Identify Target SID

**Context**: Determine the SID of the admin agent to clone (e.g., inspect network requests or dashboard for 'gemini-pro').

### Step 3: Execute IDOR PATCH

**Context**: Send the PATCH request to overwrite the SID, cloning the admin agent.

**Command** ([[commands/patch-agent-config-clone]]):
```bash
curl -X PATCH https://eu.dust.tt/api/w/BSsJ1zPUYE/assistant/agent_configurations/JpY5xizXRo \
  -H "Content-Type: application/json" \
  -H "Cookie: redacted" \
  -d '{"assistant":{"name":"gemini-pro-clone","pictureUrl":"https://dust.tt/static/emojis/bg-blue-300/brain/1f9e0","description":"An assistant designed to provide clear, concise, and factual responses efficiently.","instructions":"test-gemini-pro","status":"active","scope":"private","actions":[],"model":{"modelId":"claude-3-5-sonnet-20241022","providerId":"anthropic","temperature":0.7},"maxStepsPerRun":8,"visualizationEnabled":true,"templateId":null,"tags":[]}}'
```

> This command updates the agent's configuration, overriding the SID to 'gemini-pro'. Expected output: 200 OK with updated config. The clone now inherits the admin agent's model access.

### Step 4: Verify Cloning

**Context**: Test the cloned agent to confirm functionality.

**Instructions**: Use the cloned agent in the dashboard to run a query; it should invoke the target model.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence
- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Account Manipulation]] Account Manipulation
- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/patch-agent-config-clone]]

## Tools Used


## Tags

- idor
- api
- cloning
- persistence
