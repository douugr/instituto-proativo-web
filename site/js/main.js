// Melhorias opcionais: a página funciona sem este arquivo.
document.addEventListener("DOMContentLoaded", function () {
  // Ano corrente no rodapé
  document.querySelectorAll("[data-ano-atual]").forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });

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
