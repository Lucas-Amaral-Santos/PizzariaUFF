/// <reference path="../../typings/globals/jquery/index.d.ts" />

$(function () {
  $('[data-toggle="tooltip"]').tooltip({ boundary: 'window' });
  $('[data-toggle="popover"]').popover();


  // $("#nome").addEventListener("blur", function() { nomeValidoFunction() }, false)
  $("#id-form").submit(function (e) { validaCadastroFunction(e) });
  $("#log-form").submit(function (e) { validaLoginFunction(e) });




  function validaLoginFunction(e) {
    alert("valida Login");
    e.preventDefault();

      let login_valido = loginValidoFunction();

    if (login_valido) {
      alert("Tudo Ok!");
      // $("#id-form").submit()
    }
    else {
      alert("Deu erro!");
    }
  }

  function validaCadastroFunction(e) {
    alert("valida Cadastro");
    e.preventDefault();

    let nome_valido = nomeValidoFunction();
    let sexo_valido = sexoValidoFunction();
    let campus_valido = campusValidoFunction();
    let ciencia_valida = cienciaValidaFunction();
    let email_valido = emailValidoFunction();

    if (nome_valido && sexo_valido && campus_valido && ciencia_valida && email_valido) {
      alert("Tudo Ok!");
      // $("#id-form").submit()
    }
    else {
      alert("Deu erro!");
    }
  }

  function cienciaValidaFunction() {
    let ciencia = $("#ciencia");

    let feedback_excursao = $("#feedback-excursao");

    let botoes = $("input.excursao:checked")
    if (botoes.length === 0) {
      ciencia.addClass("is-invalid");
      ciencia.removeClass("is-valid");
      return false;
    }
    else {
      ciencia.addClass("is-valid");
      ciencia.removeClass("is-invalid");
      return true;
    }
  }

  function campusValidoFunction() {
    let campus = $("#campus");

    if (campus.val() === '') {
      camous.addClass("is-invalid");
      campus.removeClass("is-valid");
      return false;
    }
    else {
      campus.removeClass("is-invalid");
      campus.addClass("is-valid");
      return true;
    }
  }

  function sexoValidoFunction() {
    let sexo_masc = $("#sexo-masc");
    let sexo_fem = $("#sexo-fem");

    let sexo_feedback = $("#sexo-feedback");

    let botoes = $("input[name='sexo']:checked");
    if (botoes.length === 0) {
      sexo_masc.addClass("is-invalid");
      sexo_masc.removeClass("is-valid");
      sexo_fem.addClass("is-invalid");
      sexo_fem.removeClass("is-valid");
      sexo_feedback.addClass("d-block");
      return false;
    }
    else {
      sexo_masc.removeClass("is-invalid");
      sexo_masc.addClass("is-valid");
      sexo_fem.removeClass("is-invalid");
      sexo_fem.addClass("is-valid");
      sexo_feedback.removeClass("d-block");
      return true;
    }
  }

  function nomeValidoFunction() {
    alert("nome valido");
    let nome = $("#nome");

    if (nome.val() === '') {
      nome.addClass("is-invalid");
      nome.removeClass("is-valid");
      return false;
    }
    else {
      nome.removeClass("is-invalid");
      nome.addClass("is-valid");
      return true;
    }
  }

  function emailValidoFunction() {
    alert("email valido");
    let email = $("#email");
    let senha = $("#senha");
    let confirma = $("#confirma-senha");
    if ((email.val() === '') && (senha.val() === '') && (confirma.val() === '')) {
      email.addClass("is-invalid");
      email.removeClass("is-valid");
      senha.addClass("is-invalid");
      senha.removeClass("is-valid");
      confirma.addClass("is-invalid");
      confirma.removeClass("is-valid");
      return false;
    }
    else {
      email.removeClass("is-invalid");
      email.addClass("is-valid");
      senha.addClass("is-invalid");
      senha.removeClass("is-valid");
      confirma.addClass("is-invalid");
      confirma.removeClass("is-valid");
      if (senha.val() === confirma.val())
        return true;
      else
        alert("Senhas não compatíveis");
    }

    function loginValidoFunction() {
      alert("email valido");
      let email = $("#email");
      let senha = $("#senha");

      if (email.val() === '' && senha.val() === '') {
        email.addClass("is-invalid");
        email.removeClass("is-valid");
        senha.addClass("is-invalid");
        senha.removeClass("is-valid");
        return false;
      }
      else {
        email.removeClass("is-invalid");
        email.addClass("is-valid");
        senha.addClass("is-invalid");
        senha.removeClass("is-valid");
      }
    }
  }

  var curtido=0;
  var descurtido=0;
  $("#like").text($("#like").data('like'));
  $("#dislike").text($("#dislike").data('dislike'));

  
  $("#btn-like").click(function () {
    var like = $("#like").data('like');
    if(curtido){
      curtido=0;
      like=like-1;
      $("#like").data('like',like);
      $("#like").text(like);
      $(this).find("i").removeClass("fas");
      $(this).find("i").addClass("far");
    }else{

      if(descurtido){
        $("#btn-dislike").click();
      }
      curtido=1;
      like=like+1;
      $("#like").data('like',like);
      $("#like").text(like);
      $(this).find("i").removeClass("far");
      $(this).find("i").addClass("fas");  
    
    }
  })


  $("#btn-dislike").click(function () {

    var dislike = $("#dislike").data("dislike");

    if(descurtido){
      descurtido=0;
      dislike=dislike-1;
      $("#dislike").data('dislike',dislike);
      $("#dislike").text(dislike);
      $(this).find("i").removeClass("fas");
      $(this).find("i").addClass("far");
    }else{
      if(curtido){
        $("#btn-like").click();
      }
      descurtido=1;
      dislike=dislike+1;
      $("#dislike").data('dislike',dislike);
      $("#dislike").text(dislike);
      $(this).find("i").removeClass("far");
      $(this).find("i").addClass("fas");  
    
    }
  })
});