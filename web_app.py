from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
from qr_detector import SimpleQRDetector

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB

detector = SimpleQRDetector()

# Create upload folder
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Fake QR Code Detector</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                background: #f5f5f5;
            }
            .container {
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            h1 {
                color: #333;
                text-align: center;
            }
            .upload-box {
                border: 2px dashed #ccc;
                padding: 40px;
                text-align: center;
                margin: 20px 0;
                border-radius: 5px;
            }
            button {
                background: #4CAF50;
                color: white;
                padding: 12px 24px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
                margin: 10px;
            }
            button:hover {
                background: #45a049;
            }
            #result {
                margin-top: 30px;
                padding: 20px;
                border-radius: 5px;
                display: none;
            }
            .safe { background: #d4edda; color: #155724; }
            .danger { background: #f8d7da; color: #721c24; }
            .warning { background: #fff3cd; color: #856404; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔒 Fake QR Code Detector</h1>
            
            <div class="upload-box">
                <h3>Upload QR Code Image</h3>
                <input type="file" id="fileInput" accept="image/*">
                <br><br>
                <button onclick="uploadImage()">📤 Upload & Scan</button>
            </div>
            
            <div id="result"></div>
        </div>
        
        <script>
            function uploadImage() {
                const fileInput = document.getElementById('fileInput');
                const file = fileInput.files[0];
                
                if (!file) {
                    alert('Please select a file!');
                    return;
                }
                
                const formData = new FormData();
                formData.append('file', file);
                
                fetch('/scan', {
                    method: 'POST',
                    body: formData
                })
                .then(response => response.json())
                .then(data => {
                    displayResult(data);
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('Scan failed!');
                });
            }
            
            function displayResult(data) {
                const resultDiv = document.getElementById('result');
                
                let statusClass = 'safe';
                if (data.status.includes('DANGEROUS')) statusClass = 'danger';
                else if (data.status.includes('SUSPICIOUS')) statusClass = 'warning';
                
                let html = `
                    <div class="${statusClass}">
                        <h2>${data.status}</h2>
                        <p><strong>Risk Score:</strong> ${data.risk_score}/100</p>
                        <p><strong>Data:</strong> ${data.data}</p>
                `;
                
                if (data.warnings && data.warnings.length > 0) {
                    html += `<h4>⚠️ Warnings:</h4><ul>`;
                    data.warnings.forEach(warning => {
                        html += `<li>${warning}</li>`;
                    });
                    html += `</ul>`;
                } else {
                    html += `<p>✅ No warnings detected</p>`;
                }
                
                html += `</div>`;
                resultDiv.innerHTML = html;
                resultDiv.style.display = 'block';
            }
        </script>
    </body>
    </html>
    '''

@app.route('/scan', methods=['POST'])
def scan():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'})
    
    # Save file
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    
    # Scan QR code
    result = detector.scan(filepath)
    
    # Clean up
    os.remove(filepath)
    
    if result:
        return jsonify(result)
    else:
        return jsonify({'error': 'Failed to scan QR code'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)