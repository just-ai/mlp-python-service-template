# mlp-python-service-template

This repository is a project template for creating a new [Caila](https://app.caila.io/) service.

> Caila is a platform for hosting microservices based on ML models.
> It is a powerful tool that can cover every aspect of your solution’s lifecycle, from model training and QA to deployment and monitoring.

[Create a new project](https://github.com/new?template_name=mlp-python-service-template&template_owner=just-ai) from this template to start developing a service of your own!

## Get started

Start by getting yourself acquainted with the contents of [`main.py`](./src/main.py).
In terms of features, this is a simple “Hello World” service:

- It has no `fit` method, so it can’t be trained.
- Its `predict` method returns a greeting message to whatever’s passed as the `name` in the request body.

The service relies on the Caila [Python SDK](https://github.com/just-ai/mlp-python-sdk) to expose its functionality to the platform.

## Build Docker image

To build the service locally, run `./build.sh` in the project root.
You need to have [Docker Engine](https://docs.docker.com/engine/install/) installed and running.

The build script will create a Docker image, push it to the [public Caila Docker registry](https://docker-pub.caila.io/), and print the image URL to the console:

```txt
--------------------------------------------------
Docker image: docker-pub.caila.io/caila-public/mlp-hello-world-service-xxxxxxxxxxxxxxxx:main
--------------------------------------------------
```

You will need this URL to configure your service in Caila.

> ⚠ The public Caila Docker registry has a limited storage time and is intended for educational purposes only.
> Do not use it for production.

## Create Caila service

1. Sign in to [Caila](https://app.caila.io/) or sign up for a new account.
2. Go to *My space* and select *Images* in the sidebar.
    > 🛈 If you don’t see this tab, go to *My space* → *Services*, select *Create service*, and submit a request for access.
    > Our customer support team will get back to you shortly.
3. Select *Create image*. Provide the image name and the URL you got from the build script.
4. On the image description page, select *Create service*. Provide the service name and leave the other settings at their defaults.
5. You should now see your service in the *Services* tab. Go to its details page and select *Diagnostics*.
6. Select *Add instance*. Wait for the instance to start (the status indicator should turn from yellow to green).
7. Go to the *Testing* and try sending a request with a JSON body like `{"name": "John Doe"}`.

If you see `{"response": "Hello, John Doe!"}` in the output, congratulations!
Your service is up and running.

If you would like to learn more about Caila, check out our official [documentation](https://docs.caila.io/).

## License

This project is licensed under Apache License 2.0.
