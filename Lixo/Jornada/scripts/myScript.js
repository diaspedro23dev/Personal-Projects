$(document).ready(function () {

	function barra_progresso(elem, value) {
		let meio = $(`div[id='${elem}']`);
		meio.prop("ariaValueNow", parseInt(value));
		meio.text(value + "%");
		meio.prop("style", `width: ${value}%`);
	}

	function constantes() {
		return {
			"inputJornada": converteEmMinutos($("input[id='inputJornada']").val()),
			"inputAlmoco": converteEmMinutos($("input[id='inputAlmoco']").val()),
			"inputBancoHoras": converteEmMinutos($("input[id='inputBancoHoras']").val()),
			"novaJornada": converteEmMinutos($("input[id='novaJornada']").val()),
			"entrada_manha": converteEmMinutos($("input[id='entrada_manha']").val()),
			"saida_manha": converteEmMinutos($("input[id='saida_manha']").val()),
			"entrada_tarde": converteEmMinutos($("input[id='entrada_tarde']").val()),
			"saida_tarde": converteEmMinutos($("input[id='saida_tarde']").val())
		}
	}

	$("button[id='mais']").click(function () {
		let horario = constantes();
		let novaJornada = horario["inputJornada"] + horario["inputAlmoco"] + horario["inputBancoHoras"]
		let novaHora = converteEmHoras(novaJornada);
		$("input[id='novaJornada']").val(novaHora);
	});
	
	$("button[id='menos']").click(function () {
		let horario = constantes();
		let novaJornada = horario["inputJornada"] + horario["inputAlmoco"] - horario["inputBancoHoras"];
		let novaHora = converteEmHoras(novaJornada);
		$("input[id='novaJornada']").val(novaHora);
	});
	
	$("input[id='saida_manha']").change(function () {
		let horario = constantes()
		let barraPreAlmoco = Number(100 * (horario["saida_manha"] - horario["entrada_manha"]) / constantes["novaJornada"]).toPrecision(4);
		barra_progresso("barraPreAlmoco", barraPreAlmoco);
		
		$("#ajuda").text(JSON.stringify({horario}));
		let entrada_tarde = converteEmHoras(horario["inputAlmoco"] + horario["saida_manha"]);
		$("input[id='entrada_tarde']").val(entrada_tarde);
	});
	
	$("input[id='entrada_tarde']").change(function () {
		const horario = constantes();
		const porcentMiddle = Number(100 * (horario["almoco"]) / horario["novaJornada"]).toPrecision(4);
		barra_progresso("barra_Almoco", porcentMiddle);
		
		let excesso_Almoco = converteEmHoras((horario["entrada_tarde"] - horario["saida_manha"]) - horario["inputAlmoco"]);
		$("input[id='excesso_Almoco']").val(excesso_Almoco);
	});
	
	$("input[id='saida_tarde']").change(function () {
		const horario = constantes();
		const porcentPos = horario["porcentPos"];
		barra_progresso("barraPosAlmoco", porcentPos);
	});

});
