(* Ejemplo básico *)

let digito = "0|1|2"
let numero = "digito(digito)*"
let letra = "a|b|c"
let identificador = "letra(letra|digito)*"

rule tokens =
  identificador	{ print("Identificador\n") }
  | numero			{ print("Número\n") }
  | '+'				{ print("Operador de suma\n") }
  | '*'				{ print("Operador de multiplicación\n") }
  | '='				{ print("Operador de asignación\n") }
