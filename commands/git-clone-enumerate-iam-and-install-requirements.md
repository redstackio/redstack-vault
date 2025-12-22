---
type: command
executor: bash
data: |-
  git clone https://github.com/andresriancho/enumerate-iam.git
  cd enumerate-iam
  pip install -r requirements.txt
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - setup
  - python
verified: true
validated: true
---

# git-clone-enumerate-iam-and-install-requirements

## Command

```bash
git clone https://github.com/andresriancho/enumerate-iam.git
cd enumerate-iam
pip install -r requirements.txt
```

## Description

This command clones the enumerate-iam GitHub repository and installs its Python dependencies, preparing the environment to run AWS IAM permission enumeration scripts. Use this as the initial setup step before executing permission probes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | No parameters; uses default Git and pip behavior | No |

## Examples

### Basic Usage

```bash
git clone https://github.com/andresriancho/enumerate-iam.git
cd enumerate-iam
pip install -r requirements.txt
```

### With Virtual Environment (Recommended)

```bash
python -m venv env
source env/bin/activate  # On Windows: env\\Scripts\\activate
pip install -r requirements.txt
```

## Expected Output

Git clone: "Cloning into 'enumerate-iam'..." followed by progress bars and "done." Pip: "Collecting boto3... Successfully installed boto3-1.x.x ..." with a list of packages.

## Related

- [[procedures/AWS-IAM-Permissions-Enumeration]]
