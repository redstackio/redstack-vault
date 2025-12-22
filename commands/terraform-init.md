---
id: 6323d1e8-02c6-452b-9618-28fba8eb8d2a
name: terraform-init
type: command
executor: bash
data: terraform init
output: >-
  Initializing the backend...


  Initializing provider plugins...

  - Checking for available provider plugins...

  - Downloading plugin for provider "aws" (hashicorp/aws) 2.31.0...


  The following providers do not have any version constraints in configuration,

  so the latest version was installed.


  To prevent automatic upgrades to new major versions that may contain breaking

  changes, it is recommended to add version = "..." constraints to the

  corresponding provider blocks in configuration, with the constraint strings

  suggested below.


  * provider.aws: version = "~> 2.31"


  Terraform has been successfully initialized!


  You may now begin working with Terraform. Try running "terraform plan" to see

  any changes that are required for your infrastructure. All Terraform commands

  should now work.


  If you ever set or change modules or backend configuration for Terraform,

  rerun this command to reinitialize your working directory. If you forget,
  other

  commands will detect it and remind you to do so if necessary.
created_at: '2019-10-10T18:18:30.568376+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - terraform
  - cloud
  - infrastructure
verified: true
validated: true
---

# terraform-init

## Command

```bash
terraform init
```

## Description

Initializes a Terraform working directory by downloading required provider plugins (e.g., AWS) and setting up the backend. Use this before applying any configuration to prepare the environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; run in the directory containing .tf files | Yes |

## Examples

### Basic Usage

```bash
terraform init
```

Run this in your project directory to fetch providers.

### Advanced Usage

```bash
terraform init -upgrade
```

Upgrades existing providers to the latest compatible versions.

## Expected Output

Initializing the backend...

Initializing provider plugins...
- Checking for available provider plugins...
- Downloading plugin for provider "aws" (hashicorp/aws) 2.31.0...

The following providers do not have any version constraints in configuration,
so the latest version was installed.

To prevent automatic upgrades to new major versions that may contain breaking
changes, it is recommended to add version = "..." constraints to the
corresponding provider blocks in configuration, with the constraint strings
suggested below.

* provider.aws: version = "~> 2.31"

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.

## Related

- [[procedures/Terraform-Create-Kali-Linux-EC2-Instance]]
- [[commands/terraform-apply]]
