#I have removed app from 'import app' snytax.I've added below 'create_app' instead of it.
from app import create_app, db, cli
from app.models import User, Post, Notification, Message, Task

#ask Jorge about the section below since it wasn't here
app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return{'db': db, 'User': User, 'Post': Post, 'Message': Message, 
            'Notification': Notification, 'Task': Task}