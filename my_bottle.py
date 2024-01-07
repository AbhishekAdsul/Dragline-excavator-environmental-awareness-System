from bottle import Bottle, request
import subprocess

app = Bottle()

@app.route('/deploy', method='POST')
def deploy():
    # Execute the deployment command
    subprocess.run(['python', 'C:\\Users\\Abhishek\\Desktop\\koyal yantrik\\main.py'])
    return 'Deployment initiated!'

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
