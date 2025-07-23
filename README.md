# 🎵 Spotify Android Automation Framework

Hybrid automation framework using **Python**, **Appium**, **Pytest**, and **POM** that automates key user flows in the Spotify Android app.

---

## 📂 Tech Stack

| Layer      | Tech / Tool                         |
|------------|-------------------------------------|
| Language   | Python 3.10+                        |
| Mobile Test| Appium + UIAutomator2               |
| Framework  | Pytest + Page Object Model (POM)    |
| Device     | Android Emulator                    |
| IDE        | VS Code                             |

---

## 📁 Project Structure

```
spotify-automation/
├── pages/               # POM classes for Spotify actions
│   └── spotify_page.py
├── tests/               # Pytest test cases
│   └── test_spotify.py
├── utils/               # Driver factory and helper functions
│   ├── driver_factory.py
│   └── helpers.py
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

---

## ✅ Features

### 🎧 Spotify Android App Automation

- Launch Spotify app  
- Search for a specific song (`All The Stars`)  
- Control playback (play/pause)  
- Add song to a playlist (`My Fav`)  
- Gracefully finalize and close app  

---

## ⚙️ Installation & Run

### 🔧 Install Dependencies

```bash
pip install -r requirements.txt
```

### 📱 Prerequisites

- Appium server running at `http://localhost:4723/`
- Android Emulator launched via Android Studio
- Spotify app installed on the emulator
- Proper capabilities set in `driver_factory.py`

---

### 🧪 Run Spotify Test

```bash
pytest tests/test_spotify.py
```

---

## 📬 Author

**Santanu Kumar Behera**  
*Python | Appium | Automation Engineer*  
🔗 [LinkedIn](https://www.linkedin.com/in/santanukb/)

---

## 📝 Notes

- Ensure Appium and Android tools are correctly installed and configured.
- Update package name/activity in driver setup if Spotify app changes.
- Emulator must be running before test execution.
- The script simulates real user behavior via UI automation.

---