# 🔮 ChurnIQ — Telecom Customer Churn Prediction System

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.1-green?style=flat-square&logo=flask)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.6-orange?style=flat-square&logo=scikit-learn)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## 📌 Project Overview
An end-to-end Machine Learning system that predicts whether a telecom 
customer will churn (leave the service) using supervised and unsupervised 
learning techniques. The system includes a professional interactive 
dashboard connected to a real trained ML model via Flask API.

> **University:** Iqra University, Chak Shahzad Campus, Islamabad
> **Course:** AIC-221L — Introduction to Machine Learning Lab
> **Instructor:** Abdul Baqi Malik
> **Semester:** BSAI — 5th Semester
> **Deadline:** 17 June 2026

---

## 🎯 Problem Statement
A telecom company is facing a major challenge — many customers are 
leaving their services frequently. The goals are:
- ✅ Predict which customers will churn **before** they leave
- ✅ Segment customers into groups for targeted marketing
- ✅ Provide business insights and actionable recommendations

---

## 📊 Dataset
| Property | Value |
|----------|-------|
| Source | [Kaggle — Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) |
| Total Customers | 7,043 |
| Total Features | 21 |
| Target Variable | Churn (Yes/No) |
| Churn Rate | 26.5% |
| Missing Values | 11 hidden blank values (fixed) |

---

## 🤖 Machine Learning Models

### Supervised Learning Results
| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| ⭐ Logistic Regression | **81.2%** | 67.3% | 56.8% | 61.6% |
| Random Forest | 80.1% | 65.8% | 50.2% | 56.9% |
| K-Nearest Neighbors | 77.4% | 60.1% | 49.3% | 54.2% |
| Naive Bayes | 75.6% | 55.2% | 67.4% | 60.7% |
| Decision Tree | 73.2% | 51.4% | 51.8% | 51.6% |

> ⭐ **Best Model: Logistic Regression** with 81.2% accuracy

### Unsupervised Learning Results
| Algorithm | Clusters | Purpose |
|-----------|----------|---------|
| KMeans (K=3) | 3 segments | Customer segmentation |
| Hierarchical Clustering | 3 groups | Confirmed KMeans results |
| DBSCAN | Auto-detect | Outlier detection |

---

## 👥 Customer Segments
| Segment | Type | Avg Tenure | Churn Risk |
|---------|------|------------|------------|
| Cluster 0 | 🟢 Loyal Customers | 45+ months | 4% |
| Cluster 1 | 🔴 At-Risk Customers | 12–18 months | 58% |
| Cluster 2 | 🟡 New Customers | 1–6 months | 28% |

---

## 🏗️ Project Structure
