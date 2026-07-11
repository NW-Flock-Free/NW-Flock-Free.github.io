// Mobile nav toggle. Progressive enhancement: with JS off, the noscript
// rule in each page head forces .nav-menu to display on small screens,
// so the links stay reachable even though this toggle button does nothing.
(function () {
  var toggle = document.querySelector(".nav-toggle");
  var menu = document.getElementById("nav-menu");
  if (!toggle || !menu) return;

  function close(returnFocus) {
    menu.classList.remove("open");
    toggle.setAttribute("aria-expanded", "false");
    if (returnFocus) toggle.focus();
  }

  toggle.addEventListener("click", function () {
    var open = menu.classList.toggle("open");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
  });

  // Escape closes the menu and returns focus to the toggle; choosing a link closes it too.
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && menu.classList.contains("open")) close(true);
  });
  menu.addEventListener("click", function (e) {
    if (e.target.closest("a")) close(false);
  });
})();
