var remote_filename = 'namuwiki-190415.sql';
if ('setLatest' in window) {
  setLatest(remote_filename);
}

var local = document.querySelector('#latest');
if (local) {
  var local_filename = local.getAttribute('data-filename');
  if (local_filename == remote_filename) {
    local.innerHTML = '✅ 최신버전입니다';
  } else {
    var s='⚠️ 새 버전 내려받기: <code>' + remote_filename + '</code>';
    local.innerHTML = '<a href="modum://exec/download" class="exec">'+s+'</a>';
  }
}

