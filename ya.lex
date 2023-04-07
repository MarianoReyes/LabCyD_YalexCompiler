(* Ejemplo básico *)

let digito = "0|1|2|3|4|5|6|7|8|9"
let numero = "digito+"
let letra = "a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z"
let identificador = "letra(letra|digito)*"

rule tokens =
  identificador	{ print("Identificador\n") }
  | numero			{ print("Número\n") }
  | '+'				{ print("Operador de suma\n") }
  | '*'				{ print("Operador de multiplicación\n") }
  | '='				{ print("Operador de asignación\n") }
