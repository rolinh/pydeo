from shutil import copy
import sys

from invoke import (
    task,
    run
)

# define projects directories
app_dir = 'app'
config_dir = 'config'
db_dir = 'db'
lib_dir = 'lib'
ctrl_lib_dir = lib_dir + '/controllers'
mdls_lib_dir = lib_dir + '/models'
test_dir = 'test'
func_test_dir = test_dir + '/functional'
unit_test_dir = test_dir + '/unit'
    
@task
def set_settings(environment='production'):
    if environment not in ['production', 'development', 'test']:
        print('Error: ' + environment + ' is not a valid parameter',
              file=sys.stderr)
        exit(1)

    src = config_dir + '/settings-' + environment + '.py.sample'
    dst = config_dir + '/settings.py'
    print('Copying ' + src + ' to '  + dst)
    copy(src, dst)
    print('Done')

@task('set_settings')
def test_func(environment='test'):
    run_cmd('nosetests -w ' + func_test_dir)

@task('set_settings')
def test_unit(environment='test'):
    run_cmd('nosetests -w ' + unit_test_dir)

@task('test_func', 'test_unit')
def test():
    pass

@task
def pep8():
    cmd = 'pep8 ' + app_dir + ' ' + ctrl_lib_dir + ' ' + mdls_lib_dir + ' '\
            + config_dir + ' ' + db_dir + ' ' + test_dir
    run_cmd(cmd)

@task
def clean():
    run_cmd("find . -name '__pycache__' -exec rm -rf {} +")
    run_cmd("find . -name '*.pyc' -exec rm -f {} +")
    run_cmd("find . -name '*.pyo' -exec rm -f {} +")
    run_cmd("find . -name '*~' -exec rm -f {} +")
    run_cmd("find . -name '._*' -exec rm -f {} +")

@task('clean')
def clean_env():
    run_cmd('rm -r ./env && mkdir env && touch env/.keep')

@task
def init_submodules():
    run_cmd('git submodule init && git submodule update')

@task
def update_submodules():
    run_cmd('git submodule foreach git pull')

def run_cmd(cmd):
    print('Running \'' + cmd + '\'...')
    run(cmd)
    print('Done')

