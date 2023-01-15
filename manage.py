import uvicorn
from config import *
import sys
from config import *

import os

# os.chdir(os.getenv('PYTHONPATH'))

def __main__():
    if sys.argv[1] == 'runserver':
        if len(sys.argv[1:]) == 1:
            uvicorn.run(app="app.main:app",port=PORT,host=HOST)
        else:
            raise Exception('The command is invalid')

    elif sys.argv[1] == 'makemigrations':
        if len(sys.argv[1:]) == 2:
            os.system('alembic revision --autogenerate -m \"'+sys.argv[2]+'\"')
            # print('alembic revision -m \"'+sys.argv[2]+'\"')
        else:
            raise Exception('The command is invalid')

    elif sys.argv[1] == 'migrate':
        if len(sys.argv[1:]) == 1:
            # print('alembic upgrade head')
            os.system('alembic upgrade head')
        else:
            raise Exception('The command is invalid')

    elif sys.argv[1] == 'showmigrations':
        if len(sys.argv[1:]) == 1:
            print('alembic history')
            os.system('alembic history')
        else:
            raise Exception('The command is invalid')
    else:
        raise Exception(sys.argv[1]+' is not a x-fit command')

__main__()