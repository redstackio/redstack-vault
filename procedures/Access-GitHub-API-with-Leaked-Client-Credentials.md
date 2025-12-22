---
id: 17298077-c776-4b90-ba99-638c6158df6d
name: Access-GitHub-API-with-Leaked-Client-Credentials
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:52.246442+00:00'
updated_at: '2023-04-06T03:55:52.282457+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques: []
tags:
  - '[[tags/API Key Leaks]]'
  - '[[tags/Github client id and client secret]]'
  - credential-access
  - api-authentication
commands:
  - '[[commands/curl-github-api-user-query-with-client-creds]]'
platforms:
  - Web
  - API
tools: []
validated: true
---

# Access-GitHub-API-with-Leaked-Client-Credentials

## Summary

This procedure demonstrates how to authenticate and query the GitHub API using leaked or stolen client ID and client secret credentials. These credentials, typically obtained through code vulnerabilities, social engineering, or misconfigurations, allow unauthorized access to user data, repositories, and other resources, enabling further malicious activities such as data exfiltration or repository manipulation.

## Description

GitHub API keys, including client IDs and secrets, are used for OAuth authentication in applications and integrations. If an attacker obtains these credentials—often from leaked source code, environment variables, or phishing—they can impersonate the legitimate application to interact with the GitHub API. This procedure focuses on making authenticated API requests to retrieve user information, which can reveal account details, organizations, and repositories. It assumes the attacker has already acquired the credentials and is operating from a system with network access to api.github.com. Success grants the attacker the same API permissions as the compromised application, potentially leading to broader impacts like intellectual property theft or supply chain attacks. This aligns with scenarios where credentials are harvested from files or registries but emphasizes their subsequent misuse.

## Requirements

1. Valid GitHub client ID and client secret (obtained via leakage or social engineering).
2. Network access to https://api.github.com (no firewall blocks on port 443).
3. curl tool installed (available on most Linux/macOS systems; use Invoke-WebRequest in PowerShell on Windows).
4. Basic knowledge of the target user's GitHub username for querying.

## Defense

Defensive measures and detection strategies:

- Regularly audit and rotate GitHub OAuth application credentials, especially after potential compromises.
- Enable two-factor authentication (2FA) on all GitHub accounts and monitor for unauthorized OAuth grants.
- Use GitHub's audit logs to detect anomalous API access patterns, such as queries from unfamiliar IPs.
- Implement code scanning tools (e.g., GitHub Advanced Security) to detect hardcoded credentials in repositories.
- Monitor for API rate limit exceedances or unusual user queries that indicate credential abuse.

## Objectives

1. Authenticate to the GitHub API using stolen client credentials to validate their usability.
2. Retrieve sensitive user account information, including profile details and affiliations.
3. Enable further actions like repository access or data manipulation using the authenticated session.
4. Confirm successful credential exploitation without triggering immediate alerts.

## Instructions

### Step 1: Prepare the API Query with Credentials

**Context**: Identify the target GitHub user and prepare the authentication parameters. The client ID and secret act as basic auth for OAuth apps, allowing API access without a full user login. Replace placeholders with actual leaked values to avoid invalid requests.

**Command** ([[commands/curl-github-api-user-query-with-client-creds]]):
```bash
curl 'https://api.github.com/users/$_TARGET_USERNAME?client_id=$_CLIENT_ID&client_secret=$_CLIENT_SECRET'
```

> This command sends a GET request to the GitHub API's users endpoint, authenticating via the provided client credentials. It retrieves public and private (if permitted) user data. The response will include JSON with user details if successful, or an error (e.g., 401 Unauthorized) if credentials are invalid or expired. Verify the output for fields like 'login', 'name', 'email', and 'organizations' to confirm access level.

### Step 2: Validate Response and Extract Data

**Context**: Parse the API response to confirm authentication success and extract usable information. This step ensures the credentials grant the expected permissions and identifies any rate limiting or scoping issues.

Use a JSON parser or manual inspection to review the output from Step 1.

**Command** (built-in echo or jq for parsing):
```bash
echo '$_API_RESPONSE' | jq '.login, .email'
```

> Expected: Filtered JSON showing user identifiers. If 'message' field appears with 'Bad credentials', the keys are invalid—recheck leakage source. Success here indicates viable access for chaining to other API endpoints (e.g., /user/repos).

### Step 3: Test Extended Access (Optional Escalation)

**Context**: If basic user query succeeds, test broader permissions like listing repositories to assess impact. This helps determine if the credentials allow read/write operations.

**Command** ([[commands/curl-github-api-user-query-with-client-creds]] variant):
```bash
curl 'https://api.github.com/user/repos?client_id=$_CLIENT_ID&client_secret=$_CLIENT_SECRET' -H 'Accept: application/vnd.github.v3+json'
```

> This queries the authenticated user's repositories. Expected: JSON array of repo objects if permissions allow. Errors like 403 indicate scoped limitations. Use this to map further attack paths, such as cloning private repos.
