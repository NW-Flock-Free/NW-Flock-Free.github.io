// Shared site JS: (1) mark that JS is on, (2) mobile nav toggle,
// (3) one reveal-on-scroll helper used by every page. No framework.

// (1) Flag JS as available so CSS can safely hide reveal elements only when
// they can be revealed again. With JS off, .reveal has no hidden state.
document.documentElement.classList.add("js");

// (2) Mobile nav toggle. Progressive enhancement: with JS off, the noscript
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

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && menu.classList.contains("open")) close(true);
  });
  menu.addEventListener("click", function (e) {
    if (e.target.closest("a")) close(false);
  });
})();

// (3) Reveal-on-scroll. Any element with class .reveal fades and rises 12px
// when it scrolls into view, once. Reduced-motion and no-IntersectionObserver
// are both handled by revealing everything immediately (never leaves content
// hidden). Per-element stagger comes from an inline --i on the element.
(function () {
  var items = document.querySelectorAll(".reveal");
  if (!items.length) return;

  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce || !("IntersectionObserver" in window)) {
    for (var i = 0; i < items.length; i++) items[i].classList.add("visible");
    return;
  }

  var io = new IntersectionObserver(function (entries, obs) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        obs.unobserve(entry.target);
      }
    });
  }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });

  items.forEach(function (el) { io.observe(el); });
})();

// (4) Optional news TOC scroll-spy. Marks the active pill as sections pass the
// top. Only runs when a .toc exists and IntersectionObserver is supported;
// otherwise the pills are still plain working anchor links.
(function () {
  var toc = document.querySelector(".toc");
  if (!toc || !("IntersectionObserver" in window)) return;
  var links = Array.prototype.slice.call(toc.querySelectorAll("a[href^='#']"));
  if (!links.length) return;

  var byId = {};
  links.forEach(function (a) { byId[a.getAttribute("href").slice(1)] = a; });

  var spy = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        links.forEach(function (a) { a.removeAttribute("aria-current"); });
        var active = byId[entry.target.id];
        if (active) active.setAttribute("aria-current", "true");
      }
    });
  }, { rootMargin: "-30% 0px -60% 0px", threshold: 0 });

  Object.keys(byId).forEach(function (id) {
    var sec = document.getElementById(id);
    if (sec) spy.observe(sec);
  });
})();
