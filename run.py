from views.view import app

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['LOCAL_PORT'], debug=app.config['DEBUG'])
