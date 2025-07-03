from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit
import random
import time

app = Flask(__name__)
socketio = SocketIO(app)

# Store quizzes
quizzes = {}

# Store active quiz sessions
active_quizzes = {}

# Store students' answers
students = {}

@app.route('/')
def index():
    return render_template('teacher_dashboard.html', quizzes=quizzes)

@app.route('/create_quiz', methods=['GET', 'POST'])
def create_quiz():
    if request.method == 'POST':
        quiz_title = request.form['title']
        questions = []
        for i in range(int(request.form['num_questions'])):
            question_type = request.form[f'question_type_{i}']
            question_text = request.form[f'question_{i}']
            
            if question_type == 'multiple_choice':
                options = [
                    request.form[f'option_{i}_0'],
                    request.form[f'option_{i}_1'],
                    request.form[f'option_{i}_2'],
                    request.form[f'option_{i}_3'],
                ]
                correct_answer = request.form[f'correct_{i}']
                questions.append({
                    'type': 'multiple_choice',
                    'question': question_text,
                    'options': options,
                    'correct': correct_answer
                })

            elif question_type == 'word_cloud':
                questions.append({
                    'type': 'word_cloud',
                    'question': question_text,
                })

            elif question_type == 'open_ended':
                questions.append({
                    'type': 'open_ended',
                    'question': question_text,
                })

            elif question_type == 'rating':
                questions.append({
                    'type': 'rating',
                    'question': question_text,
                })

            elif question_type == 'ranking':
                options = [
                    request.form[f'option_{i}_0'],
                    request.form[f'option_{i}_1'],
                    request.form[f'option_{i}_2'],
                    request.form[f'option_{i}_3'],
                ]
                questions.append({
                    'type': 'ranking',
                    'question': question_text,
                    'options': options,
                })

            elif question_type == 'q_and_a':
                questions.append({
                    'type': 'q_and_a',
                    'question': question_text,
                })

        quiz_id = f'quiz{len(quizzes) + 1}'
        quizzes[quiz_id] = {'title': quiz_title, 'questions': questions}

        return redirect(url_for('index'))

    return render_template('create_quiz.html')

@app.route('/start_quiz/<quiz_id>', methods=['POST'])
def start_quiz(quiz_id):
    if quiz_id in quizzes:
        active_quizzes[quiz_id] = {
            'start_time': time.time(),
            'questions_answered': 0,
            'responses': {},
            'students': []
        }
        return render_template('quiz_game.html', quiz=quizzes[quiz_id], quiz_id=quiz_id)
    return "Quiz not found", 404

@app.route('/stop_quiz/<quiz_id>', methods=['POST'])
def stop_quiz(quiz_id):
    if quiz_id in active_quizzes:
        del active_quizzes[quiz_id]
        return redirect(url_for('index'))
    return "Quiz not found", 404

@socketio.on('submit_answer')
def handle_submit_answer(data):
    quiz_id = data['quiz_id']
    username = data['username']
    answer = data['answer']
    
    if quiz_id in active_quizzes:
        if username not in active_quizzes[quiz_id]['responses']:
            active_quizzes[quiz_id]['responses'][username] = []

        active_quizzes[quiz_id]['responses'][username].append(answer)
        
        # For certain question types, we could immediately show results
        emit('show_feedback', {'message': 'Answer submitted!'}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
