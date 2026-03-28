from flask import Flask, render_template, request, jsonify
from database import init_db, add_sample_data, get_db
from datetime import datetime, timedelta

app = Flask(__name__)

# Initialize database
init_db()

@app.route('/')
def index():
    return render_template('index.html')

# ===== STUDENT ROUTES =====
@app.route('/api/students', methods=['GET', 'POST'])
def students():
    db = get_db()
    
    if request.method == 'POST':
        data = request.json
        db.execute('INSERT INTO students (name, email) VALUES (?, ?)',
                   [data['name'], data['email']])
        db.commit()
        return jsonify({'success': True})
    
    students = db.execute('SELECT * FROM students').fetchall()
    return jsonify([dict(s) for s in students])

# ===== TOPIC ROUTES =====
@app.route('/api/topics')
def get_topics():
    db = get_db()
    topics = db.execute('SELECT * FROM topics').fetchall()
    return jsonify([dict(t) for t in topics])

# ===== QUESTION ROUTES =====
@app.route('/api/questions/<int:topic_id>')
def get_questions(topic_id):
    db = get_db()
    questions = db.execute('SELECT * FROM questions WHERE topic_id = ?', 
                          [topic_id]).fetchall()
    return jsonify([dict(q) for q in questions])

# ===== ATTEMPT ROUTES =====
@app.route('/api/attempt', methods=['POST'])
def submit_attempt():
    data = request.json
    db = get_db()
    
    # Get correct answer
    question = db.execute('SELECT answer FROM questions WHERE id = ?',
                         [data['question_id']]).fetchone()
    
    is_correct = data['answer'].lower().strip() == question['answer'].lower().strip()
    
    db.execute('''INSERT INTO attempts (student_id, question_id, is_correct, date)
                  VALUES (?, ?, ?, ?)''',
               [data['student_id'], data['question_id'], int(is_correct), 
                datetime.now().isoformat()])
    db.commit()
    
    return jsonify({
        'correct': is_correct,
        'answer': question['answer']
    })

# ===== ANALYSIS ROUTES =====
@app.route('/api/analysis/<int:student_id>')
def analyze_student(student_id):
    db = get_db()
    
    # Get all attempts with topic info
    query = '''
        SELECT t.name as topic, t.subject, a.is_correct
        FROM attempts a
        JOIN questions q ON a.question_id = q.id
        JOIN topics t ON q.topic_id = t.id
        WHERE a.student_id = ?
    '''
    attempts = db.execute(query, [student_id]).fetchall()
    
    # Calculate topic performance
    topic_stats = {}
    for attempt in attempts:
        topic = attempt['topic']
        if topic not in topic_stats:
            topic_stats[topic] = {
                'name': topic,
                'subject': attempt['subject'],
                'total': 0,
                'correct': 0
            }
        topic_stats[topic]['total'] += 1
        topic_stats[topic]['correct'] += attempt['is_correct']
    
    # Calculate accuracy for each topic
    weak_topics = []
    strong_topics = []
    
    for topic, stats in topic_stats.items():
        accuracy = (stats['correct'] / stats['total'] * 100) if stats['total'] > 0 else 0
        topic_data = {
            'name': stats['name'],
            'subject': stats['subject'],
            'accuracy': round(accuracy, 1),
            'attempts': stats['total']
        }
        
        if accuracy < 60:
            weak_topics.append(topic_data)
        elif accuracy >= 80:
            strong_topics.append(topic_data)
    
    # Overall score
    total_attempts = len(attempts)
    total_correct = sum(1 for a in attempts if a['is_correct'])
    overall_score = (total_correct / total_attempts * 100) if total_attempts > 0 else 0
    
    # Generate recommendations
    recommendations = []
    for topic in weak_topics:
        recommendations.append({
            'topic': topic['name'],
            'message': f"Practice more {topic['name']} questions. Current: {topic['accuracy']}%",
            'priority': 'High' if topic['accuracy'] < 40 else 'Medium'
        })
    
    return jsonify({
        'overall_score': round(overall_score, 1),
        'weak_topics': weak_topics,
        'strong_topics': strong_topics,
        'recommendations': recommendations,
        'total_attempts': total_attempts
    })

# ===== UTILITY ROUTES =====
@app.route('/api/seed', methods=['POST'])
def seed_data():
    add_sample_data()
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
  
