from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app=Flask(_name_)
@app.route('/htop')
def htop():
name="Rajneesh Ravi Raj"
username=os.getnv("USER")or
os.getnv("USERNAME")
ist=pytz.timezone('Asia/Kolkata')
server_time=datetime.now(ist).strftime("%Y-%m-%d %H: %M:%S.%f")

top_output=subprocess.getoutput("top-bn1")

return f"""
Name:{name}<br>
User:{username}<br>
Server Time(IST):{server_time}<br><br>
TOP output:<br><pre>{top_output}</pre>"""

if _name_=='main_';
app.run(host='0.0.0.0'port=5000)
