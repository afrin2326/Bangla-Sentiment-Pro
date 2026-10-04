# Bangla Sentiment Pro 🇧🇩

**Bangla Sentiment Analysis and Emotion Detection using BanglaBERT**

Bangla Sentiment Pro is an NLP-based application designed to analyze the sentiment and detect emotions in Bengali text using BanglaBERT and deep learning. It provides prediction results with confidence scores through an interactive Streamlit interface, supported by a FastAPI backend.

## 🚀 Features

* **Sentiment Analysis:** Predicts the sentiment expressed in Bengali text.
* **Emotion Detection:** Identifies the emotion conveyed by the input text.
* **BanglaBERT:** Uses a Bengali language model for contextual text understanding.
* **Confidence Scores:** Displays confidence scores alongside prediction results.
* **Interactive Web Interface:** Provides a user-friendly interface built with Streamlit.
* **REST API:** Exposes prediction functionality through FastAPI.
* **Deep Learning:** Uses PyTorch for model implementation and inference.

## 🛠️ Technologies Used

| Technology                | Purpose                                   |
| ------------------------- | ----------------------------------------- |
| Python                    | Core programming language                 |
| BanglaBERT                | Bengali language representation           |
| PyTorch                   | Deep learning and model inference         |
| FastAPI                   | Backend API                               |
| Streamlit                 | Interactive web interface                 |
| Hugging Face Transformers | Transformer model ecosystem               |
| Pandas                    | Data processing                           |
| Scikit-learn              | Machine learning utilities and evaluation |

## 🏗️ Project Architecture

```text
User
  |
  v
Streamlit Web Interface
  |
  v
FastAPI Backend
  |
  v
Bangla Text Processing
  |
  v
BanglaBERT-based Model
  |
  +--> Sentiment Prediction
  |
  +--> Emotion Prediction
  |
  v
Prediction Results and Confidence Scores
```

## 📂 Project Structure

```text
Bangla-Sentiment-Pro/
│
├── api/
│   └── main.py
│
├── webapp/
│   └── app.py
│
├── models/
│   ├── model_state.pt
│   └── banglabert_model/
│
├── requirements.txt
├── .gitattributes
└── README.md
```

*Note: The directory structure above highlights the main application files. Additional files may exist in the repository.*

## ⚙️ Installation and Setup

### Prerequisites

* Python installed on your system
* Git
* A compatible environment for PyTorch and Hugging Face Transformers

### 1. Clone the Repository

```bash
git clone https://github.com/afrin2326/Bangla-Sentiment-Pro.git
cd Bangla-Sentiment-Pro
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

**Windows (Git Bash):**

```bash
source venv/Scripts/activate
```

**Windows (Command Prompt):**

```cmd
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Make sure the required PyTorch and Transformers versions are compatible with your environment.

## ▶️ Run the Application

Start the FastAPI backend in the first terminal:

```bash
uvicorn api.main:app --reload
```

The backend will be available at:

`http://127.0.0.1:8000`

Open the interactive API documentation:

`http://127.0.0.1:8000/docs`

Start the Streamlit frontend in a second terminal:

```bash
streamlit run webapp/app.py
```

The web application will be available at:

`http://localhost:8501`

Keep the backend running while using the frontend.

## 🧠 Model Information

The project uses a BanglaBERT-based deep learning model for Bengali text analysis.

The trained model state is stored in:

```text
models/model_state.pt
```

The `.pt` file contains the saved PyTorch model state. The corresponding model architecture and tokenizer configuration must also be available for inference.

The repository uses Git Large File Storage (Git LFS) to manage the large model file.

## 🔌 API Usage

The backend exposes a prediction endpoint at:

```text
POST /predict
```

You can explore the endpoint, inspect its expected request format, and test predictions through the FastAPI Swagger UI:

`http://127.0.0.1:8000/docs`

The exact request fields and response format are defined by the FastAPI application.

## 🎯 Use Cases

* Bengali social media sentiment analysis
* Opinion mining from Bengali text
* Emotion analysis of user-generated content
* Bengali NLP research and experimentation
* Text analytics for Bengali-language applications

## 🔮 Future Improvements

* Expand evaluation across diverse Bengali datasets and dialects.
* Improve robustness to spelling variations and informal language.
* Add comprehensive model evaluation metrics.
* Deploy the application for public access.
* Extend support for additional Bengali NLP tasks.

## 👩‍💻 Author

**Mst Afrin Binte Amin**

Computer Science and Engineering | Machine Learning & NLP Enthusiast

* GitHub: [@afrin2326](https://github.com/afrin2326)
* Project Repository: [Bangla-Sentiment-Pro](https://github.com/afrin2326/Bangla-Sentiment-Pro)

## 📄 License

A license has not been specified in this README. Add an appropriate `LICENSE` file before distributing the project for reuse.

---

*Built to explore Bengali Natural Language Processing through transformer-based deep learning.*
