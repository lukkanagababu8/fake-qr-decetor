#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fake QR Code Detector
"""

import re
from urllib.parse import urlparse
import requests
import os

try:
    from pyzbar.pyzbar import decode
    from PIL import Image
    HAS_DECODER = True
except ImportError:
    HAS_DECODER = False
    print("Warning: Install pyzbar and PIL for QR decoding")
    print("Run: pip install pyzbar pillow")

class SimpleQRDetector:
    def __init__(self):
        self.blacklist = [
            'bit.ly', 'tinyurl.com', 'shorturl', 'ow.ly',
            'file://', 'javascript:', 'data:', 'ftp://'
        ]
    
    def decode_qr(self, image_path):
        """Read QR code from image"""
        if not HAS_DECODER:
            print("No QR decoder available.")
            data = input("Enter QR code content manually: ")
            return data
        
        try:
            img = Image.open(image_path)
            decoded = decode(img)
            
            if decoded:
                data = decoded[0].data.decode('utf-8')
                return data
            return None
        except Exception as e:
            print(f"Decode error: {e}")
            return None
    
    def analyze_content(self, data):
        """Check if content is suspicious"""
        warnings = []
        risk_score = 0
        
        is_url = data.startswith(('http://', 'https://', 'www.', 'ftp://'))
        
        # Check blacklisted patterns
        for pattern in self.blacklist:
            if pattern in data.lower():
                warnings.append(f"Suspicious pattern: {pattern}")
                risk_score += 30
        
        # Check for executable files
        exec_extensions = ['.exe', '.bat', '.sh', '.jar', '.apk', '.dmg', '.msi']
        for ext in exec_extensions:
            if ext in data.lower():
                warnings.append(f"Executable file: {ext}")
                risk_score += 40
        
        # Check URL structure
        if is_url:
            try:
                parsed = urlparse(data if '://' in data else f'http://{data}')
                
                if re.match(r'^\d+\.\d+\.\d+\.\d+$', parsed.netloc):
                    warnings.append("Uses IP address instead of domain")
                    risk_score += 25
                
                if '@' in data:
                    warnings.append("Contains @ symbol (credential embedding)")
                    risk_score += 35
                
                if parsed.netloc.count('.') > 3:
                    warnings.append("Too many subdomains")
                    risk_score += 15
                
                suspicious_words = ['login', 'secure', 'verify', 'bank', 'paypal', 'password']
                for word in suspicious_words:
                    if word in data.lower():
                        warnings.append(f"Sensitive keyword: {word}")
                        risk_score += 10
            
            except:
                pass
        
        # Check for crypto addresses
        crypto_patterns = [
            r'0x[a-fA-F0-9]{40}',
            r'[13][a-km-zA-HJ-NP-Z1-9]{25,34}'
        ]
        for pattern in crypto_patterns:
            if re.search(pattern, data):
                warnings.append("Cryptocurrency address")
                risk_score += 20
        
        # Determine safety level
        if risk_score >= 60:
            status = "DANGEROUS"
        elif risk_score >= 30:
            status = "SUSPICIOUS"
        elif risk_score >= 10:
            status = "CAUTION"
        else:
            status = "SAFE"
        
        return {
            'data': data,
            'is_url': is_url,
            'risk_score': risk_score,
            'status': status,
            'warnings': warnings,
            'total_warnings': len(warnings)
        }
    
    def scan(self, image_path):
        """Complete scan of QR code"""
        print(f"\n{'='*50}")
        print(f"Scanning: {image_path}")
        print('='*50)
        
        data = self.decode_qr(image_path)
        if not data:
            print("No QR code found or cannot decode!")
            return None
        
        print(f"Decoded Data: {data[:100]}..." if len(data) > 100 else f"Decoded Data: {data}")
        
        result = self.analyze_content(data)
        
        print(f"\nSAFETY STATUS: {result['status']}")
        print(f"Risk Score: {result['risk_score']}/100")
        
        if result['warnings']:
            print(f"\nWARNINGS ({result['total_warnings']} found):")
            for warning in result['warnings']:
                print(f"  * {warning}")
        else:
            print("\nNo warnings detected")
        
        if result['is_url']:
            print(f"\nURL Detected")
            url = data if '://' in data else f'http://{data}'
            try:
                response = requests.head(url, timeout=3, allow_redirects=True)
                print(f"Online check: HTTP {response.status_code}")
            except:
                print(f"Online check: Not reachable")
        
        return result