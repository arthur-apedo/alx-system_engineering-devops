# POSTMORTEM: API MISCONFIGURATIONS

## INTRODUCTION
On May 6, 2024 our organisation faced an impactful challenge from 10:00 A.M to 12:14 P.M UTC. Our application suffered an api misconfiguration that substancially affected 65% of our users who were unbale to retrieve old documents that were shared beteen users. The root cause was traced to misconfiguration in the updated version of the routing criteria of the application

## TIMELINE
- 10:00 A.M UTC: The issue was first detected when users began reporting problems retrieving shared documents.
- 10:15 A.M UTC: Initial investigation began by the on-call engineering team.
- 10:45 A.M UTC: The issue was identified as a potential misconfiguration in the API routing criteria.
- 11:00 A.M UTC: The engineering team rolled back the recent update to the previous stable version to mitigate the impact.
- 11:30 A.M UTC: Testing and validation were conducted to ensure the rollback resolved the issue.
- 12:14 P.M UTC: The application was fully operational, and the incident was officially declared resolved.

## IMPACT
The API misconfiguration affected approximately 65% of our user base. Users were unable to retrieve previously shared documents, leading to significant disruptions in workflows and communications. The issue predominantly affected document retrieval functions, while other application functionalities remained operational.

## ROOT CAUSE
The incident was caused by an incorrect configuration in the updated version of our API routing criteria. Specifically, the routing logic failed to properly handle requests for old documents shared between users. This misconfiguration led to routing failures and prevented the API from accessing the necessary document storage.

## RESOLUTION AND RECOVERY
To resolve the issue, the following actions were undertaken:

- Rollback: Reverted the API routing configuration to the previous stable version.
- Testing: Conducted comprehensive tests to ensure the rollback was successful and that document retrieval was fully functional.
- Deployment: Redeployed the stable version of the application to all servers.

##PREVENTIVE MEASURES
To prevent similar incidents in the future, the following measures will be implemented:

- Configuration Audits: Regular audits of API configurations will be conducted to identify and rectify potential issues before deployment.
- Enhanced Testing: Implement more rigorous testing protocols for routing changes, including regression testing and automated configuration checks.
- Monitoring and Alerts: Improve monitoring systems to detect and alert on configuration-related anomalies in real-time.
- Documentation and Training: Enhance documentation and provide additional training for the engineering team on best practices for API configuration management.

##CONCLUSION
This incident highlighted the critical importance of rigorous testing and monitoring of API configurations. By implementing the outlined preventive measures, we aim to mitigate the risk of similar issues occurring in the future and ensure a more resilient and reliable application for our users.
