---
data: firebase init hosting
tags:
  - firebase
  - hosting
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.354Z'
id: b22f462a-5c2e-4afe-94cc-f66708f729f7
verified: false
validated: true
submitted: true
---
# firebase-init

## Command

```bash
firebase init hosting
```

## Description

Initializes Firebase Hosting in the current directory, prompting for project selection, public directory setup, and configuration. Used to prepare for deploying static content like malicious pages.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| hosting | Specifies hosting service | Yes (implicit) |

## Examples

### Basic Usage

```bash
firebase init hosting
```

### With Project ID

```bash
firebase init hosting --project hackerone-jm
```

## Expected Output

Interactive prompts: Select project, set public dir to ., configure as SPA (y/n). Creates firebase.json with hosting config.

## Related

- [[commands/firebase-deploy]]
- [[procedures/Deploy-Malicious-Page-to-Firebase-Hosting]]
