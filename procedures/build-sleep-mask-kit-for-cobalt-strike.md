---
type: procedure
tactics:
  - '[[Defense Evasion]]'
techniques:
  - '[[Obfuscated Files or Information]]'
sub_techniques: []
tags:
  - cobalt-strike
  - kits
  - sleep-mask-kit
  - evasion
  - obfuscation
commands:
  - '[[commands/execute-sleep-mask-build-script]]'
  - '[[commands/execute-sleep-mask-build-batch]]'
tools:
  - '[[tools/Cobalt-Strike]]'
platforms:
  - Linux
  - Windows
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Build Sleep Mask Kit for Cobalt Strike

## Summary

This procedure outlines the process of building the Sleep Mask Kit within Cobalt Strike, which generates obfuscated files and scripts designed to evade detection by security tools. The kit is used to create stealthy payloads for unauthorized access, data exfiltration, or lateral movement in target environments.

## Description

The Sleep Mask Kit is a specialized component in Cobalt Strike that applies obfuscation techniques to payloads, making them harder for antivirus and EDR solutions to detect. By building the kit, operators can produce customized executable files or scripts that mask malicious behavior, such as command execution or persistence mechanisms. This procedure is applicable in red team engagements simulating advanced persistent threats (APTs) where evasion is critical. It requires familiarity with Cobalt Strike's Malleable C2 profiles and basic scripting. The target environment typically involves a controlled attacker workstation with Cobalt Strike licensed and configured. Successful execution results in obfuscated artifacts ready for deployment via initial access vectors like phishing or exploit kits.

## Requirements

1. Licensed Cobalt Strike installation on the attacker workstation
2. Access to the Sleep Mask Kit source files (downloaded from Cobalt Strike team server or repository)
3. Knowledge of scripting and file obfuscation techniques
4. Compatible build environment: Bash for Linux/Unix or Command Prompt for Windows
5. Administrative privileges on the build system to execute build scripts

## Defense

Defensive measures and detection strategies:

- Regularly update and patch Cobalt Strike detection signatures in EDR tools like CrowdStrike or Carbon Black
- Implement behavioral monitoring for obfuscated file creation and unusual script execution patterns
- Use file integrity monitoring to detect modifications to known good binaries
- Enforce application whitelisting to block unsigned or obfuscated executables
- Monitor for Cobalt Strike-specific artifacts, such as beacon processes or C2 traffic over HTTP/S

## Objectives

1. Compile and obfuscate the Sleep Mask Kit to produce evasive payloads
2. Verify the build output for functionality without triggering static detection
3. Prepare artifacts for integration into Cobalt Strike operations for stealthy access

## Instructions

### Step 1: Prepare the Build Environment

**Context**: Set up the project directory containing the Sleep Mask Kit files, ensuring all dependencies like Cobalt Strike's build tools are available. This step confirms the environment is ready for compilation.

Navigate to the directory where the Sleep Mask Kit source is located.

**Expected Output**: Confirmation that the build scripts (build.sh or build.bat) are present and executable.

### Step 2: Execute Unix Build Script

**Context**: For Linux or Unix-based systems, run the Bash build script to compile the kit. This automates obfuscation, linking, and generation of executable files tailored for evasion.

**Command** ([[commands/execute-sleep-mask-build-script]]):
```bash
./build.sh
```

> This command invokes the build script, which may include compiling source code, applying obfuscation layers (e.g., string encryption, control flow flattening), and outputting the final kit artifacts. Monitor for any errors related to missing dependencies. If successful, it produces obfuscated binaries or scripts in an output directory.

**Expected Output**: Build completion message, such as "Sleep Mask Kit built successfully. Artifacts in ./output/", along with generated files like obfuscated EXEs or scripts.

### Step 3: Execute Windows Build Batch

**Context**: For Windows environments, use the batch file to perform the build. This is equivalent to the Unix script but adapted for Command Prompt, handling Windows-specific paths and tools.

**Command** ([[commands/execute-sleep-mask-build-batch]]):
```cmd
build.bat
```

> Run this in the project directory via Command Prompt. The script handles compilation with MinGW or Visual Studio tools if configured, applies evasion techniques, and generates Windows-compatible outputs. Check for build logs in case of failures due to path issues or missing libraries.

**Expected Output**: Console output indicating successful build, e.g., "Build complete: Obfuscated payloads generated in output folder.", with files like masked DLLs or executables.

### Step 4: Verify Build Artifacts

**Context**: Test the generated files to ensure they function without immediate detection. Load them into Cobalt Strike's aggressor scripts or test in a sandbox.

Use Cobalt Strike's kit builder interface or manual inspection to confirm obfuscation (e.g., check for encrypted strings via hex editor).

**Expected Output**: Artifacts load correctly in Cobalt Strike without errors; basic execution tests (e.g., in a VM) show no AV alerts.

**Success Indicators**:
- No compilation errors during build
- Generated files exhibit obfuscated characteristics (e.g., non-readable strings)
- Integration with Cobalt Strike team server succeeds
