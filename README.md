Smart Exam-Prep Knowledge Gap Analyzer
======================================

A simple and intuitive web application that helps students identify their knowledge gaps and improve exam performance through intelligent analysis of practice questions.

📋 Table of Contents
--------------------

*   Features
    
*   Demo
    
*   Installation
    
*   Usage
    
*   Project Structure
    
*   How It Works
  
*   API Documentation
    
*   Technologies Used

*   Customization

*   Testing

*   Roadmap
    

✨ Features
----------

*   📊 **Performance Analysis** - Automatically identifies weak and strong topics based on practice performance
    
*   🎯 **Smart Recommendations** - Get personalized study recommendations with priority levels
    
*   📝 **Practice Questions** - Topic-wise practice questions with instant feedback
    
*   📈 **Progress Tracking** - Track overall performance and improvement over time
    
*   👥 **Multi-Student Support** - Manage multiple students in one application
    
*   🎨 **Clean UI** - Simple, intuitive interface that's easy to use
    
*   💾 **Local Database** - All data stored locally using SQLite
    
*   🚀 **Quick Setup** - Get started in minutes with sample data
    

🎥 Demo
-------

### How Knowledge Gap Analysis Works:

1.  **Practice Questions** - Students answer questions from different topics
    
2.  **Automatic Analysis** - System calculates accuracy per topic
    
3.  **Gap Identification** - Topics with <60% accuracy marked as "weak"
    
4.  **Recommendations** - Prioritized study plan generated automatically
    

### Performance Metrics:

*   ✅ **Strong Topics**: 80%+ accuracy
    
*   ⚠️ **Needs Improvement**: 60-79% accuracy
    
*   ❌ **Weak Topics**: <60% accuracy
    

🚀 Installation
---------------

### Prerequisites

*   Python 3.7 or higher
    
*   pip (Python package installer)
    

### Step 1: Clone the Repository

`   git clone https://github.com/yourusername/exam-prep-analyzer.git  cd exam-prep-analyzer   `

### Step 2: Install Dependencies

`   pip install flask   `

### Step 3: Initialize Database

The database will be created automatically when you first run the application.

### Step 4: Run the Application

`   python app.py   `

### Step 5: Open in Browser

Navigate to http://localhost:5000 in your web browser.

📖 Usage
--------

### Quick Start Guide

1.  **Load Sample Data**
    
    *   Click "Load Sample Data" button on the welcome screen
        
    *   This creates sample topics and questions
        
2.  **Create a Student**
    
    *   Click "New Student" button
        
    *   Enter name and email
        
    *   Click "Create"
        
3.  **Practice Questions**
    
    *   Select a student from dropdown
        
    *   Choose a topic from the practice section
        
    *   Click "Start Practice"
        
    *   Answer questions and submit
        
4.  **Analyze Performance**
    
    *   Click "Analyze My Performance" button
        
    *   View weak topics, strong topics, and recommendations
        
    *   See overall score and statistics
        

### Sample Data Included

*   **Mathematics - Algebra**: 3 questions (Easy-Medium)
    
*   **English - Grammar**: 2 questions (Easy)
    
*   **Science - Physics Laws**: 1 question (Medium)
    

📁 Project Structure
--------------------

exam-prep-analyzer/  
│  
├── app.py                  # Main Flask application  
├── database.py             # Database initialization and helpers  
├── exam_prep.db           # SQLite database (created automatically)  
│  
├── templates/  
│   └── index.html         # Main HTML template  
│  
├── static/  
│   ├── style.css          # Stylesheet  
│   └── script.js          # Frontend JavaScript  
│  
├── README.md              # This file  
└── requirements.txt       # Python dependencies (optional)  

🔧 How It Works
---------------

### Database Schema

    SQLstudents (id, name, email)  
    topics (id, name, subject)  
    questions (id, topic_id, question, answer, difficulty)  
    attempts (id, student_id, question_id, is_correct, date)   

### Analysis Algorithm

    # Topic is marked as WEAK if:  
    accuracy < 60%  
    # Topic is marked as STRONG if:  
    accuracy >= 80%  
    # Overall Score:  
    overall_score = (total_correct / total_attempts) * 100   

### Recommendation Priority

*   **High Priority**: Topics with <40% accuracy
    
*   **Medium Priority**: Topics with 40-59% accuracy
    
*   **Maintenance**: Strong topics requiring periodic revision
    

🔌 API Documentation
--------------------

### Students

#### Get All Students

    GET /api/students   

#### Create Student

    POST /api/students  
    Content-Type: application/json  
    {    
      "name": "John Doe",    
      "email": "john@example.com"  
    }   

### Topics

#### Get All Topics

    GET /api/topics  

### Questions

#### Get Questions by Topic

    GET /api/questions/{topic_id}  

### Attempts

#### Submit Answer

    POST /api/attempt  
    Content-Type: application/json  
    {
      "student_id": 1,    
      "question_id": 1,    
      "answer": "4"  
    }   

**Response:**

    { 
       "correct": true,    
       "answer": "4"  
     }   

### Analysis

#### Get Student Analysis

    GET /api/analysis/{student_id}   `

**Response:**

    {
      "overall_score": 75.5,    
      "weak_topics": [...],    
      "strong_topics": [...],    
      "recommendations": [...],    
      "total_attempts": 10  
    }   `

### Utilities

#### Seed Sample Data

    POST /api/seed   

🛠️ Technologies Used
---------------------

### Backend

*   **Flask** - Python web framework
    
*   **SQLite** - Lightweight database
    
*   **Python 3** - Programming language
    

### Frontend

*   **HTML5** - Structure
    
*   **CSS3** - Styling
    
*   **Vanilla JavaScript** - Interactivity
    
*   **Fetch API** - HTTP requests
    

🎨 Customization
----------------

### Adding New Questions

Edit database.py and add to the add\_sample\_data() function:

    questions = [  
        (1, 'Your question here?', 'answer', 'Easy'),
        # Add more questions...
    ]   

### Changing Thresholds

Edit app.py to modify analysis thresholds:

    # In the /api/analysis route  
    if accuracy < 60:  # Change this value      
        weak_topics.append(topic_data)  
    elif accuracy >= 80:  # Change this value    
        strong_topics.append(topic_data)   

### Styling

Modify static/style.css to change colors, fonts, or layout:

    .btn-primary {    
        background: #4299e1;  /* Change button color */ 
    }   

🧪 Testing
----------

### Manual Testing Checklist

*    Create new student
    
*    Load sample data
    
*    Answer questions correctly
    
*    Answer questions incorrectly
    
*    Run analysis with no attempts
    
*    Run analysis with mixed results
    
*    Check weak topics display
    
*    Check strong topics display
    
*    Verify recommendations
    

### Test Data

Use the included sample data to test:

*   3 different topics
    
*   Various difficulty levels
    
*   Different subjects
    

🚧 Roadmap
----------

### Planned Features

*    Export reports to PDF
    
*    Graphical performance charts
    
*    Time-based analytics
    
*    Question difficulty adjustment
    
*    Study schedule generator
    
*    Mobile responsive design improvements
    
*    Dark mode
    
*    Multiple choice question support
    
*    Image-based questions
    
*    User authentication
    
