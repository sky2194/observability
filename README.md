# Monitoring Stack – Prometheus, Grafana, Alertmanager, Node Exporter

A full local monitoring solution using **Docker Compose** on macOS, providing real-time metrics collection, alerting, and visualization.

**Flow Explanation:**

1. **Node Exporter** collects system metrics (CPU, memory, disk).  
2. **Prometheus** scrapes Node Exporter and other targets.  
3. **Alertmanager** receives alerts from Prometheus when rules trigger.  
4. **Grafana** visualizes metrics from Prometheus.  
5. Browser interacts with Grafana, Prometheus, and Alertmanager.

---

## ⚡ Features

- Real-time monitoring of system metrics.  
- Demo alert pre-configured to test Alertmanager.  
- Grafana dashboards for visualization.  
- Fully macOS compatible with Docker Compose.  
- Quick start/stop with a single command.

---

## 🛠️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/monitoring-stack.git
cd monitoring-stack


Prometheus:   http://localhost:9090 

Grafana:      http://localhost:3000
U/P:          admin/admin

Alertmanager  http://localhost:9093

Node Exporter http://localhost:9100/metrics







---

## 🛠️ Services

### Prometheus
- Runs on port `9090`  
- Scrapes metrics from Node Exporter, App1, App2, and Alertmanager  

### Grafana
- Runs on port `3000`  
- Login: `admin/admin`  
- Import dashboards for Node Exporter (`1860`) or create custom panels for App1/App2  

### Alertmanager
- Runs on port `9093`  
- Receives alerts from Prometheus based on rules  

### Node Exporter
- Runs on port `9100`  
- Exposes host-level metrics: CPU, memory, disk, network  

### App1 – Demo Service
- Runs on port `8001`  
- Prometheus metric: `app1_requests_total`  
- Visit:  
  - [http://localhost:8001](http://localhost:8001) → increments counter  
  - [http://localhost:8001/metrics](http://localhost:8001/metrics) → Prometheus metrics  

### App2 – Demo Service
- Runs on port `8002`  
- Prometheus metric: `app2_requests_total`  
- Visit:  
  - [http://localhost:8002](http://localhost:8002) → increments counter  
  - [http://localhost:8002/metrics](http://localhost:8002/metrics) → Prometheus metrics  

---

## 🚀 Quick Start

1. **Clone the repository**:

```bash
git clone https://github.com/<your-username>/observability.git
cd observability
