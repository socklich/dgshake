"""发布前运行：给 index.html 打上新的版本号，并写入 version.json。
用法：python tools/stamp.py
页面打开时会用不走缓存的请求读取 version.json，版本不一致就自动跳到最新版。"""
import io, json, re, datetime, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
build = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
p = root / 'index.html'
s = io.open(p, encoding='utf-8').read()
s, n = re.subn(r"const BUILD = '[^']*';", f"const BUILD = '{build}';", s)
assert n == 1, 'BUILD marker not found'
io.open(p, 'w', encoding='utf-8', newline='\n').write(s)
io.open(root / 'version.json', 'w', encoding='utf-8', newline='\n').write(json.dumps({'build': build}) + '\n')
print(build)
