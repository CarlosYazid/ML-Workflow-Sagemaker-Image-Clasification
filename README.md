# 🚀 Deployment and Monitoring of a Machine Learning Workflow on AWS

This repository contains a **Machine Learning workflow for image classification**, deployed on **AWS**.  
The workflow leverages **AWS Step Functions** as an orchestrator and integrates multiple **AWS Lambda Functions** along with an **Amazon SageMaker Endpoint** for inference.

The use case simulates a business scenario where it is necessary to:

- Automatically process images.  
- Perform predictions on their content.  
- Make decisions based on a configurable confidence threshold.  

<p align="center">
  <img src="static/images/Screenshot 2025-09-16 2.25.30 PM.png" alt="Workflow architecture diagram" width="650"/>
</p>

---

## 📂 Repository Structure

```bash
ml-image-classification-workflow/
├── notebooks/
│   └── starter.ipynb              # Jupyter notebook for data preparation and model deployment
├── scripts/
│   ├── lambdas/
│   │   ├── retrieve_image_to_s3.py # Lambda: fetches image from S3 and serializes it
│   │   ├── inference.py            # Lambda: invokes SageMaker endpoint for inference
│   │   └── valid_confidence.py     # Lambda: validates prediction confidence threshold
│   └── step-function/
│       └── definition.json         # AWS Step Functions state machine definition
├── static/
│   └── images/                     # Architecture diagrams and workflow screenshots
├── requirements.txt                # Project dependencies
├── .gitignore                      # Ignored files/directories
├── LICENSE                         # License file
└── README.md                       # Project documentation
```

---

## ⚙️ Workflow Architecture

The workflow is orchestrated by **AWS Step Functions** and consists of three main stages:  

1. **Retrieve data**  
   - Lambda: `retrieve_image_to_s3.py`  
   - Downloads the image from S3, encodes it as base64, and returns it to the workflow.  

2. **Inference**  
   - Lambda: `inference.py`  
   - Calls a **SageMaker Endpoint** (set in the `ENDPOINT` variable) to obtain prediction probabilities.  

3. **Valid confidence**  
   - Lambda: `valid_confidence.py`  
   - Checks if any prediction exceeds the configured threshold (`THRESHOLD = 0.75`).  
   - If not, the workflow ends with an error (`THRESHOLD_CONFIDENCE_NOT_MET`).  

<p align="center">
  <img src="static/images/Screenshot 2025-09-16 2.26.23 PM.png" alt="AWS Step Functions workflow view" width="650"/>
</p>

---

## 🔑 Key Files

- **`notebooks/starter.ipynb`** → Notebook with steps for training and deploying the SageMaker image classification model.  
- **`scripts/lambdas/retrieve_image_to_s3.py`** → Lambda that retrieves and serializes images from S3.  
- **`scripts/lambdas/inference.py`** → Lambda that calls a SageMaker endpoint. ⚠️ **Remember to configure the `ENDPOINT` variable with your model name.**  
- **`scripts/lambdas/valid_confidence.py`** → Lambda that validates the prediction confidence threshold.  
- **`scripts/step-function/definition.json`** → Step Functions state machine definition.  

---

## ▶️ How to Use

### 1. Environment Setup
```bash
pip install -r requirements.txt
```

### 2. Deployment
1. Train and deploy the model in SageMaker using the notebook (`starter.ipynb`).  
2. Create the **Lambda functions** in AWS using the scripts in `scripts/lambdas/`.  
   - Assign IAM roles with permissions for **S3, SageMaker, and CloudWatch**.  
   - Configure environment variables if needed.  
3. Create the **Step Function** in AWS using the definition in `scripts/step-function/definition.json`.  

### 3. Execution
Run the Step Function with an input JSON like:  

```json
{
  "s3_bucket": "my-bucket",
  "s3_key": "images/example.png"
}
```

---

## 📊 Monitoring

- **AWS CloudWatch Logs** → Check logs from each Lambda function.  
- **Step Functions Console** → Visualize executions and transitions.  
- **SageMaker Metrics** → Monitor the deployed model endpoint.  

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).  
