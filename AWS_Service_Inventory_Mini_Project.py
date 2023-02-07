# AWS Service Inventory List - Week12

# 1) This list should be empty initially

services = []

# 2) Populate the list using append or insert

services.append('EC2')
services.append('Cloud9')
services.append('DynamoDB')
services.append('VPC')
services.append('Lambda')
services.append('S3')
services.append('RDS')
services.append('IAM')
services.append('CloudFront')
services.append('ElastiCache')
services.append('CloudShell')
services.append('CodeDeploy')
services.append('CodeCommit')
services.append('API Gateway')
services.append('CodeBuild')

# 3) Print the list and the length of the list

print(services)
print(len(services))

# 4) Remove two specific services from the list by name or by index.

del services[10]
del services[11]

# 5) Print the new list and the new length of the list.

print(services)
print(len(services))

# Mini Project for Week 12 - Red Team