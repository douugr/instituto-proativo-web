// Melhorias opcionais: a página funciona sem este arquivo.
document.addEventListener("DOMContentLoaded", function () {
  // Ano corrente no rodapé
  document.querySelectorAll("[data-ano-atual]").forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });

  // Fecha o seletor de idioma ao clicar fora dele ou apertar Esc
  var idioma = document.querySelector(".lang-switch");
  if (idioma) {
    document.addEventListener("click", function (e) {
      if (idioma.open && !idioma.contains(e.target)) idioma.open = false;
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && idioma.open) {
        idioma.open = false;
        idioma.querySelector("summary").focus();
      }
    });
  }

  // Fecha o menu móvel ao escolher uma seção
  var menu = document.getElementById("menu-principal");
  if (!menu || !window.bootstrap) return;
  menu.querySelectorAll("a[href^='#']").forEach(function (link) {
    link.addEventListener("click", function () {
      if (menu.classList.contains("show")) {
        window.bootstrap.Collapse.getOrCreateInstance(menu).hide();
      }
    });
  });
});
