# Automation with Python
This repository showcase my work to achieve automation through python programming language.
## Project 1:
Using the python file:- 
- ec2-status-check.py and eks-status-check.py, you can check the status of AWS EC2 instance and EKS cluster, and schedule the status check task for every 5 mins.
- volume-backups.py , you can periodically schedule snapshot generation of AWS EC2 instance volume.
- restore-snapshots.py, you can restore the volume using snapshot(latest).
- cleanup-snapshot.py, you can delete the older version of snapshot and, save the resources and cut the cost.

## Project 2: Website Mointerning
With this project we can monitor our website hosted on IaaS, we are checking if the server is down or the application is down, if so, it send email to the concerned(mentioned) email address. It also restart the container or server to fix the problem.
