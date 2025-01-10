### Steps to Set Up and Simulate a DDoS Project Using Docker

---

#### **Step 1: Build the DDoS Bot Image**
Create a Docker image named `ddos-bot` with the tag `v1` using the `Dockerfile-ddos-bot` file. Run the following command in the same directory as the Dockerfile:

```bash
docker build -f Dockerfile-ddos-bot -t ddos-bot:v1 .
```

---

#### **Step 2: Create a Docker Network**
Set up a Docker network named `ddos-project-network` with the subnet `1.2.3.0/24`. This network will facilitate communication between the containers.

```bash
docker network create --subnet 1.2.3.0/24 ddos-project-network
```

---

#### **Step 3: Deploy the Website Using Docker Compose**
Run the `docker-compose-website.yml` file to launch a website container. This file contains details such as:
- **Web server name and version**: Uses `nginx:latest`.
- **Website container's IP address**: `1.2.3.69` (targeted by the DDoS bot).
- **Exposed ports**:
  - **80**: Port exposed to the network.
  - **8080**: Port accessible locally on your machine.
- **Resource limits**: Constraints on CPU and memory for the website container.
- **Network**: Configured to use `ddos-project-network`.

Run the command below to start the container in detached mode:

```bash
docker compose -f docker-compose-website.yml up -d
```

---

#### **Step 4: Verify Website Accessibility**
Open the website on your local browser using the URL [http://0.0.0.0:8080](http://0.0.0.0:8080). This maps to the internal address `1.2.3.69:80` via Docker networking.

---

#### **Step 5: Deploy the DDoS Botnet**
Run the `docker-compose-ddos-bot.yml` file to start the DDoS botnet. Key details in this file include:
- **Operating system**: Uses `ubuntu:latest`.
- **Number of attacking containers**: Configurable under `services:deploy:replicas`. Increase this value to simulate a larger botnet.
- **Network**: Configured to use the same `ddos-project-network`.

Execute the following command to deploy the botnet:

```bash
docker compose -f docker-compose-ddos-bot.yml up -d
```

---

#### **Step 6: Monitor the Impact**
1. **Check resource utilization**: Open Docker Desktop and monitor the website container's CPU and memory usage.
2. **View container logs**:
   - For the website container:
     ```bash
     docker logs <website-container-name> -f
     ```
   - For the attacker containers:
     ```bash
     docker logs <attacker-container-name> -f
     ```
3. **Verify website availability**: Try accessing the website at [http://0.0.0.0:8080](http://0.0.0.0:8080).
   - If the website is inaccessible, **Hurray!** the DDoS attack is successful!
   - If the website is still accessible, consider lowering the resource limits for the website container in `docker-compose-website.yml` and repeat the test.

---
This mini-project walks you through how to simulate a DDoS attack using Docker. By tweaking things like resource limits and the number of attacking containers, you can see how the botnet affects the target and learn more about how containerized networks handle stress. It’s also a great example of how Docker makes it super easy to set up flexible and reusable testing environments.