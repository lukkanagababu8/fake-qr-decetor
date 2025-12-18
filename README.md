# 🔒 Fake QR Code Detector

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8%2B-green)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

A comprehensive security tool to detect malicious QR codes that could lead to phishing sites, malware downloads, or scam pages. Protect yourself from QR code-based attacks with real-time analysis and threat detection.

## 🚀 Features

### 🔍 **Multi-Layer Detection**
- **URL Analysis**: Checks for suspicious patterns, URL shorteners, and phishing attempts
- **Content Scanning**: Detects executable files, malicious scripts, and dangerous protocols
- **Visual Tampering Detection**: Identifies physically altered or re-encoded QR codes
- **Threat Intelligence**: Integrates with security databases (Google Safe Browsing, VirusTotal)

### 🎯 **Detection Capabilities**
- ✅ URL shorteners (bit.ly, tinyurl, etc.)
- ✅ Executable files (.exe, .apk, .jar, .msi)
- ✅ JavaScript and data URI schemes
- ✅ IP address URLs and local network links
- ✅ Credential embedding attacks (@ symbol trick)
- ✅ Homograph attacks and typosquatting
- ✅ Suspicious TLDs (.xyz, .top, .gq, .ml)
- ✅ Base64 encoded malicious content

### 💻 **Multiple Interfaces**
- **Command Line Interface** - Quick scans and batch processing
- **Web Application** - User-friendly browser interface
- **Webcam Scanner** - Real-time QR code scanning
- **API Endpoints** - Integrate with other applications

## 📸 Screenshots

| Command Line Interface | Web Interface | Risk Analysis |
|-----------------------|---------------|---------------|
| ![CLI Screenshot](screenshots/cli.png) | ![Web Screenshot](screenshots/web.png) | ![Analysis Screenshot](screenshots/analysis.png) |

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Webcam (optional, for real-time scanning)

### Quick Install (One Command)
```bash
# Clone the repository
https://github.com/lukkanagababu8/fake-qr-decetor.git
cd fake-qr-detector

# Run the setup script
python main.py
python web_app.py
