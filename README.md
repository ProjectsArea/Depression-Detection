# MindCare - Depression Detection System

A professional AI-powered web application for detecting depression patterns in text using advanced machine learning models. This system provides mental health screening tools with a beautiful, user-friendly interface.

## 🌟 Features

- **AI-Powered Analysis**: Uses ensemble of ML models (SVM, Random Forest, BiLSTM)
- **Professional UI**: Modern, responsive web interface with mental health theme
- **Real-time Processing**: Instant text analysis with confidence scores
- **Privacy-First**: All processing done locally, no data storage
- **Support Resources**: Integrated emergency helplines and mental health resources
- **Beautiful Design**: Full-width hero sections with custom wireframe imagery
- **Mobile Responsive**: Works seamlessly on all devices

## 🧠 About the Project

MindCare is an advanced depression detection system that analyzes text patterns to identify potential indicators of depression. The system uses:

- **Natural Language Processing** to understand emotional patterns
- **Machine Learning Ensemble** combining multiple models for accuracy
- **Professional UI Design** created with mental health context in mind
- **Evidence-based Approach** built on clinical standards

### Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Machine Learning**: Scikit-learn, TensorFlow/Keras
- **UI Framework**: Custom CSS with FontAwesome icons
- **Typography**: Inter font family

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd Depression
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify Model Files**
   Ensure the following model files exist in the `saved_models/` directory:
   - `tfidf_vectorizer.pkl`
   - `svm_model.pkl`
   - `rf_model.pkl`
   - `tokenizer.pkl`
   - `bilstm_model.keras`
   - `ensemble_config.pkl`

5. **Add Your Image**
   Place your wireframe image as `static/Image.png` for the hero sections

6. **Run the Application**
   ```bash
   python app.py
   ```

7. **Access the Application**
   Open your browser and navigate to: `http://127.0.0.1:5001`

## 📁 Project Structure

```
Depression/
├── app.py                 # Main Flask application
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── static/
│   ├── style.css         # Professional styling
│   └── Image.png         # Wireframe hero image
├── templates/
│   ├── home.html         # Professional home page
│   ├── index.html        # Detection page
│   └── about.html        # About page with features
└── saved_models/         # Pre-trained ML models
    ├── tfidf_vectorizer.pkl
    ├── svm_model.pkl
    ├── rf_model.pkl
    ├── tokenizer.pkl
    ├── bilstm_model.keras
    └── ensemble_config.pkl
```

## 🎯 How It Works

### 1. Text Input
Users enter their thoughts and feelings in a secure, private text area.

### 2. Preprocessing
- Text cleaning and normalization
- Tokenization and feature extraction
- TF-IDF vectorization

### 3. Model Analysis
The system uses an ensemble approach:

- **SVM Model**: Pattern recognition in text features
- **Random Forest**: Feature importance analysis
- **BiLSTM Neural Network**: Sequential pattern detection

### 4. Result Generation
- Confidence score calculation (0-100%)
- Depression likelihood assessment
- Support resource recommendations

### 5. Support Resources
If depression is detected, the system provides:
- Emergency helpline numbers
- Professional help resources
- Support group information

## 🛠️ Technical Details

### Machine Learning Pipeline

1. **Text Preprocessing**
   ```python
   def clean_text(text):
       # Lowercase conversion
       # Special character removal
       # Tokenization
   ```

2. **Feature Extraction**
   - TF-IDF Vectorization (5000 features)
   - Sequential tokenization for BiLSTM

3. **Model Ensemble**
   - Individual model predictions
   - Weighted averaging for final result
   - Confidence threshold optimization

### API Endpoints

- `GET /` - Redirects to home page
- `GET /home` - Professional home page
- `GET /about` - About page with features
- `GET /detect` - Detection page
- `POST /detect` - Text analysis endpoint

### Model Performance

- **Accuracy**: ~85-90% (depending on dataset)
- **Processing Time**: <2 seconds
- **Confidence Threshold**: 0.4-0.5 (configurable)

## 🎨 UI/UX Features

### Design Principles
- **Mental Health Focus**: Calming colors and thoughtful design
- **Accessibility**: WCAG compliant design patterns
- **Privacy**: No data storage, local processing only
- **Professional**: Healthcare-grade interface standards

### Key UI Elements
- **Hero Sections**: Full-width with custom wireframe imagery
- **Navigation**: Clean, intuitive menu system
- **Forms**: User-friendly input with character counting
- **Results**: Beautiful confidence bars and visual indicators
- **Resources**: Emergency helplines prominently displayed

## 📱 Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## 🔧 Configuration

### Environment Variables
```bash
# Optional configuration
FLASK_ENV=development
FLASK_DEBUG=True
```

### Model Configuration
Edit `saved_models/ensemble_config.pkl` to adjust:
- Model weights
- Confidence thresholds
- Feature parameters

## 🚨 Important Disclaimer

**This tool is for informational purposes only and is not a substitute for professional medical diagnosis, advice, or treatment.**

- Always consult with qualified healthcare professionals
- Emergency situations: Call 988 or local emergency services
- This tool does not store any personal data
- Results should be used as screening, not diagnosis

## 🆘 Emergency Resources

### United States
- **988** - Suicide & Crisis Lifeline (24/7)
- **1-800-662-HELP (4357)** - National Mental Health Helpline
- **Text HOME to 741741** - Crisis Text Line

### International
- Contact local emergency services
- Seek professional mental health support
- Visit local healthcare providers

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Mental health professionals for clinical guidance
- Open-source ML libraries (Scikit-learn, TensorFlow)
- Mental health advocacy organizations
- User testing and feedback contributors

## 📞 Support

For technical support or questions:
- Create an issue in the repository
- Check the troubleshooting section below

## 🔧 Troubleshooting

### Common Issues

1. **Model Loading Errors**
   - Verify all model files exist in `saved_models/`
   - Check file permissions
   - Ensure compatible Python/ML library versions

2. **Port Already in Use**
   ```bash
   # Change port in app.py
   app.run(host="127.0.0.1", port=5002, debug=True)
   ```

3. **Dependencies Installation**
   ```bash
   # Upgrade pip
   python -m pip install --upgrade pip
   
   # Install requirements
   pip install -r requirements.txt --force-reinstall
   ```

4. **Image Not Displaying**
   - Ensure `static/Image.png` exists
   - Check file path and permissions
   - Verify image format (PNG recommended)

### Performance Optimization

- Use GPU for BiLSTM model if available
- Optimize TF-IDF vectorizer memory usage
- Implement caching for repeated analyses

## 📈 Future Enhancements

- [ ] Multi-language support
- [ ] Voice input capability
- [ ] Mobile app development
- [ ] Integration with healthcare systems
- [ ] Advanced emotion detection
- [ ] Longitudinal tracking features

---

**Built with ❤️ for mental health awareness and support**

*Remember: Your mental health matters. This tool is here to help, but professional care is always the best choice.*
