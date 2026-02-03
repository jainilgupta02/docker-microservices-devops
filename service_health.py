import requests
import time

SERVICES = {
    "users": "http://localhost:5001/health",
    "orders": "http://localhost:5002/health",
    "payments": "http://localhost:5003/health",
}

def check_services():
    print("🔍 Checking microservices health...\n")

    for name, url in SERVICES.items():
        try:
            r = requests.get(url, timeout=2)
            status = "🟢 UP" if r.status_code == 200 else "🟡 DEGRADED"
        except Exception as e:
            status = f"🔴 DOWN ({e})"

        print(f"{name.upper():<10} → {status}")

if __name__ == "__main__":
    check_services()
