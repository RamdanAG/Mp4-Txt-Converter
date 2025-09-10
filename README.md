# MP4 ⇆ TXT Converter

A simple web app to **convert MP4 files into text (Base64)** and back from **TXT into MP4**.  
Built with **Python (Flask)** for backend and **HTML + CSS + JavaScript** for frontend.  

Includes:
- ✅ File upload & download  
- ✅ Encode MP4 → TXT (Base64)  
- ✅ Decode TXT → MP4  
- ✅ Progress bar (upload & processing)  
- ✅ Ready to deploy on **Vercel**  

---

## Features
- Convert any `.mp4` file into a `.txt` file with Base64 encoding.
- Convert `.txt` (Base64 string) back into `.mp4`.

---
## 🛠️ Installation & Usage
### 1. Clone the repository
```bash
git clone https://github.com/your-username/mp4-txt-converter.git
cd mp4-txt-converter
````

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install flask flask-cors
```

### 3. Install dependencies
```bash
python app.py
```

## Notes
- Encoding to Base64 increases file size (about +33%), this is not compression.
- Use this tool if you need MP4 data in text form (e.g., for transport over text-only channels).
