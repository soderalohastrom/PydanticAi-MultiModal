# 🖼️ Pydantic-AI MultiModal Image Processor

A demonstration project showcasing how to use MultiModal capabilities with Pydantic-AI to process and analyze images using OpenAI's LLM. This project specifically focuses on resume analysis and information extraction from images, Feel free to customize it as per your needs.

## ✨ Features
- 🔄 Image processing using OpenAI's LLM
- 📊 Structured data extraction using Pydantic models
- 🎨 Support for multiple image formats
- 📄 Resume information extraction including:
  - 🔗 LinkedIn profile
  - 💻 GitHub profile
  - 📧 Email
  - 💼 Work experience
  - 🎓 Education
  - 🛠️ Skills

## 📋 Prerequisites
- 🐍 Python 3.8+
- 🔑 OpenAI API key
- 📦 Git

## 🚀 Installation
1. Clone the repository:
```bash
git clone https://github.com/rawheel/Pydantic-ai-MultiModal-Example.git
cd Pydantic-ai-MultiModal-Example
```

2. Set up virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Environment variables:
```env
LLM_MODEL=gpt-4o-mini
OPENAI_API_KEY=your_openai_api_key_here
```

## 📝 Usage
Basic usage web URLs:
```python
from app import ImageSummarizer
# Initialize summarizer
summarizer = ImageSummarizer()
# Example image URLs
image_urls = [
    'https://example.com/path/to/image.jpg',
    # Add more image URLs as needed
]
# Run analysis
summary = summarizer.summarize(image_urls, "summarize the resume")
print(summary)
```

Run the example script:
```bash
python app.py
```

## 📁 Project Structure
```
├── app.py            # Main application file
├── config.py         # Configuration settings
├── requirements.txt  # Project dependencies
├── .env             # Environment variables (create this)
└── README.md        # Project documentation
```

## ⚙️ Configuration
The project uses environment variables for configuration. Available options:
- `LLM_MODEL`: The OpenAI model to use (example: "gpt-4o-mini")
- `OPENAI_API_KEY`: Your OpenAI API key

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments
- [Pydantic-AI](https://ai.pydantic.dev/)
- [OpenAI](https://platform.openai.com/docs/)

## 👤 Author
**Raheel Siddiqui**
- 🌐 GitHub: [@rawheel](https://github.com/rawheel)
- 💼 LinkedIn: [Raheel Siddiqui](https://www.linkedin.com/in/rawheel/)

---

⭐️ If you find this project useful, please consider giving it a star!
