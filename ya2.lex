(* Ejemplo básico *)

let digito = "0|1|2|3|4|5|6|7|8|9"
let negativo = "-"
let numero = "negativo?digito(digito)*"
let igual = "="
let letra = "a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z"
let identificador = "letra(letra|digito)*"

rule tokens =
  identificador	{ print("Identificador\n") }
  | digito			{ print("Dígito\n") }
  | letra			{ print("Letra\n") }
  | numero			{ print("Número\n") }
  | negativo			{ print("Negativo\n") }
  | igual			{ print("Igual\n") }
