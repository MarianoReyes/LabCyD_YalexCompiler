(* Archivo Final *)
(* A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z *)

let if = "if"
let else = "else"
let switch = "switch"
let case = "case"
let digito = "0|1|2|3|4|5|6|7|8|9"
let negativo = "-"
let numero = "negativo?digito(digito)*"
let numero_hexadecimal = "numero(a|b|c|d|e|f|A|B|C|D|E|F)"
let igual = "="
let letra = "a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z"
let identificador = "letra(letra|digito)*"

rule tokens =
  if	{ print("IF\n") }
  | else	{ print("ELSE\n") }
  | switch	{ print("SWITCH\n") }
  | case	{ print("CASE\n") }
  | identificador	{ print("Identificador\n") }
  | digito			{ print("Dígito\n") }
  | letra			{ print("Letra\n") }
  | numero			{ print("Número\n") }
  | numero_hexadecimal			{ print("Número Hexadecimal\n") }
  | negativo			{ print("Negativo\n") }
  | igual			{ print("Igual\n") }
