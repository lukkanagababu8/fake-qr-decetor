import os

def fix_file_encoding(filename):
    """Remove BOM from file"""
    try:
        with open(filename, 'rb') as f:
            content = f.read()
        
        # Remove UTF-8 BOM if present
        if content.startswith(b'\xef\xbb\xbf'):
            content = content[3:]
        
        # Remove UTF-16 BOM if present
        elif content.startswith(b'\xff\xfe') or content.startswith(b'\xfe\xff'):
            # This is UTF-16, convert to UTF-8
            content = content.decode('utf-16').encode('utf-8')
        
        # Write back without BOM
        with open(filename, 'wb') as f:
            f.write(content)
        
        print(f"Fixed: {filename}")
        return True
        
    except Exception as e:
        print(f"Error fixing {filename}: {e}")
        return False

# Fix all Python files
files = ['main.py', 'qr_detector.py', 'web_app.py']
for file in files:
    if os.path.exists(file):
        fix_file_encoding(file)