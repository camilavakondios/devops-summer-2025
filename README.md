## Project Documentation

The full project report, including implementation details, troubleshooting and learning outcomes, is available here:

[View Project Report (PDF)](./CamilaPFaria_Book-Catalogue.pdf)


# Book Catalogue 2025

The Book Catalogue API allows users to create, update, delete and retrieve books from a catalogue. It is an API created as part of the Diploma in DevOps course and it is also deployed using Docker images, Kubernetes, Helm Chart and ArgoCD.


The API allows users to create a new book as showed below:

If a use wants to add the following title, it is possible by the endpoint from the endpopint: /api/books/


{
    "isbn": "12345AB",
    "title": "Harry Potter",
    "description": "Young wizard in Hogwarts trying to survive his enemy Voldemort",
    "author": "JK Rowling",
    "published_date": "1997-03-03"
}



 

A 200 OK response indicates that the title has been successfully added to the catalogue. 
Now, if the user wants to retrieve the title, it is possible by inserting the ISBN to the end of the URL: 12345AB 

<img width="975" height="342" alt="image" src="https://github.com/user-attachments/assets/3bea48ce-acf6-4488-a1ad-4e7df6863822" />

 
http://127.0.0.1:8000/api/books/12345AB/
Once, the title is retrieved, users can now update or delete the title from the catalogue. 

A 200 OK response indicates that the book was deleted, also displaying the confirmation message.

<img width="884" height="331" alt="image" src="https://github.com/user-attachments/assets/d235f01d-439d-4aad-afbc-4bbe63d4ed82" />


 Local Build and Run instructions

 After cloning the repository, it is necessary to create

CI/CD pipelines 

 The CI/CD pipeline automates building, testing, and deploying the application using GitHub, Docker, and Kubernetes with ArgoCD.

Version control: All source code is stored in GitHub. We use branches and pull requests to manage changes.

CI process: When a new commit is pushed or a PR is merged:

GitHub Actions is triggered.

It installs dependencies, runs unit tests (e.g., with pytest or Django test framework), and builds a Docker image.

The Docker image is tagged (e.g., :main) and pushed to GitHub Container Registry (GHCR).

CD process: We use ArgoCD for GitOps-based deployment.

ArgoCD watches our Helm chart repository or Kubernetes manifests in a Git repo.

When a new image is available (or Helm values are updated), ArgoCD syncs the changes to our Kubernetes cluster.

It handles deploying the image, applying configuration (like environment variables), and ensures the app is healthy.

The pipeline also includes health checks (e.g., readiness/liveness probes) and rollback mechanisms using Helm if something goes wrong.


Docker container images

1. Create a Docker file inside the root directory of your project.
2. The Entrypoint.sh file is also created inside the same directory to create a connection with the database and run the migrations once the database is ready.
3. Once both files are created the docker image can be created and pushed:
    - docker build -t ghcr.io/youruser/hello-k8s:latest .
    - docker push ghcr.io/youruser/hello-k8s:latest


5. 

Once the files are created, the docker images are build and pushed with the commands:
docker build -t ghcr.io/youruser/hello-k8s:latest .
docker push ghcr.io/youruser/hello-k8s:latest

