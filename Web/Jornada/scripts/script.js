$(document).ready(function(){

    $("#cargaHoraria").on("change mousemove",function(){
        $("span#carga").text( $(this).val() );        
    });
    
    /*
    // jornada de 8 horas = 8 * 60
    let jornada = 8 * 60;
    let almoco = 1 * 60;
    let parcial = jornada + almoco;

    function converteEmHoras(horas) {
        let saldo = horas.split(":");
        let minutos = 60 * parseInt(saldo[0]) + parseInt(saldo[1]);
        let novaHora = minutos + jornada;
        let h = parseInt(minutos / 60);
        let m = parseInt(minutos % 60);
        return h + ":" + m;
    }

    $("button#devendo").click(function() {
       let banco = $("#saldo_banco").val();
       let total = parcial + minutos;
       $("#ontem").text(converteEmHoras(total));
    });

    $("button#sobrando").click(function() {
        let banco = $("#saldo_banco").val();
        let saldo = banco.split(":");
        let minutos = 60 * parseInt(saldo[0]) + parseInt(saldo[1]);
        let total = parcial - minutos;
        $("#ontem").text(converteEmHoras(total));
    });
    */

});