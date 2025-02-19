# CI/CD
Google stuff.

Reading materials are optional and are provided for your comfort.


## Defining CI/CD
### Deliveries:

* Defining Continuous Integration
* Defining Continuous Delivery
* Defining Continuous Deployment
* Why do we need CI/CD?

### Reading materials:
* [CI/CD in 100 seconds video](https://www.youtube.com/watch?v=scEDHsr3APg)
* https://opensource.com/article/18/8/what-cicd


## GitHub Actions Concepts
### Deliveries:

* Understand basic concepts
    * `.github/workflows/` directory
    * Event
        * `on:`
    * Runner
        * `runs-on:`
    * Job
    * Step
        * `runs:`
    * Action
        * `uses:`
        * Github marketplace
    * Environment
        * `env:`
    * Secrets
    * Run jobs in a container
        * `container:`
* Pull repo code
    * `actions/checkout`
* Install python
    * `actions/setup-python`

Reading materials:

* https://docs.github.com/en/actions
* https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions
* Google the relevant actions


## Continuous Integration - Linting
### Deliveries:

* Linting
* Why do you need linting?

Reading materials:

* https://www.earthdatascience.org/blog/unit-testing-linting-ci-python/ **\* Read until Our Toolbox header**
* https://pybit.es/articles/linting-with-flake8/

### Drill:

* Write a CI pipeline that lints the [example python application](./example_fastapi_app-main)
    * Fork the example into a repository of your own
    * Write a CI pipeline that will lint the example
    * Configure the pipeline so that you can't merge without it passing
    * Fix the example and merge it to master

## Continuous Integration - Testing
### Deliveries:

* Why do you need testing
* Types of tests
    * Unit testing
    * Integration testing
    * System testing - know that it exists
* TDD

### Reading materials:

* [Software Testing Explained in 100 Seconds video](https://www.youtube.com/watch?v=u6QfIXgjwGQ)
* https://realpython.com/pytest-python-testing/
* https://fastapi.tiangolo.com/tutorial/testing/

### Drill:

* Write tests for your fork of the [example python application](./example_fastapi_app-main)
    * Write unit tests for the inner functions using pytest
    * Write unit tests for the REST api endpoints using FastAPI's integrated testing
* Write a CI job that runs the tests
    * Use the forked example from the previous segment
    * Add a CI job to your pipeline that will test the example
    * Fix the example and merge it to master


## Continuous Integration - Building
### Deliveries:

* Common building jobs
    * Building a Binary
    * Building a Package
    * Building a Container
* Artifacts
    * What are Artifacts?
    * `actions/upload-artifact`
    * `actions/download-artifact`
* Dependencies between stage
    * `needs:`
* Cache
    * `actions/cache`


### Reading materials:
* Google the relevant actions
* How to package a python project (guide) - https://packaging.python.org/en/latest/tutorials/packaging-projects/
* Python project structure & how to prepare the project for CICD (0:00-8:00) - https://www.youtube.com/watch?v=DhUpxWjOhME

### Drill:

* Write a CI job that builds a python package for your fork of the [example python application](./example_fastapi_app-main)
* Write a Dockerfile that will install the package and run the python http server as it's entrypoint
* Write a CI job that uses the output of the package build job as a dependency and builds the Dockerfile


## Continuous Delivery
### Deliveries:

* Uploading artifacts to a registry 
* Creating a release

Reading materials:
* https://docs.github.com/en/actions/use-cases-and-examples/publishing-packages/publishing-docker-images
* https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry
* https://github.com/softprops/action-gh-release

### Drill:

* Write a CD job that publishes a docker container to `ghcr.io`
