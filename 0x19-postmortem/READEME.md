# Postmortem: Web Server Outage

## Issue Summary
- **Duration of Outage:** August 14, 2024, 10:00 AM - 12:30 PM (UTC)
- **Impact:** The web server responsible for delivering the company’s primary website was down for 2.5 hours. During this time, 80% of users experienced either complete downtime or significant slowdowns when trying to access the site. The outage impacted e-commerce transactions, leading to an estimated revenue loss of $15,000.
- **Root Cause:** A configuration error in the Nginx load balancer caused a failure in routing traffic to the web server, which was exacerbated by a spike in traffic during a promotional event.

## Timeline
- **10:00 AM:** The issue was first detected by an automated monitoring alert that reported a significant drop in website response time.
- **10:05 AM:** The on-call engineer received the alert and began investigating the web server's logs, initially suspecting a high load due to the ongoing promotion.
- **10:20 AM:** The engineer assumed a traffic spike issue and scaled up the web server instances, but the issue persisted.
- **10:35 AM:** Further investigation revealed that while server instances were healthy, they were not receiving any traffic.
- **10:50 AM:** The network team was escalated to investigate potential issues with the load balancer.
- **11:15 AM:** A configuration error in the Nginx load balancer was discovered; it was incorrectly routing all traffic to a single, non-functional server.
- **11:45 AM:** The load balancer configuration was corrected, and traffic began routing properly across all web server instances.
- **12:30 PM:** Full service was restored, and normal operation resumed.

## Root Cause and Resolution
- **Root Cause:** The root cause was traced to a misconfiguration in the Nginx load balancer. A recent change intended to optimize traffic routing was not properly tested and caused all incoming traffic to be directed to a single server instance that was not properly configured to handle it. This issue was compounded by the timing of the problem, coinciding with a scheduled promotional event that significantly increased web traffic.
- **Resolution:** The issue was resolved by reverting the Nginx configuration to the last known good state and thoroughly testing the configuration before applying it to the production environment. Additionally, the load balancer was reconfigured to ensure even distribution of traffic across all available servers.

## Corrective and Preventative Measures
- **Improvements/Fixes:**
  - Implement a more rigorous testing process for configuration changes, particularly those involving critical infrastructure like the load balancer.
  - Enhance monitoring systems to detect and alert on uneven traffic distribution across servers more effectively.
  - Establish a rollback plan for critical configuration changes to allow for quick reversion if issues arise.

- **Tasks to Address the Issue:**
  1. **Patch Nginx Server:** Review and update the Nginx configuration file to prevent similar routing issues in the future.
  2. **Implement Load Testing:** Add a load-testing phase to the deployment pipeline to simulate traffic spikes and ensure configurations can handle the load.
  3. **Enhance Monitoring:** Integrate additional monitoring for load balancer traffic distribution to catch any irregularities immediately.
  4. **Documentation:** Update the deployment and configuration documentation to include detailed rollback procedures for critical infrastructure changes.

