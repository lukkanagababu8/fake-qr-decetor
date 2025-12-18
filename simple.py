echo import re > simple.py
echo. >> simple.py
echo class QRDetector: >> simple.py
echo     def check(self, text): >> simple.py
echo         score = 0 >> simple.py
echo         warnings = [] >> simple.py
echo         text_lower = text.lower() >> simple.py
echo         if "bit.ly" in text_lower: >> simple.py
echo             score += 40 >> simple.py
echo             warnings.append("URL shortener") >> simple.py
echo         if ".exe" in text_lower: >> simple.py
echo             score += 60 >> simple.py
echo             warnings.append("Executable file") >> simple.py
echo         if "javascript:" in text_lower: >> simple.py
echo             score += 80 >> simple.py
echo             warnings.append("JavaScript code") >> simple.py
echo         if score ^> 60: result = "DANGEROUS" >> simple.py
echo         elif score ^> 30: result = "SUSPICIOUS" >> simple.py
echo         else: result = "SAFE" >> simple.py
echo         return {"score": score, "result": result, "warnings": warnings} >> simple.py
echo. >> simple.py
echo def main(): >> simple.py
echo     print("FAKE QR DETECTOR") >> simple.py
echo     detector = QRDetector() >> simple.py
echo     while True: >> simple.py
echo         text = input("Enter QR content: ") >> simple.py
echo         if text == "exit": break >> simple.py
echo         result = detector.check(text) >> simple.py
echo         print(f"Result: {result['result']} ({result['score']}/100)") >> simple.py
echo         if result['warnings']: >> simple.py
echo             for w in result['warnings']: print(f"  Warning: {w}") >> simple.py
echo. >> simple.py
echo if __name__ == "__main__": >> simple.py
echo     main() >> simple.py