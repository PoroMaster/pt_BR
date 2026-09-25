// Formulario de Login //
const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

// Notificaçoes //
localStorage.setItem("read","2");

// Ganhador do Mes //
localStorage.setItem("winner", "fehtheworld#9360");

// Mensagems //
localStorage.setItem("msg_title", "Testando novas formas de notificiar o publico!");
localStorage.setItem("msg_box", "Apenas uma mensagem de testes, Mas gostaria de agradecer por voce estar aqui!");
localStorage.setItem("msg_title2", "Divulgue nosso modskin!");
localStorage.setItem("msg_box2", "Gostaria que voce divulga-se meu modskin, ele é bom neh?!");

// Data Base das Imagens e Variaveis //
var sem_nivel = "discord/def538381113.png";
var nivel_1 = "discord/86d8a85dcaa0.png";
var nivel_2 = "discord/ff7e54949e41.png";
var nivel_3 = "discord/c4214e21501e.png";
var nivel_4 = "discord/bba50849e7fd.png";
var nivel_5 = "discord/fdefabf78257.png";
var nivel_6 = "discord/2afb643e2fc2.png";
var nivel_7 = "discord/5ed19f4a28a5.png";
var sequencia_0 = "discord/a6fb5699580c.png";
var sequencia_1 = "discord/b6d363d3628a.png";
var sequencia_2 = "discord/fcb97bce4184.png";
var sequencia_3 = "discord/f5e10a621d57.png";
var sequencia_4 = "discord/a082cdef0e39.png";
var sem_ranked = "discord/11e10fe01012.png";
var ranked_bronze = "discord/1b6dd010740c.png";
var ranked_prata = "discord/eb157ba7c054.png";
var ranked_ouro = "discord/79970e293de9.png";
var ranked_platina = "discord/0b34837aee14.png";
var ranked_diamante = "discord/c01574d6ed5b.png";
var ranked_mestre = "discord/1cb13a2110e5.png";
var ranked_desafiante = "discord/dc145fd11fd7.png";
var cargo_dev = "discord/f298519f5f42.png";
var cargo_mod = "discord/d3183aace4ae.png";
var cargo_supp = "discord/580aea2321f8.png";
var cargo_tester = "discord/4f67b6910cc7.png";
var cargo_corretor = "discord/bfcc2d2f1747.png";
var cargo_designer = "discord/63f904d33399.png";
var vfalse = "hidden";
var vtrue = "revert"
var imune = "∾"
var sem = "Sem";
var prata = "Prata";
var ouro = "Ouro";
var platina = "Platina";
var diamante = "Diamante";
var mestre = "Mestre";
var desafiante = "Desafiante";
var dev = "Dev";
var mod = "Mod";
var supp = "Supp";
var supp_ini = "Supp Ini.";
var tester = "Tester"
var corretor = "Corretor"
var designer = "Designer"
const urlhref = "verification.html"

// Url do Perfil //
var url = "image/Profile/"


// Perfis dos Usuarios! //
const ID01 = {
  Nome: "Lucas",
  Imagem: url+"Porito.png",
  Pontos: imune,
  Level_Pontos: imune,
  Pontos_Miticos: imune,
  Sequencia: imune,
  Level_Image: sem_nivel,
  Sequencia_Image: sequencia_0,
  Ranked: imune,
  Ranked_Image: sem_ranked,
  Imune: vtrue,
  Risco: vfalse,
  Cargo: dev,
  Cargo_Image: cargo_dev,
};
const ID02 = {
  Nome: "Raguem",
  Imagem: url+"Foxy.png",
  Pontos: 122,
  Level_Pontos: 2,
  Pontos_Miticos: 0,
  Sequencia: 0,
  Level_Image: nivel_2,
  Sequencia_Image: sequencia_0,
  Ranked: sem,
  Ranked_Image: sem_ranked,
  Imune: vfalse,
  Risco: vfalse,
  Cargo: supp,
  Cargo_Image: cargo_supp,
};
const ID03 = {
  Nome: "Gabriel",
  Imagem: url+"Gece.png",
  Pontos: 131,
  Level_Pontos: 3,
  Pontos_Miticos: 0,
  Sequencia: 0,
  Level_Image: nivel_3,
  Sequencia_Image: sequencia_0,
  Ranked: sem,
  Ranked_Image: sem_ranked,
  Imune: vfalse,
  Risco: vfalse,
  Cargo: mod,
  Cargo_Image: cargo_mod,
};
const ID04 = {
  Nome: "Matheus",
  Imagem: url+"Mono.png",
  Pontos: 101,
  Level_Pontos: 1,
  Pontos_Miticos: 0,
  Sequencia: 0,
  Level_Image: nivel_1,
  Sequencia_Image: sequencia_0,
  Ranked: sem,
  Ranked_Image: sem_ranked,
  Imune: vfalse,
  Risco: vfalse,
  Cargo: supp,
  Cargo_Image: cargo_supp,
};
const ID05 = {
  Nome: "Fernanda",
  Imagem: url+"Fehtheworld.png",
  Pontos: 135,
  Level_Pontos: 3,
  Pontos_Miticos: 1,
  Sequencia: 2,
  Level_Image: nivel_3,
  Sequencia_Image: sequencia_2,
  Ranked: sem,
  Ranked_Image: sem_ranked,
  Imune: vfalse,
  Risco: vfalse,
  Cargo: designer,
  Cargo_Image: cargo_designer,
};
const ID06 = {
  Nome: "Gustavo",
  Imagem: url+"Krap.png",
  Pontos: 108,
  Level_Pontos: 1,
  Pontos_Miticos: 0,
  Sequencia: 0,
  Level_Image: nivel_1,
  Sequencia_Image: sequencia_0,
  Ranked: sem,
  Ranked_Image: sem_ranked,
  Imune: vfalse,
  Risco: vfalse,
  Cargo: supp_ini,
  Cargo_Image: cargo_supp,
};
const ID07 = {
  Nome: "Guilherme",
  Imagem: url+"Buddha.png",
  Pontos: 100,
  Level_Pontos: 1,
  Pontos_Miticos: 0,
  Sequencia: 0,
  Level_Image: nivel_1,
  Sequencia_Image: sequencia_0,
  Ranked: sem,
  Ranked_Image: sem_ranked,
  Imune: vfalse,
  Risco: vfalse,
  Cargo: tester,
  Cargo_Image: cargo_tester,
};
const ID08 = {
  Nome: "Vitor",
  Imagem: url+"Trick.png",
  Pontos: 102,
  Level_Pontos: 1,
  Pontos_Miticos: 0,
  Sequencia: 0,
  Level_Image: nivel_1,
  Sequencia_Image: sequencia_0,
  Ranked: sem,
  Ranked_Image: sem_ranked,
  Imune: vfalse,
  Risco: vfalse,
  Cargo: supp_ini,
  Cargo_Image: cargo_supp,
};
const ID09 = {
  Nome: "Leandro",
  Imagem: url+"JasonMiler.png",
  Pontos: 100,
  Level_Pontos: 1,
  Pontos_Miticos: 0,
  Sequencia: 0,
  Level_Image: nivel_1,
  Sequencia_Image: sequencia_0,
  Ranked: sem,
  Ranked_Image: sem_ranked,
  Imune: vfalse,
  Risco: vfalse,
  Cargo: tester,
  Cargo_Image: cargo_tester,
};

// Login //
if (loginButton) loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if (username == "Porito#0000" || username == "Porito" ) {
        location.href = urlhref;
        localStorage.setItem("userdate", username);
        localStorage.setItem("validate", "museu");
        localStorage.setItem("user_name", ID01.Nome);
        localStorage.setItem("points", ID01.Pontos);
        localStorage.setItem("level_points", ID01.Level_Pontos);
        localStorage.setItem("sequence", ID01.Sequencia);
        localStorage.setItem("points_mitics", ID01.Pontos_Miticos);
        localStorage.setItem("ranked_mitico", ID01.Ranked);
        localStorage.setItem("imune", ID01.Imune);
        localStorage.setItem("risco", ID01.Risco);
        localStorage.setItem("cargo", ID01.Cargo);
        localStorage.setItem("userdate_img", ID01.Imagem);
        localStorage.setItem("level_points_img", ID01.Level_Image);
        localStorage.setItem("sequence_img", ID01.Sequencia_Image);
        localStorage.setItem("ranked_mitico_img", ID01.Ranked_Image);
        localStorage.setItem("cargo_img", ID01.Cargo_Image);
    }
    else if (username == "Kawai Foxy#3471" || username == "Kawai Foxy" ) {
        location.href = urlhref;
        localStorage.setItem("userdate", username);
        localStorage.setItem("validate", "museu");
        localStorage.setItem("user_name", ID02.Nome);
        localStorage.setItem("points", ID02.Pontos);
        localStorage.setItem("level_points", ID02.Level_Pontos);
        localStorage.setItem("sequence", ID02.Sequencia);
        localStorage.setItem("points_mitics", ID02.Pontos_Miticos);
        localStorage.setItem("ranked_mitico", ID02.Ranked);
        localStorage.setItem("imune", ID02.Imune);
        localStorage.setItem("risco", ID02.Risco);
        localStorage.setItem("cargo", ID02.Cargo);
        localStorage.setItem("userdate_img", ID02.Imagem);
        localStorage.setItem("level_points_img", ID02.Level_Image);
        localStorage.setItem("sequence_img", ID02.Sequencia_Image);
        localStorage.setItem("ranked_mitico_img", ID02.Ranked_Image);
        localStorage.setItem("cargo_img", ID02.Cargo_Image);
    } 
    else if (username == "' gece ✪#9960" || username == "Gece" ) {
        location.href = urlhref;
        localStorage.setItem("userdate", username);
        localStorage.setItem("validate", "museu");
        localStorage.setItem("user_name", ID03.Nome);
        localStorage.setItem("points", ID03.Pontos);
        localStorage.setItem("level_points", ID03.Level_Pontos);
        localStorage.setItem("sequence", ID03.Sequencia);
        localStorage.setItem("points_mitics", ID03.Pontos_Miticos);
        localStorage.setItem("ranked_mitico", ID03.Ranked);
        localStorage.setItem("imune", ID03.Imune);
        localStorage.setItem("risco", ID03.Risco);
        localStorage.setItem("cargo", ID03.Cargo);
        localStorage.setItem("userdate_img", ID03.Imagem);
        localStorage.setItem("level_points_img", ID03.Level_Image);
        localStorage.setItem("sequence_img", ID03.Sequencia_Image);
        localStorage.setItem("ranked_mitico_img", ID03.Ranked_Image);
        localStorage.setItem("cargo_img", ID03.Cargo_Image);
    } 
    else if (username == "亗𝓟𝓲𝓮𝓬𝓴亗#4930" || username == "Mono" ) {
        location.href = urlhref;
        localStorage.setItem("userdate", username);
        localStorage.setItem("validate", "museu");
        localStorage.setItem("user_name", ID04.Nome);
        localStorage.setItem("points", ID04.Pontos);
        localStorage.setItem("level_points", ID04.Level_Pontos);
        localStorage.setItem("sequence", ID04.Sequencia);
        localStorage.setItem("points_mitics", ID04.Pontos_Miticos);
        localStorage.setItem("ranked_mitico", ID04.Ranked);
        localStorage.setItem("imune", ID04.Imune);
        localStorage.setItem("risco", ID04.Risco);
        localStorage.setItem("cargo", ID04.Cargo);
        localStorage.setItem("userdate_img", ID04.Imagem);
        localStorage.setItem("level_points_img", ID04.Level_Image);
        localStorage.setItem("sequence_img", ID04.Sequencia_Image);
        localStorage.setItem("ranked_mitico_img", ID04.Ranked_Image);
        localStorage.setItem("cargo_img", ID04.Cargo_Image);
    } 
    else if (username == "fehtheworld#9360" || username == "Fehtheworld" ) {
        location.href = urlhref;
        localStorage.setItem("userdate", username);
        localStorage.setItem("validate", "museu");
        localStorage.setItem("user_name", ID05.Nome);
        localStorage.setItem("points", ID05.Pontos);
        localStorage.setItem("level_points", ID05.Level_Pontos);
        localStorage.setItem("sequence", ID05.Sequencia);
        localStorage.setItem("points_mitics", ID05.Pontos_Miticos);
        localStorage.setItem("ranked_mitico", ID05.Ranked);
        localStorage.setItem("imune", ID05.Imune);
        localStorage.setItem("risco", ID05.Risco);
        localStorage.setItem("cargo", ID05.Cargo);
        localStorage.setItem("userdate_img", ID05.Imagem);
        localStorage.setItem("level_points_img", ID05.Level_Image);
        localStorage.setItem("sequence_img", ID05.Sequencia_Image);
        localStorage.setItem("ranked_mitico_img", ID05.Ranked_Image);
        localStorage.setItem("cargo_img", ID05.Cargo_Image);
    } 
    else if (username == "Krap ♛#1541" || username == "Krap" ) {
        location.href = urlhref;
        localStorage.setItem("userdate", username);
        localStorage.setItem("validate", "museu");
        localStorage.setItem("user_name", ID06.Nome);
        localStorage.setItem("points", ID06.Pontos);
        localStorage.setItem("level_points", ID06.Level_Pontos);
        localStorage.setItem("sequence", ID06.Sequencia);
        localStorage.setItem("points_mitics", ID06.Pontos_Miticos);
        localStorage.setItem("ranked_mitico", ID06.Ranked);
        localStorage.setItem("imune", ID06.Imune);
        localStorage.setItem("risco", ID06.Risco);
        localStorage.setItem("cargo", ID06.Cargo);
        localStorage.setItem("userdate_img", ID06.Imagem);
        localStorage.setItem("level_points_img", ID06.Level_Image);
        localStorage.setItem("sequence_img", ID06.Sequencia_Image);
        localStorage.setItem("ranked_mitico_img", ID06.Ranked_Image);
        localStorage.setItem("cargo_img", ID06.Cargo_Image);
    } 
    else if (username == "Buddha#5046" || username == "Buddha" ) {
        location.href = urlhref;
        localStorage.setItem("userdate", username);
        localStorage.setItem("validate", "museu");
        localStorage.setItem("user_name", ID07.Nome);
        localStorage.setItem("points", ID07.Pontos);
        localStorage.setItem("level_points", ID07.Level_Pontos);
        localStorage.setItem("sequence", ID07.Sequencia);
        localStorage.setItem("points_mitics", ID07.Pontos_Miticos);
        localStorage.setItem("ranked_mitico", ID07.Ranked);
        localStorage.setItem("imune", ID07.Imune);
        localStorage.setItem("risco", ID07.Risco);
        localStorage.setItem("cargo", ID07.Cargo);
        localStorage.setItem("userdate_img", ID07.Imagem);
        localStorage.setItem("level_points_img", ID07.Level_Image);
        localStorage.setItem("sequence_img", ID07.Sequencia_Image);
        localStorage.setItem("ranked_mitico_img", ID07.Ranked_Image);
        localStorage.setItem("cargo_img", ID07.Cargo_Image);
    } 
    else if (username == "Shuba Duck#4828" || username == "Trick" ) {
        location.href = urlhref;
        localStorage.setItem("userdate", username);
        localStorage.setItem("validate", "museu");
        localStorage.setItem("user_name", ID08.Nome);
        localStorage.setItem("points", ID08.Pontos);
        localStorage.setItem("level_points", ID08.Level_Pontos);
        localStorage.setItem("sequence", ID08.Sequencia);
        localStorage.setItem("points_mitics", ID08.Pontos_Miticos);
        localStorage.setItem("ranked_mitico", ID08.Ranked);
        localStorage.setItem("imune", ID08.Imune);
        localStorage.setItem("risco", ID08.Risco);
        localStorage.setItem("cargo", ID08.Cargo);
        localStorage.setItem("userdate_img", ID08.Imagem);
        localStorage.setItem("level_points_img", ID08.Level_Image);
        localStorage.setItem("sequence_img", ID08.Sequencia_Image);
        localStorage.setItem("ranked_mitico_img", ID08.Ranked_Image);
        localStorage.setItem("cargo_img", ID08.Cargo_Image);
    } 
    else if (username == "JasonMiler#4652" || username == "JasonMiler" ) {
        location.href = urlhref;
        localStorage.setItem("userdate", username);
        localStorage.setItem("validate", "museu");
        localStorage.setItem("user_name", ID09.Nome);
        localStorage.setItem("points", ID09.Pontos);
        localStorage.setItem("level_points", ID09.Level_Pontos);
        localStorage.setItem("sequence", ID09.Sequencia);
        localStorage.setItem("points_mitics", ID09.Pontos_Miticos);
        localStorage.setItem("ranked_mitico", ID09.Ranked);
        localStorage.setItem("imune", ID09.Imune);
        localStorage.setItem("risco", ID09.Risco);
        localStorage.setItem("cargo", ID09.Cargo);
        localStorage.setItem("userdate_img", ID09.Imagem);
        localStorage.setItem("level_points_img", ID09.Level_Image);
        localStorage.setItem("sequence_img", ID09.Sequencia_Image);
        localStorage.setItem("ranked_mitico_img", ID09.Ranked_Image);
        localStorage.setItem("cargo_img", ID09.Cargo_Image);
    } 
    else {
        loginErrorMsg.style.opacity = 1;
        localStorage.clear();
    }
})
