$(document).ready(() => {
    
    $("button[id^='lineActivate']").css({"display": "none"});
    // Apagar essa depois
    
    const contadorDeLinhas = () => {
        let tab = $("table#tabelaTarefas")
        let numbers = tab.find("tbody > tr")
        return numbers.length
    };
    
    const mostrarDataeHora = () => {
        let hoje = new Date()
        
        let dia      = hoje.getDate()
        let mes      = hoje.getMonth() + 1
        let ano      = hoje.getFullYear()
        let horas    = hoje.getHours()
        let minutos  = hoje.getMinutes()
        let segundos = hoje.getSeconds()
        
        if (dia      < 10) { dia      = `0${dia}` }
        if (mes      < 10) { mes      = `0${mes}` }
        if (horas    < 10) { horas    = `0${horas}` }
        if (minutos  < 10) { minutos  = `0${minutos}` }
        if (segundos < 10) { segundos = `0${segundos}` }
        
        return `${ano}-${mes}-${dia}T${horas}:${minutos}:${segundos}`
    };
    
    const limparLinhas = () => {
        $("input#new-task").val("");
        $("input#new-local").val("");
        $("input#new-datetime").val(mostrarDataeHora());
    }

    $("button#limparLinha").click(() => {limparLinhas()});

    const apresentacao = dataFeia => {
        let dataNova = dataFeia.split("T");
        let data = dataNova[0].split("-").reverse();
        let dataBoa = `${data} ${dataNova[1]}`.replaceAll(",", "/");
        return dataBoa;
    }

    $("button#criarLinha").click(() => {
        let qtdeLinhas = contadorDeLinhas() + 1;

        let newTask = $("input#new-task").val()
        let newLocal = $("input#new-local").val()

        let itemNovo = `<tr>
            <td>${qtdeLinhas}</td>
            <td>${newTask}</td>
            <td>${newLocal}</td>
            <td>${apresentacao(mostrarDataeHora())}</td>
            <td>
                <div class='d-flex justify-content-around'>
                    <p><span class='badge badge-secondary statusLinha${qtdeLinhas} bg-success'>Ativada</span></p>
                    <div class='btn-group'>
                        <button type='button' class='btn btn-sm btn-secondary dropdown-toggle' data-toggle='dropdown' aria-haspopup='true' aria-expanded='false'>Ações</button>
                        <div class='dropdown-menu dropdown-menu-right'>
                            <button class='dropdown-item btn btn-sm border-success Ativar' type='button' alt='Ativar' title='Ativar' id='lineActivate${qtdeLinhas}' name='lineActivate${qtdeLinhas}'><img alt='Ativar' src='https://img.icons8.com/color/25/null/toggle-on--v1.png'/><span class='text-center'>Ativar</span></button>
                            <button class='dropdown-item btn btn-sm border-warning Editar' type='button' alt='Editar' title='Editar' id='lineEdit${qtdeLinhas}' name='lineEdit${qtdeLinhas}'><img alt='Editar' src='https://img.icons8.com/fluency/25/null/edit.png'/><span class='text-center'>Editar</span></button>
                            <button class='dropdown-item btn btn-sm border-danger Desativar' type='button' alt='Desativar' title='Desativar' id='lineDeactivate${qtdeLinhas}' name='lineDeactivate${qtdeLinhas}'><img alt='Desativar' src='https://img.icons8.com/color/25/null/toggle-off.png'/><span class='text-center'>Desativar</span></button>
                        </div>
                    </div>
                </div>
            </td>
        </tr>`;
        $("tbody#corpoTabela").append(itemNovo);
        limparLinhas();
        $("button[id^='lineActivate']").css({"display": "none"});
    });
    
});
