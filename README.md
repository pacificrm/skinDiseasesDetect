# 🩺 Skin Disease Detection Model

An application for detecting skin diseases using advanced Vision Transformer models. The model is quantized with ONNX for efficient performance and is served via a FastAPI backend.

---

## 📂 Dataset Used  

The dataset used for this project is publicly available on Kaggle:  
[Skin Disease Dataset](https://www.kaggle.com/datasets/pacificrm/skindiseasedataset)  

This dataset consists of images classified into 22 distinct skin disease categories.

---

## 🧠 Model Information  

- **Model Architecture**: Vision Transformer (ViT)  
- **Model Optimization**: Quantized using ONNX for faster inference and reduced resource usage.  

---

## ⚙️ Backend Details  

The backend is built with **FastAPI**, enabling seamless API interactions.  

### API Hosted Link:  
[Skin Disease Detect API Documentation](https://skindiseasesdetect-2.onrender.com/docs)  

---

## 🛠️ Local Setup  

### Prerequisites  

Ensure you have Python and pip installed. Then install the required packages:  

```bash
pip install -r requirements.txt
```
## 🛠️ Running the Application  

To start the application locally, run the following command:  

```bash
gunicorn service.main:app --workers 2 --worker-class uvicorn.workers.UvicornWorker
```
## ✍️ Owner Information
Developed and maintained by Prashant Kumar Mishra.

GitHub: [pacificrm](https://github.com/pacificrm)      
LinkedIn: [Profile Link](https://www.linkedin.com/in/pacificrm)  
For queries, suggestions, or contributions, feel free to reach out!
