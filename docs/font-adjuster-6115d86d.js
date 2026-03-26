// Font size adjuster for Chinese reading comfort
(function () {
  var STORAGE_KEY = 'book-font-size';
  var DEFAULT = 18;
  var MIN = 14;
  var MAX = 26;
  var STEP = 2;

  function getSize() {
    var saved = localStorage.getItem(STORAGE_KEY);
    return saved ? parseInt(saved, 10) : DEFAULT;
  }

  function applySize(px) {
    var rem = px / 10;
    document.documentElement.style.setProperty('--base-font-size', rem + 'rem');
    var label = document.getElementById('font-size-label');
    if (label) label.textContent = px + '';
    localStorage.setItem(STORAGE_KEY, String(px));
  }

  function createUI() {
    var rightButtons = document.querySelector('.right-buttons');
    if (!rightButtons || document.getElementById('font-size-adjuster')) return;

    var container = document.createElement('div');
    container.id = 'font-size-adjuster';

    var btnMinus = document.createElement('button');
    btnMinus.innerHTML = '<small>A</small>';
    btnMinus.title = '缩小字体';
    btnMinus.setAttribute('aria-label', '缩小字体');

    var label = document.createElement('span');
    label.id = 'font-size-label';
    label.textContent = String(getSize());

    var btnPlus = document.createElement('button');
    btnPlus.innerHTML = '<big>A</big>';
    btnPlus.title = '放大字体';
    btnPlus.setAttribute('aria-label', '放大字体');

    container.appendChild(btnMinus);
    container.appendChild(label);
    container.appendChild(btnPlus);

    // Insert before the first existing button
    rightButtons.insertBefore(container, rightButtons.firstChild);

    btnMinus.addEventListener('click', function () {
      var size = Math.max(MIN, getSize() - STEP);
      applySize(size);
    });

    btnPlus.addEventListener('click', function () {
      var size = Math.min(MAX, getSize() + STEP);
      applySize(size);
    });
  }

  // Apply saved size immediately
  applySize(getSize());

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', createUI);
  } else {
    createUI();
  }
})();
