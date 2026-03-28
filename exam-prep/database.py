import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('exam_prep.db')
    c = conn.cursor()
    
    # Students table
    c.execute('''CREATE TABLE IF NOT EXISTS students
                 (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
    
    # Topics table
    c.execute('''CREATE TABLE IF NOT EXISTS topics
                 (id INTEGER PRIMARY KEY, name TEXT, subject TEXT)''')
    
    # Questions table
    c.execute('''CREATE TABLE IF NOT EXISTS questions
                 (id INTEGER PRIMARY KEY, topic_id INTEGER, 
                  question TEXT, answer TEXT, difficulty TEXT)''')
    
    # Attempts table
    c.execute('''CREATE TABLE IF NOT EXISTS attempts
                 (id INTEGER PRIMARY KEY, student_id INTEGER, 
                  question_id INTEGER, is_correct INTEGER, 
                  date TEXT)''')
    
    conn.commit()
    conn.close()

def add_sample_data():
    conn = sqlite3.connect('exam_prep.db')
    c = conn.cursor()
    
    # Add topics
    topics = [
        ('Algebra', 'Mathematics'),
        ('Grammar', 'English'),
        ('Physics Laws', 'Science')
    ]
    c.executemany('INSERT INTO topics (name, subject) VALUES (?, ?)', topics)
    
    # Add questions
    questions = [
        (1, 'What is 2 + 2?', '4', 'Easy'),
        (1, 'Solve: x + 5 = 10', '5', 'Easy'),
        (1, 'What is 15 × 3?', '45', 'Medium'),
        (2, 'What is a noun?', 'person, place, or thing', 'Easy'),
        (2, 'What is a verb?', 'action word', 'Easy'),
        (3, 'What is Newton\'s first law?', 'inertia', 'Medium')
    ]
    c.executemany('INSERT INTO questions (topic_id, question, answer, difficulty) VALUES (?, ?, ?, ?)', questions)
    
    conn.commit()
    conn.close()

def get_db():
    conn = sqlite3.connect('exam_prep.db')
    conn.row_factory = sqlite3.Row
    return conn
