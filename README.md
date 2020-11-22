# ops-technical-test

This project contains source code and supporting files for the ops-technical-test serverless application. It includes the following files and folders.

- hello_world - Contains code and tests for the hello world endpoint.
- meta - Contains code for the meta data endpoint.
- template.yaml - Template that defines the application's AWS resources.

The application uses AWS Lambda functions and an API Gateway API. These resources are defined in the `template.yaml` file in this project.

## Endpoints
- hello world: https://taz5qgxmv6.execute-api.ap-southeast-2.amazonaws.com/Prod/hello/ 
- meta: https://taz5qgxmv6.execute-api.ap-southeast-2.amazonaws.com/Prod/meta/

## Deploying the application

I have implemented CD for this project using AWS Code Pipeline and Code Deploy. The different stages in the build process are defined in the `buildspec.yml` file. The deployment is triggered when code is pushed to the main branch.