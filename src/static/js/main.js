import { apiGet, apiPost } from './api.js';

document.addEventListener("DOMContentLoaded", () => {
  const sections = {
    destaquePets: document.getElementById("destaque-pets"),
    produtosPromocao: document.getElementById("produtos-promocao"),
    outrosPets: document.getElementById("outros-pets"),
    servicos: document.getElementById("servicos"),
  };

  const modalLogin = document.getElementById("modalLogin");
  const modalDetalhes = document.getElementById("modalDetalhes");

  const btnLogin = document.getElementById("btnLogin");
  const closeLogin = document.getElementById("closeLogin");
  const cancelLogin = document.getElementById("cancelLogin");

  const loginForm = document.getElementById("loginForm");
  const emailInput = document.getElementById("email");
  const senhaInput = document.getElementById("senha");
  const loginError = document.getElementById("loginError");

  const modalTitulo = document.getElementById("modalTitulo");
  const modalImagem = document.getElementById("modalImagem");
  const btnLike = document.getElementById("btnLike");
  const likeCount = document.getElementById("likeCount");
  const btnComentario = document.getElementById("btnComentario");
  const comentarioCount = document.getElementById("comentarioCount");
  const novoComentario = document.getElementById("novoComentario");
  const btnSend = document.getElementById("btnSend");
  const comentarioErro = document.getElementById("comentarioErro");
  const listaComentarios = document.getElementById("listaComentarios");
  const closeDetalhes = document.getElementById("closeDetalhes");

  let usuarioLogado = JSON.parse(localStorage.getItem("usuario"));
  let postAtual = null;
  let curtido = false;

  // Funções para abrir e fechar modais
  function abrirModalLogin() {
    modalLogin.classList.remove("hidden");
    loginError.textContent = "";
    emailInput.classList.remove("input-error");
    senhaInput.classList.remove("input-error");
    loginForm.reset();
  }
  function fecharModalLogin() {
    modalLogin.classList.add("hidden");
  }

  function abrirModalDetalhes(post) {
    postAtual = post;
    modalTitulo.textContent = post.titulo;
    modalImagem.src = post.imagem || '/static/images/default.png';
    likeCount.textContent = post.curtidas?.length || 0;
    comentarioCount.textContent = post.comentarios?.length || 0;
    curtido = usuarioLogado && post.curtidas?.some(c => c.usuario_id === usuarioLogado.id);

    btnLike.classList.toggle("liked", curtido);

    listaComentarios.innerHTML = "";
    (post.comentarios || []).forEach(c => {
      const li = document.createElement("li");
      li.textContent = c.conteudo;
      listaComentarios.appendChild(li);
    });

    novoComentario.value = "";
    comentarioErro.textContent = "";

    modalDetalhes.classList.remove("hidden");
  }
  function fecharModalDetalhes() {
    modalDetalhes.classList.add("hidden");
    postAtual = null;
  }

  // Login botão e modal
  btnLogin.addEventListener("click", abrirModalLogin);
  closeLogin.addEventListener("click", fecharModalLogin);
  cancelLogin.addEventListener("click", fecharModalLogin);

  loginForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    loginError.textContent = "";
    emailInput.classList.remove("input-error");
    senhaInput.classList.remove("input-error");

    const email = emailInput.value.trim();
    const senha = senhaInput.value.trim();

    let valid = true;
    if (!email) {
      emailInput.classList.add("input-error");
      valid = false;
    }
    if (senha.length < 3) {
      senhaInput.classList.add("input-error");
      valid = false;
    }
    if (!valid) return;

    try {
      const usuario = await apiPost("/login", { email, senha });
      localStorage.setItem("usuario", JSON.stringify(usuario));
      usuarioLogado = usuario;
      fecharModalLogin();
      carregarTodasSecoes();
    } catch (err) {
      loginError.textContent = "Credenciais incorretas";
      emailInput.classList.add("input-error");
      senhaInput.classList.add("input-error");
    }
  });

  // Fechar modal detalhes
  closeDetalhes.addEventListener("click", fecharModalDetalhes);

  // Curtir post
  btnLike.addEventListener("click", async () => {
    if (!usuarioLogado) {
      abrirModalLogin();
      return;
    }
    try {
      // TODO: implementar API para curtir/descurtir
      curtido = !curtido;
      if (curtido) {
        btnLike.classList.add("liked");
        likeCount.textContent = parseInt(likeCount.textContent) + 1;
      } else {
        btnLike.classList.remove("liked");
        likeCount.textContent = parseInt(likeCount.textContent) - 1;
      }
    } catch (err) {
      alert("Erro ao curtir o post");
    }
  });

  // Abrir modal comentários
  btnComentario.addEventListener("click", () => {
    if (!usuarioLogado) {
      abrirModalLogin();
      return;
    }
    novoComentario.focus();
  });

  // Enviar comentário
  btnSend.addEventListener("click", async () => {
    const texto = novoComentario.value.trim();
    comentarioErro.textContent = "";

    if (texto.length < 3) {
      comentarioErro.textContent = "Não é possível enviar um comentário";
      return;
    }
    try {
      // TODO: implementar API para enviar comentário
      const li = document.createElement("li");
      li.textContent = texto;
      listaComentarios.appendChild(li);
      comentarioCount.textContent = parseInt(comentarioCount.textContent) + 1;
      novoComentario.value = "";
    } catch (err) {
      comentarioErro.textContent = "Erro ao enviar comentário";
    }
  });

  // Função para criar card de post
  function criarCard(post) {
    const card = document.createElement("article");
    card.classList.add("card");
    card.tabIndex = 0;

    const img = document.createElement("img");
    img.src = post.imagem || '/static/images/default.png';
    img.alt = post.titulo;

    const content = document.createElement("div");
    content.classList.add("card-content");

    const title = document.createElement("h3");
    title.classList.add("card-title");
    title.textContent = post.titulo;

    const desc = document.createElement("p");
    desc.classList.add("card-description");
    desc.textContent = post.descricao || "";

    const footer = document.createElement("footer");
    footer.classList.add("card-footer");

    const iconeCoracao = document.createElement("img");
    iconeCoracao.src = '/static/images/coracao.svg';
    iconeCoracao.alt = "Curtir";
    iconeCoracao.classList.add("icon-footer");

    const iconeChat = document.createElement("img");
    iconeChat.src = '/static/images/chat.svg';
    iconeChat.alt = "Comentários";
    iconeChat.classList.add("icon-footer");

    const likesSpan = document.createElement("span");
    likesSpan.textContent = post.curtidas ? post.curtidas.length : 0;

    const comentariosSpan = document.createElement("span");
    comentariosSpan.textContent = post.comentarios ? post.comentarios.length : 0;

    const likesDiv = document.createElement("div");
    likesDiv.classList.add("likes");
    likesDiv.appendChild(iconeCoracao);
    likesDiv.appendChild(likesSpan);

    const comentariosDiv = document.createElement("div");
    comentariosDiv.classList.add("comentarios");
    comentariosDiv.appendChild(iconeChat);
    comentariosDiv.appendChild(comentariosSpan);

    footer.appendChild(likesDiv);
    footer.appendChild(comentariosDiv);

    content.appendChild(title);
    content.appendChild(desc);

    card.appendChild(img);
    card.appendChild(content);
    card.appendChild(footer);

    card.addEventListener("click", () => {
      if (!usuarioLogado) {
        abrirModalLogin();
        return;
      }
      abrirModalDetalhes(post);
    });

    return card;
  }

  // Carregar posts e distribuir nas seções
  async function carregarTodasSecoes() {
    try {
      const posts = await apiGet("/posts");

      const destaquePets = posts.filter(p => p.tipo === "pet").slice(0, 4);
      const produtosPromocao = posts.filter(p => p.tipo === "produto").slice(0, 4);
      const outrosPets = posts.filter(p => p.tipo === "pet").slice(4, 8);
      const servicos = posts.filter(p => p.tipo === "servico");

      sections.destaquePets.innerHTML = "";
      sections.produtosPromocao.innerHTML = "";
      sections.outrosPets.innerHTML = "";
      sections.servicos.innerHTML = "";

      destaquePets.forEach(post => {
        sections.destaquePets.appendChild(criarCard(post));
      });
      produtosPromocao.forEach(post => {
        sections.produtosPromocao.appendChild(criarCard(post));
      });
      outrosPets.forEach(post => {
        sections.outrosPets.appendChild(criarCard(post));
      });
      servicos.forEach(post => {
        sections.servicos.appendChild(criarCard(post));
      });
    } catch (err) {
      console.error("Erro ao carregar seções:", err);
    }
  }

  carregarTodasSecoes();
});
