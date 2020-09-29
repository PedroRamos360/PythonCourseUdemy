import sqlite3

# usar r antes da string para invalidar formatações de texto com \
path = r'D:\GitHub\PythonCourseUdemy\kivy\aulas\Seção 28 - Python e SQL\04 - Criação BD'
connection = sqlite3.connect(path+r'\teste.db')

