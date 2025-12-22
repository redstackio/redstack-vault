---
id: 222b1101-1084-4344-baf5-15f5409a3e2f
name: git-clone-and-install-nps-payload
type: command
executor: bash
data: |-
  git clone https://github.com/trustedsec/nps_payload.git
  cd nps_payload && pip install -r requirements.txt
output: >-
  root@kali:~# git clone https://github.com/trustedsec/nps_payload.git

  Cloning into 'nps_payload'...

  remote: Enumerating objects: 31, done.

  remote: Total 31 (delta 0), reused 0 (delta 0), pack-reused 31

  Unpacking objects: 100% (31/31), done.

  root@kali:~# cd nps_payload && pip install -r requirements.txt

  Requirement already satisfied: netifaces in
  /usr/local/lib/python2.7/dist-packages (from -r requirements.txt (line 1))
  (0.10.9)

  Requirement already satisfied: pexpect in /usr/lib/python2.7/dist-packages
  (from -r requirements.txt (line 2)) (4.6.0)
created_at: '2019-11-14T23:38:41.520291+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - setup
  - payload-generation
verified: true
validated: true
---

# git-clone-and-install-nps-payload

## Command

```bash
git clone https://github.com/trustedsec/nps_payload.git
cd nps_payload && pip install -r requirements.txt
```

## Description

This command clones the nps_payload repository from GitHub and installs its Python dependencies, preparing the tool for generating MSBuild-compatible payloads to bypass AppLocker.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | No parameters; runs Git clone and pip install sequentially | No |

## Examples

### Basic Usage

```bash
git clone https://github.com/trustedsec/nps_payload.git
cd nps_payload && pip install -r requirements.txt
```

### Advanced Usage

Run in a virtual environment: `python -m venv env && source env/bin/activate && pip install -r requirements.txt` after cloning.

## Expected Output

Cloning confirmation and dependency installation messages, indicating the tool is ready for use.

## Related

- [[procedures/Windows-AppLocker-Whitelist-Bypass-Using-MSBuild]]
- [[tools/nps-payload]]
