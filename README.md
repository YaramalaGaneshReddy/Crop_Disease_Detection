# 🌿 CropDoc — AI Crop Disease Detection

> **Snap a leaf. Find the problem. Fix it early.**

CropDoc is a **multilingual AI-powered crop health assistant** for farmers. Upload a photo of a diseased leaf or describe the problem in plain language, and CropDoc — powered by **Google Gemini** — instantly identifies the likely disease, pest, or nutrient deficiency and suggests practical treatment steps.

---

## ✨ Features

| Feature | Details |
|---|---|
| 📷 **Photo diagnosis** | Upload a leaf/plant photo directly in the chat |
| 🌐 **Multilingual** | Replies in English, Hindi, Gujarati, Telugu, Tamil, Marathi, or Kannada |
| 🌾 **Crop-aware** | Tailored advice for Tomato, Potato, Rice, Wheat, Cotton, Maize, Groundnut & more |
| 📄 **Downloadable report** | Generate and save a plain-text diagnosis report |
| ⚕️ **Safe & honest** | Confidence levels clearly stated; never gives exact pesticide dosages |
| 🔄 **Multi-turn chat** | Conversational: ask follow-up questions in the same session |

---

## 🖼️ Demo

<p align="center">
  <img src="https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit badge"/>
  <img src="https://img.shields.io/badge/Powered%20by-Google%20Gemini-4285F4?logo=google&logoColor=white" alt="Gemini badge"/>
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white" alt="Python badge"/>
</p>

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- A [Google AI Studio](https://aistudio.google.com/) account (free) to get a **Gemini API key**

### 1. Clone the repository

```bash
git clone https://github.com/YaramalaGaneshReddy/Crop_Disease_Detection.git
cd Crop_Disease_Detection
```

### 2. Create and activate a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Copy the example secrets file and add your Gemini API key:

```bash
# Windows
copy .streamlit\secrets.toml.example .streamlit\secrets.toml

# macOS / Linux
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
```

Then edit `.streamlit/secrets.toml`:

```toml
GEMINI_API_KEY = "your_actual_gemini_api_key_here"
```

> Warning: **Never commit `secrets.toml` to version control.** It is already listed in `.gitignore`.

### 5. Run the app

```bash
streamlit run app.py
```

Open your browser at [http://localhost:8501](http://localhost:8501).

---

## 📁 Project Structure

```
Crop_Disease_Detection/
├── app.py                      # Main Streamlit application
├── prompts.py                  # Re-export shim for prompts
├── promts.py                   # System prompt, welcome message & report template
├── requirements.txt            # Python dependencies
├── .gitignore                  # Files excluded from version control
└── .streamlit/
    ├── secrets.toml            # Your API key (NOT committed)
    └── secrets.toml.example    # Template for secrets
```

---

## 🏗️ How It Works

```
User (farmer)
    |
    v
Streamlit UI (app.py)
    |  --- text or image input --->
    v
Google Gemini API (multimodal)
    |  <-- structured diagnosis ---
    v
Chat response displayed with:
  * Likely problem & confidence level
  * Visible symptoms
  * Organic + cultural + chemical treatment steps
  * Prevention tips
    |
    v
Optional: Generate & download a plain-text report
```

---

## 🌍 Supported Languages

English · Hindi · Gujarati · Telugu · Tamil · Marathi · Kannada

---

## 🛡️ Safety & Disclaimer

- CropDoc **never provides exact pesticide dosages** — always directs farmers to read the product label.
- All diagnoses are clearly labelled as **AI estimates, not laboratory tests**.
- Users are encouraged to confirm results with their local **Krishi Vigyan Kendra (KVK)** or agriculture officer.

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `streamlit` | Web UI framework |
| `google-genai` | Google Gemini API client |

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Yaramala Ganesh Reddy**  
GitHub: [@YaramalaGaneshReddy](https://github.com/YaramalaGaneshReddy)
