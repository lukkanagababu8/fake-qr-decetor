#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fake QR Code Detector - Main Script
"""

import os
import sys
from qr_detector import SimpleQRDetector

def main():
    detector = SimpleQRDetector()
    
    print("\n" + "="*50)
    print("   FAKE QR CODE DETECTOR")
    print("="*50)
    
    while True:
        print("\nOPTIONS:")
        print("1. Scan QR code from image file")
        print("2. Scan using webcam")
        print("3. Generate test QR code")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == '1':
            file_path = input("Enter image file path: ").strip()
            
            if not os.path.exists(file_path):
                print("Error: File not found!")
                continue
            
            detector.scan(file_path)
        
        elif choice == '2':
            print("\nWebcam feature requires OpenCV.")
            print("Install: pip install opencv-python")
            continue
        
        elif choice == '3':
            generate_test_qr()
        
        elif choice == '4':
            print("\nGoodbye!")
            break
        
        else:
            print("Invalid choice!")

def generate_test_qr():
    """Generate test QR codes"""
    try:
        import qrcode
        
        print("\nGenerate Test QR Code:")
        print("1. Safe QR (Google.com)")
        print("2. Suspicious QR (Short URL)")
        print("3. Dangerous QR (Fake login)")
        
        choice = input("Select type (1-3): ").strip()
        
        test_data = {
            '1': 'https://www.google.com',
            '2': 'https://bit.ly/test-fake-qr',
            '3': 'http://paypal-verify-secure.xyz/login'
        }.get(choice)
        
        if test_data:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(test_data)
            qr.make(fit=True)
            
            filename = f"test_qr_{choice}.png"
            img = qr.make_image(fill='black', back_color='white')
            img.save(filename)
            
            print(f"\nTest QR code saved as '{filename}'")
            print(f"Content: {test_data}")
        else:
            print("Invalid choice!")
    
    except ImportError:
        print("Install qrcode: pip install qrcode[pil]")

if __name__ == "__main__":
    main()