
### Steps to Set Up and Simulate a DDoS Project Using Docker

---

#### **Step 1: Build the DDoS Bot Image**
Create a Docker image named `ddos-bot` with the tag `v1` using the `Dockerfile-ddos-bot` file. Run the following command in the `dockerfiles` directory:

```bash
docker build -f dockerfiles/Dockerfile-ddos-bot -t ddos-bot:v1 .
```

---

#### **Step 2: Create a Docker Network**
Set up a Docker network named `ddos-project-network` with the subnet `1.2.3.0/24`. This network will facilitate communication between the containers.

```bash
docker network create --subnet 1.2.3.0/24 ddos-project-network
```

---

#### **Step 3: Deploy the Flask-Based Website**
Build the `python3-flask-img` Docker image using `Dockerfile-flask`. Run the following command in the `dockerfiles` directory:

```bash
docker build -f dockerfiles/Dockerfile-flask -t python3-flask-img:latest .
```

Run the `docker-compose-website.yml` file to launch the Flask website container. This file contains details such as:
- **Web server**: Flask application served on port 80.
- **Website container's IP address**: `1.2.3.69` (targeted by the DDoS bot).
- **Exposed ports**:
  - **80**: Port exposed to the network.
  - **8080**: Port accessible locally on your machine.
- **Resource limits**: Constraints on CPU for the website container.
- **Network**: Configured to use `ddos-project-network`.

Run the command below to start the container in detached mode:

```bash
docker compose -f dockerfiles/docker-compose-website.yml up -d
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
docker compose -f dockerfiles/docker-compose-ddos-bot.yml up -d
```

---

#### **Step 6: Monitor the Impact**
1. **Check resource utilization**: Open Docker Desktop and monitor the website container's CPU usage.
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

This updated mini-project introduces a Flask-based application as the website and uses `Dockerfile-ddos-bot` and `Dockerfile-flask`. You can tweak the number of attacking containers and resource limits to observe how the botnet affects the target. It’s a practical demonstration of using Docker for setting up flexible and reusable testing environments.
