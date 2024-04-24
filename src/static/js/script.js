document.addEventListener("DOMContentLoaded", function() {
  const botao = document.querySelector(".mostrar-conteudo");
  const conteudo = document.querySelector(".conteudo");


  function alternarTextoBotao() {
    if (conteudo.style.display === "none") {
      botao.textContent = "Mostrar Conteúdo";
    } else {
      botao.textContent = "Ocultar Conteúdo";
    }
  }

  botao.addEventListener("click", function() {
    if (conteudo.style.display === "none") {
      conteudo.style.display = "block";
      
      
    } else {
      conteudo.style.display = "none";
    }
    alternarTextoBotao();
  });
  alternarTextoBotao();
});
