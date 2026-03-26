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
    var rem = px / 10; // mdBook html font-size: 62.5% → 1rem = 10px
    document.documentElement.style.setProperty('--base-font-size', rem + 'rem');
    var label = document.getElementById('font-size-label');
    if (label) label.textContent = px + 'px';
    localStorage.setItem(STORAGE_KEY, px);
  }

  function createUI() {
    // Insert into the right side of the menu bar
    var menuBar = document.querySelector('.right-buttons');
    if (!menuBar) return;

    var container = document.createElement('div');
    container.id = 'font-size-adjuster';

    var btnMinus = document.createElement('button');
    btnMinus.textContent = 'A-';
    btnMinus.title = '缩小字体';
    btnMinus.setAttribute('aria-label', '缩小字体');

    var label = document.createElement('span');
    label.id = 'font-size-label';

    var btnPlus = document.createElement('button');
    btnPlus.textContent = 'A+';
    btnPlus.title = '放大字体';
    btnPlus.setAttribute('aria-label', '放大字体');

    container.appendChild(btnMinus);
    container.appendChild(label);
    container.appendChild(btnPlus);
    menuBar.prepend(container);

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

  // Create UI when DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', createUI);
  } else {
    createUI();
  }
})();
