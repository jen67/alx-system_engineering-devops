# Postmortem: SSH Key Authentication Failure on Ubuntu Web Terminal

## Issue Summary
- **Duration of Outage:** August 14, 2024, 2:30 PM - 4:00 PM (UTC)
- **Impact:** During this period, I was unable to access the Ubuntu web terminal via SSH due to key authentication failures. This prevented me from managing server configurations and deploying updates, impacting my workflow and causing a delay in project development.
- **Root Cause:** The SSH key used for authentication was not properly recognized due to a permissions issue on the server and a mismatch between the key's format on the local machine and what the server expected.

## Timeline
- **2:30 PM:** The issue was first detected when I received an "Access Denied" error while attempting to SSH into the Ubuntu server. The error message indicated that the public key was not accepted.
- **2:35 PM:** I initially suspected a network issue or a problem with the server's SSH daemon and restarted my SSH client and terminal.
- **2:45 PM:** After restarting the SSH client and verifying the network connection, I realized that the problem persisted. I checked the local SSH configuration and found that the private key file had incorrect permissions.
- **3:00 PM:** I attempted to regenerate the SSH key pair and replace the old key on the server. The key was successfully added to the server's `~/.ssh/authorized_keys` file, but I continued to face authentication issues.
- **3:15 PM:** It was discovered that the SSH key format on the local machine was different from what the server was configured to accept. I adjusted the key format to match the server's requirements.
- **3:30 PM:** After correcting the key permissions and ensuring the key format was compatible, I was able to successfully authenticate and access the server.
- **4:00 PM:** Full access was restored, and normal operations resumed.

## Root Cause and Resolution
- **Root Cause:** The SSH key authentication failure was due to a permissions issue with the private key file on my local machine and a format mismatch between the key generated on my local machine and the key expected by the server.
- **Resolution:** The issue was resolved by updating the permissions of the private key file to `600` and ensuring the SSH key format was compatible with the server. Additionally, I re-added the key to the server's `~/.ssh/authorized_keys` file after regenerating it in the correct format.

## Corrective and Preventative Measures
- **Improvements/Fixes:**
  - Regularly verify and update key file permissions to avoid similar issues in the future.
  - Ensure SSH key formats are compatible between local machines and servers by following best practices for key generation and deployment.
  - Implement automated checks to validate key permissions and formats before deployment to avoid manual errors.

- **Tasks to Address the Issue:**
  1. **Update Key Permissions:** Review and adjust the permissions of SSH key files to `600` to ensure proper security and accessibility.
  2. **Verify Key Format:** Check and confirm the SSH key format matches server requirements and make necessary adjustments during key generation.
  3. **Automate Key Checks:** Implement scripts or tools to automate the validation of SSH key permissions and formats before use.
  4. **Document SSH Key Procedures:** Update documentation to include best practices for generating and deploying SSH keys to prevent similar issues in the future.


