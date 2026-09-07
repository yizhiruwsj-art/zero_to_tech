from http.server import BaseHTTPRequestHandler, HTTPServer
import json

profile = {
    "heroTitle": "关于我",
    "heroSubtitle": "项目，创意，灵感，心得，我的作品",
}

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/profile":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            body = json.dumps(profile, ensure_ascii=False)  # ensure_ascii=False：让中文原样输出
            self.wfile.write(body.encode("utf-8"))
        elif self.path == "/hello":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")   # ← 一会儿改成 text/plain 再试
            self.end_headers()
            self.wfile.write("<h1>你好，HTTP</h1>".encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

print("后端已启动：http://localhost:8000/api/profile")
HTTPServer(("", 8000), Handler).serve_forever()
