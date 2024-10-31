get_indexhtml_file:
  file.managed:
    - name: /home/user/index.html
    - source: salt://files/index.html
    - user: user
    - group: user
    - mode: 0640
    - template: jinja

start_httpserver:
  cmd.run:
    - name: 'python3 -m http.server 8089'
    - cwd: /home/user
    - runas: user
    - bg: True
