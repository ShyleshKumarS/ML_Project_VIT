# ML Project: Credit Classification

## Overview
This project aims to predict credit classification using machine learning models. Two different models were developed and evaluated: one without Principal Component Analysis (PCA) and another with PCA included.
### Card.ipynb has used in Website implementation 

### Files
- `Card.ipynb`: Jupyter Notebook containing the implementation of the credit classification model without PCA.
- `Best_Card.ipynb`: Jupyter Notebook containing the implementation of the credit classification model with PCA.
- `credit_rating.xls`: Dataset used for training and testing the models.

## Model Comparison
Here's a comparison of the performance metrics for both models:

### Model without PCA (`Card.ipynb`)
- **Accuracy**: 90%
- **Precision (class 0)**: 87%
- **Precision (class 1)**: 95%
- **Recall (class 0)**: 96%
- **Recall (class 1)**: 85%
- **F1-score (class 0)**: 91%
- **F1-score (class 1)**: 90%

### Model with PCA (`Best_Card.ipynb`)
- **Accuracy**: 94%
- **Precision (class 0)**: 90%
- **Precision (class 1)**: 99%
- **Recall (class 0)**: 99%
- **Recall (class 1)**: 89%
- **F1-score (class 0)**: 95%
- **F1-score (class 1)**: 94%

## Conclusion
The model with PCA shows improved performance compared to the model without PCA, with higher accuracy and better precision, recall, and F1-scores for both classes. Therefore, incorporating PCA into the model enhances its predictive capability for credit classification.
