# usage: gen.py slug "Title" "Group" "description" body.html
import sys,re,os
slug,title,group,desc,bodyf=sys.argv[1:6]
import pathlib
here=pathlib.Path(__file__).resolve().parent
site=str(here/'site')+'/'
s=open(site+'index.html').read()
head=s[:s.index('  <main class="main">')]
head=head.replace('<title>Overview — Token Controller Docs</title>',f'<title>{title} — Token Controller Docs</title>')
head=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="{desc}">',head)
head=head.replace('<link rel="canonical" href="https://docs.tokencontroller.com">',f'<link rel="canonical" href="https://docs.tokencontroller.com/{slug}">')
def cur(x):
    x=x.replace('<a class="cur" href="/">','<a href="/">')
    return x.replace(f'<a href="/{slug}">',f'<a class="cur" href="/{slug}">')
head=cur(head)
mside=cur(s[s.index('    <details class="mside">'):s.index('</details>')+len('</details>')])
body=open(here/bodyf).read()
lead_end=body.index('</p>')+4
heads=re.findall(r'<h2 id="([^"]+)">([^<]+)</h2>',body)
toc='\n'.join(f'      <li><a href="#{i}">{t}</a></li>' for i,t in heads)
main=f'''  <main class="main">
    <div class="crumb"><a href="/">Docs</a> / {group} / {title}</div>
    <h1>{title}</h1>
{body[:lead_end]}

{mside}
{body[lead_end:]}

    <div class="foot">
      <span>Last updated 8 October 2026 · <a href="https://github.com/tokencontroller/tokencontroller/blob/main/apps/docs/{bodyf}">Edit this page</a></span>
      <span>© 2026 Jan Beck · <a href="https://tokencontroller.com/privacy">Privacy</a> · <a href="https://tokencontroller.com/imprint">Imprint</a></span>
    </div>
  </main>

  <nav class="toc" aria-label="On this page">
    <h4>On this page</h4>
    <ul>
{toc}
    </ul>
  </nav>
</div>

</body>
</html>
'''
os.makedirs(site+slug,exist_ok=True)
open(site+slug+'/index.html','w').write(head+main)
print('ok',slug,len(heads))
