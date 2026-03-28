# Smart Exam-Prep Knowledge Gap Analyzer

A simple and intuitive web application that helps students identify their knowledge gaps and improve exam performance through intelligent analysis of practice questions.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![SQLite](https://img.shields.io/badge/SQLite-3-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [API Documentation](#api-documentation)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## ✨ Features

- 📊 **Performance Analysis** - Automatically identifies weak and strong topics based on practice performance
- 🎯 **Smart Recommendations** - Get personalized study recommendations with priority levels
- 📝 **Practice Questions** - Topic-wise practice questions with instant feedback
- 📈 **Progress Tracking** - Track overall performance and improvement over time
- 👥 **Multi-Student Support** - Manage multiple students in one application
- 🎨 **Clean UI** - Simple, intuitive interface that's easy to use
- 💾 **Local Database** - All data stored locally using SQLite
- 🚀 **Quick Setup** - Get started in minutes with sample data

## 🎥 Demo

### How Knowledge Gap Analysis Works:

1. **Practice Questions** - Students answer questions from different topics
2. **Automatic Analysis** - System calculates accuracy per topic
3. **Gap Identification** - Topics with <60% accuracy marked as "weak"
4. **Recommendations** - Prioritized study plan generated automatically

### Performance Metrics:

- ✅ **Strong Topics**: 80%+ accuracy
- ⚠️ **Needs Improvement**: 60-79% accuracy  
- ❌ **Weak Topics**: <60% accuracy

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step-by-Step Setup

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/exam-prep-analyzer.git
cd exam-prep-analyzer
