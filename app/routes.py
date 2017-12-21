from app import app
@app.route('/')
@app.route('/index')
def index():
    user = {'usename': 'prutha'}
    return '''
<html>
  <head>
    <title> web app page</title>
  </head>
  <body>
   <h1> hello , ''' + user['usename'] + ''' </h1>
  </body>
</html>'''
