# Simple AI Chat Application

This project aims to be a very simple AI chat application.

## Table of Contents

- [Getting Started](#getting-started)
- [Running](#running)
- [Usage](#usage)
- [Long-Term-Considerations](#Long-Term-Considerations)

## Getting Started

Human-machine interfaces are becoming increasingly sophisticated. Integrating AI capabilities improves user experience, offers instant answers, and aids human operators.

### Running

To use this project , you only need docker-compose to be installed on your system and to use the project you can run:
```docker-compose build``` and then ```docker-compose up```. These project consist of two docker services: fastApi server and a postgres database.

You have to notice that chat-app service which will be our fast-api server will allocate port ```8000``` of your system.  

### Usage
I have provided a postman collection beside the project , but in this section we want to have an overview of our REST-API endpoints.

- Create Interaction: By calling this endpoint you will create a new interaction by making a Post request to this endpoint: ```http://localhost:8000/interaction/```.
The output of this api will include an Id which will be used in the next APIs.
     

- Get Interactions: By calling this endpoint, you will get a list of all the interactions with their messages, you have to make a Get request to this endpoint: ```http://localhost:8000/interaction/```.


- Respond Message: After creating your interaction , you can communicate with our AI agent via calling this API. You have to make a Post request by calling this endpoint: ```http://localhost:8000/message/respond/{Interaction_ID}/```.
You should pass your message by providing a body that follows this structure: ```{""content": "YOUR_PROMPT""}```.
 

- Get Messages Of An Interaction: This is our last API. By make a GET request to this endpoint: ```http://localhost:8000/message/{Interaction_ID}/```.
You will get a list of all messages between human and our AI agent.

### Long-Term-Considerations
Perhaps this project is a very simple chat application as we have mentioned before. In this section we want to give some advices on long term considerations.

- **Scalability**:
    -  **Data Access**  In this application we have used Postgres database to persist our data. In the real world , access to data have significant effect of real-time applications.
We can separate our interactions into two groups: Cold and Hot. Cold Interaction: The interactions that are not active. Their last messages are about to long times ago.
At the other hand , Hot interactions are active and users are actively communicating with our ai agent using them.
To speed up our data access we can provide some In-Memory data solutions like ```Redis``` or ```Mem-Cached``` to keep the data of these hot interactions.
       
    - **Summarization** We used ChatGPT as our AI-agent and as we know these LLMs are stateless. It means that if we want our AI model to remember our dialog context. we have to pass this context to the model in each message smartly.
    For the sake of simplicity, we did not pay so much attention to this issue.We will pass the whole of our dialog in each message to the AI agent which will raise issues due to our token limitations. 
    
    - **Container Orchestration** If we want our system to be ready for production grade traffic we have to use new Operational solutions. Using Kubernates as our container orchestrator can be a promising solution for this issue.
      


- **Extensibility** we have to provide some infrastructure , to connect our system with other AI services. With the emergence of Generative AI field , our system
  should have this potential to provide other generative AI services such as Image generation. We have developed this simple chat application in this manner , we can develop other services in our service package and connect them to our current application.
  

- **Security** We did not have any user management processes in this simple application. In the future this feature will be necessary without doubt. We can use common security solutions to protect our user's data. For example , we can use JWT authentication method.
To protect our other critical data such as database credential , we can encrypt them . This solution for credentials security has already been implemented in Kubernetes using some specific Kuber kinds.
 

- **Domain Segregation** To bridge the gap between our stored data and the state of our application we used ORM. We used our service layer to connect our API routes to data layer to separate these two layers, and to make sure that our stored data and the application state are sync. 
 
