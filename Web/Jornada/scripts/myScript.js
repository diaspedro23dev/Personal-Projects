$(document).ready(function () {

	function converteEmMinutos(horas) {
		let tempo = horas.split(":")
		return 60 * Number(tempo[0]) + Number(tempo[1])
	}

	function converteEmHoras(tempo) {
		let hora = parseInt(tempo / 60);
		let minutos = tempo % 60;
		if (hora < 10) { hora = "0" + hora }
		if (minutos < 10) { minutos = "0" + minutos }
		return `${hora}:${minutos}`
	}

	function constantes() { return {
			"jornada": converteEmMinutos($("input[id='inputJornada']").val()),
			"almoco": converteEmMinutos($("input[id='inputAlmoco']").val()),
			"bancoHoras": converteEmMinutos($("input[id='inputBancoHoras']").val())
		}
	}
	
	function cargaHoraria () { return {
		"novaJornada": converteEmMinutos($("input[id='novaJornada']").val()),
			"entrada_manha": converteEmMinutos($("input[id='entrada_manha']").val()),
			"saida_manha": converteEmMinutos($("input[id='saida_manha']").val()),
			"entrada_tarde": converteEmMinutos($("input[id='entrada_tarde']").val()),
			"saida_tarde": converteEmMinutos($("input[id='saida_tarde']").val())
		}
	}

	function barra_progresso (elem, value, text) {
		let meio = $(`div[id='${elem}']`);
		meio.prop("ariaValueNow", value);
		meio.text(value + "% de " + text);
		meio.prop("style", `width: ${value}%`);
	}
	
	$("button[id='mais']").click(function () {
		let tempos = constantes();
		let novaJornada = tempos["jornada"] + tempos["almoco"] + tempos["bancoHoras"];
		let novaHora = converteEmHoras(novaJornada);
		$("input[id='novaJornada']").val(novaHora);
	});
	
	$("button[id='menos']").click(function () {
		let tempos = constantes();
		let novaJornada = tempos["jornada"] + tempos["almoco"] - tempos["bancoHoras"];
		let novaHora = converteEmHoras(novaJornada);
		$("input[id='novaJornada']").val(novaHora);
	});

	$("button[id='calcular']").click(function () {
		const horario = cargaHoraria();
		
		let antesAlmoco = horario["saida_manha"] - horario["entrada_manha"];
		let porcentPre = parseInt(100 * (antesAlmoco / horario["novaJornada"]));
		let porcentMiddle = parseInt(100 * (horario["entrada_tarde"] - horario["saida_manha"]) / horario["novaJornada"]);
		let porcentPos = 100 - porcentPre;

		barra_progresso("barra_antesAlmoco", porcentPre.toPrecision(4), "AM");
		barra_progresso("barra_almoco", porcentMiddle.toPrecision(4), "LUNCH!");
		barra_progresso("barra_depoisAlmoco", porcentPos.toPrecision(4), "PM");
	});
	
});
