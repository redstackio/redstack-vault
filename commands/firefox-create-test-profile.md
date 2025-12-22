---
id: added-uuid-create-profile
name: firefox-create-test-profile
type: command
executor: bash
data: firefox -CreateProfile "Test" .\\test_profile
output: null
created_at: '2023-04-06T03:56:17.501365+00:00'
updated_at: '2023-04-06T03:56:17.513906+00:00'
platforms:
  - Windows
tags:
  - profile-creation
  - firefox
verified: true
validated: true
---

# firefox-create-test-profile

## Command

```bash
firefox -CreateProfile "Test" .\\test_profile
```

## Description

This command creates a new Firefox user profile named 'Test' in the specified directory. Profiles allow isolated browsing sessions with custom settings, useful for testing or attack isolation without affecting the default profile.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -CreateProfile | Flag to create a new profile | Yes |
| "Test" | Name of the profile to create | Yes |
| .\\test_profile | Path to store the profile files (relative or absolute) | Yes |

## Examples

### Basic Usage

```bash
firefox -CreateProfile "Test" .\\test_profile
```

### Advanced Usage

```bash
firefox -CreateProfile "AttackProfile" C:\\Users\\User\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\attack
```

## Expected Output

Firefox executable runs briefly and exits without errors. A new directory (e.g., test_profile) is created containing files like profiles.ini. No stdout output; verify via file system: the directory should exist with subfolders like 'extensions' and 'prefs.js'.

## Related

- [[commands/firefox-open-irc-with-test-profile]]
- [[procedures/Application-Escape-and-Breakout-via-Unassociated-Protocols-in-Firefox]]
