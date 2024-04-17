document.addEventListener("DOMContentLoaded", function() {
    // Seleciona o botão e o conteúdo associado
    const botao = document.querySelector(".mostrar-conteudo");
    const conteudo = document.querySelector(".conteudo");
  
    // Define a função para alternar o texto do botão
    function alternarTextoBotao() {
      if (conteudo.style.display === "none") {
        botao.textContent = "Mostrar Conteúdo";
      } else {
        botao.textContent = "Ocultar Conteúdo";
      }
    }
  
    // Define a ação quando o botão for clicado
    botao.addEventListener("click", function() {
      // Alterna o display do conteúdo entre visível e oculto
      if (conteudo.style.display === "none") {
        conteudo.style.display = "block";
      } else {
        conteudo.style.display = "none";
      }
      // Chama a função para alterar o texto do botão
      alternarTextoBotao();
    });
  
    // Chama a função inicialmente para definir o texto do botão corretamente
    alternarTextoBotao();
  });
  