#!/usr/bin/python
# coding=utf8

header = """<!DOCTYPE html>
<html lang="ko">
<head>
  <title>나무위키 덤프</title>

  <meta charset="utf-8"/>
  <meta name="viewport" content="user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, width=device-width"/>

  <meta http-equiv="cache-control" content="max-age=0" />
  <meta http-equiv="cache-control" content="no-cache" />
  <meta http-equiv="expires" content="0" />
  <meta http-equiv="expires" content="Tue, 01 Jan 1980 1:00:00 GMT" />
  <meta http-equiv="pragma" content="no-cache" />

  <style>
  body { -webkit-touch-callout: none !important; }
  body { font-family:sans-serif; }
  a { color:royalblue; }
  h1 { font-size:1.3em; }
  h3 { font-size:1em; }
  .github {}
  .container div.desc { font-size:0.8em; }
  .container span.filename {}
  .container span.filesize {}
  .container table { margin:0.5em; max-width:100%; }
  .container td.md5 { font-family:Courier,"Lucida Console",monospace; text-align:left; }
  .container td { padding:2px 4px; }
  .container td:last-child { font-size:0.8em; vertical-align:bottom; text-align:right; }
  .container a { text-decoration:none; }
  .container div.origin { margin-bottom:3em; padding-left:0.5em; font-size:0.8em; }
  .appstore {}
  footer { margin:0; padding:6px; border:1px solid black; }
  </style>
</head>
<body>

  <h1 class="title">나무위키 덤프</h1>

  <div class="github">
    <a href="https://github.com/modum-app/build-namuwiki-sql"><img style="position:absolute; top:-12px; right:-12px; border:0;" src="https://camo.githubusercontent.com/e7bbb0521b397edbd5fe43e7f760759336b5e05f/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6769746875622f726962626f6e732f666f726b6d655f72696768745f677265656e5f3030373230302e706e67" alt="Fork me on GitHub" data-canonical-src="https://s3.amazonaws.com/github/ribbons/forkme_right_green_007200.png"></a>
  </div>

  <div class="container">
"""

def origin(filename):
  link = 'https://namu.wiki/w/나무위키:데이터베이스%20덤프'
  return """  <h3>원본 파일명</h3>
  <div class="origin"><a href="%s">%s</a> (<a href="%s">나무위키:데이터베이스 덤프</a>)
  </div>
"""%(link,filename,link,)


footer = """  </div>

  <div class="appstore">
    <h3>오프라인 리더 앱 내려받기</h3>
    <a href="https://geo.itunes.apple.com/kr/app/namuwiki-offline-reader/id1078563836?mt=8" style="display:inline-block;overflow:hidden;background:url(http://linkmaker.itunes.apple.com/images/badges/ko-kr/badge_appstore-lrg.svg) no-repeat;width:135px;height:40px;"></a>
    <a href="https://geo.itunes.apple.com/us/app/namuwiki-offline-reader/id1078563836?mt=8" style="display:inline-block;overflow:hidden;background:url(http://linkmaker.itunes.apple.com/images/badges/en-us/badge_appstore-lrg.svg) no-repeat;width:135px;height:40px;"></a>
    <br/>
    <br/>
  </div>

  <footer>
    <a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/2.0/kr/"><img alt="크리에이티브 커먼즈 라이선스" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/2.0/kr/88x31.png" /></a><br />
    이 저작물은 <a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/2.0/kr/">크리에이티브 커먼즈 저작자표시-비영리-동일조건변경허락 2.0 대한민국 라이선스</a>에 따라 이용할 수 있습니다.
  </footer>

</body>
</html>
"""

class TableView:
  def __init__(self,filename,filesize,md5_hash):
    self.mirrors = []
    self.filename = filename
    self.filesize = filesize
    self.md5_hash = md5_hash

  def add(self,name,link):
    self.mirrors.append((name,link,))

  def render(self):
    print '<h3><span class="filename">%s</span> (<span class="filesize">%s</span>)</h3>'%(self.filename,self.filesize)
    print '<table>'
    print '  <tr>'
    print '    <td colspan="3" class="md5">' + self.md5_hash
    for i,(name,link,) in enumerate(self.mirrors):
      print '  <tr>'
      print '    <td>Mirror %d'%(i+1)
      print '    <td><a href="%s">%s</a>'%(link,name)
      print '    <td><a href="%s">📲</a>'%(link,)
    print '</table>'
    print

class Storage:
  D = 'Dropbox (direct link)'
  G = 'Google Drive'
  M = 'Microsoft OneDrive'

def main():
  print header

  normal = TableView('namuwiki-160202.sql','838M','39841b31f52c921302963e80085a5ece')
  normal.add(Storage.D, 'https://dl.dropboxusercontent.com/u/22206273/namuwiki-160202.sql')
  normal.add(Storage.G, 'https://drive.google.com/open?id=0B6dpAIVkR_3-MEFJLTd6bGRXNHM')
  normal.add(Storage.M, 'http://1drv.ms/1SCcwkX')
  normal.render()

  sample = TableView('namuwiki-160202-sample.sql','9.1M','1d3c6ccb35a23a4394a1d1c13a7ecc21')
  sample.add(Storage.D, 'https://dl.dropboxusercontent.com/u/22206273/namuwiki-160202-sample.sql')
  sample.add(Storage.G, 'https://drive.google.com/open?id=0B6dpAIVkR_3-b2NXNVhhV2t2Z1E')
  sample.add(Storage.M, 'http://1drv.ms/1SCcnho')
  sample.render()

  print origin('namuwiki160126.sql')

  print footer

if __name__ == '__main__':
  main()
