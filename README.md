# Strategy for Integrated Tests

Some years ago I wrote an article about [Strategies of Integrated Test for REST Services ]('http://www.linkedin.com/pulse/estrat%C3%A9gia-de-testes-integrados-para-servi%C3%A7os-rest-fabio-ono-tavoloni/').

Thing is that, three years after, this theme is pretty important, even more now. The adoption of Distributed Services Architecture, most using REST API's, we have the necessity to ensure that the health of our services are good. 

This is a proposal about how it's possible doing this approach for your services.

### Objectives of this Example

It'll be possible for you to simulate the entire process regarding changing a REST API, push into a remote repository, and have automatically the returning of your tests exposed in a pileline of Jenkins, like this:

<<image>>

### Technologies

Let me describe each component/tool/framework envolved in this solution:

| Component | Version | Objetive
| ------ | ------ | ------
| Component | Version | Description |
| Docker | 18.09.7 | To allow all the components running in containers
| Postman | 7.0 | To allow us create and run the tests
| Newman | 5.0.1 | A command-line collection runner for Postman
| ngrok | - | Exposes local servers behind NATs and firewalls to the public internet

### Files of this Project

| Files | Goal
| ------ | ------
| app.py | Contains a simple API, writen in Python, with a GET endpoint that simulates the return of Customers
| requirements.txt | Contains the list of packages the API will use. In this case just Flask
| docker-compose.yml | Contains the definitions of the containers. dns-server: to define a DNS for easy access thought/exposure between Jenkins and API | api: the API container | jenkins: definition of Jenkins container
| Dockerfile-flask | Basic configuration for the API
| Dockerfile-jenkins | Configuration for Jenkins
| plugins.txt | Plugins used by Jenkins
| Customers_API_Tests.postman_collection.json | Example of a test collection, representing negocial and structural approach.

## How to run the Application


What I suggest to work with this solution in an easier way is to create a brand new repository in your Github.

Then, download this project, pushe the content to your account in Github. Open the command line and run the command:

```
docker-compose up
```

After running this command, you will be with the API, Jenkins and DNS up and running:

<<image>>

Let's test the API now. Open the Postman and import the file Customers_API_Tests.postman_collection.json

<<image>>

Now, you can login as admin. We should make some configurations on Jenkins. Go to Manage Jenkins -< Configure Systems:

<<>>

Let's now create the our Project on Jenkins. Click New Item:

<<image>>

Let's configure this project to make use of our API Tests. Build execute shell.

<<image>>

Let's configure the Pipeline now.

<<image>>

Let's configure Github.

<<image>>


