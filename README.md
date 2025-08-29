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
