let currentStudent = null;
let currentQuestions = [];
let currentQuestion = 0;

// Load students on page load
window.onload = function() {
    loadStudents();
    loadTopics();
};

// Load students
async function loadStudents() {
    const response = await fetch('/api/students');
    const students = await response.json();
    
    const select = document.getElementById('studentSelect');
    select.innerHTML = '<option value="">Select Student</option>';
    
    students.forEach(student => {
        const option = document.createElement('option');
        option.value = student.id;
        option.textContent = student.name;
        select.appendChild(option);
    });
    
    select.onchange = function() {
        currentStudent = this.value;
        if (currentStudent) {
            showDashboard();
        }
    };
}

// Load topics
async function loadTopics() {
    const response = await fetch('/api/topics');
    const topics = await response.json();
    
    const select = document.getElementById('topicSelect');
    select.innerHTML = '<option value="">Choose a topic</option>';
    
    topics.forEach(topic => {
        const option = document.createElement('option');
        option.value = topic.id;
        option.textContent = `${topic.subject} - ${topic.name}`;
        select.appendChild(option);
    });
}

// Show/hide sections
function showDashboard() {
    document.getElementById('welcomeScreen').classList.add('hidden');
    document.getElementById('dashboard').classList.remove('hidden');
}

function showNewStudentForm() {
    document.getElementById('studentModal').classList.remove('hidden');
}

function closeModal() {
    document.getElementById('studentModal').classList.add('hidden');
}

// Create student
async function createStudent() {
    const name = document.getElementById('studentName').value;
    const email = document.getElementById('studentEmail').value;
    
    if (!name || !email) {
        alert('Please fill all fields');
        return;
    }
    
    await fetch('/api/students', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({name, email})
    });
    
    document.getElementById('studentName').value = '';
    document.getElementById('studentEmail').value = '';
    closeModal();
    loadStudents();
}

// Analyze performance
async function analyzePerformance() {
    if (!currentStudent) {
        alert('Please select a student first');
        return;
    }
    
    const response = await fetch(`/api/analysis/${currentStudent}`);
    const data = await response.json();
    
    // Update stats
    document.getElementById('overallScore').textContent = data.overall_score + '%';
    document.getElementById('weakCount').textContent = data.weak_topics.length;
    document.getElementById('strongCount').textContent = data.strong_topics.length;
    document.getElementById('totalAttempts').textContent = data.total_attempts;
    
    // Show weak topics
    const weakDiv = document.getElementById('weakTopics');
    if (data.weak_topics.length === 0) {
        weakDiv.innerHTML = '<p class="empty">No weak topics! Great job!</p>';
    } else {
        weakDiv.innerHTML = data.weak_topics.map(topic => `
            <div class="topic-item weak">
                <h3>${topic.name}</h3>
                <p>${topic.subject}</p>
                <div class="accuracy low">${topic.accuracy}% (${topic.attempts} attempts)</div>
            </div>
        `).join('');
    }
    
    // Show strong topics
    const strongDiv = document.getElementById('strongTopics');
    if (data.strong_topics.length === 0) {
        strongDiv.innerHTML = '<p class="empty">Keep practicing!</p>';
    } else {
        strongDiv.innerHTML = data.strong_topics.map(topic => `
            <div class="topic-item strong">
                <h3>${topic.name}</h3>
                <p>${topic.subject}</p>
                <div class="accuracy high">${topic.accuracy}% (${topic.attempts} attempts)</div>
            </div>
        `).join('');
    }
    
    // Show recommendations
    const recDiv = document.getElementById('recommendations');
    if (data.recommendations.length === 0) {
        recDiv.innerHTML = '<p class="empty">No recommendations yet</p>';
    } else {
        recDiv.innerHTML = data.recommendations.map(rec => `
            <div class="recommendation ${rec.priority.toLowerCase()}">
                <h4>${rec.topic}</h4>
                <p>${rec.message}</p>
                <span class="priority ${rec.priority.toLowerCase()}">${rec.priority} Priority</span>
            </div>
        `).join('');
    }
}

// Start practice
async function startPractice() {
    const topicId = document.getElementById('topicSelect').value;
    
    if (!topicId) {
        alert('Please select a topic');
        return;
    }
    
    if (!currentStudent) {
        alert('Please select a student');
        return;
    }
    
    const response = await fetch(`/api/questions/${topicId}`);
    currentQuestions = await response.json();
    
    if (currentQuestions.length === 0) {
        alert('No questions available for this topic');
        return;
    }
    
    currentQuestion = 0;
    document.getElementById('questionArea').classList.remove('hidden');
    showQuestion();
}

// Show question
function showQuestion() {
    if (currentQuestion >= currentQuestions.length) {
        document.getElementById('questionArea').innerHTML = `
            <div class="question-box">
                <h3>Practice Complete! 🎉</h3>
                <p>Click "Analyze My Performance" to see your progress</p>
            </div>
        `;
        return;
    }
    
    const q = currentQuestions[currentQuestion];
    document.getElementById('questionText').textContent = 
        `Question ${currentQuestion + 1}: ${q.question}`;
    document.getElementById('answerInput').value = '';
    document.getElementById('feedback').classList.add('hidden');
    document.getElementById('nextBtn').classList.add('hidden');
}

// Submit answer
async function submitAnswer() {
    const answer = document.getElementById('answerInput').value.trim();
    
    if (!answer) {
        alert('Please enter an answer');
        return;
    }
    
    const q = currentQuestions[currentQuestion];
    
    const response = await fetch('/api/attempt', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            student_id: currentStudent,
            question_id: q.id,
            answer: answer
        })
    });
    
    const result = await response.json();
    
    const feedback = document.getElementById('feedback');
    feedback.classList.remove('hidden');
    
    if (result.correct) {
        feedback.className = 'feedback correct';
        feedback.textContent = '✓ Correct!';
    } else {
        feedback.className = 'feedback incorrect';
        feedback.textContent = `✗ Incorrect. The answer is: ${result.answer}`;
    }
    
    document.getElementById('nextBtn').classList.remove('hidden');
}

// Next question
function nextQuestion() {
    currentQuestion++;
    showQuestion();
}

// Load sample data
async function loadSampleData() {
    await fetch('/api/seed', {method: 'POST'});
    alert('Sample data loaded!');
    loadStudents();
    loadTopics();
}
