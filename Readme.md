Absolutely! Here’s a **step-by-step guide** for deploying your Flask app on an **AWS EC2 instance running Linux**, using Docker to containerize and run it.

---

# Deploy Flask App on AWS EC2 with Docker (Linux)

---

## 1. Prepare Your Flask App and Dockerfile

Use the **same Flask app** and Dockerfile as before:

### `app.py`

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Flask on EC2 with Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### `Dockerfile`

```Dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install flask

EXPOSE 5000
CMD ["python", "app.py"]
```

---

## 2. Build and Push Docker Image (Optional)

* You can build the Docker image locally and push to Docker Hub as before,
* Or build it directly on the EC2 instance.

*If you build on EC2, no need to push/pull Docker Hub.*

---

## 3. Launch an EC2 Instance

* Go to AWS Console → EC2 → Launch Instance
* Choose **Amazon Linux 2 AMI** or **Ubuntu Server**
* Choose instance type: t2.micro (Free Tier eligible)
* Configure security group:

  * Allow inbound ports:

    * **22** (SSH)
    * **5000** (for Flask app, or 80 if you plan to map port 5000 → 80)
* Launch instance and download the `.pem` key file.

---

## 4. Connect to EC2 via SSH

```bash
ssh -i your-key.pem ec2-user@<EC2-public-IP>    # Amazon Linux 2
# or for Ubuntu:
ssh -i your-key.pem ubuntu@<EC2-public-IP>
```

---

## 5. Install Docker on EC2

Run these commands on the EC2 instance terminal:

### For Amazon Linux 2

```bash
sudo yum update -y
sudo amazon-linux-extras install docker
sudo service docker start
sudo usermod -a -G docker ec2-user
# Log out and log back in for group changes to take effect
```

### For Ubuntu

```bash
sudo apt-get update
sudo apt-get install -y docker.io
sudo systemctl start docker
sudo usermod -aG docker ubuntu
# Log out and back in
```

---

## 6. Copy Your Flask App and Dockerfile to EC2

From your local machine, use `scp` to copy your project:

```bash
scp -i your-key.pem app.py Dockerfile ec2-user@<EC2-public-IP>:~/
```

Replace `ec2-user` with `ubuntu` if Ubuntu.

---

## 7. Build and Run Docker Image on EC2

SSH back into EC2 and run:

```bash
docker build -t flask-ec2-app .
docker run -d -p 5000:5000 flask-ec2-app
```

* `-d` runs container in detached mode
* `-p 5000:5000` maps container port 5000 to EC2 port 5000

---

## 8. Access Your Flask App

Open browser:

```
http://<EC2-public-IP>:5000/
```

You should see:

```
Hello from Flask on EC2 with Docker!
```

---

## Summary Table

| Step                 | Command / Action                                         |
| -------------------- | -------------------------------------------------------- |
| Launch EC2           | Use Amazon Linux 2 or Ubuntu                             |
| SSH                  | `ssh -i key.pem ec2-user@<public-ip>`                    |
| Install Docker       | `sudo yum install docker` / `sudo apt install docker.io` |
| Copy Files           | `scp -i key.pem app.py Dockerfile ec2-user@<ip>:~/`      |
| Build Docker Image   | `docker build -t flask-ec2-app .`                        |
| Run Docker Container | `docker run -d -p 5000:5000 flask-ec2-app`               |
| Access App           | `http://<public-ip>:5000`                                |

---

## Optional: Run Flask on Port 80 (HTTP default)

If you want your app accessible on port 80 (so no port in URL), you can map ports:

```bash
docker run -d -p 80:5000 flask-ec2-app
```

Make sure port 80 is allowed in your EC2 security group.

---
