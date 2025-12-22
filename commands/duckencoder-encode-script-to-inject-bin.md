---
id: 833cc87a-ff3c-4127-b276-cdd7deffe305
type: command
executor: bash
data: java -jar duckencoder.jar -i $_INPUT_FILE -o $_OUTPUT_FILE
output: >-
  root@kali:~# java -jar duckencoder.jar -i ../Payloads/AV/EICAR-Test.txt
  ../Payloads/bin/inject.bin


  Hak5 Duck Encoder 2.6.3


  Loading File ..... [ OK ]

  Loading Keyboard File .... [ OK ]

  Loading Language File .... [ OK ]

  Loading DuckyScript .... [ OK ]

  DuckyScript Complete..... [ OK ]
created_at: '2023-02-17T02:28:40.027279+00:00'
updated_at: '2023-03-13T19:50:21.945040+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - hardware
  - payload-encoding
verified: true
validated: true
---

# duckencoder-encode-script-to-inject-bin

## Command

```bash
java -jar duckencoder.jar -i $_INPUT_FILE -o $_OUTPUT_FILE
```

## Description

This command compiles a Ducky Script file into a binary inject.bin file that can be placed on the microSD card of a USB Rubber Ducky device for execution when plugged into a target system. It uses the duckencoder Java tool to convert the script into the required hex format.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_INPUT_FILE | Path to the input Ducky Script file (.txt) | Yes |
| $_OUTPUT_FILE | Path to the output binary file (typically inject.bin) | Yes |
| -i | Specifies the input file | Built-in |
| -o | Specifies the output file | Built-in |

## Examples

### Basic Usage

```bash
java -jar duckencoder.jar -i payload.txt -o inject.bin
```

### Advanced Usage

```bash
java -jar duckencoder.jar -i ../scripts/custom-payload.txt -o /path/to/sd/inject.bin
```

## Expected Output

```
root@kali:~# java -jar duckencoder.jar -i ../Payloads/AV/EICAR-Test.txt ../Payloads/bin/inject.bin

Hak5 Duck Encoder 2.6.3

Loading File ..... [ OK ]
Loading Keyboard File .... [ OK ]
Loading Language File .... [ OK ]
Loading DuckyScript .... [ OK ]
DuckyScript Complete..... [ OK ]
```

## Related

- [[tools/Rubber-Ducky]]
- [[procedures/Create-and-Deploy-Rubber-Ducky-Payload]]
