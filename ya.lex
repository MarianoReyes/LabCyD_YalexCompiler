(* Ejemplo básico *)

let if = "if"
let else = "else"
let digito = "1|2|3"
let numero = "digito(digito)*"
let letra = "a|b|c|d|e"
let identificador = "letra(letra|digito)*"

rule tokens =
  if	{ print("IF\n") }
  | else	{ print("ELSE\n") }
  | identificador	{ print("Identificador\n") }
  | digito			{ print("Dígito\n") }
  | letra			{ print("Letra\n") }
  | numero			{ print("Número\n") }

