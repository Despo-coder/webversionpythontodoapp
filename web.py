import  streamlit as sl
from functions import get_todos, write_todos
import os


if not os.path.exists('todos.txt'):
    with open('todos.txt','w') as file:
        pass


todos = get_todos()
def addTodo():
    todo=sl.session_state['new_todo']
    todos.append(todo +'\n')
    write_todos(todos)
    sl.session_state['new_todo']=''


sl.title('My Todo App')
sl.subheader('Welcome to the app')
sl.write('This app is to create list of things to do. To complete/remove just check the box.')

for index, todo in enumerate(todos) :
    checkbox = sl.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del sl.session_state[index]
        sl.experimental_rerun()



sl.text_input(label='Todo Items.',placeholder='Enter a Todo...' , on_change = addTodo, key='new_todo')
