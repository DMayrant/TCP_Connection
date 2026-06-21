# Kubernetes TCP Connectivity Validation 🌏

## Overview

Validating Kubernetes application connectivity using Python sockets, a Kubernetes Service, and port forwarding.

The goal is to verify:

* Pod health
* Service connectivity
* TCP communication
* Application availability
* HTTP response validation

The environment consists of an Nginx deployment running inside Kubernetes and a Python script that establishes a TCP connection and validates the HTTP response.

---

## Architecture 🏗️

```text
Python Socket Client
        |
        v
localhost:3000
        |
kubectl port-forward
        |
nginx-web Service
        |
        v
Nginx Pods
```

![image alt](https://github.com/DMayrant/TCP_Connection/blob/main/Screenshot%202569-06-21%20at%2015.32.27.png?raw=true)

---

## Technologies Used

* Python 3
* Kubernetes
* Nginx
* TCP Sockets
* kubectl
* Docker Desktop Kubernetes (or any Kubernetes cluster)

---

## Kubernetes Deployment

Deploy the Nginx application:

```bash
kubectl apply -f nginx-deploy.yaml
```

Verify the pods are running:

```bash
kubectl get pods
```

## Verify Service Connectivity

Create a temporary curl pod:

```bash
kubectl apply -f curl.yaml
```

View logs:

```bash
kubectl logs curl
```

Expected output:

```text
HTTP/1.1 200 OK
Server: nginx/1.28.0
```

This confirms the Kubernetes Service can successfully route traffic to the Nginx pods.

---

## Port Forward the Service

Expose the Kubernetes Service locally:

```bash
kubectl port-forward svc/nginx-web 3000:80
```

Expected output:

```text
Forwarding from 127.0.0.1:3000 -> 80
```

This creates a tunnel from your local machine to the Kubernetes Service.

---

