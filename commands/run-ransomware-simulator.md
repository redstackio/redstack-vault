---
data: 'ransomware_sim.exe C:\Users\UNPRIVILIEGEDUSER\'
tags:
  - simulation
  - ransomware
type: command
output: >-
  Simulates file encryption in the target directory to mimic ransomware
  behavior.
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:51.582Z'
id: dbd59fa5-11b2-4c02-81cb-1e160ff63369
verified: false
validated: true
submitted: true
---
# run-ransomware-simulator

## Command

```cmd
ransomware_sim.exe C:\Users\UNPRIVILIEGEDUSER\"
```

## Description

Executes the ransomware simulator to target a directory, triggering Acronis detection by simulating encryption.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Target Path | Directory to simulate encryption on | Yes |

## Examples

### Basic Usage

```cmd
ransomware_sim.exe C:\Users\UNPRIVILIEGEDUSER\"
```

### Advanced Usage

Adjust target path as needed.

## Expected Output

Encryption simulation starts; Acronis alert appears.

## Related

- [[procedures/Prepare-and-Trigger-Ransomware-Simulation]]
