# 🏡 Eco Sense

**An Intelligent Smart ClassClassRoom Automation System**

Eco Sense is a smart ClassRoom automation project that uses computer vision and AI to detect human presence and automatically control ClassRoom appliances such as lights and fans.

The system aims to improve energy efficiency, reduce unnecessary electricity consumption, and make everyday ClassRoom management smarter and more convenient.

## ✨ Features

- **AI-Based Human Detection:** Detects human presence using YOLO.
- **Automatic Light Control:** Turns lights ON when a person is detected and OFF when the ClassRoom is empty.
- **Automatic Fan Control:** Controls the fan based on ClassRoom occupancy.
- **Real-Time Monitoring:** Monitors ClassRoom occupancy and appliance status.
- **Smart Dashboard:** Provides a user-friendly interface to monitor and manage connected devices.
- **Energy Efficiency:** Helps reduce electricity wastage by avoiding unnecessary appliance usage.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| React.js | Frontend development |
| Tailwind CSS | UI styling |
| Python | AI and backend development |
| FastAPI | Backend API framework |
| YOLO | Human detection |
| OpenCV | Image and video processing |
| MySQL | Database management |

## 📁 Project Structure

```text
eco-sense/
│
├── client/                 # React frontend
│
├── server/                 # FastAPI backend
│
├── ml/                     # AI and human detection
│
├── README.md
├── LICENSE
└── .gitignore
```

## ⚙️ How It Works

1. The webcam captures the ClassRoom's live Image.
2. The AI model processes the Image and detects whether a person is present.
3. The detection result is sent to the backend.
4. The backend processes the occupancy status.
5. Based on the occupancy status, the system controls the connected lights and fans.
6. The dashboard displays the current ClassRoom and appliance status.