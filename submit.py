import json
import hmac
import hashlib
import requests
from datetime import datetime, timezone

SIGNING_SECRET = b"hello-there-from-b12"
URL = "https://b12.io/apply/submission"


def main():
    payload = {
        "action_run_link": "REPLACE_ME",
        "email": "dodlasaisukruthreddy@gmail.com",
        "name": "Sai Sukruth Reddy Dodla",
        "repository_link": "https://github.com/sukruthreddy2004/b12-Application",
        "resume_link": "https://drive.google.com/file/d/1IJHMFPb4th7y2esOp1Y5iC9k8Y2e_xxo/view?usp=drive_link",
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z"),
    }

    body = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode("utf-8")

    signature = hmac.new(
        SIGNING_SECRET,
        body,
        hashlib.sha256
    ).hexdigest()

    headers = {
        "Content-Type": "application/json",
        "X-Signature-256": f"sha256={signature}",
    }

    response = requests.post(URL, data=body, headers=headers)
    response.raise_for_status()
    
    data = response.json()
    print("B12_Receipt:" , data["receipt"])


if __name__ == "__main__":
    main()
